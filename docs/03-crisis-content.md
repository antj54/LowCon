# Low Confidence — Crisis Content

*All crises, sources and reports live in the app's data files (`crises/*.json` in the repo). The engine reads content and never hard-codes it.*

## Crisis seeds

| Seed | Core question for the player | Deception angle | Status |
| --- | --- | --- | --- |
| Border buildup | A logistics buildup near a contested border: exercise, or staging for an operation? | The "exercise" story is true at first, then turns into cover | **Scripted: Crisis 01** |
| Missing shipment | Dual-use components went missing between two ports. Where are they, and who has them? | A false trail planted through a front company's paperwork | Seed |
| Ransomware group | Is a ransomware crew criminal, or working for a state? | A false-flag language artifact points at the wrong country | Seed |
| Pipeline militia | A militia threatens a pipeline while a neighbor quietly funds both sides | Liaison partner reporting is shaped by the partner's own agenda | Seed |
| Defector walk-in | A defector's story is almost too good | The defector is a dangle; their best details are circular | Seed |

## Authoring rules

1. Every crisis has **ground truth** (day by day, and it can change mid-crisis), an **adversary plan** (what they want you to believe, through which channels) and a **report stream**.
2. Every planted item has **at least one tell in its own text and at least one cross-check**, an item available by that day that contradicts it. Deception must be beatable, not random.
3. Each day's inbox mixes true signals, noise, planted items and background clutter that has nothing to do with the crisis. Target: 4 to 6 items a day.
4. At least one day per crisis has to have a **diagnostic** item, one that splits the hypotheses apart. In Phase 1 it arrives in the normal inbox. From Phase 2, at least one must come from collection.
5. The **postmortem** has to be able to explain every item: what it really was and what it should have told you. For planted items it states the tell, the cross-check by item ID and the adversary's motive.
6. Fictional countries in real regions, and fictional actors only. Real terrain and generic, publicly known methods are fine. Never use real people.
7. Don't tell the player how many days a crisis lasts; in-world deadlines are fine. The **morning read-in** states only public events and the player's own posture, never hidden truth. The **map** plots reporting (planted items included), never truth, until the postmortem.

## Data format (v0.4)

Each crisis is one JSON file. The working example is `crises/border-buildup.json` in the repo; this is the field reference.

| Field | What it holds |
| --- | --- |
| `id`, `title`, `crisisNumber`, `days`, `dayLabels` | Identity and calendar (`dayLabels` like "the 15th") |
| `briefing` | `dateLine` and `situation` paragraphs for the opening screen |
| `placeholderNote` | One line on the fictional setting |
| `customer` | `name`, `role`, `callsign`, `wants`, `context` |
| `asset` | The force the customer can move: `name` and `levels` (e.g. `home`, `company`, `battalion`, each with a `label` and `rank`) |
| `customerPolicy` | Ordered rules: `if` (`hypothesis`, `likelihood`, `confidence`, `assetAt`) → `action` (`deploy` with a `level`, `readiness`, `hold`, `relax`, `withdraw`). `likelihood` is one of `even`, `likely`, `very`, `almost`; `confidence` is the level derived from the cited evidence (`low`, `moderate`, `high`). |
| `policySummary`, `policyNote` | The customer's habits as shown to the player |
| `replies`, `replyLabels` | The customer's reply text for each outcome, and a short label for each |
| `events` | Start-of-day triggers (e.g. the early-move freeze): `atStartOfDay`, `if`, `effect`, `replyId`, `note` |
| `hypotheses` | `id`, `short`, `text`, and `claim` (the clause used in the key-judgment line, e.g. "IRON HARVEST is cover for an operation to seize Tarsk Dam") |
| `groundTruth` | Per day: `trueHypothesis`, `bestCall`, `state`, and `units` (positions shown only on the postmortem map) |
| `adversaryPlan` | Phases: `days`, `wantsYouToBelieve`, `summary`, `channels` |
| `sources` | `id`, `codeName`, `discipline`, `access`, `startingGrade`, hidden `trueReliability`, `controlledByAdversary`, `rosterHidden`, `postmortemNote` |
| `reports` | `id`, `day`, `sourceId`, `discipline`, `sourceGrade`, `credibility`, `text`, `kind` (`true`, `noise`, `planted`, `clutter`), `supports`, `contradicts`, `tells`, `diagnostic`, `pin` (map position and label), `postmortemNote`, and for planted items `reveal` (`tell`, `crossCheck.ids`, `crossCheck.text`, `motive`) |
| `tellLabels` | Human-readable label for each tell tag |
| `scoring` | `call` (right/wrong points per likelihood), `evidence` and `challenge` (points per kind), `maxEvidence`. The confidence rule itself is engine doctrine, not crisis data. |
| `endings` | Ordered: `if` (`assetAt`, `since`), `title`, `tone`, `points`, `text`; one has `default: true` |
| `countdown`, `dailyUpdates` | The read-in's countdown target and each day's public update |
| `map` | Illustrated map: `viewBox`, `river`, `reservoir`, `border`, `forests`, `training`, `highlands`, `regions`, `places`, `offmap`, `friendly` positions, `legend` |
| `postmortem` | `script` (per day or group of days) and `lessons` |
| `collectionResults` | Phase 2: collection triggers and the report each one delivers. Empty in Crisis 01. |

## Scripted crises

| # | Title | Seed | Data | Notes |
| --- | --- | --- | --- | --- |
| 01 | Exercise or Operation? | Border buildup | `crises/border-buildup.json` | Phase 1 build. Phase 0 script: `claude/crisis-01-player-packet.md` (rules predate Phase 1) and `claude/crisis-01-gm-key.md` (spoilers, current). |
