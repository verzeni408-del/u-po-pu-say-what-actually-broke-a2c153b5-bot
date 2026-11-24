"""Error copy for 'Say What Actually Broke': writes the one-line message to /output/entry.txt (stdlib only)."""
from pathlib import Path

ERROR_LINE = "The file you uploaded is a photo of a spreadsheet, not a spreadsheet. Please upload the actual spreadsheet."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(ERROR_LINE, encoding="utf-8")
