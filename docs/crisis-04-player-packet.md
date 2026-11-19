# Crisis 04: The Missing Shipment · Player packet (paper)

*No spoilers in this file. The answer key is `claude/crisis-04-gm-key.md`, and it spoils the campaign as well as this scenario: don't open it. Paper version, Act 2 (#67). In the built game you won't be told how many days the crisis runs; on paper it has to show all of them.*

---

## Before you start: your service record

| From your record | Effect here |
| --- | --- |
| How Crisis 02 ended | Sets your starting credibility with Marlowe and her opening line (Appendix A) |
| Were you reassigned, and not since recovered? | If so, you have no third analyst: skip Marrow's notes |

## Situation (read once)

The autumn after the Southern Line. Day 1 is the 3rd.

Your cell is working for **Under Secretary H. Marlowe** again.

Elsin's defence ministry ordered forty crates of secure communications hardware, CX-4 terminals, from the alliance contractor **Corvane Systems**. They are replacements for the terminals Elsin's ministry uses to talk to the alliance. The consignment travelled by sea in one container to **Halsk**, Marrat's free port, where the forwarder **Tessaly Freight** was to put it on a train to Kalsa.

It was due in Halsk on the 1st. Nobody can find it.

## Your customer

**Under Secretary H. Marlowe.** Her question every day: *Where is it, who has had it, and what do I tell Kalsa to do about it?*

How she acts on your brief:

| Your brief | What Marlowe does |
| --- | --- |
| H2 at High | Tells Elsin the consignment is compromised: refuse it, and send it back unopened if it turns up |
| H2 at Medium | Asks Elsin to hold the consignment on arrival for inspection before anything is installed |
| H3 at Medium or High | Asks Marrat, through Elsin, to investigate Tessaly Freight for theft. If the consignment turns up, that ends the matter. |
| H1 at Medium or High | Tells Elsin to wait, and to install on arrival |
| Any hypothesis at Low | Changes nothing |

**A hold means Corvane's own engineers inspect it. Only a refusal keeps it out of the building.** And she won't accuse a neighbour's port on a guess.

**Credibility.** It starts where Crisis 02 left it. It drops if she has to take back something she told Kalsa on your word, if a move of hers is rebuffed, and if you call Low two days running.

## Hypotheses

| ID | Hypothesis |
| --- | --- |
| H1 | **A paperwork failure.** The container never left Halsk. It's in the wrong shed and will turn up. |
| H2 | **Kordav.** The consignment has been, or is, in Kordav's hands. |
| H3 | **Theft for resale.** Someone in Halsk took it to sell. |

## Sources on file

| Code name | Discipline | Access | File grade |
| --- | --- | --- | --- |
| CORVANE | Commercial | Corvane Systems' account manager for Elsin. Honest about what he knows. Wants the contract to go smoothly. | B |
| HARBOUR | Liaison | Halsk port authority and Marrat customs, reporting what their records say | C |
| WREN | Liaison | Elsin's military intelligence liaison desk, run by Col. E. Rhun. Dislikes Marrat's free port and says so. | B *(upgraded after Crisis 03)* |
| TESSALY | Commercial | Tessaly Freight's public statements | E |
| TRACKER | OSINT | Commercial ship-tracking data | B |
| GANNET | HUMINT | A dock foreman at Halsk. Sees what moves through the bonded sheds at night. New. Don't task him two days running. | C |
| MERIDIAN | SIGINT | Tasked coverage only | B |
| CIRRANE | IMINT | Tasked coverage only | B |
| CWS | OSINT | Continental Wire Service | B |
| SOCIAL | OSINT | Forums, listings and social media. Unvetted. | F |

## Your analysts

Imre Vasko (regional), Noor Halden (technical) and Tess Marrow (open sources). Notes are opinion: you can't cite or doubt them, and they don't score.

## Collection

**What arrives without asking:** public and commercial reporting, and whatever the port, the forwarder and Elsin's liaison desk choose to say. **Everything else you task.**

**Budget:** 5 points a day. Results arrive the next morning. Liaison requests go to Kalsa over LATTICE, the alliance's link to Elsin's ministry, and Kalsa passes them on.

| Discipline | Cost |
| --- | --- |
| IMINT (CIRRANE) | 2 |
| SIGINT (MERIDIAN) | 3 |
| HUMINT: GANNET | 3 |
| OSINT | 1 |
| Liaison request, through Kalsa | 0 |

| PIR | Question | Targets you can task |
| --- | --- | --- |
| PIR 1 | Where is the consignment? | Brask waterfront, in Kordav (IMINT) · Halsk bonded sheds (IMINT) · The coaster *Maren Lys* (OSINT) · A port-police check on Tessaly (Liaison request) |
| PIR 2 | Who has handled it? | Tessaly Freight's office (SIGINT) · GANNET · Tessaly's shipping history (OSINT) · The grey-market listing (OSINT, from Day 2) |
| PIR 3 | What has been done to it? | The warehouse at Brask (SIGINT, from Day 2) |

Look up what you tasked in Appendix C, and read only the entries you paid for.

## How to play a day

1. **Days 2 onward:** read Marlowe's reply in Appendix A, then your collection results in Appendix C.
2. Read the inbox and the analyst notes. Doubt anything you judge false or deliberately misleading, and mark clutter as not relevant.
3. Task collection for tomorrow.
4. **Brief:** one hypothesis, one confidence level, and up to 3 item IDs as key evidence.

## Scoring

| Confidence | Right | Wrong |
| --- | --- | --- |
| Low | +1 | −1 |
| Medium | +2 | −2 |
| High | +3 | −4 |

Cited evidence: true +1, noise 0, clutter −1, planted −2. Doubting a report: planted +1, true −1. A burned source costs −2. The ending adds a bonus or a penalty.

---

## Day 1: the 3rd

*Read-in:* A container of secure communications hardware for Elsin's defence ministry is two days overdue at Halsk.

**R-1-01** · CORVANE · received **B2**
> Forty crates of CX-4 terminals, one container, left our port on the 28th and were due at Halsk free port on the 1st for rail to Kalsa. Our forwarder, Tessaly Freight, reports the container "not located" in the bonded area.

**R-1-02** · HARBOUR · received **C3**
> Port records show the container discharged from the feeder vessel on the 1st and gated into bonded shed 6. Shed 6 reports no such container. "Discrepancies of this kind are usually resolved within the week."

> *Vasko:* Halsk loses a container a week and finds most of them. I wouldn't panic yet.

**R-1-03** · WREN · received **B3**
> Col. Rhun: "Our ministry wants its hardware. Halsk is a thieves' market with a customs house attached. We told procurement not to route through it."

**R-1-04** · TRACKER · received **B2**
> The coaster *Maren Lys*, on charter to Tessaly Freight, left Halsk on the night of the 1st with no cargo manifest filed, heading north-west. Its transponder went off at 0210.

> *Marrow:* No manifest and lights out is smuggling, plain and simple. Cigarettes, usually.

**R-1-05** · Embassy admin · received **A1**
> The embassy's own delivery of printer toner is also late. This is not thought to be related.

---

## Day 2: the 4th

*Read-in:* Elsin's ministry has confirmed the delay in public.

**R-2-01** · TESSALY · received **E3**
> Statement from Tessaly Freight: the company "regrets a labelling error" and "expects to locate the container within 72 hours."

**R-2-02** · SOCIAL · received **F3**
> A grey-market trading board lists "40 units, new, military-grade network encryptors, model CX-2, pickup Halsk." The photo carries Corvane's catalogue watermark.

> *Vasko:* There it is, for sale. Tessaly moves anything for anyone. A grey-market job.
> *Marrow:* Catalogue photo, and the account looks new. This listing is bait.

**R-2-03** · CWS · received **B1**
> Elsin's defence ministry confirms a delay to "a communications upgrade." The opposition asks why secure equipment was routed through a foreign free port.

**R-2-04** · HARBOUR · received **C2**
> Marrat customs has opened a routine discrepancy file. Officers searched all nine bonded sheds yesterday and did not find the container.

**R-2-05** · Embassy admin · received **A1**
> The toner has arrived. It is the wrong toner.

> *Halden, on yesterday's R-1-04:* Transponders fail. They don't usually fail at ten past two in the morning, just outside the port limit.

*Plus any collection results from Day 1 tasking (Appendix C).*

---

## Day 3: the 5th

*Read-in:* Corvane has given notice that it will invoke the contract's loss clause tomorrow.

**R-3-01** · TRACKER · received **B2**
> *Maren Lys* reappeared on tracking at 0500 today, well offshore and inbound for Halsk. It was dark for three days.

**R-3-02** · CORVANE · received **B2**
> If the container isn't found by tomorrow, we invoice Elsin under the loss clause and manufacture again: twelve weeks. If it is found, our engineers can commission the units the day they arrive.

**R-3-03** · WREN · received **B3**
> Col. Rhun: "Marrat customs tells us privately that Tessaly's owner has debts, and friends in Kordav who have paid them before. We would like this passed to your people."

> *Vasko:* Rhun's desk again, with gossip about debts. She'd say the same about any firm in Marrat.

**R-3-04** · SOCIAL · received **F3**
> The grey-market listing has been marked "SOLD. Collected."

**R-3-05** · Embassy admin · received **A1**
> The correct toner has been ordered. Delivery is expected via Halsk.

*Plus any collection results.*

---

## Day 4: the 6th

*Read-in:* The container has been found at Halsk.

**R-4-01** · HARBOUR · received **C2**
> The container has been located in bonded shed 9, mis-stowed. Customs seals are intact and the numbers match. It is released for rail to Kalsa tomorrow morning.

> *Vasko:* Found in the wrong shed. I did say: Halsk.

**R-4-02** · TESSALY · received **E3**
> Statement: "As we said, a labelling error. Tessaly Freight apologises for the inconvenience."

**R-4-03** · CORVANE · received **B2**
> Our engineer has examined the crates at Halsk. Customs seals intact, our own tamper tape intact, crate count correct. We recommend installation on arrival.

> *Marrow:* Seals intact, numbers match, customs happy. Case closed, I'd say.

**R-4-04** · CWS · received **B1**
> Elsin's defence minister says he is "delighted" and that the new terminals will be installed on the 8th.

**R-4-05** · Embassy admin · received **A1**
> A container of toner has been found in bonded shed 9.

> *Halden, on yesterday's R-3-01:* Three days dark. Long enough to reach Brask, wait a day and a half, and come back.

*Plus any collection results.*

---

## Day 5: the 7th

*Read-in:* The container left Halsk by rail at 0600 and reaches Kalsa tonight.

**R-5-01** · HARBOUR · received **C2**
> The container was loaded on the 0600 rail service. Marrat customs has closed its discrepancy file: "no offence disclosed."

**R-5-02** · WREN · received **B2**
> Col. Rhun: "The ministry installs tomorrow unless your side objects in writing today. Our procurement people are tired of this, and so am I."

**R-5-03** · SOCIAL · received **F3**
> A Halsk dockworkers' forum: the night shift at shed 9 was sent home early on the 5th, "and some private crew did the stow. Since when?"

> *Vasko:* Night shift sent home, and a private crew in a bonded shed? In Halsk even the thieves work days. That's odd.

**R-5-04** · CORVANE · received **B2**
> Our commissioning team is in Kalsa and ready. We would be grateful for confirmation that installation can proceed.

**R-5-05** · Embassy admin · received **A1**
> The toner is the right toner. The printer has been condemned.

> *Halden, on yesterday's R-4-03:* An intact seal tells you about the seal.

*Plus any collection results. Collection you task on Day 5 won't arrive in time.*

---

## Appendix A: Marlowe's replies

**Day 1 opening, by how Crisis 02 ended:**

| Crisis 02 ending | Marlowe |
| --- | --- |
| Exposed | "You were right about the walk-in when it would have been easier not to be. I've a missing container. Same standard, please." |
| Survived or Shelved | "Last time we got through it. I'd like to do better than get through it. I've a missing container." |
| Sidelined or Burned | "I signed something on your reading once. I read more carefully now. I've a missing container." |

**After each brief:**

| What she did | Marlowe |
| --- | --- |
| Told Elsin to refuse it (H2 High) | "I've told Kalsa to send it back unopened. Their minister asked what I know that Corvane's engineers don't. I said: where it's been." |
| Asked for a hold (H2 Medium) | "I've asked Kalsa to hold it for inspection. Corvane will send engineers. If you want it kept out of the building altogether, I need more than medium." |
| Asked for a theft inquiry (H3) | "I've asked Kalsa to have Marrat look at Tessaly for theft. Marrat's customs were very polite about it." |
| Told Elsin to wait and install (H1) | "I've told Kalsa to wait for it and get on with the installation when it comes." |
| Changed nothing (Low) | "Then we wait." |
| Already in place | "That stands. Keep at it." |
| Took back a refusal or a hold | "I've withdrawn what I told Kalsa. Their minister is beginning to keep a list." *Credibility −1.* |

**Day 2 only:** if you briefed H2 at High on Day 1, read Appendix B *instead of* the table.

## Appendix B: sealed note (Day 2)

> "You told me Kordav had it, on the first morning, with nothing in your hand. I asked Marrat to search the port for a consignment 'believed to be in hostile custody.' They searched. It isn't there, and they'd like to know what we meant. Kalsa has asked me to keep this commercial. For two days, I will."

*Effect: nothing you brief on Day 2 or Day 3 changes what she tells Kalsa. Day 4 and Day 5 briefs do. Credibility −2. −5 points.*

## Appendix C: collection results

Read only the entries you tasked, on the morning they arrive. Anything not listed, or tasked outside its window, returns **"Nothing significant."**

| ID | Tasking | Tasked on | Result |
| --- | --- | --- | --- |
| C-01 | IMINT · Brask waterfront | Days 1–2 | "*Maren Lys* is alongside a fenced quay at Brask. One container stands on the quay under a tarpaulin, beside a windowless warehouse with a new roof. Two guards at the gate." |
| C-02 | IMINT · Brask waterfront | Days 3–4 | "The fenced quay at Brask is empty. The warehouse doors are shut. *Maren Lys* is not in port." |
| C-03 | IMINT · Halsk bonded sheds | Days 1–3 | "Shed 9's doors stand open in every pass: pallets only. No container with the consignment's markings anywhere in the bonded area." |
| C-04 | IMINT · Halsk bonded sheds | Days 4–5 | "One container with the consignment's markings in shed 9." |
| C-05 | OSINT · the coaster *Maren Lys* | Days 1–4 | "*Maren Lys* has made the same run twice before: Halsk to Brask and back with its transponder off, each time inside four days. Its owner of record is a holding company with an address in Kordav." |
| C-06 | Liaison request · a port-police check on Tessaly | Days 1–3 | "Halsk port police visited Tessaly's office and sheds 4 and 6 this morning at Kalsa's request. The staff had the paperwork laid out before the officers arrived. Nothing found." |
| C-07 | SIGINT · Tessaly Freight's office | Days 1–3, **if you have never tasked C-06** | "Tessaly's owner to an unidentified man: 'Thirty-six hours, same as before. It goes back the way it came, same shed fee.' The other man: 'Seals?' 'My man has the pliers and the numbers.'" |
| C-07T | SIGINT · Tessaly Freight's office | Days 1–3, **if you tasked C-06 on an earlier day** | "Tessaly's office line is quiet. One call: staff are told to 'use the other phones this week.'" |
| C-08 | GANNET | Days 1–2 | "GANNET: a container left shed 6 on the night of the 1st on a Tessaly truck. It went to the coaster berth, not to the rail siding. The gate log was written up afterwards." |
| C-09 | GANNET | Days 4–5 | "GANNET: the container came back on the night of the 5th. A private crew stowed it in shed 9 and one of them was closing seals with a hand tool. He has never seen customs seals put on at night." |
| C-10 | OSINT · Tessaly's shipping history | Days 1–4 | "Tessaly has handled one earlier consignment for Corvane Systems: four years ago, the original terminal hardware for Elsin's defence ministry. Port logs show it sat in Halsk a day and a half longer than booked." |
| C-11 | OSINT · the grey-market listing | Days 2–4 | "The seller account was created the day the loss became public. The model listed, CX-2, has been out of production for six years. Corvane shipped CX-4." |
| C-12 | SIGINT · the warehouse at Brask | Days 2–3 | "A voice at the Brask warehouse, to an unidentified office: 'Forty of forty done. Closing up.'" |

*GANNET: if you task him on two days running, read this instead of the second result: "GANNET wasn't at the gate. His shift has been changed." He is burned (−2) and gives nothing more.*
