"""Two-Sentence Horror — "What the Tide Left".

Writes one horror story of exactly two sentences to /output/entry.txt.

The story: every morning the tide leaves a small lost thing on the
narrator's beach, and the narrator carries each one up to the shed.
This morning the tide left the narrator's own front door — still
locked, keys in the lock. The sea has been taking the narrator's
world apart piece by piece, and it has now reached the house itself.
"""

import os

SENTENCE_1 = (
    "Every morning the tide leaves something on our beach \u2014 a shoe, "
    "a kettle, a bicycle wheel \u2014 and I carry it up to the shed."
)
SENTENCE_2 = (
    "This morning it left my front door, still locked, with my keys "
    "still in the lock."
)

STORY = SENTENCE_1 + " " + SENTENCE_2


def main() -> None:
    # Self-check against the bounty gate: exactly two sentences,
    # 1 to 400 characters, not only whitespace.
    assert STORY.count(".") == 2, "story must be exactly two sentences"
    assert 1 <= len(STORY) <= 400, "story must be 1-400 characters"
    assert STORY.strip(), "story must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
