# Crisis 03: The Southern Line · GM key and postmortem (paper)

*SPOILERS. Open this only after you've sent your last brief from `claude/crisis-03-player-packet.md`. Written for Phase 3 (#57, #58): the service record, analyst notes, push/pull collection and credibility. Nothing here is built.*

---

## What this scenario is for

Crisis 01 rewards trusting your agent. Crisis 02 rewards distrusting a walk-in. This one makes **suspicion the mistake, twice**:

1. The item that looks most like agenda-driven noise, WREN's unsourced claim on Day 1, is true. So is its warning on Day 3.
2. On Day 5 the adversary's own liaison officer tells the truth, because by then the truth suits him.

And the usual suspect, Kordav, did nothing. Everything pointing at Kordav was put there by Marrat, except one tidy intercept that is about something else entirely.

**The lesson:** a tell is something you can point to in the item, and a weakness is a reason to check, not a reason to doubt.

## Ground truth

| Day | What's really happening | True hypothesis |
| --- | --- | --- |
| 1 (14th) | Marrat's intelligence service has been paying and equipping the Front for a month. The valve was a rehearsal. The aim: frighten Elsin into a pact that puts Marrat's guards on the line. Marrat is also laying a trail that points at Kordav. | **H3** |
| 2 (15th) | Marrat's advisers plant a Kordav-made detonator fragment and hand over a forged transcript. The next target is already chosen: Tolen bridge. | **H3** |
| 3 (16th) | The advisers look over Tolen's guard post and leave for the holiday. The raid goes in that night. | **H3** |
| 4 (17th) | Marrat has what it wanted, or has been caught, and either way it cuts the Front loose: the paymaster leaves and the money stops. Oro, who was promised his land back, turns on Marrat and plans his own attack on the thing he actually hates. | **H1** |
| 5 (18th) | Oro's column gathers at the quarry. Marrat learns of it through its old contacts and warns Elsin, truthfully, because a rogue militia is the best advertisement its guards could have. The attack on the compressor station is set for dawn on the 19th. | **H1** |

## Adversary plans

| Who | Days | Wants you to believe | Channels |
| --- | --- | --- | --- |
| Marrat | 1–3 | **H2:** Kordav is behind the Front | Its news agency, its advisers' "forensics," its liaison officer's transcript, a new social media account |
| Marrat | 4–5 | That it was never involved, and that it's now the only one who can help | Its liaison officer. On Day 5 he tells the truth. |
| Oro's faction | 5 | That the Front has stood down | A statement from a "political office" that didn't exist last week |
| Kordav | — | Nothing. Kordav isn't in this one. | — |

## Sources (hidden values)

| Code name | True reliability | Adversary-controlled? | Notes |
| --- | --- | --- | --- |
| WREN | 0.7 here | No (biased) | Right on Days 1 and 3, for good reasons it doesn't share until asked. Wrong on Days 4 and 5, because it has stopped looking. Its bias finally pointed the right way, then kept pointing after the facts moved. |
| ESC | 0.9 | No (the channel) | Honest reporting from a building with Marrat's advisers in it. It reports the planted detonator accurately. |
| ROOK | — | **Yes** | Lies on Day 2, says nothing on Day 4, tells the truth on Day 5 |
| MAGPIE | 0.85 | No | Sees money and vehicles. His three reports are the spine of the scenario. |
| KESTREL, FINCH | 0.85, 0.9 | No | If they survived, each clears Kordav from the inside |
| MERIDIAN, CIRRANE | 0.9 | No | Nothing staged on either, unless the callback item says so |
| MNA | — | Yes | |
| FRONT | — | Its own agenda | Oro's signed communiqués are honest about what he wants. The unsigned one isn't. |
| SOCIAL | 0.3 | Partly | "Valley Truth" is Marrat's |

---

## Item key: push

Kinds: **T** true · **N** noise · **P** planted · **C** clutter

### Day 1 (truth H3). Best call: H3 at Low

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-1-01 | T | H1, H3 | — | A cheap local charge and a nine-hour repair: an attack designed to be noticed. It also contradicts "special forces instructors." |
| R-1-02 | **T** | H3 | — | **The genuine item that looks like noise.** It has the same surface as WREN's Day 1 alarm in Crisis 01: no sourcing, and an axe to grind. The difference is that this time there's sourcing to be had. Ask (C-01, free) and it arrives with dates and photographs. Doubting it costs a point. |
| R-1-03 | T | H1, H3 | — | Oro means every word. "We answer to the valley" is what he believes, even while taking Marrat's money. |
| R-1-04 | P | H2 | only-one-chain, no-detail | See the reasoning below |
| R-1-05 | C | — | — | The canteen |

### Day 2 (truth H3). Best call: H3 at Medium

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-2-01 | P | H2 | found-by-beneficiary | See the reasoning below. ESC reports the find accurately; the fragment is the plant. |
| R-2-02 | P | H2 | no-raw-material, knows-too-much | See the reasoning below |
| R-2-03 | T | H3 | — | Motive, stated in public |
| R-2-04 | T | H2, H3 | — | Someone is paying. It rules against H1 and can't say who. |
| R-2-05 | C | — | — | The auditors |

### Day 3 (truth H3). Best call: H3 at High

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-3-01 | T | H3 | — | A reconnaissance of the target by the people who chose it, and an alibi for the night |
| R-3-02 | T | H3 | — | WREN is right again, and gives the timing |
| R-3-03 | P | H2 | wrong-currency | The callback item. See the table and the reasoning below. |
| R-3-04 | T | H1, H3 | — | Timing: before the signing |
| R-3-05 | C | — | — | The market. (The holiday itself matters; the refund doesn't.) |

### Day 4 (truth H1). Best call: H1 at Medium

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-4-01 | T | — | — | The public result of the night. Either version is true reporting. |
| R-4-02 | T | **H1** | — | **The break, in Oro's own words,** and the next target named: "the compressor that took our fields still stands." |
| R-4-03 | N | — | — | A denial. False about last week, true about today, and no use either way. |
| R-4-04 | N | H3 | agenda-aligned | WREN has stopped looking. It was right for three days and assumes it still is. |
| R-4-05 | C | — | — | The regulator |

### Day 5 (truth H1). Best call: H1 at High

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-5-01 | **T** | H1 | — | **True, from the adversary.** Marrat knows Oro's plans because it trained his people, and it warns Elsin because a rogue militia sells the pact better than a tame one. Doubting it costs a point. The motive is self-serving and the content is right; those are separate questions. |
| R-5-02 | P | — | unsigned, new-voice | See the reasoning below |
| R-5-03 | N | H3 | agenda-aligned | WREN, wrong, for the same reason it was right on Day 1 |
| R-5-04 | T | H1 | — | Oro's people looking over their route |
| R-5-05 | C | — | — | Adequate |

## Item key: pull

| ID | Tasking | Window | Kind | What it really was |
| --- | --- | --- | --- | --- |
| C-01 | Liaison · WREN's sourcing | Days 1–3 | T, **diagnostic** | What turns R-1-02 from a claim into evidence. Free. |
| C-02 | MAGPIE | Days 1–2 | T, **diagnostic** (second path) | Marrat's money, in sequence |
| C-03 | MAGPIE | Day 3 | T | Timing and direction: south, tonight or tomorrow |
| C-04 | MAGPIE | Day 4 | T, **diagnostic** for the break | The money stopped and Oro broke the handset |
| C-05 | SIGINT · the Front's radios | Days 1–3 | T | Marrat's kit |
| C-06 | SIGINT · the Front's radios | Day 4 | T | The break, and the target: "quarry" |
| C-07 | OSINT · detonator markings | Days 2–4 | T | The fragment is Kordav-made and Marrat-owned. One point. |
| C-08 | SIGINT · Kordav 4th Army nets | Days 1–4 | **N** | **The tidy item that is nothing.** B-graded, on topic, and about Kordav's own fuel spur at Varn and what the contractors will charge. The tell is in the text: Varn is KESTREL's depot, 300 km inside Kordav. Citing it scores 0. |
| C-09 | KESTREL | Days 1–3, two mornings later | T | Clears Kordav from the depot floor. Only if he survived Crisis 01. |
| C-10 | IMINT · Kordav's southern crossings | Days 1–4 | T | The weaker way to the same answer, for players who burned KESTREL |
| C-11 | FINCH | Days 1–3, two mornings later | T | Clears Kordav from the ministry. Only if he survived Crisis 02. |
| C-12 | IMINT · Tolen approaches | Day 3 | T | The raiding party, waiting |
| C-13 | IMINT · the ford | Days 1–3 | T | The supply route from Marrat |
| C-14 | IMINT · the ford | Days 4–5 | T | The route goes dead: the break |
| C-15 | IMINT · Sarn valley | Days 1–3 | T | More fighters and newer vehicles than a valley could pay for |
| C-16 | IMINT · Sarn valley | Days 4–5 | T, **diagnostic** for the target | The column at the quarry. Also what exposes R-5-02. |
| C-17 | OSINT · "Valley Truth" | Days 3–4 | T | Marrat's account |

Kessa returns nothing on every day. It's a deliberate dry hole: looking where the usual suspect would strike, and finding nothing, is information.

## The callback item (R-3-03)

One item on Day 3 depends on the service record. Marrat has read the same after-action reports Kordav has.

| On your record | Version of R-3-03 | Tell | Cross-check |
| --- | --- | --- | --- |
| You cited, or didn't doubt, the snow photo in Crisis 01 (R-5-05) | A photo of "Kordavan instructors in the Sarn valley" | Ostrel's water tower is in the background: it's from the IRON HARVEST press pack | C-17, C-10 |
| You cited, or didn't doubt, the staged recall in Crisis 02 (C-06) | No push item. Instead, tasking the Front's radios on Day 3 returns C-05 plus a call in Kordavan-accented speech on an open channel, naming Kessa. | Every other Front call that week is encrypted (C-05). The one call in the clear names the wrong target in the wrong accent. | C-05, C-12, C-03 |
| Neither, or no record | The payment order in the packet | A Kordavan army order that pays in Marrat crowns | C-02, C-17 |

The postmortem says which you got and why: "They tried this because it worked on you last time," or "They tried something new because you caught the last one."

---

## Planted items: the reasoning

### R-1-04 (Day 1, MNA): "Kordavan instructors"

- **What gave it away:** unnamed "security sources," no place, no number, no date, from the state outlet of the country offering to sell Elsin the cure.
- **Check it against R-1-01:** the charge was a quarrying charge sold up and down the valley, placed by someone who knew the housing. Special forces instructors don't teach that.
- **Why Marrat planted it:** start the Kordav story on Day 1, before anyone has looked.

### R-2-01 (Day 2, ESC): the detonator fragment

- **What gave it away:** Elsin's engineers swept the site and found nothing. The fragment appeared on a second sweep, in the hands of the advisers whose government benefits.
- **Check it against R-1-01 and C-07:** the first report describes a quarrying charge (R-1-01). The lot number, for one point, traces to a batch Kordav sold to Marrat's mining ministry (C-07).
- **Why Marrat planted it:** physical evidence outranks talk. ESC reported it honestly, which is why it arrives graded B.

### R-2-02 (Day 2, ROOK): the transcript

- **What gave it away:** translated text only, with no date and no audio. And it names the next target. How would Marrat's liaison officer know what the Front will hit next?
- **Check it against R-1-04 and R-2-01:** three items in two days point at Kordav, and all three came through Marrat's hands. If you tasked Kordav's own nets (C-08), they're talking about a fuel spur at Varn.
- **Why Marrat planted it:** to have Kordav blamed in advance for an attack Marrat had already scheduled. The plant is false about who and true about where, which is the most useful thing in it.

### R-3-03 (Day 3, SOCIAL): the payment order (default version)

- **What gave it away:** a Kordavan army order that pays in Marrat crowns.
- **Check it against C-02 and C-17:** MAGPIE says the Front is paid in new Marrat crowns by "a cousin from across the river" (C-02). The account is ten days old and its first followers work for Marrat's news agency (C-17).
- **Why Marrat planted it:** one more push before the raid. The forger used the currency he had to hand.

### R-5-02 (Day 5, FRONT): "suspended operations"

- **What gave it away:** the Front has never had a "political office," and every earlier statement was signed by Oro.
- **Check it against R-4-02, R-5-04 and C-16:** yesterday Oro said the compressor still stands (R-4-02). Last night strangers photographed the quarry road gate (R-5-04). Imagery shows eight vehicles in the quarry (C-16).
- **Why Oro's people planted it:** one quiet night is all they needed.

---

## The analysts

Notes are authored. Each analyst goes wrong in the way their trait says.

| Analyst | Trait | Notes | Right | How they went wrong |
| --- | --- | --- | --- | --- |
| Imre Vasko | Anchors on the first theory | R-1-02, R-2-01, R-4-02, R-5-01 | 1 of 4 | His first note is the best advice in the scenario: ask WREN for its sourcing. Then the detonator hands him a theory, Kordav, and he reads everything after it that way, through two changes of truth. |
| Noor Halden | Slow but careful | R-1-01, R-2-01, R-3-01, each a day late | 3 of 3 | Never wrong. Her note on the Tolen reconnaissance arrives the morning after the raid. |
| Tess Marrow | Overconfident | R-1-03, R-3-03, R-5-02 | 1½ of 3 | "Home-grown, full stop" was wrong for three days and right by accident on the fourth. She authenticates the forged payment order from its letterhead and misses the currency. Her last note is sharp. |

## Halvorsen's moves, and the two nights

**Policy:** High moves the full company to the site that goes with the hypothesis (H1 Sarn, H2 Kessa, H3 Tolen). Medium sends a platoon there and returns the rest to reserve. Low changes nothing.

**Night of Day 3: Tolen** (Marrat's raid)

| Force after the Day 3 brief | Outcome | Points | Credibility |
| --- | --- | --- | --- |
| Company at Tolen, arrived on Day 3 | **Caught.** Seven prisoners and Marrat-pattern radios. The pact talks are postponed. | +4 | — |
| Company at Tolen since Day 1 or 2 | **Displaced.** Marrat's advisers saw it. The raid hits the Dessa valve yard instead. | −2 | −1 |
| Platoon at Tolen | **Driven off.** No prisoners. | +1 | — |
| Company at Kessa | **Cut,** with the company at the wrong end of the country | −3 | −2 |
| Anything else | **Cut.** | −3 | — |

**Dawn after Day 5: the Sarn compressor station** (Oro's attack). These are the endings.

| Force after the Day 5 brief | Ending | Points |
| --- | --- | --- |
| Company at Sarn | **Held.** Oro's column comes up the quarry road at first light and meets a company that has been waiting since dusk. It's over in ten minutes. Oro is taken alive, still asking about his fields. | +3 |
| Platoon at Sarn | **Damaged.** The platoon holds the control building. The cooling plant burns. The line is down for three weeks. | 0 |
| Nothing at Sarn | **Burning.** The compressor station is alight by sunrise and the line is down for the summer. The task force goes onto trucked fuel. | −3 |

**Epilogue line, by what happened at Tolen:**

- *Caught:* "The pact is dead. Elsin sends Marrat's advisers home with their radios."
- *Driven off or Displaced:* "Elsin signs a thinner pact in the autumn. Marrat's guards get the southern third of the line."
- *Cut:* "Elsin signs on the 20th. Marrat's guards are on the line within the month, protecting it from a militia Marrat built."

**Credibility:** starts where Crisis 01 left it. Triggers: the company moved from one site to another on Days 1–3 (−1), Displaced (−1), Cut with the company at Kessa (−2), Low two days running (−1 each). Moving the company from Tolen to Sarn on Day 4 or 5 costs nothing: the facts changed, and Halvorsen can see that they did. Outcome adjustment: Held +1, Burning −1, and +1 more if Caught.

---

## Postmortem script

> **Day 1.** WREN told you who was behind it, in one unsourced sentence with a grudge attached. It looked exactly like the alarm it raised over Tarsk, and that time it was guessing. This time it had a surveillance log, and all you had to do was ask. Marrat's news agency told you it was Kordav. It had nothing.
>
> **Day 2.** A detonator turned up on the second sweep, found by the people selling the pact. A transcript with no date and no audio named the next target. Everything that pointed at Kordav had passed through Marrat's hands first.
>
> **Day 3.** The advisers looked over a six-man guard post and went on holiday. MAGPIE's diesel went south. A platoon could be there without anyone knowing. A company arriving that day was a surprise; a company sitting there since the 14th was an announcement.
>
> **Day 4.** The money stopped. Oro, who had been promised his fields, said so in public and named what he'd burn. WREN, right for three days, didn't notice the answer had changed.
>
> **Day 5.** Marrat's liaison officer told the truth, because the truth had started to suit him. WREN called it a trick. The Front's "political office" said the fighting was over. Eight vehicles were already in the quarry.

**Lessons:**

1. A weakness is a reason to check, not a reason to doubt. Ask for the sourcing.
2. A tell is something you can point to in the item. A feeling about the source isn't one.
3. Ask whose hands each item passed through. Three items from one hand are one item.
4. A source that was right yesterday is not right today because of it.
5. An adversary can tell you the truth. Judge the content and the motive separately.
6. When a sponsor lets go of a proxy, the proxy doesn't stop. It goes after what it wanted in the first place.
7. Being right too visibly is a way of being wrong.

---

## What the service record changes

| On the record | Effect in Crisis 03 |
| --- | --- |
| Crisis 01 ending and final credibility | Halvorsen's opening line and your starting credibility. At 5, one extra collection point a day; at 1, two fewer and he discounts your confidence from Day 1. |
| KESTREL burned | C-09 is gone. C-10 (imagery, weaker) is the other way to clear Kordav. |
| FINCH burned | C-11 is gone |
| WREN's track record | Its file grade is C. That's the reason R-1-02 arrives as C3 and looks so easy to dismiss. |
| Which plants fooled you | The version of R-3-03 |
| This scenario writes | Whether MAGPIE was burned, the two outcomes, Halvorsen's final credibility, and which of Marrat's plants you cited |

## Designer notes (critic hat)

**Does it play differently again?**

| | Crisis 01 | Crisis 02 | Crisis 03 |
| --- | --- | --- | --- |
| Question | What is an army doing? | Is one man telling the truth? | Whose hand is behind a third party? |
| Decision | Whether to move | What to tell an ally | Where to stand, and how visibly |
| Truth | Shifts once (Day 3) | Fixed | Shifts once (Day 4), in the unexpected direction |
| Right instinct | Trust your agent | Distrust the gift | Check before you doubt |
| The usual suspect | Guilty | Guilty | Innocent |
| Consequences | One, at the end | One, at the end | Two: mid-scenario and at the end |

**Dominant-strategy check** (paper estimate: calls, the Tolen night and the ending; before evidence, doubts and burned sources):

| Strategy | Tolen | Sarn | Total |
| --- | --- | --- | --- |
| Best play: H3 Low, H3 Medium, H3 High, H1 Medium, H1 High | Caught | Held | **+18** |
| The same, with H1 High on Day 4 | Caught | Held | **+19** |
| Believe WREN at once: H3 High from Day 1, then H1 Medium, H1 High | Displaced | Held | **+15** |
| Never above Medium, right hypothesis each day | Driven off | Damaged | **+11** |
| Slow believer: H1 Low, H3 Low, H3 Medium, H1 Low, H1 High | Driven off | Held | **+10** |
| Distrust WREN, suspect Kordav, catch up late: H1, H2, H2 at Medium, then H1 Medium, H1 High | Cut | Held | **−1** |
| Always hedge (Low, right hypothesis) | Cut | Burning | **−1** |
| Always Marrat (H3 High every day) | Displaced | Burning | **−4** |
| Local all along (H1 Medium every day) | Cut | Damaged | **−5** |
| Always Kordav (H2 Medium every day) | Cut | Burning | **−16** |

**Watch for:**

- **"Believe WREN at once" is only 3 points behind best play.** That's by design, since trusting the right thing early should beat distrusting it, but the Displaced outcome is carrying the whole gap. If testers find Displaced unfair, the warning has to be louder: it's currently one line in Halvorsen's habits ("a company is not discreet").
- **Confidence doubles as visibility.** A player who is honestly sure on Day 2 may want the quiet platoon anyway, and the brief has no way to say "High, but quietly." This strains #23 (the customer commits in proportion to confidence). If it grates in play, the fix is a posture choice on the brief, which is a new mechanic and belongs in a decision, not a patch.
- **Day 5's true warning from ROOK** will be doubted by almost everyone on a first run. That's the point, but it must not feel like a trick: R-4-02, R-5-04 and C-16 all support it without him.
- **WREN going wrong on Day 4** right after being vindicated is the meanest beat in the scenario. R-4-02 contradicts it the same morning, in Oro's own words.
- **Reading load.** Five push items plus up to three analyst notes a day, plus results. Time Day 2 and Day 3 before adding anything.
- **Three states and a militia.** Marrat has one motive (guards on the line) and one voice (ROOK), and Kordav never speaks. Keep it that way.
- **MAGPIE carries a lot.** A player who burns him on Day 2 loses the timing report and the break report. C-12, C-06 and C-14 cover the same ground through other disciplines, so the two-path rule holds.

**Engine needs before building** (Phase 3):

- **The service record:** read at the start (credibility, source availability, item variants), written at the end
- **Item variants** chosen by a record flag (R-3-03) or by an earlier outcome (R-4-01)
- **A mid-scenario outcome:** an event that reads where the force is, picks the first matching result, scores it, sets a flag, and changes the next morning's read-in and reply
- **Endings with an epilogue line** chosen by that flag
- **Analyst notes** on items, with a hit-rate table in the postmortem
- **A source burned by consecutive tasking** (MAGPIE) already works as in Crisis 01
- **States** are site and size (reserve, platoon or company at each of three sites): data only, on the v0.9 named-state policy
- **Map:** the line from Kessa to Tolen, the Sarn valley and quarry, the ford, Dessa, and the borders with Kordav and Marrat
