"""Stitch all Dreamreel-V2-*.md files in output/ together, ordered by header number."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
DEST = ROOT / "stories" / "Contumelious-Ectogenesis" / "S1-Dreamreel" / "Dreamreel.md"

SECTION_RE = re.compile(r"^## (\d+)\. ", re.MULTILINE)


def extract_sections(text: str):
    """Return list of (number, section_text) for every '## N. ...' block."""
    matches = list(SECTION_RE.finditer(text))
    sections = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        num = int(m.group(1))
        sections.append((num, text[start:end].rstrip()))
    return sections


def main():
    files = sorted(OUTPUT_DIR.glob("Dreamreel-V2-*.md"))
    all_sections = []
    for f in files:
        all_sections.extend(extract_sections(f.read_text(encoding="utf-8")))

    all_sections.sort(key=lambda s: s[0])

    body = "\n\n".join(text for _, text in all_sections)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(f"# Dreamreel\n\n{body}\n", encoding="utf-8")
    print(f"Wrote {len(all_sections)} sections from {len(files)} files to {DEST}")


if __name__ == "__main__":
    main()
