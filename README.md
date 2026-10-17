# The NIL Arms Race

An explainable, multi-sport athletics investment research project: how should a
university allocate discretionary resources across athlete compensation,
coaching, program support and retained budget when rivals also make decisions?

**Current status, October 17, 2026: initial evidence audit and financial
inventory. No fitted spending returns, school recommendations or simulator.**

Start with the [research notebook](notebooks/01_research.ipynb), its
[HTML export](reports/research.html), and the
[feasibility note](reports/feasibility.md).
[PROJECT_BRIEF.md](PROJECT_BRIEF.md) defines the full project and acceptance gates.

## Work implemented

- Downloaded and audited eight official EADA annual archives, 2017–18 through
  2024–25. Checks cover institution/sport grain, joins, missing/zero separation,
  schema differences and source-total reconciliation.
- Recorded financial coverage for football, men's and women's basketball,
  baseball, softball and women's volleyball; retained department breadth.
- Created source/rights, policy, assumptions and field-definition registers,
  a provisional institution-year identity crosswalk and an access-failure log.
- Added a reproducible notebook environment and data integrity tests.

Financial availability does not satisfy the empirical release gate. Performance
outcomes, annual definition/date harmonization, CPI, campus/sport membership and
several permissions remain unresolved. **There are zero joined analysis-ready
observations.** The project does not treat this as a completed empirical study.

## Reproduce

Use Python 3.13; the tested environment is macOS arm64. From this directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/acquire_eada.py
.venv/bin/python scripts/audit_data.py
.venv/bin/python scripts/summarize_audit.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/execute_notebook.py
```

`requirements.txt` defines the supported dependency bounds;
`requirements-lock.txt` records the tested package resolution. The notebook
script creates a fresh local kernel, executes top to bottom and exports HTML;
no global kernel installation is required. Acquisition needs internet access;
the audit and notebook use cached local archives and make no network calls.
No API credentials are needed for this first stage.

Open `reports/research.html` directly in a browser. For a static local preview:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Then view [the audit export](http://127.0.0.1:8000/reports/research.html).
`docs/index.html` has not been built; no simulator build command exists yet.
Phase 4 must add readable JS, a deterministic build and Python/browser parity
checks before claiming an offline simulator. No public publishing is configured.

## Evidence and permissions

[data/README.md](data/README.md) explains acquisition, units, missingness and
accounting. Raw EADA archives and monetary diagnostics stay under ignored
`data/local/`; only catalog/schema metadata, identifiers and aggregate coverage
are included in review outputs while redistribution rights are unresolved.

The Athletic interactive is **optional**. Its original figures and methodology
were inaccessible and no estimates were used. Lawfully viewed screenshots can
go in `data/local/restricted/athletic/`; see the
[intake instructions](reports/athletic_intake.md). Keep source title/URL, update
date, methodology, legend, units and reported ranges visible. A football roster
budget is not automatically external NIL, and current estimates cannot explain
earlier seasons.

[Policy status](reports/policy_status.md) distinguishes verified Senate passage
and proposal text from incomplete latest-status verification. The proposed
retention exception is excluded from the baseline; the 2026–27 numeric benefits
cap remains unverified. No allowance increases funded cash.

## Next gate

Complete annual finance definitions, fiscal/availability dates and permissions;
acquire and audit official sport results; verify campus and year-specific sport
membership; build a multi-sport panel and publish inclusion/exclusion counts.
Freeze validation seasons before model selection. Historical associations and
scenario assumptions remain separate throughout.

Project-authored code is MIT licensed. Third-party data, articles and images
retain their own rights; see the source register. No restricted tables, athlete
contracts or individual valuations are required.
