"""Execute the saved notebook in a fresh project-venv kernel and export HTML.

No network acquisition occurs in the notebook. Kernel files stay inside the
workspace; no user-wide Jupyter kernel registration is necessary.
"""
import json
import hashlib
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JUPYTER = ROOT / ".venv/share/jupyter"
KERNEL = JUPYTER / "kernels/spendgame"
KERNEL.mkdir(parents=True, exist_ok=True)
(KERNEL / "kernel.json").write_text(json.dumps({
    "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
    "display_name": "Spend Game Theory (project environment)", "language": "python"
}))
os.environ["JUPYTER_PATH"] = str(JUPYTER)
os.environ["JUPYTER_RUNTIME_DIR"] = str(ROOT / ".venv/jupyter-runtime")
os.environ["IPYTHONDIR"] = str(ROOT / ".venv/ipython")
os.environ["JUPYTER_PLATFORM_DIRS"] = "1"

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter

path = ROOT / "notebooks/01_research.ipynb"
nb = nbformat.read(path, as_version=4)
# Clear prior execution state; a failing run must not leave stale success output.
for cell in nb.cells:
    if cell.cell_type == "code":
        cell.outputs = []
        cell.execution_count = None
nbformat.write(nb, path)
record = {"command": ".venv/bin/python scripts/execute_notebook.py",
          "started_at_utc": datetime.now(timezone.utc).isoformat(),
          "kernel": "fresh project-local spendgame kernel",
          "python": sys.version, "status": "running",
          "scope": "Phase 0 evidence audit and initial financial inventory only"}
record_path = ROOT / "reports/notebook_execution.json"
record_path.write_text(json.dumps(record, indent=2) + "\n")
try:
    NotebookClient(nb, timeout=300, kernel_name="spendgame",
                   resources={"metadata": {"path": str(ROOT)}}).execute()
except Exception as error:
    record.update(status="failed", error_type=type(error).__name__)
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    raise
nbformat.write(nb, path)
exporter = HTMLExporter(template_name="lab")
exporter.exclude_input_prompt = False
exporter.mathjax_url = ""
exporter.require_js_url = ""
html, resources = exporter.from_notebook_node(nb)
# This audit contains static tables and text, so scripts are unnecessary.
# Strip exporter bootstrap scripts as well as empty src tags for a clean,
# network-independent reading artifact. The future simulator has its own build.
html = re.sub(r"<script\b[^>]*>.*?</script\s*>", "", html,
              flags=re.IGNORECASE | re.DOTALL)
(ROOT / "reports/research.html").write_text(html)
record.update(status="success", completed_at_utc=datetime.now(timezone.utc).isoformat(),
              executed_code_cells=sum(c.cell_type == "code" for c in nb.cells),
              notebook_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
              inventory_sha256=hashlib.sha256((ROOT / "reports/inventory.json").read_bytes()).hexdigest())
record_path.write_text(json.dumps(record, indent=2) + "\n")
print("Executed notebooks/01_research.ipynb and exported reports/research.html")
