"""Download selected official catalog entries; immutable archives stay local-only.

Run from the project root. No guessed file paths, authentication or bulk scraping.
Reuses the exact URLs exposed by the public download interface. At most eight
archives in the initial research window; one request at a time, no retry loop.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data/raw/metadata/2026-10-17/eada_catalog.json"
BASE = "https://ope.ed.gov/athletics/api/dataFiles/file?fileName="


def acquire(years: list[int]) -> list[dict]:
    catalog = json.loads(CATALOG.read_text())
    folder = ROOT / "data/local/eada"
    folder.mkdir(parents=True, exist_ok=True)
    records = []
    for year in years:
        matches = [r for r in catalog if r["Year"] == year
                   and r["FileName"] == f"EADA_{year-1}-{year}.zip"]
        if len(matches) != 1:
            raise ValueError(f"Expected one split-table catalog entry for {year}")
        entry = matches[0]
        path = folder / entry["FileName"]
        url = BASE + quote(entry["FileName"], safe="")
        if not path.exists():
            # Stage first: failed downloads must never look like valid archives.
            with urlopen(url, timeout=45) as response:
                payload = response.read(40_000_001)
            if len(payload) > 40_000_000:
                raise ValueError("Unexpected archive size; inspect source manually")
            partial = path.with_suffix(".partial")
            partial.write_bytes(payload)
            with ZipFile(partial) as archive:
                if archive.testzip() is not None:
                    raise ValueError("Corrupt EADA archive")
            partial.rename(path)
            retrieved_at = datetime.now(timezone.utc).isoformat()
            path.with_suffix(".receipt.json").write_text(json.dumps({
                "source_url": url, "retrieved_at_utc": retrieved_at,
                "sha256": hashlib.sha256(payload).hexdigest(),
                "rights": "local analysis; raw redistribution review pending"
            }, indent=2) + "\n")
        with ZipFile(path) as archive:
            if archive.testzip() is not None:
                raise ValueError(f"Corrupt cached archive: {path.name}")
        receipt_path = path.with_suffix(".receipt.json")
        if not receipt_path.exists():
            raise ValueError(f"Cached archive has no acquisition receipt: {path.name}; inspect provenance")
        receipt = json.loads(receipt_path.read_text())
        if receipt["sha256"] != hashlib.sha256(path.read_bytes()).hexdigest():
            raise ValueError(f"Cached snapshot changed: {path.name}; do not overwrite its receipt")
        records.append({"year": year, "path": str(path.relative_to(ROOT)),
                        "source_url": url,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        print(f"Ready {path.name}", flush=True)
    return records


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--years", type=int, nargs="+", default=list(range(2018, 2026)))
    args = parser.parse_args()
    acquire(args.years)
