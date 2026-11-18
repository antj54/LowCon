# Decisions pending paste-in

*Entries proposed on 2026-11-18 that aren't in `02-decisions-log.md` yet. Paste them into the log (newest at the top), make the doc changes listed below, then delete this file. Superseded entries are marked so you can skip or keep them for history.*

## Log entries

| # | Date | Decision | Why / notes |
| --- | --- | --- | --- |
| 34 | 2026-11-18 | Working title: **Low Confidence** | Names the core mechanic, matches the project and repo, and carries the dry tone |
| 33 | 2026-11-18 | Customers: a small recurring cast of 2–3 decision-makers who rotate across crises and remember your track record | Variety plus "the world remembers." Credibility carries across crises in a way you feel. |
| 32 | 2026-11-18 | You can't be fired. At rock-bottom credibility you're **reassigned**: you lose your team and unlocks but keep your track record. | Real stakes without wiping weeks of daily play. Built in Phase 3. |
| 31 | 2026-11-18 | Setting: **fictional countries placed in real regions**. Crisis 01's Kordav and Elsin stay as they are. | Won't date, accuses no real government, keeps real terrain and threat types |
| 30 | 2026-11-18 | Blind playtest runs on a separate playtest build: results sync automatically to a shared record, with optional one-tap reactions, a per-item "Not realistic?" flag and a 4-question end debrief. The owner sees a Testers tab. | The tester shouldn't have to fill anything in. The realism flag captures an intel professional's judgment where it matters. |
| 29 | 2026-11-18 | Project docs are mirrored in the repo under `docs/`. The claude.ai project stays the source of truth for docs, and the repo copy is refreshed when they change. | Everything about the game lives in one repo, without two copies that can both be edited |
| 28 | 2026-11-18 | The GitHub repo `antj54/LowCon` (public) is the source of truth for code and crisis data. The claude.ai page is the published build, updated from the repo. | Version history and a home for the code outside the chat. `tools/simulate.js` is the balance check to run after any change. |
| 27 | 2026-11-18 | The time-per-day measure counts active time only (page visible, input in the last 2 minutes) | Day 1 showed 28 minutes because idle time counted |
| 26 | 2026-11-18 | Situation map: plots reporting as it arrives (planted items included), own forces and doubted items. Ground truth appears only in the postmortem, by day. | Gives an evolving picture of the scenario while keeping the deception intact. The postmortem overlay is the payoff. |
| 25 | 2026-11-18 | Each day opens with a morning read-in: public events, countdown, own posture, yesterday's line. It never states hidden truth. | Shows how the overall picture is changing without becoming an answer key |
| 24 | 2026-11-18 | Crisis length stays at 5 days | Anthony's playtest: 5 was enough |
| 23 | 2026-11-18 | Halvorsen commits in proportion to confidence: Moderate sends a lead company, High the full battalion. Deterred needs the battalion in place by the Day 4 brief; a company alone or a battalion only on Day 5 gets Standoff. | High confidence had no effect in the world, so Moderate dominated. Now confidence is a real call and teaches calibration. |
| 22 | 2026-11-18 | Each item has one per-item judgment, **Doubt this report**: the player judges the information false or deliberately misleading. The source letter can't be challenged per item. Scoring as in #19. Replaces the wording of #19. | A good source can carry a bad report (R-4-02 arrives B2 and is planted). Attacking the letter would punish the channel for the adversary's trick. |
| 21 | 2026-11-18 | Every planted item has a tell in its own text and at least one cross-check: an item available by that day that contradicts it. The postmortem names the tell, the cross-check item IDs and the adversary's motive. | Deception has to be explainable from the evidence, not asserted by the answer key |
| 20 | 2026-11-18 | Source reliability belongs to the source, not to each report. It shows on the roster, and from Phase 3 it changes between crises based on the source's track record. | Matches real tradecraft and the design doc. Supports "the world remembers." |
| 19 | 2026-11-18 | *(Wording superseded by #22.)* Item grading is accept or challenge: each item arrives with the collector's grade, and the player can challenge it. Planted +1, true −1, noise and clutter 0. Replaces #16. | Re-entering a grade already on the card was busywork |
| 18 | 2026-11-18 | Progress saves to the player's account through the page's private per-user storage, with a copy on the device as a fallback | Keeps #7 ("play from any device") with no server of our own |
| 17 | 2026-11-18 | Day lock on by default; a Play ahead switch is available from the start | Matches the design doc and keeps playtests quick. Resolves the open "one day per real day" question. |
| 16 | 2026-11-18 | *(Superseded by #19.)* Phase 1 records grades but doesn't score them | |
| 15 | 2026-11-18 | Phase 0 gate passed for Crisis 01, and the Phase 1 build is published | Anthony read it and judged it fun and believable |
| 14 | 2026-11-18 | An early false alarm has a cost: troops moved on Day 1 or 2 are ordered back on Day 3 and moves are frozen for 48 hours | Stops "always assume the worst" from getting the best ending |
| 13 | 2026-11-18 | Scoring: Right/Wrong = Low +1/−1, Moderate +2/−2, High +3/−4. Cited evidence scores true +1, noise 0, clutter −1, planted −2. Plus an ending bonus or penalty. | High only pays off above about ⅔ certainty |
| 12 | 2026-11-18 | Ground truth can change during a crisis. Each daily brief is scored against what was true that day. | Intent really does change. Serves "every day counts." |
| 11 | 2026-11-18 | Authoring rule 4 amended: in Phase 1 crises the diagnostic item arrives in the normal inbox. From Phase 2 on, at least one diagnostic item has to come from collection. | Phase 1 has no collection |
| 10 | 2026-11-18 | First crisis: Border buildup, "Exercise or Operation?", 5 days, with made-up stand-in country names | Easiest first-time question, the truth changes mid-crisis, and every plant can be caught from the inbox |

**Open questions this resolves:** all six. First crisis seed (#10), play ahead (#17), real vs fictional countries (#31), getting fired (#32), one customer or many (#33), working title (#34). The open questions list in the log can be emptied.

## Doc changes

### `01-design-doc.md`

- **Core loop:** add a step before "Read the inbox": *"0. Morning read-in (about 15 sec). What's changed in public, the countdown, your forces' posture and the map."*
- **Core loop, step 2:** replace "Grade each item, flag anything that doesn't add up" with *"Decide whether to believe each item: doubt anything you judge false or deliberately misleading, and flag clutter as not relevant."*
- **Sources and reliability:** replace "The grade you see is the one you assign" with *"Each item arrives with the collector's grade. You decide whether to believe the report. A source's file grade updates between crises as it builds a track record."*
- **Customer and consequences:** add *"The customer commits in proportion to your confidence. A Moderate brief buys a partial move, and a High brief buys the full one."*
- **Platform and tech:** add *"A situation map plots reporting as it arrives. The real positions appear only in the postmortem."* and *"Code and crisis data live in the GitHub repo `antj54/LowCon`. The claude.ai page is published from it."*
- **Title:** change the header to *"Low Confidence — Game Design Doc"* and replace the working-title options line with *"Working title: **Low Confidence**."*
- **Setting:** replace the first sentence with *"The game uses fictional countries placed in real regions in the early 2030s."*
- **Customer** (under Setting): replace with *"A small recurring cast of 2–3 decision-makers, each with a personality and priorities. One runs each crisis, and they remember your track record."*
- **Credibility** (under Player role and progression): add *"You can't be fired. At rock-bottom credibility you're reassigned to a new cell: you lose your team and unlocks but keep your track record."*
- **Roadmap:** move *(current)* from **0 · Paper prototype** to **1 · First playable (MVP)**.

### `03-crisis-content.md`

- **Rule 2:** *"Every planted item has **at least one tell in its own text and at least one cross-check**, an item available by that day that contradicts it. Deception must be beatable, not random."*
- **Rule 4:** add *"(Phase 1: the diagnostic item arrives in the normal inbox. Phase 2+: at least one must come from collection.)"*
- **Rule 5:** add *"For planted items, the postmortem states the tell, the cross-check by item ID and the adversary's motive."*
- **Data format:** now **v0.3**. Point to `crises/border-buildup.json` in the repo as the working example. New fields since the draft are listed at the end of `crisis-01-gm-key.md`.
- **Scripted crises:** replace "None yet" with *"Crisis 01: Exercise or Operation? (Border buildup). Data: `crises/border-buildup.json`. Phase 0 script: `docs/crisis-01-player-packet.md` and `docs/crisis-01-gm-key.md`."*

## Parking lot

- The adversary reacting to the customer's moves (for example switching crossings if forces move early). Phase 3–4.
- Reverse image search as an OSINT action. Phase 2.
- Pressure from the liaison partner ("act alone") as its own mechanic. Phase 3.
- Tapping a map area to aim collection there. Phase 2.
- Letting the player mark their own judgments on the map. Phase 3.
