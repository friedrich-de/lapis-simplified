import genanki
import yaml
import sys

if len(sys.argv) < 2:
    print("Usage: python build_anki_deck.py <output_file>")
    sys.exit(1)

SIMPLIFIED_LAPIS_TEMPLATE_ID = 1667218449923
SIMPLIFIED_LAPIS_DECK_ID = 1759068131727

with open("../src/front.html", "r") as front_file:
    front_content = front_file.read()

with open("../src/back.html", "r") as back_file:
    back_content = back_file.read()

with open("../src/styling.css", "r") as css_file:
    css_content = css_file.read()

with open("anki_fields.yaml", "r", encoding="utf-8") as fields_file:
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

with open("example_card.csv", "r") as f:
    for line in f:
        fields_content = line.strip().split("\t")
        deck.add_note(
            genanki.Note(
                model=lapis, fields=fields_content, tags=["アニメ::小市民シリーズ"]
            )
        )

package = genanki.Package(deck)
package.media_files = [
    "media_files/yomitan_audio_2024-07-20-15-08-08-382.ogg",
    "media_files/shoushiminseries04_08m44s853ms_08m47s653ms.ogg",
    "media_files/shoushiminseries04_08m46s485ms.webp",
    "media_files/yomitan_dictionary_media_1_2024-07-20-15-08-08-382.svg",
]
package.write_to_file(sys.argv[1])
