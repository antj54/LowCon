# Crisis 05: Lights Out · Player packet (paper)

*No spoilers in this file. The answer key is `claude/crisis-05-gm-key.md`, and it spoils the campaign as well as this scenario: don't open it. Paper version, Act 2 (#67, #68). In the built game you won't be told how many days the crisis runs; on paper it has to show all of them.*

---

## Before you start: your service record

| From your record | Effect here |
| --- | --- |
| How your last scenario ended | Your new customer has read your file. A good ending starts you one step up, a bad one a step down. |
| Were you reassigned, and not since recovered? | If so, you have no third analyst: skip Marrow's notes |

## Situation (read once)

January. Day 1 is the 9th, in the first hard cold of the winter.

At 0312 this morning the control systems for Elsin's northern power grid, and for the pumping controls on the Southern Line, were encrypted. A criminal crew called **Grey Ledger** has claimed it and wants paying. Kalsa is on rolling blackouts.

Your cell has been lent to the alliance's **Infrastructure Protection Cell** in Kalsa for as long as this lasts.

## Your customer

**Director Ilse Brandt** runs the Infrastructure Protection Cell. She is an engineer. She has no patience for estimative language and says so. Her question every day: *Who did this, so I know which way to fix it?*

She has three ways to get the lights back:

| Option | How long | The catch |
| --- | --- | --- |
| **Pay** the ransom and use the crew's decryptor | A day | It pays criminals, and it only works if the crew wants it to |
| **Restore** the six control servers from the vendor's clean system images | Two days | It trusts what the vendor's update server sends |
| **Rebuild** the control servers by hand, from parts and paper | Nine days | Nine more days of blackouts in January |

How she acts on your brief:

| Your brief | What Brandt does |
| --- | --- |
| H1 at High | Pays |
| H2 at High | Orders a rebuild by hand, and tells the operators to trust nothing supplied from outside |
| H3 at High | Orders a restore from the vendor's images, and recommends Elsin expel Marrat's remaining advisers |
| Anything at Medium or Low | **Nothing.** "I can't run a grid on a maybe." |

**She only moves on High.** And the minister has a clock of his own: you'll hear about it.

**Credibility.** She's new to you, so it starts from your file. It drops if money she paid on your word buys nothing, if the minister overrules her, and if you go three days running without giving her a High.

## Hypotheses

| ID | Hypothesis |
| --- | --- |
| H1 | **Crime.** Grey Ledger did this for money, as it has nineteen times before. |
| H2 | **Kordav.** Kordav is behind it, using the crew as cover. |
| H3 | **Marrat.** Marrat is behind it, still sore about the pipeline. |

## Sources on file

| Code name | Discipline | Access | File grade |
| --- | --- | --- | --- |
| IPC LAB | Technical | The Infrastructure Protection Cell's forensic team. Careful, and slower than anyone would like. | B |
| GRID | Liaison | Elsin's grid operator and the energy minister's office | B |
| CORVANE | Commercial | Corvane Systems, which built and maintains the control servers. Honest about what it knows. | B |
| WREN | Liaison | Elsin's military intelligence liaison desk, Col. E. Rhun | B |
| LEDGER | OSINT | Grey Ledger's own posts and ransom messages | E |
| PETREL | HUMINT | A broker on criminal forums who has dealt with Grey Ledger. Hears what the crew complains about. New. Don't task him two days running. | C |
| MERIDIAN | SIGINT | Tasked coverage only | B |
| KSB | OSINT | Kordav State Broadcaster | D |
| MNA | OSINT | Marrat News Agency | D |
| CWS | OSINT | Continental Wire Service | B |
| SOCIAL | OSINT | Forums and social media. Unvetted. | F |

## Your analysts

Imre Vasko (regional), Noor Halden (technical) and Tess Marrow (open sources). Notes are opinion: you can't cite or doubt them, and they don't score.

## Collection

**What arrives without asking:** the lab's findings as it reaches them, the grid operator, the vendor, the crew's own messages, and public reporting. **Everything else you task.**

**Budget:** 5 points a day. Results arrive the next morning. Liaison requests go to Kalsa's ministries over LATTICE.

| Discipline | Cost |
| --- | --- |
| Technical (a specific job for IPC LAB) | 2 |
| SIGINT (MERIDIAN) | 3 |
| HUMINT: PETREL | 3 |
| OSINT | 1 |
| Liaison request | 0 |

| PIR | Question | Targets you can task |
| --- | --- | --- |
| PIR 1 | Who is Grey Ledger working for this time? | The ransom wallet's history (OSINT) · PETREL · The crew negotiator's communications (SIGINT, from Day 2) · Marrat's energy ministry (SIGINT) |
| PIR 2 | How did the malware know where to go? | Compare the malware's target list with the network diagram (Technical, from Day 2) · Ask the registry who holds the diagram (Liaison request) · The language in the malware (OSINT, from Day 2) |
| PIR 3 | Is the recovery safe? | Corvane's release history (OSINT) · Examine Corvane's system images (Technical, from Day 4) |

Look up what you tasked in Appendix C, and read only the entries you paid for.

## How to play a day

1. **Days 2 onward:** read Brandt's reply in Appendix A, then your collection results in Appendix C.
2. Read the inbox and the analyst notes. Doubt anything you judge false or deliberately misleading, and mark clutter as not relevant.
3. Task collection for tomorrow.
4. **Brief:** one hypothesis, one confidence level, and up to 3 item IDs as key evidence.

## Scoring

| Confidence | Right | Wrong |
| --- | --- | --- |
| Low | +1 | −1 |
| Medium | +2 | −2 |
| High | +3 | −4 |

Cited evidence: true +1, noise 0, clutter −1, planted −2. Doubting a report: planted +1, true −1. A burned source costs −2. What happens to the grid adds or subtracts points at the end.

---

## Day 1: the 9th

*Read-in:* Kalsa is on rolling blackouts. Grey Ledger has claimed the attack.

**R-1-01** · GRID · received **B1**
> At 0312 the six control servers for the northern grid and the Southern Line's pumping controls were encrypted. Both are being run by hand. The operator's office network is also down. Blackouts are scheduled district by district.

**R-1-02** · LEDGER · received **E3**
> Ransom message: 4 million in cryptocurrency within 96 hours. "Nothing personal. Pay, receive the decryptor, and we never meet again. Ask our previous customers."

> *Marrow:* Grey Ledger: nineteen victims in three years, always money, always pay-and-walk. This is them, and it's about money.

**R-1-03** · IPC LAB · received **B2**
> The malware is a known Grey Ledger strain. It came in through a contractor's remote-access account. It went straight to the six control servers by name and ignored some four hundred other machines until those six were done.

**R-1-04** · CORVANE · received **B2**
> We can supply clean system images for all six control servers from our update server within 24 hours of a request. Standard recovery: two days to full operation.

> *Vasko:* Marrat lost a pact over that pipeline, and now its pumps are dark. Look at who's smiling.

**R-1-05** · Cell admin · received **A1**
> Our own building has power. It does not have heating. Facilities describe these as separate systems.

---

## Day 2: the 10th

*Read-in:* A second night of blackouts. The main hospital is on generators.

**R-2-01** · IPC LAB · received **B2**
> The malware's loader contains text strings in Marrat's language, and its build times fall within office hours in Marrat. The strings sit in a section appended after the program was built.

> *Vasko:* Marrat. I said so.

**R-2-02** · MNA · received **D2**
> Marrat's government "categorically denies any involvement" and offers to send engineers to help Elsin recover.

**R-2-03** · LEDGER · received **E3**
> Grey Ledger posts a sample of stolen office documents as proof, and, unasked, lowers its demand to 2.5 million "for a quick close."

> *Marrow:* They never discount this early. Odd. Perhaps they need the cash.

**R-2-04** · CWS · received **B1**
> Elsin's energy minister says "all options are open" and that he expects power restored "within days, not weeks."

**R-2-05** · Cell admin · received **A1**
> Portable heaters have been issued. They may not be plugged in during a scheduled blackout, which is when they are needed.

> *Halden, on yesterday's R-1-03:* Four hundred machines to choose from, and it walked straight to six. That isn't scanning. Somebody gave it a map.

*Plus any collection results from Day 1 tasking (Appendix C).*

---

## Day 3: the 11th

*Read-in:* The energy minister has set a deadline.

**R-3-01** · GRID · received **B1**
> The minister has told Director Brandt that restoration from the vendor's images will begin at 1800 on the 13th unless she gives him a reason, in writing, to do something else.

**R-3-02** · IPC LAB · received **B2**
> The remote-access account belongs to a Corvane field engineer. His credentials were valid, and he says he was asleep. The malware carried a list of six server names matching the as-built network diagram, issue 7. Issue 7 went to five named holders on paper three weeks ago. One electronic copy was lodged with the alliance over LATTICE.

**R-3-03** · WREN · received **B2**
> Col. Rhun: "My service has traced part of the ransom wallet's history. Grey Ledger received 1.1 million two weeks before the attack, from an exchange in Kordav's capital. Criminals are not usually paid in advance."

> *Marrow:* Wallet tracing from a liaison service? I'd want to see the chain data myself.

**R-3-04** · KSB · received **D1**
> Kordav's state broadcaster leads with Kalsa in the dark: "An alliance that cannot keep its friends warm."

**R-3-05** · Cell admin · received **A1**
> The heaters have been recalled. One of them was plugged in.

> *Halden, on yesterday's R-2-01:* Those strings were stapled on afterwards. A programmer writes in his own language as he goes. He doesn't add a paragraph of it at the end.

*Plus any collection results.*

---

## Day 4: the 12th

*Read-in:* Corvane's images are ready. The minister's deadline is tomorrow evening.

**R-4-01** · SOCIAL · received **F3**
> An anonymous post on a criminal forum claims to be a leaked Grey Ledger chat log. The negotiator writes: "We are obliged to our esteemed friend in the liaison office in Kalsa, who provided the diagram."

> *Vasko:* The liaison office. That's Rhun's shop. She's had it in for half of Kalsa for years.

**R-4-02** · LEDGER · received **E3**
> Grey Ledger extends its own deadline by a day and lowers the demand to 1.5 million. "We are reasonable people."

**R-4-03** · CORVANE · received **B2**
> The images are staged on our update server and our engineer is on site. We can have the first control server running six hours after the order.

**R-4-04** · GRID · received **B2**
> Deputy Director O. Lind, in a memo to the minister copied to Brandt: "A rebuild by hand means nine more days of blackouts in January. People will die of it. I recommend the vendor restore."

**R-4-05** · Cell admin · received **A1**
> Staff are reminded that the building's fire alarm also depends on mains power.

> *Halden, on yesterday's R-3-02:* Six names on a target list. I'd like to see how they're spelled, next to the diagram.

*Plus any collection results.*

---

## Day 5: the 13th

*Read-in:* The vendor restore begins at 1800 today unless Brandt countermands it.

**R-5-01** · GRID · received **B1**
> Restoration from Corvane's images begins at 1800. Corvane's engineer is in the control room.

**R-5-02** · KSB · received **D1**
> Kordav's state broadcaster: "Elsin hunts a traitor in its own liaison office as the capital freezes."

> *Marrow:* State TV had "liaison office" in a headline four hours after an anonymous forum post. They read fast in Kordav.

**R-5-03** · WREN · received **B2**
> Col. Rhun: "I know what is being said about my desk. My copy of issue 7 has been in my safe since the day it was handed to me. You are welcome to come and look."

**R-5-04** · IPC LAB · received **B2**
> Corvane's update server holds a new image set for this model of control server dated the 7th: two days before the attack. Corvane's published schedule shows no release this winter.

**R-5-05** · Cell admin · received **A1**
> Heating has been restored to the building. Power is now intermittent.

> *Halden, on yesterday's R-4-03:* Before anyone installs an image, I'd like to know when it was built, and who asked for it.

*Plus any collection results. Collection you task on Day 5 won't arrive in time.*

---

## Appendix A: Brandt's replies

**Day 1 opening:**

| Your last scenario | Brandt |
| --- | --- |
| Ended well | "Your file says you get it right. I need it right and I need it in one word. Who?" |
| Otherwise | "I've read your file. I'd like a name and a level of certainty I can act on. I can act on one level." |
| You were reassigned | "They've sent me a new cell. Fine. The grid doesn't care who you used to be. Who did this?" |

**After each brief:**

| What she did | Brandt |
| --- | --- |
| Nothing (Medium or Low) | "That's a maybe. I can't run a grid on a maybe." |
| Paid (H1 High) | "Paid. If the decryptor works, we're done by tomorrow night and I'll take the criticism." |
| Ordered a rebuild by hand (H2 High) | "Rebuild by hand, starting now. Nothing from outside goes near those servers. Nine days. The minister used a word I hadn't heard since I was an apprentice." |
| Ordered a vendor restore (H3 High) | "Vendor restore ordered, and I've told the minister who I think he should send home." |
| Already ordered | "That's in hand. Tell me if it changes." |

**The morning after she pays:** read this instead of the table.

> "The decryptor works on the office machines. On all six control servers it fails and leaves them worse than before. They took the money and kept the part that mattered." *−3 points. Credibility −1.*

**Day 2 only:** if you briefed H2 at High on Day 1, read Appendix B instead.

## Appendix B: sealed note (Day 2)

> "I told the minister it was Kordav, on your word, six hours in. He asked what we had. I said a judgment. He has informed me that the recovery is now his decision and not mine, and that he will take advice from people with evidence."

*Effect: nothing you brief on Days 2, 3 or 4 changes what is done to the grid. Your Day 5 brief does. Credibility −2. −5 points.*

## Appendix C: collection results

Read only the entries you tasked, on the morning they arrive. Anything not listed, or tasked outside its window, returns **"Nothing significant."**

| ID | Tasking | Tasked on | Result |
| --- | --- | --- | --- |
| C-01 | OSINT · the ransom wallet's history | Days 1–4 | "The wallet named in the ransom note received 1.1 million two weeks before the attack, in one payment, from an exchange in Kordav's capital. Nothing else came in until this week." |
| C-02 | PETREL | Days 1–3 | "PETREL: Grey Ledger took a contract last month. 'Hit six boxes, leave the rest, paid up front.' The crew thinks the client is another gang. They were told which six." |
| C-03 | PETREL | Days 4–5 | "PETREL: the crew is fed up. The client has told them to keep talking and not to close. 'The money doesn't matter. Keep them busy until the 13th.'" |
| C-04 | SIGINT · the crew negotiator's communications | Days 2–4 | "The negotiator's instructions arrive through a relay that also carries traffic for a trading company in Kordav's capital. That company has fronted for the Bureau before." |
| C-05 | SIGINT · Marrat's energy ministry | Days 1–4 | "Marrat's officials are alarmed that their language is being found in the malware. The minister has ordered an inquiry of his own and asked who is trying to embarrass him." |
| C-06 | Technical · compare the target list with the diagram | Days 2–4 | "The malware's target list spells one server 'PCS-O6', with a letter O. The five paper copies of issue 7 print 'PCS-06', with a zero. The electronic copy lodged over LATTICE has the letter O." |
| C-07 | Liaison request · who holds the diagram | Days 1–4 | "The registry lists five paper copies of issue 7: Director Brandt; Deputy Director O. Lind; Col. E. Rhun, liaison desk; Maj. T. Arle, Task Force VEYL; and Corvane's site engineer. Maj. Arle's copy was never collected. He has been on leave, and it is still sealed in the registry. One electronic copy was lodged over LATTICE." |
| C-07K | *Read the morning after C-07 arrives* | — | "KSB, in passing: 'Officials in Kalsa spent yesterday searching their own registry for who holds which documents.'" |
| C-08 | OSINT · the language in the malware | Days 2–4 | "The Marrat-language strings contain two errors typical of machine translation, and one word that Marrat's speakers stopped using decades ago." |
| C-09 | OSINT · Corvane's release history | Days 1–4 | "Corvane's public release log shows no update for this model of control server since the spring. Its update server nonetheless lists a new image set dated the 7th." |
| C-10 | Technical · examine Corvane's system images | Day 4 | "The staged images were built on the 7th by an automated job that nobody at Corvane scheduled. They include a remote-management component that isn't on Corvane's published build list." |

*PETREL: if you task him on two days running, read this instead of the second result: "PETREL's account has been deleted." He is burned (−2) and gives nothing more.*
