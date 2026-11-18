# Phase 2 design (paper) · Low Confidence

*Status: paper design only, nothing built. Written 2026-11-18 while the Phase 1 playtest runs. Phase 2 starts when the Phase 1 gate passes.*

**Phase 2 scope:** collection tasking, the hypotheses board, credibility, and a second crisis to prove the systems generalize.
**Gate to Phase 3:** the second crisis plays differently from the first.
**Out of scope (Phase 3):** analysts and their notes, linked crises, the recurring customer cast carrying memory across crises, reassignment.

## The daily turn with Phase 2

| Step | Target time | New in Phase 2 |
| --- | --- | --- |
| 0. Morning read-in | 15 sec | Yesterday's collection results are flagged as yours |
| 1. Read the inbox | 1 min | Some items are results of your own tasking |
| 2. Assess | 2–3 min | Optional: pin items to the hypotheses board |
| 3. Task collection | 1 min | **New step** |
| 4. Write the brief | 1–2 min | Board shows the least-contradicted hypothesis as a nudge |

The turn grows by about 2 minutes. Syd's turns ran about 2 minutes and were rated "about right," so a 4–6 minute turn is still well inside the target.

## 1. Collection tasking

### How it works

- **PIRs.** Each crisis defines 3–4 Priority Intelligence Requirements, shown to the player as questions. For Crisis 01 they might be: *PIR 1: Are 4th Army units moving toward the border outside the exercise area? PIR 2: Has Kordav's leadership authorized action against Tarsk? PIR 3: Is Kordav preparing to cross the Veyl (bridging, medical, fuel)?*
- **Targets.** Each PIR lists the named areas or targets that could answer it (Dolan crossing, Ostrel, Varn depot, 4th Army nets, the defence ministry). Targets are also map areas, so the player can task by tapping the map, which brings in the parking-lot idea.
- **Budget.** A daily allowance of collection points (start: 4). Disciplines cost what the design doc's table says: OSINT 1, Liaison 0, IMINT 2, SIGINT 3, HUMINT 3. Results arrive the next morning, or in 2 days for HUMINT.
- **Resolution.** Each tasking (discipline × target) resolves overnight to an authored report if the crisis has one for that combination and day range. If not, it returns "nothing significant," which is true and tells you something too.
- **Risks, deterministic and authored.** No dice, so every outcome can be explained in the postmortem:
  - **HUMINT:** tasking the same source on consecutive days can burn it. The crisis marks which taskings are risky, and the source goes quiet.
  - **SIGINT:** after the adversary's comms-security trigger (Crisis 01's 0400 switch), the old nets return nothing.
  - **OSINT:** cheap, but the adversary plants into it. Some planted items only reach you because you tasked OSINT.
  - **Liaison:** free, and it always carries the partner's agenda.
- **Diagnostic rule (authoring rule 4, Phase 2).** At least one diagnostic item is only reachable through collection. A player who never tasks the right target has to call it on weaker evidence.

### Phone UI

A **Collection** tab after the inbox. It lists the PIRs, each with its targets as rows. Tap a target and the affordable disciplines appear as chips with their cost. A budget meter sits at the top, and pending taskings show "arrives tomorrow" or "in 2 days." Tapping a map area opens the same picker.

### Postmortem payoff

A new section, **The collection you didn't do**. For each day, it shows what the best tasking would have returned that you didn't ask for. That's the strongest lesson collection can teach: the gap you left open.

### Data (format v0.5 sketch)

- `pirs[]`: `id`, `question`, `targets[]`
- `targets[]`: `id`, `name`, `pin`, `pirs[]`
- `collection`: `budget`, `costs`, `delays`
- `collectionResults[]`: `trigger` (`discipline`, `target`, `fromDay`, `toDay`), `reportId`, `risk` (for example `burnsSource`)
- `collectionFallback`: the "nothing significant" text per discipline
- Reports gain `via: "collection"` so they only appear when tasked

## 2. Hypotheses board (ACH-lite)

**Decision needed.** Options:

| Option | How it works | Tradeoff |
| --- | --- | --- |
| **A. Pin and mark, unscored** (recommended) | Pin up to 3 items a day to the board and mark each as consistent, inconsistent or neither for each hypothesis. The board ranks hypotheses by how much evidence contradicts them, which is the core idea of ACH, and greys out items that fit every hypothesis because they can't tell them apart. | A real tradecraft tool that stays optional and quick. It doesn't change your score directly; it helps you make better calls. |
| B. Engine-filled board | The board fills itself from the crisis's authored supports and contradicts | No taps, but the game does the analysis for you, and the authored labels describe how items look on the surface, so they'd mislead the player |
| C. Scored board | Your marks are scored against an answer key | Turns into a quiz with an arbitrary key, the same problem as the old per-item grading |

## 3. Credibility

**Key constraint:** credibility can't move on whether you're right during a crisis, because that would leak the hidden truth. It can only move on consequences the customer can see.

**Decision needed.** Options:

| Option | How it works | Tradeoff |
| --- | --- | --- |
| **A. Visible consequences only** (recommended) | A meter with the customer. It moves on things he can see: an early move he has to reverse (the Day 3 freeze), hedging two days running ("I've stopped reading the roughly-evens"), and the crisis outcome at the end. Low credibility trims tomorrow's collection budget, and the customer acts one step more cautiously. | No truth leak, and it supports "the world remembers." Within one crisis it has few levers. Its real weight comes in Phase 3, when it carries across crises. |
| B. Daily on correctness | Moves every day on whether your call was right | Leaks the truth during play |
| C. Defer to Phase 3 | Leave credibility out of Phase 2 | Simplest, but the roadmap's Phase 2 has three systems, and this drops one |

## 4. Crisis 02 seed

**Decision needed.** The gate needs Crisis 02 to play differently from Crisis 01. Options:

| Seed | Core question | Why it plays differently | Tradeoff |
| --- | --- | --- | --- |
| **Defector walk-in** (recommended) | Is the walk-in genuine, a dangle feeding deception, or a fabricator after money? | The decision is about one source, not troop moves. Collection is used to verify his claims. His best details turn out to be circular. It punishes "always trust HUMINT," Crisis 01's known weak spot. | HUMINT-heavy, so the discipline mix needs care. Liaison and SIGINT do the verifying. |
| Missing shipment | Where are the dual-use components, and who has them? | A "where" question with locations as hypotheses. The most collection-driven of the seeds, so the best showcase for tasking. | Less of a judgment-and-confidence call. Closer to a search puzzle. |
| Ransomware group | Criminal crew or state-directed? | Cyber attribution with a false-flag language artifact, and a very different discipline mix | Needs technical depth to stay authentic, and it suits the map less |

The customer would be the second member of the recurring cast. For the defector: a senior policy official deciding whether to act on his claims and whether to resettle him.

## 5. Build order

Each step is playable on its own.

1. **Collection tasking**, retrofitted into Crisis 01 with 3 PIRs and a handful of collection results, so it can be tuned on known content. One existing item, such as the Day 4 imagery, becomes reachable earlier through tasking.
2. **Hypotheses board.**
3. **Credibility meter.**
4. **Crisis 02 on paper** (player packet and key, Phase 0 style), then as data.
5. **Playtest** Crisis 02 blind, and replay Crisis 01 with collection.

## Decisions needed

1. Hypotheses board: **A**, B or C
2. Credibility: **A**, B or C
3. Crisis 02 seed: **Defector**, Missing shipment or Ransomware
4. Retrofit collection into Crisis 01 first: **yes** or no
