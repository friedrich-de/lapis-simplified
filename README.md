# lapis-simplified

https://github.com/user-attachments/assets/5bd7d122-79cc-4d9e-b4b8-426936b07102

Fork of Lapis intended for modifications that align it with my personal preferences and the original, thoughtfully designed Animecards template. The idea is to split the card's information into two categories:

- Essential: Word, Reading, Meaning
- Non-essential: Picture, Sentence, Audio

When reviewing and passing the card, we only pay attention to the essential information. When lapsing a card, we use the non-essential information to remind ourselves. This allows us to review cards very quickly while maintaining high review quality.

Therefore, the following changes are made:

- The image no longer appears next to the word and is left-shifted -> It's non-essential information and should be lower on the card.
- The definition has been moved below the word and reading -> It's essential information and should be higher on the card.
- Moved the audio buttons below the sentence.

Note: These changes are now achievable with the original Lapis by changing the CSS variables in `styling.css`. 

Additionally the following changes are made for the sake of simplification:

- Removed `ExpressionFurigana`: Expression and ExpressionReading are sufficient.
- Removed `SentenceFurigana`: Furigana insertion is prone to mistakes and not needed. Make cards with native audio instead. Especially as a beginner you should never rely on any sort of furigana insertion. It's simply an unsolved problem and not something that should be attempted automatically.
- Removed `IsWordAndSenteneCard` , `IsClickCard`, `IsSentenceCard` , `IsAudioCard`: These card types are not needed for a good workflow and clutter the card template unnecessarily.

If you do want to use furigana insertion, consider using the original Lapis or another template that supports it.
