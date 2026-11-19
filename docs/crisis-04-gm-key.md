# Crisis 04: The Missing Shipment · GM key and postmortem (paper)

**SPOILERS FOR THIS SCENARIO AND FOR THE CAMPAIGN. Anthony: don't open this (#67, #68). It depends on `claude/story-key.md`.**

*Written for Act 2. Paper only. Player packet: `claude/crisis-04-player-packet.md`.*

---

## What this scenario is for

1. A scenario where **the good news is the deception.** For three days the question is where the container went. On Day 4 it comes back, sealed and counted, and everyone with a stake wants the matter closed. The right late call is that the return is the problem.
2. **"It's Kordav" is right again,** straight after a scenario where it was wrong. The lesson of Crisis 03 was to check, not to switch suspects.
3. **The campaign's first hard clue.** The container holds replacement terminals for LATTICE. The Bureau is doing to them what it did to the originals four years ago, with the same forwarder, the same coaster and the same day and a half.
4. **The player can tip the other side off** by tasking through liaison, and can see that it happened without being told why.

## Ground truth

The answer to the hypothesis never changes: Kordav. What changes is what the evidence looks like.

| Day | What's really happening | True hypothesis | What it looks like |
| --- | --- | --- | --- |
| 1 (3rd) | The container left Halsk on the night of the 1st on *Maren Lys* and is on a fenced quay at Brask. A Bureau technical team has started on the forty units. Tessaly's clerk wrote a false gate entry for shed 6. | **H2** | A lost container, or a theft |
| 2 (4th) | Work continues at Brask. Tessaly's owner announces a "72-hour" search, which is how long he knows it will take. The Bureau posts a fake listing to make it look like theft for resale. | **H2** | Theft for resale |
| 3 (5th) | The work is finished ("forty of forty"). *Maren Lys* sails for Halsk. The fake listing is marked sold. | **H2** | Theft, getting worse |
| 4 (6th) | The container was put in shed 9 overnight by a private crew and resealed with copied customs seals. It is "found." | **H2** | A paperwork failure, happily resolved |
| 5 (7th) | It goes to Kalsa by rail. Elsin installs tomorrow unless told not to. | **H2** | Closed |

## Adversary plan

| Days | Wants you to believe | Channels |
| --- | --- | --- |
| 1–3 | **H3:** a grubby theft for resale. Keeps attention on Halsk and off Brask. | Tessaly's statement, the fake listing |
| 4–5 | **H1:** it was never gone. Everyone can stop looking. | Tessaly again. The rest is done for the Bureau by honest people: the port's records, Corvane's engineer and Elsin's minister all say what they sincerely believe. |

**The meta-tell:** the forwarder knew to the day how long it would take to find a container he said was lost.

## Sources (hidden values)

| Code name | True reliability | Adversary-controlled? | Notes |
| --- | --- | --- | --- |
| CORVANE | 0.9 | No | Honest, and wrong on Day 4. He checks the outside of crates because that's what his procedure covers. |
| HARBOUR | 0.7 | No (the channel) | Reports its records accurately. Two of the records are false. |
| WREN (Col. Rhun) | 0.7 | No (biased) | Rude about Halsk on Day 1 for no reason, and right about Tessaly on Day 3 for a good one. |
| TESSALY | — | **Yes** | The Bureau's forwarder, for the second time in four years |
| TRACKER | 0.9 | No | |
| GANNET | 0.85 | No | Sees exactly what happened, both nights |
| MERIDIAN, CIRRANE | 0.9 | No | |
| SOCIAL | 0.3 | Partly | Carries the fake listing, and on Day 5 a true complaint from the night shift |

---

## Item key: push

Kinds: **T** true · **N** noise · **P** planted · **C** clutter

### Day 1 (truth H2). Best call: H2 at Low

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-1-01 | T | — | The baseline: what was shipped (CX-4), when, and by whom |
| R-1-02 | N | — | The port reports its records honestly. The gate entry for shed 6 was written by Tessaly's clerk after the container had gone. Not scored as a plant because HARBOUR isn't lying; it's the first of several honest people repeating a false thing. |
| R-1-03 | N | agenda-aligned | Rhun's standing opinion of Halsk. It tells you nothing about this container. |
| R-1-04 | T | — | **The best item of the day.** The forwarder's own chartered ship left the same night with no manifest, heading toward Kordav's coast, and went dark. It's why Low on H2 is defensible on Day 1. |
| R-1-05 | C | — | Toner |

### Day 2 (truth H2). Best call: H2 at Medium

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-2-01 | P | knows-too-much | See the reasoning below |
| R-2-02 | P | wrong-model, catalogue-photo | See the reasoning below |
| R-2-03 | T | — | The political cost of the delay, which is what makes everyone want it over |
| R-2-04 | T | — | **Remember this one.** Customs searched all nine sheds on the 3rd. On Day 4 the container is "found" in shed 9. |
| R-2-05 | C | — | The wrong toner |

### Day 3 (truth H2). Best call: H2 at High

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-3-01 | T | — | Three days dark, and back the way it went |
| R-3-02 | T | — | Pressure, honestly applied. The loss clause is why Corvane wants it found. |
| R-3-03 | T | — | **WREN is right, again, for a reason it gives.** Looks like Day 1's sneer and isn't. |
| R-3-04 | P | too-neat | See the reasoning below |
| R-3-05 | C | — | More toner |

### Day 4 (truth H2). Best call: H2 at High

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-4-01 | T | — | True reporting of a staged discovery. The tell is in what you already have: shed 9 was searched on the 3rd (R-2-04). Doubting it costs a point, because the port is telling the truth about what it found. |
| R-4-02 | P | knows-too-much | See the reasoning below |
| R-4-03 | N | — | An honest inspection of the wrong thing. Seals and tape tell you about seals and tape. Citing it scores 0. |
| R-4-04 | T | — | The deadline |
| R-4-05 | C | — | Toner, in shed 9 |

### Day 5 (truth H2). Best call: H2 at High

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-5-01 | T | — | "No offence disclosed" is true: nobody disclosed one |
| R-5-02 | T | — | The last chance, and Rhun's patience |
| R-5-03 | T | — | **The push-only player's best evidence.** An F-graded forum post that is exactly right. A night shift sent home and a private crew in a bonded shed. |
| R-5-04 | T | — | Corvane wants to finish the job |
| R-5-05 | C | — | The printer |

## Item key: pull

| ID | Tasking | Window | Kind | What it really was |
| --- | --- | --- | --- | --- |
| C-01 | IMINT · Brask waterfront | Days 1–2 | T, **diagnostic** | The container, in Kordav, beside a guarded warehouse |
| C-02 | IMINT · Brask waterfront | Days 3–4 | T | Too late: it's been and gone |
| C-03 | IMINT · Halsk sheds | Days 1–3 | T | Shed 9 was empty. This is what breaks Day 4's good news. |
| C-04 | IMINT · Halsk sheds | Days 4–5 | T | It's there now |
| C-05 | OSINT · *Maren Lys* | Days 1–4 | T | The coaster's pattern and its Kordavan owner. One point. |
| C-06 | Liaison request · port-police check | Days 1–3 | T | **The tip-off.** The request went to Kalsa over LATTICE, and Tessaly knew before the police did. Free, tempting, and it costs the player C-07. |
| C-07 | SIGINT · Tessaly's office | Days 1–3, not tipped | T, **diagnostic** | The whole operation in four lines |
| C-07T | SIGINT · Tessaly's office | Days 1–3, tipped | T | What you get if you warned them. "Use the other phones." |
| C-08 | GANNET | Days 1–2 | T | How it left, and that the gate log is false |
| C-09 | GANNET | Days 4–5 | T, **diagnostic** | How it came back, and who sealed it |
| C-10 | OSINT · Tessaly's history | Days 1–4 | T, **case file** | The same forwarder, the same route and the same day and a half, four years ago, on the hardware LATTICE runs on. States a fact and draws no conclusion. |
| C-11 | OSINT · the listing | Days 2–4 | T | The listing is bait |
| C-12 | SIGINT · the Brask warehouse | Days 2–3 | T, **diagnostic** | "Forty of forty done." Something was done to every unit. |

**Two-path rule:** that Kordav had it is reachable by C-01, C-07, C-12 or C-05 with R-1-04. That the return was staged is reachable by C-03 with R-2-04, by C-09, or on push alone by R-2-04 with R-5-03.

---

## Planted items: the reasoning

### R-2-01 (Day 2, TESSALY): "within 72 hours"

- **What gave it away:** a man who has lost a container knows exactly how long it will take to find.
- **Check it against R-1-04:** his own chartered coaster left the night the container vanished, with no manifest, and went dark.
- **Why it was planted:** to keep everyone waiting quietly for three days. Seventy-two hours is the round trip to Brask and a day and a half alongside.

### R-2-02 (Day 2, SOCIAL): the listing

- **What gave it away:** it offers model CX-2, and the photo is from Corvane's catalogue.
- **Check it against R-1-01:** Corvane shipped CX-4. Whoever wrote the listing had never seen the crates. For one point, C-11 adds that CX-2 went out of production six years ago and the seller account is two days old.
- **Why it was planted:** a theft for resale is an ordinary crime in Halsk, and an ordinary crime doesn't send anyone to look at Brask.

### R-3-04 (Day 3, SOCIAL): "SOLD. Collected."

- **What gave it away:** forty military encryptors sold and collected within a day, in a port whose bonded sheds customs had just searched.
- **Check it against R-2-04 and R-3-01:** customs was in every shed on the 3rd (R-2-04), and the forwarder's coaster was at that moment on its way back (R-3-01).
- **Why it was planted:** to close the theft story before the container reappeared, so the two stories wouldn't have to share a day.

### R-4-02 (Day 4, TESSALY): "As we said"

- **What gave it away:** he said 72 hours, and it took 72 hours.
- **Check it against R-2-04 and R-4-01:** customs searched all nine sheds on the 3rd and found nothing (R-2-04). The container was found in shed 9 (R-4-01).
- **Why it was planted:** the last line of the cover story, delivered with an apology.

---

## The analysts

| Analyst | Notes | Right | How it went |
| --- | --- | --- | --- |
| Vasko | R-1-02, R-2-02, R-3-03, R-4-01, R-5-03 | 1 of 5 | Anchored on Halsk being Halsk: first a lost container, then a theft, then a lost container again. He dismissed Rhun when she was right. His last note is the only one that looks at what's in front of him. |
| Halden | R-1-04, R-3-01, R-4-03, each a day late | 3 of 3 | Her note on the seals arrives on Day 5, the morning of the last brief. A player who waited for her on Day 4 lost nothing but a point of confidence. |
| Marrow | R-1-04, R-2-02, R-4-03 | 1½ of 3 | Half right on Day 1 (smuggling, wrong cargo). Sharp on the listing, and in open disagreement with Vasko. Flatly wrong on Day 4: "Case closed." |

Day 2 is the first time two analysts disagree under the same item. The player has to choose.

## Marlowe's actions and the endings

| State | Triggered by | Notes |
| --- | --- | --- |
| Refuse | H2 at High, Days 2–5 | Withdrawn by H1 or H3 at Medium or High. Credibility −1. |
| Hold | H2 at Medium | Corvane's engineers inspect. They pass it. |
| Theft inquiry | H3 at Medium or High | Ends when the container turns up |
| Install on arrival | H1 at Medium or High | — |
| Rebuffed | H2 at High on Day 1 | Marrat searches Halsk on her word and finds nothing, because it's in Brask. Days 2–3 frozen. Credibility −2. −5 points. |

**Endings** (what Kalsa does on the 8th):

| State after the Day 5 brief | Ending | Points |
| --- | --- | --- |
| Refuse | **Sent back.** The crates go back to Corvane unopened. Their engineers are offended. Six weeks later an independent lab opens one, and Corvane's chairman flies to Kalsa in person. | +5 |
| Hold | **Passed.** Corvane's engineers inspect seals, tape and serial numbers for three weeks and find nothing wrong, because nothing is wrong with the seals, the tape or the serial numbers. The terminals are installed in the new year. | 0 |
| Anything else | **Installed.** The terminals are in the ministry's communications room by the evening of the 8th. The minister is photographed with one. | −5 |

**Credibility:** starts where Crisis 02 left it with Marlowe. Outcome adjustment: Sent back +1, Passed 0, Installed 0. If the terminals are installed, Marlowe doesn't know it was the wrong call, and won't for a long time. That's deliberate: this is the first scenario where the customer may never learn the truth inside the scenario.

## What it writes to the record

| Outcome | Alliance | Pressure | Case file | For Act 3 |
| --- | --- | --- | --- | --- |
| Sent back | 0 | 0 | +1 | The Bureau has only the old implant |
| Passed | 0 | +1 | — | New implant in place, a month late |
| Installed | 0 | +1 | — | New implant in place. The leak gets worse in Act 3. |
| Rebuffed on Day 1 | −1 | — | — | — |
| C-10 collected | — | — | +1 | The four-year-old pattern is in the file |
| C-06 tasked, then C-07T seen | — | — | +1 | The player has watched a liaison request tip off the target |

## Postmortem script

> **Day 1.** A container vanished and the forwarder's own ship left that night with its lights off. The port's records said shed 6. The records were written afterwards.
>
> **Day 2.** Tessaly's owner said it would take 72 hours to find. A listing appeared offering the wrong model with a catalogue photo. Both were meant to keep you looking at Halsk.
>
> **Day 3.** Rhun, who had sneered on Day 1, passed on something true. The ship turned for home.
>
> **Day 4.** The container was found in a shed that customs had searched three days earlier. Its seals were perfect. Everyone who told you so was telling the truth as they knew it.
>
> **Day 5.** A dockworkers' forum asked why the night shift had been sent home. Nobody else did.

**An open question** (the campaign thread; states facts only):

> Four years ago the same forwarder handled the ministry's original terminals, and they too spent an extra day and a half in Halsk. And if you asked Kalsa to have the port police look at Tessaly, Tessaly's staff were ready for them.

**Lessons:**

1. When something lost comes back, ask where it has been, not whether it's all there.
2. A seal tells you about the seal.
3. Honest people can carry a false story further than a liar can.
4. A source that sneers and a source that reports can be the same source on different days. Read the item.
5. How you ask is part of what you learn. Some questions warn the people you're asking about.

---

## Designer notes (critic hat)

**Dominant-strategy check** (paper estimate: calls, the rebuff and the ending; before evidence, doubts and burned sources):

| Strategy | Ending | Total |
| --- | --- | --- |
| Best play: H2 Low, H2 Medium, then H2 High | Sent back | **+17** |
| Push only, slower: H2 Low, Low, Medium, Medium, High | Sent back | **+14**, with a credibility hit for two Lows |
| Always Kordav (H2 High from Day 1) | Passed (rebuffed, Discounted, so Day 5 High acts as Medium) | **+10** |
| Never above Medium on H2 | Passed | **+10** |
| Believed the return: H2 to Day 3, then H1 Medium | Installed | **−4** |
| Always hedge (Low on H2) | Installed | **0** |
| Theft all along (H3 Medium, then H1 when it turns up) | Installed | **−15** |
| Paperwork all along (H1 High) | Installed | **−25** |

**Watch for:**

- **The truth never changes,** as in Crisis 02, so "always H2 High" is held back only by the Day 1 rebuff and the credibility it costs. Same weakness, same patch.
- **Day 4 is the scenario.** If testers don't feel the pull to relax, the good news isn't good enough. Corvane's engineer and the minister carry it; neither may be made to sound foolish.
- **A hold feels like the careful answer and isn't.** The packet says so in bold. If players still feel cheated, Marlowe's Medium reply should say it louder.
- **The free liaison request is a trap with a price tag.** It costs the player the best SIGINT in the scenario. It's fair because C-06's own text shows the staff were ready, and because three other paths reach the same answer. It must never be the only way to learn something.
- **The LATTICE link is visible to an attentive player from this packet alone.** That's intended: Act 2 is where the pattern is supposed to start showing. If it's too obvious on paper, the built version can drop the sentence about LATTICE from the collection rules and leave it in the Files tab.
- **Toner.** Five clutter items telling one small story. Keep or cut on tone.

**Engine needs before building:**

- **A result that depends on an earlier tasking** (C-07 or C-07T): a condition on "was this target ever tasked"
- **Case-file tags** on items and results, counted on the record, and a Case file screen
- **The three story values** (Alliance, Pressure, Case file) written at the end of each scenario and read at the start of the next
- **An "open question" block** in the postmortem
- **Two analyst notes under one item**
- Everything else (named states, the Day 1 rebuff, frozen days, credibility carry-in from the same customer, a source burned by consecutive tasking) is already in the v1.1 engine
- **Map:** Halsk and its sheds, the sea route to Brask, the rail line to Kalsa
