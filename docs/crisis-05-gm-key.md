# Crisis 05: Lights Out · GM key and postmortem (paper)

**SPOILERS FOR THIS SCENARIO AND FOR THE CAMPAIGN. Anthony: don't open this (#67, #68). It depends on `claude/story-key.md`.**

*Written for Act 2. Paper only. Player packet: `claude/crisis-05-player-packet.md`.*

---

## What this scenario is for

1. **The attack isn't the point. The recovery is.** The Bureau hired a real criminal crew to break six servers so that Elsin would repair them with images from Corvane's compromised update server. Every sensible, humane pressure in the scenario pushes toward the fix that is the harm.
2. **A customer who only moves on High.** Brandt turns the calibration problem round: hedging gets nothing done, and the minister's clock does the wrong thing by default.
3. **Two false trails.** The malware points at Marrat. A forged chat log points at a person, Col. Rhun. Both are the Bureau's, and the second is the campaign's: a mole hunt protects an implant.
4. **The second hard clue.** The attackers' map came from the electronic copy of the diagram, the one lodged over LATTICE.

## Ground truth

| Day | What's really happening | True hypothesis |
| --- | --- | --- |
| 1 (9th) | Grey Ledger, paid 1.1 million in advance by a Bureau front, encrypts the six control servers it was told to hit. The ransom demand is real; the crew would like to be paid twice. | **H2** |
| 2 (10th) | The lab finds the Marrat-language strings the Bureau had appended. The crew, told to keep the victim talking, cuts its price without being asked. | **H2** |
| 3 (11th) | The minister sets his deadline, which is the one the Bureau was counting on. | **H2** |
| 4 (12th) | The Bureau posts a forged chat log blaming "the liaison office." The altered images sit ready on Corvane's update server, built two days before the attack. | **H2** |
| 5 (13th) | Kordav's broadcaster amplifies the forgery. At 1800 the images go in unless someone stops them. | **H2** |

## Adversary plan

| Aim | How | Channels |
| --- | --- | --- |
| Get the altered images installed | Break the servers; let the vendor and the minister do the rest | Honest people: Corvane, the minister, Brandt's own deputy |
| Keep Kordav out of it | First a criminal face, then a Marrat accent | Grey Ledger's own messages; strings appended to the malware |
| Protect LATTICE by starting a mole hunt | A forged chat log naming "the liaison office," then state television | A criminal forum; KSB |

**The meta-tell:** a crew that lives on being paid keeps lowering its price and extending its deadline. It was told the money doesn't matter.

## Sources (hidden values)

| Code name | True reliability | Adversary-controlled? | Notes |
| --- | --- | --- | --- |
| IPC LAB | 0.95 | No | Reports what it finds, including the appended strings, and says they were appended |
| GRID | 0.9 | No | The minister and Lind mean well. Lind's memo is true: people will suffer in a nine-day rebuild. |
| CORVANE | 0.9 | No | Honest. Doesn't know what its update server is holding. |
| WREN (Col. Rhun) | 0.8 | No | Right about the wallet. Innocent of the leak. Her paper copy never left her safe. |
| LEDGER | — | Hired | The crew tells the truth as it understands it. It doesn't know who the client is. |
| PETREL | 0.8 | No | Hears the crew complain, which is exactly what's needed |
| KSB | — | Yes | Amplifies the forgery within hours |
| MNA | — | Yes, and telling the truth | Marrat really didn't do it |
| SOCIAL | 0.3 | Partly | Carries the forged chat log |

---

## Item key: push

Kinds: **T** true · **N** noise · **P** planted · **C** clutter

### Day 1 (truth H2). Best call: H2 at Low

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-1-01 | T | — | What was hit: six control servers, and only incidentally the office network |
| R-1-02 | T | — | A real crew making a real demand. True, and not the story. |
| R-1-03 | T | — | **The item that makes Low on H2 defensible.** It went to six machines by name and ignored four hundred. Criminals take everything; somebody chose these. |
| R-1-04 | T | — | An honest offer. It is also the trap, stated on Day 1 by a man who doesn't know. |
| R-1-05 | C | — | Heating |

### Day 2 (truth H2). Best call: H2 at Medium (High if you tasked the wallet or PETREL)

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-2-01 | P | appended-after-build | See the reasoning below. The lab reports it accurately and gives the tell itself. |
| R-2-02 | N | — | A true denial. A denial tells you nothing either way. |
| R-2-03 | T | — | A crew discounting unasked on day two. They've been told not to close. |
| R-2-04 | T | — | The political clock starts |
| R-2-05 | C | — | Heaters |

### Day 3 (truth H2). Best call: H2 at High

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-3-01 | T | — | The default. If the player gives Brandt nothing, this happens. |
| R-3-02 | T | — | The map: issue 7, five paper copies and one electronic copy on LATTICE |
| R-3-03 | T | — | **Rhun, right again,** with the fact that settles who's paying. The same fact is available a day earlier for one point (C-01). |
| R-3-04 | N | — | Gloating. It tells you Kordav is enjoying this, which it would either way. |
| R-3-05 | C | — | Heaters |

### Day 4 (truth H2). Best call: H2 at High

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-4-01 | P | out-of-register, too-on-message | See the reasoning below |
| R-4-02 | T | — | Lower again, later again. A crew that doesn't want to finish. |
| R-4-03 | T | — | Ready and waiting, and honestly offered |
| R-4-04 | T | — | **The hardest true item in the scenario.** Lind is right about the cost. He's wrong about the choice, and he isn't a villain. |
| R-4-05 | C | — | Fire alarm |

### Day 5 (truth H2). Best call: H2 at High

| ID | Kind | Tells | What it really was |
| --- | --- | --- | --- |
| R-5-01 | T | — | The deadline |
| R-5-02 | P | too-fast | See the reasoning below |
| R-5-03 | T | — | True. Her copy is in her safe. She is angry, and she's entitled to be. |
| R-5-04 | T | — | **The push-only player's best evidence:** the cure was prepared two days before the disease |
| R-5-05 | C | — | Heating |

## Item key: pull

| ID | Tasking | Window | Kind | What it really was |
| --- | --- | --- | --- | --- |
| C-01 | OSINT · wallet history | Days 1–4 | T, **diagnostic** | Paid in advance from Kordav's capital. One point, and it justifies High on Day 2. |
| C-02 | PETREL | Days 1–3 | T, **diagnostic** | A contract job: six boxes, paid up front, told which six |
| C-03 | PETREL | Days 4–5 | T | "The money doesn't matter. Keep them busy until the 13th." The client knows the minister's deadline. |
| C-04 | SIGINT · negotiator | Days 2–4 | T | The handler's relay |
| C-05 | SIGINT · Marrat's ministry | Days 1–4 | T | Clears Marrat: they're as surprised as anyone |
| C-06 | Technical · target list against diagram | Days 2–4 | T, **case file** | The letter O. The attackers' map was the electronic copy, the one that crossed LATTICE. Clears everyone who only held paper. |
| C-07 | Liaison request · who holds the diagram | Days 1–4 | T | The five names, and that Arle's copy was never collected |
| C-07K | Follows C-07 | — | T, **case file** | The request went over LATTICE, and Kordav's broadcaster knew about it the next day |
| C-08 | OSINT · language in the malware | Days 2–4 | T | The strings are machine-translated |
| C-09 | OSINT · Corvane's release history | Days 1–4 | T | An unscheduled image set dated the 7th. One point, from Day 1. |
| C-10 | Technical · examine the images | Day 4 | T, **diagnostic** | Something in the images that isn't on the build list |

**Two-path rule:** that Kordav is paying is reachable by C-01, C-02, C-04 or, on push alone, R-3-03. That the recovery is the attack is reachable by C-09, C-10 or, on push alone, R-5-04.

---

## Planted items: the reasoning

### R-2-01 (Day 2, IPC LAB): the Marrat-language strings

- **What gave it away:** the lab says it in the item. The strings sit in a section appended after the program was built.
- **Check it against R-1-02 and R-1-03:** the strain is Grey Ledger's own, used nineteen times before, and none of those had Marrat's language in it. For one point, C-08 shows the strings are machine-translated.
- **Why Kordav planted it:** Marrat had a motive everyone remembered from the pipeline. If the criminal story failed, the next suspect was ready.

### R-4-01 (Day 4, SOCIAL): the "leaked chat log"

- **What gave it away:** the voice. Grey Ledger writes "Nothing personal. Pay, receive the decryptor, and we never meet again." This log says "We are obliged to our esteemed friend in the liaison office." It reads like a civil servant's idea of a criminal.
- **Check it against R-3-02 and C-06:** the malware used the electronic copy's spelling (C-06), and the liaison desk's copy was paper (R-3-02). Whoever supplied the map didn't do it with Rhun's copy.
- **Why Kordav planted it:** this one is aimed past the scenario. If the alliance starts hunting a traitor in Rhun's office, nobody examines the link her office sits on.

### R-5-02 (Day 5, KSB): "Elsin hunts a traitor"

- **What gave it away:** state television led with a detail from an anonymous forum post within four hours of it appearing.
- **Check it against R-4-01:** one origin, repeated by the broadcaster of the state that wrote it.
- **Why Kordav planted it:** to make the forgery respectable enough to act on.

---

## The analysts

| Analyst | Notes | Right | How it went |
| --- | --- | --- | --- |
| Vasko | R-1-04, R-2-01, R-4-01 | 0 of 3 | Anchored on Marrat on Day 1, was confirmed by the plant on Day 2, and on Day 4 moved straight to suspecting Rhun. He is the voice of the mole hunt, and he's sincere. |
| Halden | R-1-03, R-2-01, R-3-02, R-4-03, each a day late | 4 of 4 | This is her scenario. "Somebody gave it a map." "Stapled on afterwards." "I'd like to see how they're spelled." "When it was built, and who asked for it." Each one points at a collection target a day after the player could first have tasked it. |
| Marrow | R-1-02, R-2-03, R-3-03, R-5-02 | 2½ of 4 | Wrong that it's about money, half right that the discount is odd, properly cautious about Rhun's wallet tracing, and sharp about the broadcaster. Her best scenario so far, which matters for what's coming. |

## Brandt's actions and the endings

**She acts only on High.**

| Brief | What happens | Notes |
| --- | --- | --- |
| H1 at High | She pays | The next morning the decryptor fails on the control servers. −3 points, credibility −1. The crew was told to keep the part that matters. |
| H2 at High on Day 1 | Overruled | The minister takes the recovery away from her. Days 2–4 are frozen. Credibility −2. −5 points. |
| H2 at High, Days 2–5 | Rebuild by hand | The right answer, and it costs nine days of cold |
| H3 at High | Vendor restore, and Marrat's advisers expelled | The Bureau's best case: the images go in early and Marrat takes the blame |
| Medium or Low | Nothing | Three days running without a High costs credibility |

**Endings:**

| State after the Day 5 brief | Ending | Points |
| --- | --- | --- |
| Rebuild ordered on Day 2 or 3 | **Clean.** The control servers are rebuilt from parts and paper. The lights come back district by district over nine days. Nobody thanks Brandt in January. In March the lab finishes with Corvane's images and the minister asks to see her. | +5 |
| Rebuild ordered on Day 4 or 5 | **Clean, and cold.** The same, started late: the blackouts run into a third week. | +3 |
| Anything else | **Lights on.** Corvane's images go in at 1800 on the 13th. Power is back in two days. The minister is photographed in a control room. Everything on those six servers now answers to someone else as well. | −5 |

**Credibility:** Brandt starts from the file (3, one step up or down by the last scenario's ending). Outcome: Clean +1, Lights on 0. As in Crisis 04, a customer who made the wrong call doesn't find out inside the scenario.

## What it writes to the record

| Outcome | Alliance | Pressure | Case file | For Act 3 |
| --- | --- | --- | --- | --- |
| Clean (either) | 0 | 0 | — | The Bureau doesn't hold the grid |
| Lights on | 0 | +1 | — | The Bureau holds the grid's controls. Used in Scenario 08. |
| H3 at High at any point | −1 | +1 | — | Marrat's advisers expelled for something Marrat didn't do. Marrat stops talking to Elsin. |
| Overruled on Day 1 | −1 | — | — | — |
| C-06 collected | — | — | +1 | The map was the electronic copy |
| C-07 tasked, C-07K seen | — | — | +1 | A second liaison request heard in Kordav |
| R-4-01 doubted | — | — | +1 | The player didn't take the bait about Rhun |

## Postmortem script

> **Day 1.** A real crew made a real demand. The malware walked past four hundred machines to reach six. The vendor offered clean images, in good faith.
>
> **Day 2.** The lab found Marrat's language in the malware and told you it had been added afterwards. The crew cut its price without being asked.
>
> **Day 3.** The minister set a deadline. Rhun told you the crew had been paid in advance, from Kordav.
>
> **Day 4.** A chat log appeared, in a voice the crew has never used, thanking a friend in the liaison office. Brandt's deputy wrote that a rebuild would kill people, and he wasn't wrong about the cold.
>
> **Day 5.** Kordav's broadcaster had the forgery in a headline within four hours. The images that would fix everything had been built two days before anything broke.

**An open question** (the campaign thread; facts only):

> The attackers' list spelled one server the way only the electronic copy of the diagram spells it. And if you asked Kalsa's registry who held the diagram, Kordav's broadcaster mentioned the search the next day.

**Lessons:**

1. Ask what the attacker wants you to do next. Sometimes the damage is only there to make you fix it.
2. A crew that doesn't want to be paid isn't working for itself.
3. Evidence that points at a person in a voice that isn't the source's own was written by someone else.
4. A true cost can be attached to a wrong choice. Lind was right about the cold.
5. Some customers can't use a maybe. Know which kind you're briefing.

---

## Designer notes (critic hat)

**Dominant-strategy check** (paper estimate: calls, events and the ending; before evidence, doubts and burned sources):

| Strategy | Ending | Total |
| --- | --- | --- |
| Fast, with collection: H2 Low, then H2 High from Day 2 | Clean | **+18** |
| Best play on push: H2 Low, Medium, then High from Day 3 | Clean | **+17** |
| Late: H2 Low, Medium, Medium, High, High | Clean, and cold | **+14**, with a credibility hit |
| Always Kordav (H2 High from Day 1) | Clean, and cold (overruled, then Day 5) | **+13** |
| Paid on Day 1, then recovered by Day 3 | Clean | **+9** |
| Never above Medium on H2 | Lights on | **+4** |
| Always hedge (Low on H2) | Lights on | **0** |
| Crime all along (H1 Medium) | Lights on | **−15** |
| Marrat (H3 Medium, then High) | Lights on | **−23** |
| Crime all along at High (pays) | Lights on | **−28** |

**Watch for:**

- **"Always H2 High" scores +13,** four behind best play. The truth is fixed for the third scenario in five, and the Day 1 overrule is the same patch as Crises 02 and 04. That's three uses. **Scenario 06 must not need it,** and the story key gives it a different shape.
- **Brandt's all-or-nothing rule bends #23** (the customer commits in proportion to confidence). It's deliberate and it's hers alone. "Never above Medium" scoring +4 is the point of her. If testers find her unfair, the fix is the packet's warning, not her rule.
- **Lind's memo is the moral weight of the scenario.** The game is asking the player to choose nine days of cold on a judgment. It should feel like that. Don't soften it.
- **The plant against Rhun has a soft tell** (register) on push alone. C-06 makes it hard. A push-only player has R-3-02's line about paper and electronic copies, which is enough if they read it closely. Watch whether testers find that fair.
- **The LATTICE thread is now loud:** it's named in R-3-02, in C-06 and in the collection rules. By the end of this scenario an attentive player should suspect the link. That's the intended state going into Scenario 06, which is about proving it and about what it costs to say so.
- **Reading load is at its highest yet.** Five items, up to three notes and up to three results a day.

**Engine needs before building:**

- **A customer who acts only on High** is data: policy rules with no Medium branch
- **A credibility trigger for a run of days without a High** (a streak on a list of confidence levels)
- **A follow-up item that appears the day after a result arrives** (C-07K): the same "depends on an earlier tasking" condition as Crisis 04
- **A new discipline name, Technical,** which is data
- Case-file tags, the three story values and the "open question" block, as listed for Crisis 04
- Everything else is in the v1.1 engine
- **Map:** a schematic of Kalsa: the control room, the ministry, the liaison desk, the registry, and the cell's cold building
