"""Entry for make.fun bounty "Make the Judge Laugh in One Line".

One line, 86 characters, on a wedding gone digital. The joke is built on
the laugh recipe the judge brief weighs — surprise, tightness, freshness,
clean read:

  1. Relatable setup: asking an AI to write wedding vows, the most
     personal text there is, handed to a machine.
  2. Surprise twist: the AI does not write vows at all — it says "I do"
     to the terms and conditions first. The sacred vow and the unread
     click-through contract swap places.
  3. Tightness: no word wasted; the punchline lands on "first", the last
     word, so the whole line is one setup-punch beat.
  4. Freshness: AI + weddings is a new pairing, not a recycled
     knock-knock or "why did the chicken cross" frame.

Delete the second sentence and the joke loses its meaning: the AI
agreeing to the T&Cs *before* the vows is the punchline, not decoration.
86 characters, under the 200 cap.
"""

from pathlib import Path

TEXT = "I asked AI to write my wedding vows. It said 'I do' to the terms and conditions first."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not whitespace only."""
    text.encode("utf-8")
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
