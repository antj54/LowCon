# Story key · Low Confidence

**SPOILERS FOR THE WHOLE CAMPAIGN. Anthony: don't open this (#67). It says who the leak is, how each act hides and reveals it, and how the endings are decided. The spoiler-free plan is `claude/story-plan.md`.**

*Written by Claude 2026-11-18 as the author's working key. Paper only. Every claim here has to end up as a tell and a cross-check in a scenario, like any other deception.*

---

## The answer

**The leak is not a person. It is the liaison link.**

The alliance and Elsin exchange intelligence over a secure terminal network called **LATTICE**, installed in Kalsa four years ago and maintained by a contractor, **Corvane Systems**. Kordav's Bureau compromised LATTICE's hardware in the supply chain before it was installed: the shipment was diverted for a day and a half on its way to Kalsa and arrived on time, sealed and altered. The Bureau has read everything that crossed the link since.

Nobody betrayed anyone. An Elsin procurement officer signed for a shipment without asking why it was a day late, and that is the whole of the human failing.

**Why this answer:**

- It's the realistic one. Compromised channels have done more damage than most moles, and a liaison link is exactly where two services' secrets meet.
- It makes the hunt a judgment problem. Every human suspect has a motive and a manner that look right. The true answer has neither, only a pattern.
- It gives Scenario 06 a real cost for the wrong call: an innocent person's career.
- It ties Act 2 together. Scenario 04's shipment and Scenario 05's attack are both the Bureau maintaining and protecting the implant.

## The pattern that proves it

**Only what crossed LATTICE ever leaked. What stayed inside the cell never did.**

| Scenario | What leaked | Did it cross the link? | What didn't leak | Did it cross the link? |
| --- | --- | --- | --- | --- |
| 01 | That we read 12th Brigade's net (so Kordav staged a call on it). The timing of our warning (so the "routine" line came hours later). | Yes: Halvorsen shared the daily assessment with Elsin. | KESTREL's existence | No: source identities never go to liaison |
| 02 | That we read the Bureau's headquarters admin net (so the recall was staged there) | Yes: an earlier product based on it went to Elsin | FINCH's name. The Bureau found him by watching the ministry, not by reading us. | No |
| 03 | Nothing from LATTICE. Marrat knew where the company was because its advisers sit in Southern Command. | — | — | — |

Scenario 03 is the deliberate false lead: it's a real leak with a human, local explanation, and it points the player at people in Elsin's service just before Act 2 asks who the leak is.

## The suspects

All introduced on the page before Scenario 06. Each can be ruled out with evidence the player can reach.

| Suspect | Who | Why they look guilty | The truth | What clears them |
| --- | --- | --- | --- | --- |
| **Col. Edda Rhun** | Head of the liaison desk in Elsin's military intelligence. She is the voice behind WREN. | Abrasive, political, hated Vell, and every leak involved something shared with her desk. | Innocent. Everything shared with her desk leaked because it reached her over LATTICE. | Items she received by hand, on paper, in Scenario 04 and 05 never leak. |
| **Maj. Tobin Arle** | Halvorsen's intelligence staff officer. He distributes your briefs. | Careless with distribution lists. Was on every list. | Innocent, and sloppy. | In Scenario 05 he's on leave for the week the diagram leaks. |
| **Tess Marrow** | Your open-source analyst | A security review flags unreported foreign travel. She joined just before things got worse. | Innocent. The travel was a funeral. | The leaks began before she arrived (Scenario 01). |
| **No leak at all** | — | Kordav may just be reading our behaviour: we're predictable. | Partly true, which is what makes it tempting. | The staged recall in 02 needed knowledge of a specific net, not a guess. |
| **LATTICE** | The link | It has no motive and no manner. Nobody suspects furniture. | **Guilty.** | — |

**The Bureau's deception in Act 2:** it wants a person blamed, because a mole hunt protects an implant. Its plants in Scenarios 05 and 06 point at Rhun, whose real grudge against Vell (visible since Scenario 02) makes her easy to believe in. This is Scenario 03's lesson turned round again: the person who looks like the problem isn't.

## Act 2, scenario by scenario

### 04 · The Missing Shipment

- **Surface question:** a consignment of dual-use components (network and encryption hardware bound for Kalsa) vanishes between two ports. Where is it: H1 lost in a customs dispute, H2 diverted to Kordav for its own use, H3 diverted to Marrat for resale.
- **Truth:** it was diverted for 36 hours to a warehouse run by a Bureau front, and then it *comes back*. On Day 4 the shipment reappears, intact and sealed, and everyone relaxes. The truth shifts from "missing" to "returned," and the right late call is that the return is the problem: H2, at High, with the recommendation not to install it.
- **Customer:** Marlowe. Her decision is whether Elsin accepts the delivery.
- **The thread:** the smugglers change route the morning after the player tasks collection *through liaison*. Tasking through the cell's own channels doesn't tip them. A careful player sees that difference without being told what it means.
- **The key clue (case file):** port records show the same broker, the same route and the same 36-hour delay on LATTICE's original delivery four years ago.
- **What the outcome sets:** if the altered units are installed, the leak gets *worse* in Act 3 (Kordav reads more, faster). If they're refused, the old implant is all Kordav has.
- **Dominant-strategy guard:** "it's always Kordav" is right here, on purpose, straight after a scenario where it was wrong.

### 05 · Lights Out

- **Surface question:** ransomware hits Elsin's grid and pipeline control systems. H1 a criminal crew after money, H2 Kordav behind a criminal false flag, H3 Marrat, still sore about the pipeline.
- **Truth:** H2, but not for the reason anyone assumes. The attack isn't the point. The recovery is: restoring from "clean vendor images" supplied by Corvane's compromised update server is how the Bureau repairs and extends its access after the scare in Scenario 04. The ransom demand is real and the crew is real; they were hired.
- **Customer:** the third member of the cast, **Director Ilse Brandt**, who runs the alliance's Infrastructure Protection Cell in Kalsa. Technical, impatient with estimative language, wants a yes or no. Her decision: pay, restore from vendor images, or rebuild by hand (slow, and the right answer).
- **The thread:** the attackers had a network diagram held by five named people and one system. Rhun, Arle and Brandt's deputy are among the five. The diagram was also stored on LATTICE.
- **The Bureau's plant:** a "leaked chat log" from the crew naming a contact "in liaison" in Kalsa. It points at Rhun.
- **Halden** is the analyst who matters here, and she is a day late as always.

### 06 · The Damage Assessment

- **The question:** who or what is the leak? H1 a person in Elsin's service (Rhun), H2 a person on our side (Arle), H3 the link itself, H4 no leak: we're predictable.
- **Truth:** H3, fixed.
- **Evidence:** this scenario's inbox is mostly *the player's own history*. Each day releases a tranche of the damage assessment: a table of what leaked, when, and which channel it travelled on, built from the three Act 1 records and the two Act 2 outcomes. The case file decides how much of that table is already filled in on Day 1.
- **Collection:** controlled tests. The player can ask for a marked item (a "barium meal") to be passed by hand to Rhun, by hand to Arle, or over LATTICE, and watch which one surfaces in Kordavan reporting two days later. Three tests fit in the scenario; four suspects don't. Choosing which tests to run is the puzzle.
- **Customer:** Marlowe, with Halvorsen copied. Her decision at High: remove a person, or shut down the link (which blinds the alliance in Kalsa for a month, a real cost).
- **Outcomes carried forward:**
  - *H3 at High:* LATTICE is shut down. The leak closes. Elsin is offended at the implication and Alliance drops by one, a price for being right.
  - *H1 or H2 at High:* that person is removed. The leak stays open. In Act 3 they reappear once, briefly, as a consequence.
  - *H4, or anything at Low or Medium:* an inquiry is opened and decides nothing. The leak stays open.

## Act 3, and what the leak does to it

| Scenario | Leak closed | Leak open |
| --- | --- | --- |
| 07 The Vote in Kalsa | Elsin's government is weaker (Alliance took the hit), but what you tell it stays between you. | Kordav's people in Kalsa are a step ahead of every warning you pass. One planted item each day is built from your own previous brief. |
| 08 Mobilisation | Kordav has to guess what you think. Its deception is generic and can be caught on its tells. | Kordav tailors its deception to your last call: brief H1 and tomorrow's plants support H1. The adversary-reacts mechanic, finally. |
| 09 The Back Channel | The envoy doesn't know your bottom line. | The envoy quotes it. That is itself the last, loudest clue for a player who still hasn't seen it. |
| 10 The Veyl | Your collection is clean. | Any tasking that goes through liaison is compromised, and the player has to work out which of their own sources to believe. |

**Scenario 09's truth depends on the record.** If Pressure is low (Kordav gained little in Acts 1 and 2), the envoy's offer is genuine: Kordav needs a way out. If Pressure is high, the offer is a stall to cover final preparations. The scenario's items are written in two sets, chosen by the record, and both sets have their tells.

**A player who names the wrong person in 06 gets one more chance.** In Scenario 09, if the envoy quotes your bottom line, a High call that the link is compromised closes the leak for the finale. It comes too late for the person who was removed.

## Endings, decided

**The world** (after the finale):

| Ending | Rule of thumb |
| --- | --- |
| The alliance holds | The finale ends well and Alliance is positive |
| A cold peace | The finale ends well and Alliance is zero or negative: Elsin survives and no longer wants us |
| Partition | The finale ends badly and Pressure is high |
| War | The finale ends badly, Pressure is high, and the back channel in 09 was misjudged |

**You:**

| Ending | Rule |
| --- | --- |
| Vindicated | Named LATTICE in Scenario 06 |
| Vindicated, late | Named it only in Scenario 09 |
| Trusted, and blind | Never named a person and never found the link, with credibility intact |
| The wrong name | Named Rhun or Arle at High in Scenario 06 |
| A new cell | Reassigned at any point and never recovered |

The closing passage for "the wrong name" is the campaign's hardest: the postmortem shows LATTICE, and then tells you what the person you named is doing now.

## Clues to plant back into Act 1

Postmortem-only, so nothing in Act 1's balance changes. Each scenario's postmortem gains a short closing section, **An open question**, which states a fact and draws no conclusion.

| Scenario | The open question | Case-file entry earned by |
| --- | --- | --- |
| 01 | "Kordav staged a call on the one net we were reading, and its 'routine' statement came out the morning after our assessment reached Kalsa. How did it know which net, and when?" | Doubting the staged call (R-4-02) |
| 02 | "The Bureau put its fake recall on the one net it believed we read. It was right. What made it believe that?" | Collecting the Bureau office's own traffic (C-01), or doubting the recall (C-06) |
| 03 | "Someone knew the guard company was at Tolen. Marrat's advisers sit in Southern Command, so this one has an answer. Not every leak does." | Doubting the transcript (R-2-02), or seeing the Displaced outcome |

**The supporting cast needs to exist before Act 2.** Rhun gets a name in Scenario 02's and 03's WREN cables ("signed, Col. E. Rhun, liaison desk"). Arle gets one in Halvorsen's replies in 01 and 03 ("Arle will circulate it"). LATTICE gets mentioned exactly once per scenario, as plumbing: "passed to Kalsa over LATTICE." These are text-only changes with no effect on scoring, to be made when Act 2 is built.

## Authoring rules for the leak (so it stays fair)

1. From Scenario 04 on, every scenario has at least one item that only makes sense if the link is compromised, and at least one that seems to and doesn't.
2. No item ever says "LATTICE is compromised" before the player does.
3. Every human suspect can be cleared by evidence available by the end of Scenario 05.
4. The pattern (crossed the link, leaked; stayed inside, didn't) must hold without exception across all ten scenarios. One counter-example breaks the whole story, so every new scenario's leaks get checked against this table.
5. Methods stay generic: "hardware altered in transit," "a compromised update server." No technical detail beyond what a newspaper would print.

## Open risks (author's own)

- **"It was the furniture" can feel like a cheat.** It's fair only if the pattern is visible before the reveal. The controlled tests in 06 are what make it earned: the player can prove it.
- **Scenario 06 has an unusual inbox** (the player's own history). It needs the engine to read the record and build items from it, which is new.
- **Act 3's tailored deception** needs plants generated from the player's previous brief. Authored variants per hypothesis will do it without anything generative: three sets of plants a day, one shown.
- **Marrow as a suspect** uses a character the player has only just met and may like. That's intended, and it should be handled gently: she's cleared early if the player looks.
