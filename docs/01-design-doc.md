# Low Confidence — Game Design Doc

*Last updated: 2026-11-18 · Owner: Anthony · Project name: Intel Cell Sim*

> The source of truth for what the game is. Decisions that change this doc are recorded first in `02-decisions-log.md`.

## Pitch and pillars

You lead a small analysis cell. Each day a crisis moves forward, and in 5 to 10 minutes you decide what's true, what to collect next and what to tell your customer. Tomorrow you find out whether you were right.

Working title: **Low Confidence**.

Every feature has to serve at least one of these pillars:

1. **Judgment under uncertainty.** There's no answer key during play. You commit to a call and a confidence level, and the truth only comes out later.
2. **Every day counts.** A full turn fits in one short session on a phone. Each day has one important decision, not twenty small ones.
3. **Authentic tradecraft.** Source grading, confidence language, collection priorities and competing hypotheses are the actual mechanics, not just flavor text.
4. **The world remembers.** Your briefs shape what your customer does. Sources you burn stay burned, and deception that fools you once can come back.

## Core loop: one daily turn

Each in-game day is one turn of about 8 minutes, and it always runs in the same steps. The time for each step is a design target.

0. **Morning read-in (about 15 sec).** What's changed in public, the countdown, your forces' posture and the situation map.
1. **Read the inbox (about 1 min).** 4 to 6 new items arrive: HUMINT reports, intercepts, imagery, OSINT posts and liaison cables. Each one shows its source code name and the grade it came in with, and the ones with a location are plotted on the map.
2. **Assess (3 to 4 min).** Decide whether to believe each item: doubt anything you judge false or deliberately misleading, and flag clutter as not relevant. From Phase 2, link items to hypotheses on the board. This is the puzzle: a timestamp that's off, a source reporting on something it couldn't have seen, two "independent" reports that trace back to the same origin.
3. **Task collection (about 1 min).** Spend a limited number of collection points on your biggest intelligence gaps. The results show up in tomorrow's inbox.
4. **Write the brief (about 2 min).** Pick a judgment and a confidence level (Low, Medium or High, color-coded), then attach up to 3 pieces of key evidence. Evidence is scored by what it really was; it doesn't change the call or what the customer does. The brief then writes your key judgment: "We assess with high confidence that…, based on…". One judgment a day keeps the turn short and the stakes clear.
5. **Overnight.** The hidden world state moves forward. Your customer acts on your brief, and tomorrow opens with their reaction and the consequences.

At the end of a crisis there's a **postmortem**: the ground truth is revealed next to your daily calls, including which items were planted, what gave each one away and what you missed. A map shows where the adversary's units really were each day. That payoff is what turns a series of guesses into learning.

## Player role and progression

You play the cell lead: hands-on with the material, but answerable to a customer and responsible for a small team. Your credibility with that customer is the main currency.

- **Your team.** You start with 2 analysts and can grow to 4. Each one adds a short note to the items in their specialty (regional, technical or OSINT). Their notes are usually helpful but not always right, and each analyst has a trait such as overconfident, slow but careful, or prone to anchoring on the first theory. Learning who to trust is part of the game.
- **Credibility.** High credibility gets you more collection points and a bigger team, and your customer acts on your briefs. If it drops, your budget gets cut and the customer starts ignoring you, even when you're right. You can't be fired: at rock-bottom credibility you're reassigned to a new cell, losing your team and unlocks but keeping your track record.
- **Calibration scoring.** A high-confidence call that's right pays the most, and a high-confidence call that's wrong costs the most: Low +1/−1, Medium +2/−2, High +3/−4. High pays off above about two-thirds certainty, Medium above even. Cited evidence scores by what it really was (true +1, noise 0, clutter −1, planted −2), and doubting a report scores planted +1, true −1. "Always hedge" loses because the customer won't act on a Low call.
- **Unlocks.** Over the course of the campaign you gain collection disciplines (imagery, SIGINT), new regions, new analysts and a higher clearance tier that opens more sensitive (and riskier) sources.

## Setting

The game uses fictional countries placed in real regions in the early 2030s. Real terrain, infrastructure and types of threat keep it grounded. Invented countries, leaders, units, militias, companies and groups mean the story won't date badly, won't accuse real governments and won't put words in real people's mouths.

- **Tone:** grounded, procedural and low-key, like a real ops center rather than a spy thriller. Some dry humor comes through in the analyst notes and the customer's replies.
- **Customers:** a small recurring cast of 2–3 decision-makers (for example a task force commander or a senior policy official), each with a personality and their own priorities. One runs each crisis, and they remember your track record.
- **Crisis seeds:** see `03-crisis-content.md`.

## Core systems

Five systems drive the game. Each one maps to a real analytic discipline, simplified so it fits into a short daily turn.

### Sources and reliability

Every source has a code name, a level of access and a reliability grade from A to F. Every report also gets an information credibility rating from 1 to 6, the same scheme as the Admiralty system. Each item arrives with the collector's grade, and your call is whether to believe the report: a good source can still carry a bad one. A source's file grade belongs to the source and updates between crises as it builds a track record. Each source also has a hidden true reliability, and a few are controlled by the adversary.

### Collection

Each day you spend collection points on your intelligence gaps. Disciplines trade off speed, cost and risk:

| Discipline | Cost (points) | Arrives | Good for | Risk |
| --- | --- | --- | --- | --- |
| OSINT | 1 | Next day | Broad, cheap signals | Noisy, easy to plant |
| Liaison | 0 | Next day | Free reporting from a partner | Partner has its own agenda |
| IMINT | 2 | Next day | Confirming physical activity | Can't show intent |
| SIGINT | 3 | Next day | Intent and plans, narrow focus | Target can go dark |
| HUMINT | 3 | 2 days | Deep access and context | Can burn the source |

All costs and timings are starting values to tune in playtesting.

### Hypotheses board (Phase 2)

Each crisis opens with 2 to 4 competing hypotheses. Pin up to 3 items a day to the board and mark each one consistent (C), inconsistent (I) or doesn't apply (–) for each hypothesis, a lightweight version of ACH. The board counts what contradicts each hypothesis and names the least contradicted; it greys out items that fit every hypothesis, because they can't tell them apart, and sets aside items you've doubted. The brief shows the board's lead as a nudge. The board isn't scored (#42, #49).

### Deception

The adversary plants items that are consistent with each other but false. Every planted item has a tell in its own text and at least one cross-check, an item you already have by that day that contradicts it. Typical tells:

- Timing that's too convenient
- A source reporting on things it couldn't have had access to
- Circular reporting, where two "independent" items come from one origin
- A story that only ever holds up on a single chain of sources
- A message that says exactly what the adversary would want overheard

### Customer and consequences

Your daily brief drives a decision by your customer, who commits in proportion to your confidence: High buys the full move, Medium a partial one, and Low none. Moving too early has a cost too. The true world state evolves out of sight, and outcomes show up a day or two later. That delay is deliberate: you have to live with a call before you find out how it turned out.

## Content: crises and reports

A crisis is a 5 to 10 day arc built from three layers. Reports are generated from the hidden truth, so every item is either a noisy reflection of what's really happening or a deliberate lie.

- **Ground truth:** what's actually happening, day by day. It can change mid-crisis, and each brief is scored against that day's truth.
- **Adversary plan:** what the other side wants you to believe, and which channels it will use to plant that.
- **Report stream:** each day's items, made up of true signals, noise, planted items and background clutter that has nothing to do with the crisis.

How it gets built over time:

1. Hand-author the first 3 crises as data files so the design can be tuned on known content.
2. Turn the patterns that work into crisis templates with variables (region, adversary type, truth branch).
3. Have Claude write the report text inside each template's structure, so the wording varies while the truth and the tells stay controlled by the engine.

The player isn't told how many days a crisis lasts; in-world deadlines (an announced end date, a vote, a deadline) are fine. The default cadence is one in-game day per real day. A Play ahead switch lets you open the next day straight away.

The crisis data format is in `03-crisis-content.md`.

## Platform and tech

The game is a single-page web app that Claude builds and publishes as a claude.ai page. You open it from a link on your phone or laptop.

- **Phone first:** items are cards, and you judge one with a tap. The hypotheses board is a compact table: one row per pinned item, one 44 px tap cell per hypothesis.
- **Situation map:** plots reporting as it arrives, planted items included, plus your own forces. The real positions appear only in the postmortem.
- **Engine and content kept separate:** crises live in JSON data files, so we can add new ones without touching the game code.
- **Saving:** progress saves to the player's claude.ai account, so phone and laptop share one game, with a copy on the device as a fallback.
- **No server of our own:** one player and one saved game. Multiplayer and leaderboards can come later if they ever earn a place.
- **Daily lock:** the next day unlocks at midnight, unless Play ahead is on.
- **Code and builds:** code and crisis data live in the GitHub repo `antj54/LowCon`, and the pages are published from it. `tools/simulate.js` runs fixed strategies through the real engine as a balance check. A separate playtest build records testers' results automatically.

## MVP scope and roadmap

The MVP is Phase 1: a single 5-day crisis you can actually play. Each phase after that adds one layer, and the next one only starts once the current one has proven fun. The phases are in order but not scheduled.

| Phase | Scope | Gate to move on |
| --- | --- | --- |
| 0 · Paper prototype | This doc plus one crisis scripted as a day-by-day table; play it through by hand | The crisis is fun to reason through on paper |
| 1 · First playable (MVP) | One 5-day crisis: read-in and map, inbox with doubting, daily brief, postmortem. No collection or team yet | A blind playtester plays all 5 days and wants a sixth |
| **2 · Core systems** *(current)* | Collection tasking, hypotheses board, credibility; a second crisis to prove the systems generalize | The second crisis plays differently from the first |
| **3 · Campaign** | 3 linked crises, analysts with traits, unlocks, the recurring customer cast, reassignment; sources and deception that carry across crises | A full campaign holds up over weeks of daily play |
| **4 · Living world** | Crisis templates with Claude-written report text; streaks, an archive of past crises | — |

## Open questions

Tracked in `02-decisions-log.md`.
