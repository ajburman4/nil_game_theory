# Initial validation — October 17, 2026

**Scope: evidence handling and financial inventory only. Research/model/product
acceptance criteria remain open.**

| Check | Result | Evidence |
|---|---|---|
| Original EADA ZIP integrity and acquisition SHA-256 receipts | Pass, eight cached archives | `scripts/acquire_eada.py`; local receipts; `inventory.json` |
| Institution and institution×sport unique grain | Pass in all eight archives | `src/spendgame/eada.py` executed by audit notebook |
| Sport-to-institution joins and classification consistency | Pass | Exact UNITID joins; unmatched/inconsistent rows raise errors |
| Department expense source-total reconciliation | 1,861 matches within $1 | Local row diagnostics; aggregate `inventory.json` |
| Missing values distinguished from observed zero | Pass | Tests; explicit coverage columns; no fillna/peer imputation |
| Invalid numeric disclosures and grain keys rejected | Pass | Negative/infinite, duplicate and null-key synthetic tests |
| Changed or unprovenanced snapshots rejected | Pass | Synthetic checksum and missing-receipt tests |
| Source IDs, acquisition hash references and register references | Pass | Final register integrity check |
| Fresh-kernel notebook execution | Pass; seven sequential executed code cells, no error outputs | `notebook_execution.json` records command, dates and hashes |
| Readable HTML generated from executed notebook | Pass, export generated | `research.html`; no remote script or stylesheet dependencies detected |

The eight unit tests use **synthetic fixtures only**. Run:

```sh
.venv/bin/python -m unittest discover -s tests -v
```

Acquisition replay reused eight cached archives and verified each receipt without
making network requests. The notebook re-read every archive in a clean kernel,
not hidden process state. Run:

```sh
.venv/bin/python scripts/execute_notebook.py
```

The execution script uses a project-local kernelspec and runtime directory.
This host's sandbox blocked Jupyter's loopback socket creation; execution
succeeded with permission for local kernel ports. No global kernel install was
needed. The environment is Python 3.13.0 on macOS arm64; exact package versions
are frozen in `requirements-lock.txt` and displayed in the notebook.

## Checks not yet satisfied

Financial accounting matches do not establish audited accuracy or harmonized
definitions. Annual dictionary/questionnaire review, fiscal/availability dates,
CPI adjustment, complete campus and year-specific sport membership, sponsorship
missingness and outcome joins remain unfinished. The empirical release gate is
**not met**: zero analysis-ready finance–performance rows.

Rolling validation, clustered uncertainty, historical model comparisons,
coaching leakage checks, optimizer/policy feasibility, finite-game regret,
multiple starts, planner comparisons, Python/JS parity, interactive-browser
offline/keyboard/mobile behavior and interaction timing are **not yet tested**.
No model or simulator exists to validate. Current-year policy verification and
source redistribution permissions are not complete. No executive findings or
publication-ready claims have been released.
