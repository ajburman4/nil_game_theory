"""Audit official split-table EADA archives without inventing sponsorship or dates.

This is a financial inventory, not an analysis-ready historical panel. School
classification is EADA's reporting-year classification, not sport membership.
"""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile

import pandas as pd


def require_unique(frame: pd.DataFrame, keys: list[str], label: str) -> None:
    if frame[keys].isna().any().any():
        raise ValueError(f"{label}: null grain key")
    if frame.duplicated(keys).any():
        raise ValueError(f"{label}: duplicate grain {keys}")


def numeric_status(value: object) -> str:
    if pd.isna(value):
        return "unknown"
    number = float(value)
    if not pd.notna(number) or number < 0 or number == float("inf"):
        raise ValueError("Expected a finite nonnegative disclosure")
    return "observed_zero" if number == 0 else "observed_positive"


def strict_sum(values: pd.Series) -> float:
    """An incomplete component list cannot be reconciled by filling gaps with 0."""
    return values.sum(min_count=len(values))


def read_archive(path: Path, end_year: int) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    receipt_path = path.with_suffix(".receipt.json")
    if not receipt_path.exists():
        raise ValueError(f"{path.name}: missing acquisition receipt")
    receipt = json.loads(receipt_path.read_text())
    checksum = hashlib.sha256(path.read_bytes()).hexdigest()
    if checksum != receipt["sha256"]:
        raise ValueError(f"{path.name}: source snapshot differs from acquisition checksum")
    with ZipFile(path) as archive:
        names = {n.lower(): n for n in archive.namelist()}
        frames = []
        members = []
        for expected in ["instlevel.xlsx", "schools.xlsx"]:
            if expected not in names:
                raise ValueError(f"{path.name}: missing {expected}; audit schema manually")
            name = names[expected]
            frame = pd.read_excel(io.BytesIO(archive.read(name)), engine="openpyxl")
            frame.columns = frame.columns.str.strip()
            members.append({"member": name, "rows": len(frame), "columns": list(frame.columns)})
            # Verified physical header difference, not a fuzzy name match.
            # Keep original headers in the manifest for exact provenance.
            if end_year == 2019 and expected == "instlevel.xlsx":
                if "ClassificationName" not in frame or "classification_name" in frame:
                    raise ValueError("2019 classification alias differs from audited schema")
                frame = frame.rename(columns={"ClassificationName": "classification_name"})
            frames.append(frame)
    inst, sport = frames
    require_unique(inst, ["unitid"], path.name + ":institution")
    require_unique(sport, ["unitid", "SPORTSCODE"], path.name + ":sport")
    if not set(sport.unitid).issubset(set(inst.unitid)):
        raise ValueError(f"{path.name}: unmatched sport UNITIDs")
    if sport[["unitid", "SPORTSCODE", "Sports"]].isna().any().any():
        raise ValueError(f"{path.name}: missing sport identifiers")
    # Fail loudly if the two tables disagree on institutional classification.
    check = sport.merge(inst[["unitid", "sector_cd", "ClassificationCode"]],
                        on="unitid", how="left", validate="many_to_one", suffixes=("", "_inst"))
    for field in ["sector_cd", "ClassificationCode"]:
        if not check[field].eq(check[field + "_inst"]).all():
            raise ValueError(f"{path.name}: inconsistent {field}")
    metadata = {"academic_year": f"{end_year-1}-{str(end_year)[-2:]}",
                "reporting_year": end_year,
                "source_id": f"eada_{end_year}",
                "sha256": checksum,
                "retrieval_date": receipt.get("retrieval_date") or receipt["retrieved_at_utc"][:10],
                "members": members}
    return inst, sport, metadata


def inventory(root: Path) -> dict:
    plan = json.loads((root / "config/research_plan.json").read_text())
    coverage, archive_records, crosswalk, reconciliation = [], [], [], []
    field_inventory = []
    for year in range(plan["candidate_start_year"], plan["candidate_end_year"] + 1):
        path = root / f"data/local/eada/EADA_{year-1}-{year}.zip"
        if not path.exists():
            archive_records.append({"reporting_year": year, "status": "not_acquired"})
            continue
        inst, sport, meta = read_archive(path, year)
        public = inst.loc[inst.sector_cd.eq(1) & inst.ClassificationCode.isin([1, 2, 3])].copy()
        selected = sport.loc[sport.unitid.isin(public.unitid)].copy()
        archive_records.append({**meta, "status": "audited", "public_di_institutions": len(public)})
        for table, frame in [("institution", inst), ("sport", sport)]:
            for col in frame.columns:
                source_col = "ClassificationName" if (
                    year == 2019 and table == "institution" and col == "classification_name"
                ) else col
                field_inventory.append({"source_id": meta["source_id"], "table": table,
                                        "source_field": source_col, "normalized_field": col,
                                        "dtype": str(frame[col].dtype),
                                        "nonmissing_rows": int(frame[col].notna().sum()),
                                        "rows": len(frame)})
        for row in public.itertuples():
            crosswalk.append({"project_id": f"eada_{int(row.unitid)}", "unitid": int(row.unitid),
                "eada_unitid": int(row.unitid), "institution_name": row.institution_name,
                "reporting_year": year, "academic_year": meta["academic_year"],
                "eada_classification": row.classification_name,
                "source_id": meta["source_id"], "evidence_class": "observed",
                "campus_match_status": "EADA identity only; IPEDS campus review pending",
                "conference": None, "sport_membership_status": "not_verified"})
        for spec in plan["sports"]:
            participants = f"PARTIC_{spec['gender']}"
            expense = f"EXP_{spec['gender']}"
            operating = f"OPEXPPERTEAM_{spec['gender']}"
            rows = selected.loc[selected.Sports.eq(spec["eada_label"])]
            for field in [participants, expense, operating]:
                if field not in rows:
                    raise ValueError(f"{year}: required field {field} not available")
                for value in rows[field]:
                    numeric_status(value)
            # Positive participation is evidence of a reported team. An absent
            # record or a blank sex column is NOT proof of non-sponsorship.
            positive = rows[participants].gt(0)
            coverage.append({"source_id": meta["source_id"], "academic_year": meta["academic_year"],
                "reporting_year": year, "sport_id": spec["id"], "evidence_class": "derived_estimate",
                "candidate_public_di_institutions": len(public),
                "sport_records": len(rows),
                "positive_participation_records": int(positive.sum()),
                "missing_participation_records": int(rows[participants].isna().sum()),
                "zero_participation_records": int(rows[participants].eq(0).sum()),
                "missing_sport_record_institutions": len(public) - len(rows),
                "positive_participation_and_expense_records": int((positive & rows[expense].notna()).sum()),
                "positive_participation_missing_expense_records": int((positive & rows[expense].isna()).sum()),
                "zero_expense_records": int(rows[expense].eq(0).sum()),
                "outcome_records_acquired": 0,
                "analysis_ready_observations": 0})
        # Source totals only; no across-source equality is forced. Unallocated
        # expense is counted exactly once. Differences are diagnostic, not fixed.
        grouped = selected.groupby("unitid")["TOTAL_EXPENSE_ALL"].agg(strict_sum)
        for row in public.itertuples():
            components = pd.Series([grouped.get(row.unitid, float("nan")),
                                    row.TOT_EXPENSE_ALL_NOTALLOC])
            difference = strict_sum(components) - row.GRND_TOTAL_EXPENSE
            reconciliation.append({"unitid": int(row.unitid), "source_id": meta["source_id"],
                "reporting_year": year,
                "difference_usd": None if pd.isna(difference) else float(difference),
                "status": "unknown_components" if pd.isna(difference) else
                          ("matches" if abs(difference) <= 1 else "discrepancy"),
                "evidence_class": "derived_estimate"})
    output = root / "reports"
    local = root / "data/local/processed"
    local.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(coverage).to_csv(output / "financial_coverage.csv", index=False)
    pd.DataFrame(field_inventory).to_csv(output / "source_field_inventory.csv", index=False)
    # Names and identifiers are a provisional factual mapping, not a public
    # school spending dataset. Money and granular discrepancies remain local.
    cw = pd.DataFrame(crosswalk)
    if not cw.empty:
        require_unique(cw, ["unitid", "reporting_year"], "crosswalk")
    cw.to_csv(root / "data/institution_crosswalk.csv", index=False)
    pd.DataFrame(reconciliation).to_csv(local / "eada_reconciliation.csv", index=False)
    statuses = pd.Series([r["status"] for r in reconciliation]).value_counts().to_dict()
    summary = {"stage": "financial_inventory_only", "as_of_date": plan["as_of_date"],
               "archives": archive_records, "reconciliation_counts": statuses,
               "historical_outcome_rows": 0, "analysis_ready_rows": 0,
               "minimum_empirical_release_gate": "NOT_MET: outcomes and harmonization missing",
               "rights": "raw archives and monetary row diagnostics local-only; public outputs are coverage/schema metadata"}
    (output / "inventory.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary
