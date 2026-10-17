# Data contract and acquisition

The current output is an **initial financial inventory**, not a joined research
panel. `data_sources.csv` separates access from permission to redistribute raw
files or publish derived outputs. Empty dates and unknown values stay empty.

- `raw/metadata/2026-10-17/eada_catalog.json`: factual official file catalog,
  retrieved from the endpoint used by EADA's public download interface.
- `local/eada/`: eight original annual ZIP archives, unchanged and excluded from
  Git; acquisition receipts include URLs and SHA-256 hashes.
- `institution_crosswalk.csv`: provisional source identity per reporting year.
  This is not a verified IPEDS campus, conference or sport-membership crosswalk.
- `data_dictionary.csv`: initial audit definitions. The raw field inventory
  records exact per-year source schemas; every later modeling field needs an
  explicit dictionary entry before use.
- `local/processed/`: granular money/reconciliation diagnostics excluded from
  Git. `reports/financial_coverage.csv` contains aggregate coverage counts only.
- `processed/`: reserved for reviewed, permitted analytical artifacts; currently
  no fitted or joined empirical table.

From the project root:

```sh
.venv/bin/python scripts/acquire_eada.py
.venv/bin/python scripts/audit_data.py
```

The acquisition script uses exact catalog-listed split-table archives. Cached
files are reused and checked as ZIPs. Retrieval uses one bounded request per
archive, without authentication or retry loops. New download failures stop for
inspection. Snapshot hashes in `reports/inventory.json` identify the bytes used.

Read each year's `SchoolsDoc*.doc` and `InstlevelDataDoc*.doc` inside the ZIP.
The 2025 codebook labels `EXP_MEN`/`EXP_WOMEN` as team expenses and separately
labels `OPEXPPERTEAM_*`. Confirm questionnaire definitions and harmonize every
year before comparing spending levels. Do not add coaching, scholarships or
game-day expenses to an inclusive team total a second time. Aggregate salary
fields are not individual head-coach compensation.

Academic year comes from catalog metadata; a reporting-year label is not a
known fiscal start/end, publication date or availability date. Those dates need
separate evidence. Contemporary 2026 roster-budget estimates never enter the
historical panel. Source missing columns/records do not establish non-sponsorship.

Raw redistribution rights remain unresolved for these OPE-hosted archives.
The ED copyright notice explicitly limits its scope to www.ed.gov. Public
downloads are available for analysis; this project keeps raw financial files
local until the applicable permissions are documented. An eventual code license
does not relicense source data.
