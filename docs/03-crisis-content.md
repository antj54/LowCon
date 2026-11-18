# Intel Cell Sim — Crisis Content

*All crises, sources and reports live here (and later in the app's data files). The engine reads content and never hard-codes it.*

## Crisis seeds (not yet scripted)

| Seed | Core question for the player | Deception angle |
| --- | --- | --- |
| Border buildup | A logistics buildup near a contested border: exercise, or staging for an operation? | The "exercise" story is true at first, then turns into cover |
| Missing shipment | Dual-use components went missing between two ports. Where are they, and who has them? | A false trail planted through a front company's paperwork |
| Ransomware group | Is a ransomware crew criminal, or working for a state? | A false-flag language artifact points at the wrong country |
| Pipeline militia | A militia threatens a pipeline while a neighbor quietly funds both sides | Liaison partner reporting is shaped by the partner's own agenda |
| Defector walk-in | A defector's story is almost too good | The defector is a dangle; their best details are circular |

## Authoring rules

1. Every crisis has **ground truth** (day by day), an **adversary plan** (what they want you to believe, through which channels) and a **report stream**.
2. Every planted item has **at least one tell** a careful player could find on the day it arrives. Deception must be beatable, not random.
3. Each day's inbox mixes true signals, noise, planted items and background clutter that has nothing to do with the crisis. Target: 4 to 6 items a day.
4. At least one day per crisis has to have a **diagnostic** item, one that splits the hypotheses apart, if the player collected well.
5. The **postmortem** has to be able to explain every item: what it really was and what it should have told you.
6. Fictional actors only. Real geography and generic, publicly known methods are fine. Never use real people.

## Data format (draft)

The app will store each crisis as one JSON file shaped like this. The fields are a draft and can change as the systems are built.

```json
{
  "id": "border-buildup",
  "title": "Exercise or Operation?",
  "days": 5,
  "customer": { "name": "Gen. R. Halvorsen", "role": "Task force commander", "wants": "A clear yes/no on whether to reposition forces" },
  "hypotheses": [
    { "id": "H1", "text": "Routine annual exercise" },
    { "id": "H2", "text": "Exercise used as cover to stage an incursion" },
    { "id": "H3", "text": "Show of force for coercion, no intent to cross" }
  ],
  "groundTruth": [
    { "day": 1, "state": "Real exercise begins", "trueHypothesis": "H1" },
    { "day": 4, "state": "Lead units diverted toward border crossing", "trueHypothesis": "H2" }
  ],
  "sources": [
    { "id": "S-KESTREL", "discipline": "HUMINT", "access": "Logistics clerk at regional depot", "startingGrade": "C", "trueReliability": 0.8, "controlledByAdversary": false }
  ],
  "reports": [
    {
      "id": "R-1-01",
      "day": 1,
      "sourceId": "S-KESTREL",
      "discipline": "HUMINT",
      "text": "Fuel allocations for the exercise are 40% higher than last year.",
      "credibility": 3,
      "kind": "true",
      "supports": ["H2", "H3"],
      "contradicts": [],
      "tells": [],
      "postmortemNote": "Early indicator: the extra fuel was for the follow-on move."
    }
  ],
  "collectionResults": [
    { "trigger": { "discipline": "IMINT", "target": "border-crossing", "fromDay": 3 }, "reportId": "R-4-02" }
  ]
}
```

`kind` is one of `true`, `noise`, `planted` or `clutter`. `tells` lists the clues on planted items (for example `"access-mismatch"`, `"circular-origin"`, `"convenient-timing"`).

## Scripted crises

*None yet. The first one gets scripted in Phase 0.*
