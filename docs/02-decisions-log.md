# Low Confidence — Decisions Log

*Newest entries at the top. This file wins over the design doc when they disagree. Anything still open is listed at the bottom. Superseded entries stay for history and are marked.*

## Decisions

| # | Date | Decision | Why / notes |
| --- | --- | --- | --- |
| 39 | 2026-11-18 | Remove the free-text "Reasoning" box from the brief. The brief instead writes a key-judgment line from the player's picks. **Build with #38 after the playtest.** | It affected nothing and both players left it empty every day. The cited evidence already is the reasoning, in structured form. |
| 38 | 2026-11-18 | Split the call into **likelihood** (chosen by the player) and **confidence** (derived from the evidence they cite), following ICD 203 and the UK PHIA framework. The customer acts on both. Replaces the single "confidence" dial. **Build after the playtest.** See "Queued after playtest." | The single dial used likelihood words under a confidence label, the combination ICD 203 warns against. Both intel-trained players stayed at Moderate, which is sound tradecraft the game punished. Deriving confidence from cited evidence keeps it to one tap and makes choosing evidence matter more. |
| 37 | 2026-11-18 | Don't tell the player how many days a crisis lasts. In-world deadlines (like the exercise's announced end date) stay. **Change after the playtest.** See "Queued after playtest" below. | Real analysts don't know when a crisis ends. A visible day count lets players play the calendar instead of the evidence, especially on the last day. |
| 36 | 2026-11-18 | Keep the company outcome: a Moderate brief sends a company that holds the dam but doesn't deter the invasion. Kordav crosses at Dolan and isolates it (Standoff). The tripwire and "eyes forward" alternatives are rejected for now. | Anthony's SME judgment: a company wouldn't deter in this situation. Partial commitment is a real consequence of under-calling a clear warning. |
| 35 | 2026-11-18 | The playtest build has Play ahead on by default, so testers can play all 5 days in one sitting. The main build keeps the daily lock. | Removes the 5-day wait for feedback. Time per day is still measured, so turn length stays testable. |
| 34 | 2026-11-18 | Working title: **Low Confidence** | Names the core mechanic, matches the project and repo, and carries the dry tone |
| 33 | 2026-11-18 | Customers: a small recurring cast of 2–3 decision-makers who rotate across crises and remember your track record | Variety plus "the world remembers." Credibility carries across crises in a way you feel. |
| 32 | 2026-11-18 | You can't be fired. At rock-bottom credibility you're **reassigned**: you lose your team and unlocks but keep your track record. | Real stakes without wiping weeks of daily play. Built in Phase 3. |
| 31 | 2026-11-18 | Setting: **fictional countries placed in real regions**. Crisis 01's Kordav and Elsin stay as they are. | Won't date, accuses no real government, keeps real terrain and threat types |
| 30 | 2026-11-18 | Blind playtest runs on a separate playtest build: results sync automatically, with optional one-tap reactions, a per-item "Not realistic?" flag and a 4-question end debrief. The owner sees a Testers tab. | The tester shouldn't have to fill anything in. The realism flag captures an intel professional's judgment where it matters. |
| 29 | 2026-11-18 | Project docs are mirrored in the repo under `docs/`. The claude.ai project stays the source of truth for docs, and the repo copy is refreshed when they change. | Everything about the game lives in one repo, without two copies that can both be edited |
| 28 | 2026-11-18 | The GitHub repo `antj54/LowCon` (public) is the source of truth for code and crisis data. The claude.ai page is the published build, updated from the repo. | Version history and a home for the code. `tools/simulate.js` is the balance check to run after any change. |
| 27 | 2026-11-18 | The time-per-day measure counts active time only (page visible, input in the last 2 minutes) | Day 1 showed 28 minutes because idle time counted |
| 26 | 2026-11-18 | Situation map: plots reporting as it arrives (planted items included), own forces and doubted items. Ground truth appears only in the postmortem, by day. | An evolving picture of the scenario that keeps the deception intact. The postmortem overlay is the payoff. |
| 25 | 2026-11-18 | Each day opens with a morning read-in: public events, countdown, own posture, yesterday's line. It never states hidden truth. | Shows how the overall picture is changing without becoming an answer key |
| 24 | 2026-11-18 | Crisis length stays at 5 days | Anthony's playtest: 5 was enough |
| 23 | 2026-11-18 | The customer commits in proportion to confidence: Moderate sends a lead company, High the full battalion. Deterred needs the battalion in place by the Day 4 brief; a company alone or a battalion only on Day 5 gets Standoff. | High confidence had no effect in the world, so Moderate dominated. Now confidence is a real call and teaches calibration. |
| 22 | 2026-11-18 | Each item has one per-item judgment, **Doubt this report**: the player judges the information false or deliberately misleading. The source letter can't be challenged per item. Doubting a planted item +1, a true item −1, noise and clutter 0. | A good source can carry a bad report (R-4-02 arrives B2 and is planted). Attacking the letter would punish the channel for the adversary's trick. |
| 21 | 2026-11-18 | Every planted item has a tell in its own text and at least one cross-check: an item available by that day that contradicts it. The postmortem names the tell, the cross-check item IDs and the adversary's motive. | Deception has to be explainable from the evidence, not asserted by the answer key |
| 20 | 2026-11-18 | Source reliability belongs to the source, not to each report. It shows on the roster, and from Phase 3 it changes between crises based on the source's track record. | Matches real tradecraft. Supports "the world remembers." |
| 19 | 2026-11-18 | *Superseded by #22.* Accept-or-challenge grading of the received grade | Re-entering a grade already on the card was busywork |
| 18 | 2026-11-18 | Progress saves to the player's account through the page's private per-user storage, with a copy on the device as a fallback | Keeps #7 ("play from any device") with no server of our own |
| 17 | 2026-11-18 | Day lock on by default; a Play ahead switch is available from the start | Matches the design doc and keeps playtests quick |
| 16 | 2026-11-18 | *Superseded by #19.* Phase 1 records grades but doesn't score them | |
| 15 | 2026-11-18 | Phase 0 gate passed for Crisis 01, and the Phase 1 build is published | Anthony read it and judged it fun and believable |
| 14 | 2026-11-18 | An early false alarm has a cost: troops moved on Day 1 or 2 are ordered back on Day 3 and moves are frozen for 48 hours | Stops "always assume the worst" from getting the best ending |
| 13 | 2026-11-18 | Scoring: Right/Wrong = Low +1/−1, Moderate +2/−2, High +3/−4. Cited evidence scores true +1, noise 0, clutter −1, planted −2. Plus an ending bonus or penalty. | High only pays off above about ⅔ certainty |
| 12 | 2026-11-18 | Ground truth can change during a crisis. Each daily brief is scored against what was true that day. | Intent really does change. Serves "every day counts." |
| 11 | 2026-11-18 | Authoring rule 4 amended: in Phase 1 crises the diagnostic item arrives in the normal inbox. From Phase 2 on, at least one diagnostic item has to come from collection. | Phase 1 has no collection |
| 10 | 2026-11-18 | First crisis: Border buildup, "Exercise or Operation?", 5 days | Easiest first-time question, the truth changes mid-crisis, and every plant can be caught from the inbox |
| 9 | 2026-11-18 | Knowledge files split into a design doc, this log and a crisis content file, all in Markdown | Each can be updated on its own; Markdown is easiest for Claude to read |
| 8 | 2026-11-18 | Tradecraft realism: **authentic but simplified** | Real concepts (Admiralty grading, estimative confidence, ACH, PIRs) streamlined so a daily turn stays short |
| 7 | 2026-11-18 | Platform: phone-first single-page web app published as an artifact, saved progress, no server for the MVP | Lets Anthony play from any device with no setup |
| 6 | 2026-11-18 | Roadmap runs in gated phases 0–4; MVP = Phase 1 (one 5-day crisis) | Prove it's fun before adding systems |
| 5 | 2026-11-18 | Setting: early 2030s, all leaders, groups, units and companies fictional (countries refined by #31) | Grounded but won't date badly; no real people depicted |
| 4 | 2026-11-18 | Session style: **short daily turns** (about 8 min), one in-game day per real day | Phone-friendly daily habit |
| 3 | 2026-11-18 | Gameplay feel: **balanced mix**; analysis puzzles feed resource decisions | |
| 2 | 2026-11-18 | Setting era: **near-future real world** | |
| 1 | 2026-11-18 | Player role: **analysis cell lead** | Hands-on with the material, answerable to a customer, manages a small team |

## Open questions

- [ ] Which seed should Crisis 02 use? (It has to prove the Phase 2 systems generalize. The defector walk-in would punish "always trust HUMINT.")
- [ ] Does Crisis 01 get a named real region, or stay unnamed?

## Queued after playtest

Changes already decided, held until the Crisis 01 playtest results are in so the test runs on one version.

- **Hide the crisis length (#37).** Remove the day count everywhere the player sees it: the header ("Day 2 of 5" becomes "Day 2"), the opening screen ("5-day arc"), the playtest note ("all 5 in one sitting") and the playtest invite text. Keep the countdown to the exercise's announced end, which is in-world. On Day 5, drop "This is your last brief before the announced end date" from the read-in; the countdown line already says "Tomorrow is the announced end of IRON HARVEST (the 20th)," which gives the deadline without saying the game ends there.

- **Likelihood plus derived confidence (#38).** Starting sketch, all values to tune with `tools/simulate.js`:
  - **Likelihood (one tap):** Roughly even (≈50%), Likely (55–80%), Very likely (80–95%), Almost certain (95–99%), using ICD 203 wording. Scored as a probability call, so over-claiming costs more than under-claiming.
  - **Confidence (shown, not chosen):** worked out only from what the player can see in the evidence they cite: how many distinct sources, how many disciplines, and the grades they arrived with. Draft: High = 3 items from at least 2 disciplines with at least 2 sources graded A–B. Moderate = at least 2 sources with at least 1 graded A–C. Low = anything less. Never uses hidden truth, so a cited plant still counts toward confidence; the evidence score is where that costs you.
  - **Coherence check:** the brief warns about an incoherent pairing (for example "almost certain" with Low confidence) before you send.
  - **Customer policy:** full battalion = Very likely or Almost certain with at least Moderate confidence. Lead company = Likely, or a higher likelihood with Low confidence. Readiness = Roughly even. Pull-back rules as now.
  - **Words in the game:** the brief reads like a real key judgment: "We assess it is very likely… (moderate confidence)."
  - **Docs to update when built:** design doc core loop step 4 and calibration scoring, crisis content `scoring` and `customerPolicy` fields, Crisis 01 key and postmortem lesson 4.
- **Remove the Reasoning box (#39).** Build with #38: drop the textarea from the brief and the Note column from the playtest log, and show the generated key-judgment line ("We assess it is very likely… (moderate confidence), based on R-4-01, R-3-02") in the brief, the send confirmation, the earlier-days record and the postmortem.

## Parking lot

- Free-text reasoning that matters: Claude reads the player's reasoning and the customer reacts to it (for example, spotting a weak basis). Phase 4.
- Variable crisis length: a crisis ends early or runs on depending on the truth and the player's calls. Phase 3–4.

- The adversary reacts to the customer's moves (for example switching crossings if forces move early). Phase 3–4.
- Reverse image search as an OSINT action. Phase 2.
- Pressure from the liaison partner ("act alone") as its own mechanic. Phase 3.
- Tapping a map area to aim collection there. Phase 2.
- Letting the player mark their own judgments on the map. Phase 3.

## Status

**Phase 1 · First playable.** Crisis 01 is built and published. Blind playtest out to testers on 2026-11-18; the Phase 1 gate waits on their results.
