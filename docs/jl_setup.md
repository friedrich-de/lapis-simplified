# JL Setup

## Basic Configuration

Once you've got JL installed and connected to AnkiConnect, you'll need to configure it for the Lapis note type. Open the Preferences menu and click on the `Anki` tab. Choose your deck from the `Deck` dropdown, and then select Lapis as the `Note Type`.

Set up your fields according to the following table:

| Field                 | Value                                      |
|-----------------------|--------------------------------------------|
| Expression            | `Primary Spelling`                         |
| ExpressionReading     | `First Reading`                            |
| ExpressionAudio       | `Audio`                                    |
| SelectionText         | `Selected Definitions`                     |
| MainDefinition        | `Definitions`                              |
| Sentence              | `Sentence`                                 |
| SentenceAudio         | `Nothing`                                  |
| Picture               | `Image`                                    |
| Glossary              | `Nothing`                                  |
| PitchPosition         | `Pitch Accent for First Reading (Numeric)` |
| Frequency             | `Frequencies`                              |
| FreqSort              | `Frequency (Harmonic Mean)`                |

## Limitations

- While JL does support exporting multiple definitions, we generally don’t recommend using that option, as it collapses all dictionaries except the one you selected for export. It’s usually better to choose the single definition you prefer and export that directly to your Anki card.
- As of now, JL only supports one pitch accent dictionary at a time and will output only the first pitch accent listed for a word, even if additional accents exist. **アクセント辞典** however, is one dictionary with very high coverage, so feel free to check that out.
- Not all Yomitan dictionaries are formatted correctly for use with JL, so please keep that in mind. That said, **JMDict** and **大辞泉** are reliable options and work well with JL as well as have a very wide coverage.
