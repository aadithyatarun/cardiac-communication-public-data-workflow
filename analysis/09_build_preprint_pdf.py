from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DELIVERABLES = PROJECT_ROOT / "deliverables" / "preprint"
FIGURES = PROJECT_ROOT / "figures" / "generated"


def markdown_blocks(path: Path) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            blocks.append(("title", line[2:]))
        elif line.startswith("## "):
            blocks.append(("h1", line[3:]))
        elif line.startswith("### "):
            blocks.append(("h2", line[4:]))
        else:
            blocks.append(("body", line))
    return blocks


def main() -> None:
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "ProjectTitle",
        parent=styles["Title"],
        fontName="Helvetica",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#17365D"),
        spaceAfter=14,
    )
    h1 = ParagraphStyle(
        "Heading1Custom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#2F5D95"),
        spaceBefore=14,
        spaceAfter=8,
    )
    h2 = ParagraphStyle(
        "Heading2Custom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12.5,
        leading=15,
        textColor=colors.HexColor("#4F81BD"),
        spaceBefore=10,
        spaceAfter=4,
    )
    body = ParagraphStyle(
        "BodyCustom",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        spaceAfter=6,
    )
    caption = ParagraphStyle(
        "CaptionCustom",
        parent=body,
        fontName="Helvetica",
        fontSize=10,
        leading=12,
        spaceBefore=4,
        spaceAfter=10,
    )

    story = []
    for kind, text in markdown_blocks(DELIVERABLES / "preprint_manuscript.md"):
        escaped = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        if kind == "title":
            story.append(Paragraph(escaped, title))
        elif kind == "h1":
            story.append(Paragraph(escaped, h1))
        elif kind == "h2":
            story.append(Paragraph(escaped, h2))
        else:
            story.append(Paragraph(escaped, body))

    story.append(PageBreak())
    story.append(Paragraph("Figures", h1))
    for figure, label in [
        (FIGURES / "dataset_overview.png", "Figure 1. Dataset register and local data audit."),
        (
            FIGURES / "kuppe_visium_celltype_overview.png",
            "Figure 2. Human myocardial infarction Visium cell-type composition.",
        ),
    ]:
        if figure.exists():
            story.append(Image(str(figure), width=6.2 * inch, height=3.7 * inch))
            story.append(Paragraph(label, caption))
            story.append(Spacer(1, 0.15 * inch))

    out = DELIVERABLES / "preprint_manuscript.pdf"
    doc = SimpleDocTemplate(
        str(out),
        pagesize=letter,
        leftMargin=0.8 * inch,
        rightMargin=0.8 * inch,
        topMargin=0.8 * inch,
        bottomMargin=0.8 * inch,
        title="Cardiac communication public data workflow",
        author="Tarun Aadithya Magesh Raghavan",
    )
    doc.build(story)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
