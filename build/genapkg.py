import genanki
import yaml
import sys
import csv
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python genapkg.py <output_file>")
    sys.exit(1)

SIMPLIFIED_LAPIS_TEMPLATE_ID = 1667218449923
SIMPLIFIED_LAPIS_DECK_ID = 1759068131727

script_dir = Path(__file__).resolve().parent
repo_root = script_dir.parent
src_dir = repo_root / "src"
build_dir = script_dir

with open(src_dir / "front.html", "r", encoding="utf-8") as front_file:
    front_content = front_file.read()

with open(src_dir / "back.html", "r", encoding="utf-8") as back_file:
    back_content = back_file.read()

with open(src_dir / "styling.css", "r", encoding="utf-8") as css_file:
    css_content = css_file.read()

with open(build_dir / "anki_fields.yaml", "r", encoding="utf-8") as fields_file:
    anki_fields = yaml.safe_load(fields_file)

lapis = genanki.Model(
    SIMPLIFIED_LAPIS_TEMPLATE_ID,
    "Lapis Simplified",
    fields=anki_fields,
    templates=[
        {
            "name": "Mining",
            "qfmt": front_content,
            "afmt": back_content,
        },
    ],
    css=css_content,
)

deck = genanki.Deck(SIMPLIFIED_LAPIS_DECK_ID, "Lapis Simplified")

cards_file = build_dir / "example_cards.csv"
if not cards_file.exists():
    raise FileNotFoundError(
        f"Cards file not found: {cards_file}. Expected TSV (tab-separated) rows with "
        f"{len(anki_fields)} fields + optional trailing tag."
    )

expected_field_count = len(anki_fields)

with open(cards_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row_index, row in enumerate(reader, start=1):
        if not row or all(not cell.strip() for cell in row):
            continue

        tag_str = ""
        fields_content = row
        if len(row) == expected_field_count + 1:
            fields_content = row[:-1]
            tag_str = row[-1].strip()
        elif len(row) != expected_field_count:
            raise ValueError(
                f"Row {row_index} has {len(row)} values; expected {expected_field_count} "
                f"or {expected_field_count + 1} (including tag)."
            )

        tags = tag_str.replace(",", " ").split() if tag_str else []
        deck.add_note(genanki.Note(
            model=lapis, fields=fields_content, tags=tags))

package = genanki.Package(deck)
media_dir = build_dir / "media_files"
if media_dir.exists():
    package.media_files = [str(p) for p in sorted(
        media_dir.iterdir()) if p.is_file()]

package.write_to_file(sys.argv[1])
