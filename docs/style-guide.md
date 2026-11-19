# Low Confidence · Writing style guide

*Draft 1, 2026-11-19 (#82). Piloted on Crisis 01. Anthony marks it up; his corrections become the house style for the other scenarios. No spoilers beyond Crisis 01.*

## The idea

Every piece of text should read as if the person or office it comes from wrote it. A depot clerk's report, an imagery readout and a general's reply don't sound alike, and none of them sounds like a narrator.

## Rules

1. **The tell survives word for word.** Before rewriting an item, list its tell and its cross-check phrases from the key. They don't change. Rerun `tools/simulate.js` afterwards.
2. **Facts first, comment labelled.** What was seen or said goes first. Anything the source, the collector or the partner adds is on its own line with a label.
3. **About 60 words an item, at most.** Format adds line breaks, not length. The turn is still 8 minutes.
4. **The card header already names the source.** Don't repeat the code name in the text.
5. **Capitals for code words and exercise names only** (KESTREL, IRON HARVEST). Places and units in normal case.
6. **One dry line a day, at most, and only in clutter.** Customers and analysts aren't comedians.
7. **Oxford spelling** as already used: defence, authorized, mechanized.
8. **Methods stay generic.** Formats below are the publicly known shape of each product, nothing more.

## A format for each channel

| Channel | Shape | Labelled lines |
| --- | --- | --- |
| HUMINT | "Source reports: …" what he saw or was told, in plain sentences | `Access:` how he knows (direct, told by, canteen talk). `Source comment:` his own view |
| SIGINT | The net, the time, a gist. Verbatim only for a short quote | `Comment:` the collector's note on pattern |
| IMINT | Place, pass, weather. One observation per line. Then what was not seen | None. It never states intent |
| Liaison | "Elsin's service assesses/passes: …" kept as theirs | `Sourcing:` what they gave, or "none given". Then what they ask for |
| Wire service | Dateline, then the news in one or two sentences | None |
| State media | Where and when it was said, then the quote | None |
| Social media | What the post shows, how far it spread, what's known about the account | "Unverified." |
| Admin, cables | An office memo. Clutter lives here | None |

## Voices

| Who | How they talk | Never |
| --- | --- | --- |
| **Halvorsen** | Orders and consequences. Units, places, times. Short declaratives. Says what he needs from you next. | Jokes, metaphors |
| **Vasko** | Confident, first person, leans on experience ("I've watched this minister for years"). Commits to a reading. | Hedging |
| **Halden** | Says what she checked and what it showed. Draws the narrowest conclusion. | Opinions on intent |
| **Narrator** (read-in, postmortem, endings) | Plain past tense. Says what happened and names the item. Lessons are one sentence of principle plus the instance from this scenario. | Maxims on their own |

To be written when their scenarios are done: Marlowe (a diplomat: full sentences, precise about who said what to whom), Brandt (an engineer: numbers and hours), Marrow (quick and informal).

## Habits to cut

- A neat closing line on every item, reply and note
- "X, not Y" and groups of three
- The same joke shape in each day's clutter
- Every character being dry in the same way

## Open questions for Anthony

1. Do the `Access:` and `Sourcing:` lines read right, and are they the right labels?
2. Liaison items now say when sourcing is absent or thin. That is more realistic and makes WREN slightly easier to judge. Keep?
3. Is Halvorsen right for a task force commander talking to his intelligence lead?
4. Should pushed HUMINT say how it arrived? It currently doesn't, because KESTREL reports on days when a meeting would break his own rule.
