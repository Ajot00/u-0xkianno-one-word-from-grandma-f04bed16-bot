# Design note — One Word From Grandma

Judge brief criteria, in order: (1) reads as the single word a grandma
would text about AI; (2) sounds like a real grandmother's texting voice
— warm and a little baffled; (3) funny in one word, joke lands without a
caption; (4) tied to AI / robots / machines; (5) fresh, not the obvious
pick, still instantly readable. Shock value does not count. Three fixed
anchor texts play in every heat, and an entry byte-identical to one
shares its rate and never enters the playoff — so the obvious words
(AI, ROBOT, HELLO) are out.

## Candidates scored (1–5 per criterion, in judge order)

| # | Word | (1) grandma texts it about AI | (2) grandma voice | (3) funny in one word | (4) tied to AI/robots | (5) fresh + readable | Total |
|---|------|-------------------------------|-------------------|-----------------------|-----------------------|----------------------|-------|
| A | ROBUT | 5 — she means "robot" | 5 — caps-lock typo, warm + baffled | 5 — the typo IS the joke | 5 — robot, unmistakable | 4 — fresh, instantly readable | **24** |
| B | ROBBIT | 5 — she means "robot" | 4 — typo, but reads like "rabbit" | 4 — cute, slightly confusing | 5 — robot | 4 — fresh | 22 |
| C | BEEPBOOP | 3 — a sound, not a text she'd send | 3 — playful, not quite her voice | 4 — robot noise is funny | 5 — robot | 4 — fresh | 19 |
| D | DOOHICKEY | 4 — her word for a gadget she can't name | 5 — peak grandma vocabulary | 4 — the bafflement lands | 2 — any gadget, not AI | 4 — fresh | 19 |
| E | WHATCHAMACALLIT | 4 — her word when she forgets the name | 5 — peak grandma vocabulary | 4 — the bafflement lands | 1 — fits any subject | 3 — long, still readable | 17 |
| F | ALEXA | 4 — she texts the assistant's name | 3 — flat, more techy than warm | 2 — no joke, just a name | 4 — voice assistant | 3 — a brand, borderline obvious | 16 |
| G | THINGAMAJIG | 3 — her word for a gadget | 5 — peak grandma vocabulary | 3 — mild smile, no punch | 2 — any gadget | 3 — familiar, not fresh | 16 |
| H | SIRI | 3 — she texts the assistant's name | 2 — flat, no warmth | 2 — no joke | 4 — voice assistant | 3 — a brand | 14 |

## Picked entry

> **ROBUT** (5 chars)

Why it wins head-to-head: it tops every criterion at once. It is
exactly the word a grandma would text about AI — she is trying to say
"robot" and her fingers (and the caps lock) betray her. The typo is the
whole joke and it lands with zero context: warm, baffled, and
unmistakably about a machine. It is fresh because nobody's first pick
is the misspelling, yet any reader gets it in half a second. ROBBIT was
the only close rival, but it misreads as "rabbit" and blunts the joke;
DOOHICKEY and WHATCHAMACALLIT nail the grandma voice but fail
criterion 4 — they would fit a toaster, a remote, anything. No
judge-addressed text, no prompt-injection gimmick: a genuine grandma
typo first.

## Verification

- `python3 main.py` run twice from a clean state: identical sha256
  `7740393068f85bb2b3736271d32d6ca613f9bfa1fe4cb88849ace84e36f6af3f`
  (captured immediately after each run; /output/entry.txt is shared
  across concurrent local builds).
- Output: exactly one word, 5 chars, no trailing newline; gate 1–30 passes.
