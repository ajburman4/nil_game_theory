"""Refresh the audit note and acquisition register from executed inventory output."""
import csv
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
summary = json.loads((ROOT / "reports/inventory.json").read_text())
coverage = pd.read_csv(ROOT / "reports/financial_coverage.csv")
path = ROOT / "data/data_sources.csv"
with path.open(newline="") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    sources = list(reader)
by_id = {s["source_id"]: s for s in sources}
for archive in summary["archives"]:
    if archive["status"] != "audited":
        continue
    source = by_id[archive["source_id"]]
    source["access_status"] = "retrieved_schema_and_grain_audited"
    source["checksum"] = archive["sha256"]
    source["units"] = "nominal USD; participant counts; source categories"
    source["coverage"] = f"{archive['public_di_institutions']} candidate public DI institutions; no outcomes joined"
    source["transformations"] = "source grain checks; public DI filter; aggregate coverage; strict source-total reconciliation; no inflation or model fit"
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(sources)

counts = coverage.groupby("sport_id")["positive_participation_and_expense_records"].agg(["min", "max"])
table = "\n".join(f"| {sport} | {int(row['min'])} | {int(row['max'])} |"
                  for sport, row in counts.iterrows())
archives = [a for a in summary["archives"] if a["status"] == "audited"]
institution_years = sum(a["public_di_institutions"] for a in archives)
note = f"""# Initial feasibility audit — October 17, 2026

**Status: Phase 0 evidence audit implemented; Phase 1 financial acquisition begun.
The empirical release gate is not met. No models or simulator are released.**

The directory originally contained only PROJECT_BRIEF.md, with no repository
instructions, source data, environment or Git repository. The implementing work
adds explicit provenance, missing-value rules, policy/assumption registers,
acquisition and audit scripts, tests and an executed narrative notebook.

## Verified financial starting point

The [official catalog](https://ope.ed.gov/athletics/api/dataFiles/fileList) lists
annual split-table archives through **2024–25**. All eight archives from
**2017–18 through 2024–25** have been downloaded and parsed. This is the proposed
financial window; it is not yet an accepted finance–performance analysis window.

The source filter (sector_cd=1 and ClassificationCode in 1,2,3) selects
**{institution_years:,} institution-year records** across the acquired archives.
Within each year, institution keys and institution×sport keys are unique,
sport keys match institution keys, and institutional classifications agree
across split tables. One explicit physical header alias is needed for the
2018–19 institution classification label; original headers remain in the manifest.

The following ranges count positive gender-specific participation with nonmissing
team expenses. Denominator: candidate public DI institutions in each source year.
Evidence class: derived_estimate (aggregate metadata from observed disclosures).
They are **potential financial-input counts**, not matched analysis samples.

| Detailed sport | Minimum annual records | Maximum annual records |
|---|---:|---:|
{table}

The financial inventory preserves all six intended sports and three women's
sports. All other source sports remain in department reconciliation and future
protected commitments. No heterogeneous other-sports competitive league is created.

**Reconciliation:** {summary['reconciliation_counts'].get('matches', 0):,}
institution-year totals match within $1 using sport total expenses plus
unallocated expenses versus the source grand total. Unknown components stay
unknown and discrepancies would be reported, not repaired. A source identity
does not establish financial audit quality or cross-source comparability.

## Consequential gaps and concrete fallbacks

1. **Performance:** zero outcome observations acquired; no spending returns or
   rankings can be estimated. NCAA statistics web retrieval failed. Next audit
   bounded official school/conference result collection and comparable
   regular-season denominators, keeping canceled seasons missing. Begin with
   men's/women's basketball, softball and women's volleyball, then baseball and
   a separately supported football subset.
2. **Dates and definitions:** source catalog years do not establish school fiscal
   dates or publication/availability dates. Read every annual questionnaire and
   dictionary; distinguish total team from game-day expenses and inclusive
   components. CPI values have not been acquired. Do not make real-dollar
   comparisons or forecast claims yet.
3. **Campus and membership:** the crosswalk is provisional EADA identity only.
   Verify IPEDS campus and year×sport membership before any cross-source joins.
   Current conference labels cannot be backfilled into earlier years.
4. **Rights:** raw EADA archives and granular money diagnostics stay local-only
   pending file-specific redistribution review. ED's www.ed.gov notice does not
   automatically cover OPE. Public outputs currently contain source catalog,
   schema, factual identifiers and aggregate counts. Knight–Newhouse requires
   registration for raw exports; no export was acquired or registration bypassed.
   A permitted owner-provided export or official university reports are fallbacks.
5. **Policy:** Senate passage and pinned proposal text were verified; live actions
   and complete enactment review were not. The current-year benefits cap, school
   participation and court/implementation updates require official confirmation.
   Current policy functionality remains disabled. See policy_status.md.
6. **The Athletic:** optional; original source and methodology inaccessible. The
   project continues without it. Lawful screenshots may inform a local-only
   2026 football reported-estimate snapshot after definition/rights review, never
   historical inputs or invented external NIL.

## Research gate and next work

**Analysis-ready rows: {summary['analysis_ready_rows']}.** The minimum release
requires at least 30 institutions, five comparable seasons and four detailed
sports including two women's sports, plus other-program commitments. Financial
coverage alone cannot satisfy this condition. Select the 40–80-school study
sample after outcome and membership coverage is audited; publish exclusions
before fitting. If the joined sample is smaller, release an explicitly scoped
pilot, not a completed full empirical study.

H1/H2 remain untested historical hypotheses; H3/H4 are conditional strategy
questions; H5 remains exploratory. The provisional split plan is written before
fitting, with exact season assignment deferred until the final joined window is
known. Finish financial definition/date/rights review and outcomes acquisition
before descriptive spending comparisons, model fitting or strategy optimization.

Reproduce with `.venv/bin/python scripts/audit_data.py`, followed by
`.venv/bin/python scripts/summarize_audit.py` and
`.venv/bin/python scripts/execute_notebook.py`.
"""
(ROOT / "reports/feasibility.md").write_text(note)
print("Updated data source checksums/status and reports/feasibility.md")
