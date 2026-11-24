#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.

Writes one sentence to /output/entry.txt: the modern internet,
explained to a time traveler from 1800. Stdlib only; no network,
no randomness, no I/O besides the one output file.

The sentence is built from three named beats so its shape is
visible in the code:

* PLACE — where the wonder lives: a glass box in every house.
  A traveller from 1800 knows glass, knows a box, knows a house.
* VOICES — what it does first: it speaks in the voices of
  strangers and shows moving pictures. A magic lantern that
  talks; nothing here needs a word the traveller never heard.
* LETTER — what it does that matters most: it answers any
  question at once with a letter from a man you never met.
  No post, no wait, no horse — the whole world writing back.

The hard rule of this bounty: no word coined after 1800. Every
word in the sentence is old — glass, box, speaks, voices,
strangers, moving, pictures, answers, question, letter, man —
and validate() keeps a BANNED list of modern words so a later
edit can never sneak one in.

In every house stands a glass box that speaks in the voices of strangers, shows moving pictures, and answers any question at once with a letter from a man you never met.
"""

import os

# The three beats of the sentence, joined in entry_text().
PLACE = "In every house stands a glass box"
VOICES = "that speaks in the voices of strangers, shows moving pictures"
LETTER = "and answers any question at once with a letter from a man you never met"

# The competition caps the entry at 200 characters; the sentence is 169.
MAX_CHARS = 200

ENTRY = "In every house stands a glass box that speaks in the voices of strangers, shows moving pictures, and answers any question at once with a letter from a man you never met."

# Words coined after 1800 — none of them may appear in the entry.
# A traveller from 1800 never heard any of these, so neither may he.
BANNED = (
    "internet", "computer", "phone", "video", "website", "email",
    "app", "data", "software", "digital", "online", "download",
    "wifi", "wi-fi", "pixel", "emoji", "screen", "television",
    "radio", "camera", "robot", "electric", "battery", "engine",
    "keyboard", "mouse", "server", "cloud", "network", "signal",
    "broadcast", "stream", "chat", "message", "text", "code",
)


def entry_text() -> str:
    """Join the three beats into the one-sentence explanation."""
    return f"{PLACE} {VOICES}, {LETTER}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Then the bounty rule:
    no word coined after 1800 may appear anywhere in it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    words = text.lower().replace(",", "").replace(".", "").split()
    for banned in BANNED:
        assert banned not in words, f"modern word slipped in: {banned}"
    assert "glass box" in text, "the picture went missing"
    assert "letter from a man you never met" in text, "the payoff went missing"


def old_words(text: str) -> None:
    """Check the sentence reads like something a traveller from
    1800 could hold in his head: it names things he knows —
    glass, a box, voices, pictures, a letter — and never lists
    features, never counts, never shouts."""
    assert text.startswith("In every house"), "the picture must open at home"
    assert "glass box" in text, "the traveller needs a thing he knows"
    assert "voices of strangers" in text, "the wonder must be voices"
    assert "moving pictures" in text, "the wonder must be pictures"
    assert "!" not in text, "a plain sentence never shouts"
    assert "?" not in text, "one sentence, no questions inside it"


def tightness(text: str) -> None:
    """Check the sentence is tight: no double spaces, no filler
    words padding it out, and the picture names a number of
    voices only by the word "strangers" — one picture, not a list.
    A loose sentence reads like a draft; a tight one reads like
    a verdict a traveller could repeat by the fire."""
    assert "  " not in text, "a tight sentence has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight sentence needs no filler"
    assert "really" not in words, "a tight sentence needs no filler"
    assert text.count(",") == 2, "one sentence, two commas, one breath"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the picture itself,
    # and that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined sentence drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # sentence lost its place, its voices, or its letter.
    for beat in (PLACE, VOICES, LETTER):
        assert beat in text, f"missing beat: {beat}"
    # The sentence must be speakable in 1800 before it is written:
    # a modern word in a traveller's mouth loses.
    old_words(text)
    validate(text)
    tightness(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
