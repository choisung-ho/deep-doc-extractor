"""Create a text PDF from the original synthetic sample (no vendor data)."""
from pathlib import Path
import textwrap
from reportlab.pdfgen import canvas

root = Path(__file__).resolve().parents[1]
source = (root / "examples/sample-manual.md").read_text()
output = root / "data/source_pdfs/sample-manual.pdf"
output.parent.mkdir(parents=True, exist_ok=True)
pdf = canvas.Canvas(str(output))
pdf.setFont("Helvetica", 11)
y = 800
for paragraph in source.splitlines():
    for line in textwrap.wrap(paragraph, width=85) or [""]:
        pdf.drawString(50, y, line)
        y -= 18
pdf.save()
print(output)
