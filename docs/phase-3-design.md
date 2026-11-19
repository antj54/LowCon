# Phase 3 design (paper) · Low Confidence

*Status: in build since #61 (Phase 2 gate waived). Originally a paper design. Drafted 2026-11-18; the four choices were settled the same day (#58), all as recommended. The Phase 2 gate is still open (#55), so this stays on paper until Anthony says otherwise.*

**Phase 3 scope (from the design doc):** three linked scenarios, analysts with traits, unlocks, the recurring customer cast, reassignment, and sources and deception that carry across scenarios.
**Gate to Phase 4:** a full campaign holds up over weeks of daily play.
**Constraint from Anthony:** Scenario 03 is not another defector.

## What Phase 3 adds, in one line each

| System | What the player feels |
| --- | --- |
| Service record | What you did in one scenario is still true in the next |
| Credibility that carries | A customer who was burned by you starts out wary; one you served well gives you room |
| Sources that carry | A burned source stays gone, and file grades move with each source's track record |
| Deception that carries | The adversary reuses the channel that fooled you last time |
| Analysts | Short notes on items from people who are usually right, each wrong in their own way |
| Scenario 03 | A scenario where suspicion is the mistake |

## 1. The service record

One record per player, kept beside the scenario saves. It holds:

- Each finished scenario: ending, score, final credibility with that customer
- Each source's state: available or burned, and its current file grade
- Flags the adversary can use: which kinds of planted item you cited as evidence
- Your team: which analysts you have

The main menu gains a **Service record** screen that shows all of this in plain words. It's the "world remembers" pillar made visible.

**The hard question is replays.** Scenarios can be replayed and, once unlocked, played in any order (#54). So which run counts?

| Option | How it works | Tradeoff |
| --- | --- | --- |
| **A. First finish is on the record** (recommended) | Your first completed run of each scenario writes the record. Replays are marked "off the record": scored and reviewed, but they change nothing. | The world really does remember, and nobody can replay their way out of a burned source. A bad first run is permanent, so reassignment (section 6) has to be a real way forward. |
| B. Latest finish counts | Every completed run overwrites the record | Forgiving, but a player who knows the answers can clean the record in ten minutes, and consequences stop meaning anything |
| C. Player chooses | After a replay, ask "put this on the record?" | Flexible, but it turns consequences into a menu option |

## 2. Credibility across scenarios

Built on #43 and #50. Inside a scenario nothing changes: it only drops, and only on what the customer can see.

- **Same customer again:** you start where you ended with them last time, outcome adjustment included. Deterred with Halvorsen means starting his next scenario at 5; Seized means starting at 1, already Discounted.
- **New customer:** they start at 3, moved one step by your overall record. "She's read your file."
- **Gains** happen only between scenarios, through outcomes. That keeps "always High" from paying off mid-scenario.
- **A reason to care at the top:** at 5, the customer grants one extra collection point a day. This is the first unlock, and it's earned rather than given.

## 3. Sources and deception that carry

**Sources**

- **Burned stays burned.** If KESTREL or FINCH was burned on the record, they are gone from every later scenario that would have used them. Each such scenario must give a costlier or slower way to the same answer, so a burned source hurts without locking the player out (the #51 two-path rule).
- **File grades move** (#20). Between scenarios each source's letter grade shifts one step with its track record: up if its reporting held, down if it didn't. The roster shows the change and the reason. WREN, wrong on Days 1–2 of Scenario 01 and right on Day 4, is a good first example.
- **The grade still isn't the answer.** A source upgraded for honesty can still carry a planted item, as MERIDIAN did twice.

**Deception**

- The record notes which kinds of plant you cited as evidence (citing only; not doubting one doesn't count, #62): state media, staged signals traffic, a recycled photo, a dangle's prepared detail.
- Each later scenario has one or two authored **callback items** that appear only if the matching flag is set. If the staged recall fooled you in Scenario 02, Scenario 03 stages something on a net again. If you caught it, the adversary tries a channel you haven't been tested on.
- Authored, not generated, so every callback still has a tell and a cross-check, and the postmortem can say: "They tried this because it worked on you last time."

## 4. Analysts

The design doc gives you 2 analysts to start and up to 4, each with a specialty and a trait. The risk is turning an 8-minute turn into a staffing game.

| Option | How it works | Tradeoff |
| --- | --- | --- |
| **A. Notes only** (recommended) | Each analyst attaches one short note a day to one item in their specialty. No assigning, no management. The player's job is to learn whose notes to trust. | Adds reading, not steps: about 20 seconds a day. All authored, so every wrong note can be explained in the postmortem. Less agency than B. |
| B. Assign analysts | Each day you put analysts on items or on collection targets, and they produce a note or a small bonus | Real management decisions, but it adds a step to every turn and competes with collection for the player's attention |
| C. Defer analysts to Phase 4 | Ship Phase 3 with the record, carry-over and Scenario 03 only | Smaller phase, but analysts are in the Phase 3 scope and are the main source of dry humor in the pitch |

**Under option A:**

- **Traits decide how an analyst goes wrong**, and the error is authored, not rolled:
  - *Overconfident:* never hedges. Right most days, and flatly wrong once per scenario in a way the evidence could have caught.
  - *Slow but careful:* always right, but the note arrives a day after the item.
  - *Anchors on the first theory:* reads every new item as support for the Day 1 hypothesis. Useful until the truth moves.
- **Starting pair:** a regional analyst who anchors, and a technical analyst (signals and imagery) who is slow but careful. **Third,** unlocked after Scenario 02: an OSINT analyst who is overconfident. **Fourth,** after Scenario 03: to be designed.
- **Notes are opinion, not evidence.** They can't be cited or doubted, and they don't score. The postmortem shows each analyst's hit rate, which is how you learn who to trust.
- **Names** are fictional, like everyone else. Working names: Imre Vasko (regional), Noor Halden (technical), Tess Marrow (OSINT).
- **Retrofit:** notes get written for Scenarios 01 and 02 as well, so the team exists from the first day of a new campaign. On the record, they appear from whenever the player reaches Phase 3 content.

## 5. Scenario 03

**What it has to do**

1. Not be a defector story.
2. Make reflexive suspicion cost something. Scenario 01 rewards trusting HUMINT; Scenario 02 rewards distrusting it. Scenario 03 has to stop "always assume deception" from becoming the new habit, which is also the real fix for the Scenario 02 balance problem (#56).
3. Use what carries: at least one returning source, one returning customer or a new one who has read your file, and one callback item.
4. Play differently again: a different question, decision and discipline mix.

**How suspicion becomes the mistake:** the item that looks most like a plant is genuine. It comes from a low-graded or agenda-aligned source, at a convenient time, and it says what someone wants said. But it has no tell in its own text, and independent collection supports it. Meanwhile the tidiest, best-graded item of the scenario is noise. A player who doubts on appearance loses points and misses the call; a player who checks before doubting gets it right. The lesson: a tell is something you can point to, not a feeling.

**Seed options**

| Seed | Core question | Why it fits | Tradeoff |
| --- | --- | --- | --- |
| **A. Pipeline militia** (recommended) | A militia is attacking a pipeline in Elsin's south. Is it acting alone, backed by Kordav, or backed by a third neighbour playing both sides? | Liaison-heavy, which neither earlier scenario is. WREN returns with a track record and an agenda, and this time its alarm is right from the start, which is the "suspicion is the mistake" turn. Attacks give the map something to plot, and imagery has a real job again. Truth can shift mid-scenario when the backer changes its mind. | Three actors plus a militia is a lot of names. Needs care to stay readable on a phone. |
| B. Missing shipment | Dual-use components vanished between two ports. Where are they, and who has them? | The most collection-driven seed, and hypotheses that are places would be new. An anonymous tip that looks too good and is true gives the suspicion turn. | More of a search than a judgment. The confidence call matters less, and that's the game's core. |
| C. Ransomware group | Criminal crew, or working for a state? | A very different discipline mix, and a false flag is a natural deception | Needs technical depth to stay authentic, has little for a map, and the "trust is right" turn is harder to build into an attribution question |

**Customer for Scenario 03**

| Option | Tradeoff |
| --- | --- |
| **A. Halvorsen returns** (recommended) | The first time a customer remembers you. His opening line and his starting credibility depend on how Scenario 01 ended. A pipeline under attack is a force-protection problem, which is his job. |
| B. A third cast member | More variety, and #33 allows up to three. But nobody has yet come back, so "they remember your track record" would still be untested after three scenarios. |

**Sketch under A and A** (to be scripted Phase 0 style once the seed is chosen): Halvorsen has to decide where to put a limited guard force along the pipeline, and whether to tell Elsin that a neighbour is funding the attacks. WREN pushes a warning on Day 1 that names the backer. It looks like Elsin's usual agenda, and it's correct. A clean, well-graded intercept points at Kordav and is noise: old traffic, re-reported. If KESTREL survived Scenario 01, he can be tasked for a cheap confirmation; if he was burned, the same answer costs an imagery tasking and a day.

## 6. Reassignment (#32)

- **Trigger:** finishing a scenario on the record with credibility 0 with its customer.
- **Effect:** you are reassigned to a new cell. You lose analysts beyond the starting two and the extra collection point, and credibility with every customer resets to 2 (Questioned). Burned sources stay burned and the record keeps everything.
- **Tone:** dry, not punishing. A posting notice, not a game over.

## 7. Build order

Each step is playable on its own.

1. **Service record** *(built, #61)*: written at the end of Scenarios 01 and 02, shown on the main menu.
2. **Carry-over** *(built, #61)*: starting credibility, burned sources and file grades applied in Scenarios 01 and 02 as they exist.
3. **Analyst notes** *(built, #63)* written into Scenarios 01 and 02.
4. **Scenario 03 on paper** (player packet and key; done, #59), then as data, with its callback items.
5. **Reassignment.**
6. **Playtest** the full campaign, which also closes the Phase 2 gate.

## Parking lot (Phase 4 or later)

- Callback items written by Claude inside a template, instead of authored by hand
- Analysts who improve or leave
- Customers who talk to each other about you
- A fourth analyst's trait

## Decisions (settled 2026-11-18, #58)

1. What goes on the record: **A, the first finish**
2. Analysts: **A, notes only**
3. Scenario 03 seed: **A, pipeline militia**
4. Scenario 03 customer: **A, Halvorsen returns**
