"""Audit cached data without accessing the network."""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))
from spendgame.eada import inventory

if __name__ == "__main__":
    result = inventory(root)
    print(json.dumps({k: v for k, v in result.items() if k != "archives"}, indent=2))
    print("Audited annual archives:", sum(r["status"] == "audited" for r in result["archives"]))
