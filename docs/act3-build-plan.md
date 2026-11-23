# Act 3 build plan · Crises 08 to 10

*Drafted 2026-11-23 (#84). No spoilers: this lists what the engine has to learn, not what the scenarios contain.*

## Order

Build and play one at a time: 08, then 09, then 10. Each one's opening depends on how the last ended, and 09's balance point should be checked against real records before 10 is built.

## What the engine needs

| # | Need | For | Size |
| --- | --- | --- | --- |
| 1 | **Pressure on the record as a condition** (`pressureAtLeast` / `pressureAtMost`), like Alliance today | 09, 10 | Small |
| 2 | **A scenario with versions:** the day's true hypothesis and best call chosen by a record condition (`groundTruth[].by`), and the postmortem saying which version was played | 09, 10 | Medium |
| 3 | **A tasking that is an action:** tasking it sets a flag that stays set (`sets`), other items and results can depend on it, and the Collect tab shows it as in force | 09, 10 (the courier) | Medium |
| 4 | **Targets that exist only if a source survives on the record** (`when: {notBurnedOnRecord}`), across all earlier scenarios | 08, 09, 10 | Small |
| 5 | **Budget changed by the record** (a halved task force, a sixth point at full trust) | 08, 10 | Small |
| 6 | **A deadline in the customer's policy:** "in position" depends on the day of the first High and on a record flag for the starting position | 08, 10 | Medium |
| 7 | **Position items:** an item kind that scores nothing when cited or doubted, shown with a "position" tag in place of a grade | 09 | Small |
| 8 | **A two-day result for one target** in an otherwise next-day discipline (the token) | 09 | Already supported per target |
| 9 | **The campaign's closing screen:** world ending and "you" ending worked out from the whole record, shown after the finale's postmortem, and kept on the Service record | 10 | Medium |
| 10 | **Record flags read across scenarios** in endings and policy (`recordStory` in `endings[].if` and `customerPolicy[].if`) | 09, 10 | Small |

Already in place and reused: items chosen by the previous day's brief, quotes of the player's own key judgment, variables in text, follow-up results, callouts, conditional events, "something to show" in the customer's policy.

## Content work per scenario

- A builder (`tools/build_<id>.py`) and a house-text file, as for 02 to 07.
- Simulator strategies, including one run per version and per starting position.
- Codex entries: new people and places, and a line on each existing entry the scenario changes.
- No new maps. The Codex map gains nothing: all three scenarios use places already on it.

## Checks before each one ships

1. Simulator: best play, always-High on each hypothesis, never above Medium, always hedge, and each record-driven variant.
2. Reload after every day.
3. A phone-width run with a record like Anthony's.
4. Every planted item's tell and cross-check present in the text.

## Open choices for Anthony

1. **Paper or straight to the game?** 09 and 10 can't be played from a packet without someone running them, because the packet would show both versions.
2. **Where 09's balance point sits.** Worth looking at once 08 has been played.
