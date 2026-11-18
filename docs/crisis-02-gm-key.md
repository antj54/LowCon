# Crisis 02: The Walk-in · GM key and postmortem (paper)

*SPOILERS. Open this only after you've sent your last brief from `claude/crisis-02-player-packet.md`. Written for Phase 2: the push/pull collection model (#51), the Low/Medium/High call (#46) and credibility (#50). Day 2 item IDs were renumbered in the #51 rewrite: the old R-2-02 (room 412) is now debrief result C-10, and the old R-2-05 (embassy traffic) is now SIGINT result C-07.*

---

## Ground truth

The truth never shifts: LANTERN is a dangle on every day. What changes is how much of the evidence shows it.

| Day | What's really happening | True hypothesis |
| --- | --- | --- |
| 1 (5th) | LANTERN is a real mid-level planning officer, recruited by the Bureau (Kordav's security service) for one job. He walked in on orders. The aim: smear Vell before the vote, and see who we ask about him. | **H2** |
| 2 (6th) | The Bureau watches the defence ministry for anyone asking about LANTERN, and puts a staged "recall" on the headquarters net it assumes we read. "Room 412" comes from a story the Bureau planted in *The Kalsa Courier* three weeks ago. | **H2** |
| 3 (7th) | The ledger is delivered: genuine Bureau paper, with entries forged from Vell's public schedule. Elsin's opposition, working alongside Kordav's media campaign, gets the vote moved up. | **H2** |
| 4 (8th) | The Bureau leaks "a defector with evidence" to an opposition MP, so the smear lands even if we keep quiet. | **H2** |
| 5 (9th) | State TV announces a "kidnapping," and LANTERN asks to go public on the morning of the vote. | **H2** |

## Adversary plan

| Objective | How | Channels |
| --- | --- | --- |
| **Make us believe H1** and pass the allegation to Elsin before the vote | A walk-in who volunteers true but worthless information about IRON HARVEST, then the allegation, then "proof," then urgency. Planted detail held back for when we ask for specifics. | LANTERN (volunteered and under questioning), KSB, *The Kalsa Courier* (planted three weeks earlier), an opposition MP |
| **Fake the damage control a real defection would cause** | A staged recall order on the Bureau's headquarters administrative net, which Kordav has assumed we read since IRON HARVEST was blown | MERIDIAN, if we task the headquarters net |
| **Find our sources** | LANTERN asks who in the ministry could vouch for him. The Bureau watches who comes asking. | LANTERN's question (R-2-02), the Bureau's watch on the ministry (burns FINCH) |
| **Win anyway if we stay quiet** | Leak the "defector" to the opposition, and stage a press statement for vote morning | The opposition MP, KSB, LANTERN |

**The meta-tell:** everything LANTERN gave us that we could check was something Kordav had already lost. Nothing he gave us cost Kordav anything. And the only damage control we ever saw was on the one net Kordav expected us to be reading.

## Push and pull

| Layer | Items | Deception in it |
| --- | --- | --- |
| **Push** (arrives every day) | STATION's notes on the room, what LANTERN volunteers, KSB, CWS, SOCIAL, WREN's pushes | The allegation, the vouching question, the ledger, the urgency, the MP's post, the kidnapping story, the press statement |
| **Pull** (only if tasked) | Debriefing lines, FINCH, three SIGINT targets, three OSINT targets, WREN on request | **Room 412** (C-10): the dangle's prepared detail, given when we press for specifics. **The staged recall** (C-06): traffic placed where Kordav assumed we listen. **FINCH's burn**: the Bureau watching for who asks. |

## Sources (hidden values)

| Code name | True reliability | Adversary-controlled? | Notes |
| --- | --- | --- | --- |
| LANTERN | — | **Yes** | A real officer on a Bureau assignment. His one true item, R-1-02, is chickenfeed. Under questioning he's accurate about his own job and vague about everything else. |
| STATION | 1.0 | No | Reports exactly what happens in the room |
| FINCH | 0.9 | No | Honest. The Bureau is watching who asks about LANTERN, so the first meeting is his last. |
| WREN | 0.6 | No (biased) | Some of its officers want Vell gone, so it repeats the doubts |
| MERIDIAN | 0.9 | No (the channel) | Reliable, but Kordav suspects the headquarters net is read and stages one message on it (C-06). The neutral-capital office's traffic is genuine. |
| KSB | — | Yes | Runs the media side of the smear |
| CWS | 0.9 | No | |
| SOCIAL | 0.3 | Partly | Carries the MP's planted claim |

---

## Item key: push

Kinds: **T** true · **N** noise · **P** planted · **C** clutter

### Day 1 (truth H2). Best call: H2 at Low

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-1-01 | T | — | — | True. Two details matter later: he asked asylum for himself only ("my wife will be fine"), and he asked to be kept secret. |
| R-1-02 | T | H1, H2 | — | **True, and worthless to Kordav.** IRON HARVEST was blown three months ago. Real information that costs the other side nothing is chickenfeed. Doubting it costs a point, which is the lesson: true isn't the same as genuine. |
| R-1-03 | P | H1 | access-mismatch, conditional-gift | See the reasoning below |
| R-1-04 | T | H2 | — | Motive and timing: the vote is why LANTERN is here this week |
| R-1-05 | C | — | — | Fire drill |

### Day 2 (truth H2). Best call: H2 at Medium

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-2-01 | T | H2 | — | A rehearsed story told by a man with nothing to fear |
| R-2-02 | P | H1 | fishing | See the reasoning below |
| R-2-03 | T | H2 | — | Kordav's media attacking the same man LANTERN accuses, the same day, and not looking for its missing officer |
| R-2-04 | C | — | — | Metro strike |

### Day 3 (truth H2). Best call: H2 at High

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-3-01 | N | H1 | agenda-aligned | Elsin's anti-Vell faction repeating itself |
| R-3-02 | P | H1 | only-public-dates | See the reasoning below |
| R-3-03 | T | **H2** | — | **The best item in the push stream.** Real agents get paid on trips nobody announces. |
| R-3-04 | T | H2 | — | The deadline LANTERN will lean on tomorrow |
| R-3-05 | C | — | — | A wedding |

### Day 4 (truth H2). Best call: H2 at High

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-4-01 | P | H1 | convenient-timing | See the reasoning below |
| R-4-02 | T | H2 | — | His story about his family changes once the pressure is on |
| R-4-03 | P | H1 | leak-origin | See the reasoning below |
| R-4-04 | T | H2 | — | The media campaign building toward the vote |
| R-4-05 | C | — | — | Still phishing |

### Day 5 (truth H2). Best call: H2 at High

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-5-01 | P | H1 | convenient-timing | See the reasoning below |
| R-5-02 | P | H1 | out-of-pattern | See the reasoning below |
| R-5-03 | T | — | — | If anything we passed ends up in the motion, this is where it shows |
| R-5-04 | C | — | — | Metro strike over |

## Item key: pull (collection results)

| ID | Tasking | Window | Kind | What it really was |
| --- | --- | --- | --- | --- |
| C-01 | SIGINT · Bureau office, neutral capital | Days 1–4 | T, **diagnostic** | **No damage control.** If an officer with the access LANTERN claims had really defected, this office would be pulling people home and changing codes. Nobody moves, nothing changes, and headquarters reminds staff about "media discipline." Also the cross-check that exposes C-06. |
| C-02 | OSINT · LANTERN's family | Days 1–4 | T, **diagnostic** (second path) | A real defector's family gets questioned and stopped from traveling. His goes to the lake. One point, and it tells you the same thing as C-01. |
| C-03 | OSINT · Elsin's press | Days 1–4 | T | The origin of "room 412." Makes C-10 circular. |
| C-04 | FINCH | Days 1–3, two mornings later | T, **burns FINCH** | Confirms the access mismatch, and his remark that someone else asked about LANTERN's friends is the Bureau's watch showing. **FINCH is burned:** −2 points, and in Phase 3 he stays gone. Strong evidence, at a price. |
| C-05 | Liaison · Vell's travel records | Days 1–4 | T | The Hotel Sorel meeting happened, logged and innocent. WREN's remark is its faction talking. |
| C-06 | SIGINT · Bureau headquarters net (first tasking) | Days 1–4 | **P** | See the reasoning below |
| C-07 | SIGINT · Kordav embassy | Days 1–4 | T | Kordav's embassy is under orders to stay hands-off. Nobody is looking for him. |
| C-08 | OSINT · Kordav defence ministry | Days 1–4 | T | The cheap version of FINCH's answer: he's a logistics planner, and the Bureau is a different service. Costs 1 point and burns nobody. |
| C-09 | Debrief · the ledger | Days 3–4 | T | A planner can't walk into the Bureau's registry, and a friend who signs him in has a name. The ledger was handed to him. |
| C-10 | Debrief · the Vell details | Days 1–3 | **P** | See the reasoning below |
| C-11 | SIGINT · Bureau headquarters net (second tasking) | Days 2–4 | T | The staged recall was a one-off. Real damage control generates traffic for days. |
| C-12 | Debrief · his access | Days 1–4 | T | Expert on his own job, vague on the Bureau's. "People talk" is not access. |
| C-13 | Debrief · his family | Days 1–3 | T | A man unafraid for his wife. A real defector knows exactly what the Bureau does to families. Pairs with R-4-02, when the story changes. |

---

## Planted items: the reasoning

Each planted item has a tell in its own text and at least one check against an item you have, or could have tasked, by that day. Nothing here relies on the key alone.

### R-1-03 (Day 1, LANTERN, push): the allegation

- **What gave it away:** he says he learned it from "colleagues in the Bureau." A planning officer doesn't see the security service's agent files. And the gift comes with a condition: resettlement first.
- **Check it against R-1-01, R-1-02:** both put him on the General Staff's planning directorate, which is military planning, not counterintelligence. Debriefing his access (C-12) or the ministry directory (C-08) confirms it.
- **Why Kordav planted it:** plant the claim on Day 1 and attach a hook, so we invest in him before we test him.

### C-10 (debrief, pull): room 412

- **What gave it away:** an exact room number he can't say how he knows.
- **Check it against R-1-03 and C-03:** a planning officer has no route to that detail (R-1-03). And it was already in print: *The Kalsa Courier* ran it three weeks ago (C-03, OSINT on Elsin's press, 1 point any day). One origin, now dressed up as two.
- **Why Kordav planted it:** a dangle is briefed with a prepared detail for when the debriefers push for specifics. Precision sounds like access.
- **How Kordav knew we'd ask:** it didn't need to. Every debriefer asks for specifics.

### R-2-02 (Day 2, LANTERN, push): "who can vouch for me?"

- **What gave it away:** a defector asking us who we have inside his own ministry.
- **Check it against R-1-03:** a man who claims to know Bureau agent files could prove himself with something only the Bureau knows. Instead, he asks us to show our hand.
- **Why Kordav planted it:** the dangle's second job was to find our sources. The Bureau was watching the ministry for whoever came asking about him. Tasking FINCH (C-04) did exactly that.

### C-06 (SIGINT on the Bureau headquarters net, pull): the staged recall

- **What gave it away:** a real compromise order goes out on the Bureau's secure operational channel at the highest precedence. This one went on the administrative net, at routine precedence, and names the officers it's recalling. It reads like a press release for an audience of one.
- **Check it against C-01, C-02 or C-07:** the neutral-capital office's own traffic shows every officer still at post and nothing changed (C-01). His family isn't questioned (C-02). The embassy is told to stay out of it (C-07). Task the headquarters net again and the recall is never mentioned (C-11). Any one of these, all available the same day, says the recall never happened.
- **Why Kordav planted it:** the strongest sign of a genuine defection is the other side's damage control. Kordav couldn't fake it everywhere, so it faked it where it thought we were listening.
- **How Kordav knew we'd look:** IRON HARVEST was blown three months ago, and the Bureau has assumed since then that its administrative net is read. It didn't know we'd task it. It put the message where we might.

### R-3-02 (Day 3, LANTERN, push): the ledger

- **What gave it away:** every payment date matches one of Vell's trips abroad.
- **Check it against R-3-03:** all of those trips are on his public schedule, and none of his private travel is. Real agents get paid on trips nobody announces. Debriefing the ledger (C-09) adds that a planner had no way into the registry it came from.
- **Why Kordav planted it:** genuine Bureau paper gets a forgery past a quick look.

### R-4-01 (Day 4, LANTERN, push): "before the vote"

- **What gave it away:** the urgency is tied to a deadline only Kordav benefits from.
- **Check it against R-3-04 and R-1-04:** the vote was moved up yesterday, and it was the reason for his timing from Day 1.
- **Why Kordav planted it:** force a decision before verification can catch up.

### R-4-03 (Day 4, SOCIAL, push): the MP's post

- **What gave it away:** the MP knows about "a Kordavan officer who has defected to an allied service."
- **Check it against R-3-01 and R-1-01:** Elsin's own service only had a rumor about "someone from Kordav" (R-3-01). LANTERN asked us to keep him secret (R-1-01). Nobody on our side said "defector." Only LANTERN's side could have. *If you passed the full allegation to Elsin, this tell doesn't hold, because the leak could be theirs. By then the crisis is lost anyway.*
- **Why Kordav planted it:** a backup plan. The smear lands even if we never share anything.

### R-5-01 (Day 5, KSB, push): the "kidnapping"

- **What gave it away:** four days of silence about a missing officer, then a kidnapping story the day before the vote.
- **Check it against R-2-03 and R-4-04:** state TV spent those days attacking Vell, not mentioning LANTERN. If you tasked the embassy (C-07), it was told to keep its distance.
- **Why Kordav planted it:** make the defection look real just in time for LANTERN to go public.

### R-5-02 (Day 5, STATION, push): the press statement

- **What gave it away:** a man who asked us to keep him secret for his safety now wants a press statement released on the morning of the vote.
- **Check it against R-1-01:** his first request was secrecy.
- **Why Kordav planted it:** the smear's last delivery route, timed for maximum effect.

---

## Marlowe's actions and the endings

**Actions** (see the player packet for her habits table):

| State | Triggered by | Reversible? |
| --- | --- | --- |
| Full allegation shared | H1 at High | **No.** Elsin acts within a day. |
| Caveated warning shared | H1 at Medium | Yes: withdrawn by any H2 call at Medium or High. Credibility −1. |
| Sharing stopped, LANTERN restricted | H2 at Medium | — |
| Smear warning sent (counter) | H2 at High | — |
| Debriefing ended | H3 at Medium or High | — Debrief taskings return nothing after this. |
| Early counter rebuffed | H2 at High on Day 1 | The warning is withdrawn. Nothing can go to Elsin on Days 2–4. Credibility −2. |

**Endings** (at the vote, the morning of the 10th):

| Condition | Ending | Points |
| --- | --- | --- |
| Full allegation shared at any point | **Burned.** Elsin arrests Vell on the morning of the vote. Six months later the ledger is exposed as a forgery built from his public schedule. Nobody in Kalsa trusts allied intelligence again. Kordav couldn't have bought a better outcome. | −5 |
| Caveated warning still in place at the vote | **Sidelined.** The caveat leaked within a day and is quoted in the opposition's speech. Vell resigns "to clear his name." Elsin's reformers lose their best voice, and Kordav never fired a shot. | −3 |
| Smear warning sent on Day 2, 3 or 4 | **Exposed.** Elsin's defence minister stands up in parliament with your warning: Kordav is running a smear, and its "defector" was sent. The motion fails by forty votes. LANTERN's statement never airs. Two Bureau officers are quietly recalled from the neutral capital, for real this time. | +5 |
| Smear warning sent only on Day 5 (including after the early-counter freeze) | **Survived.** Your warning reaches Kalsa the night before the vote. The motion fails by three. Vell keeps his job and loses his reputation. | +1 |
| None of the above | **Shelved.** You kept it to yourself. The opposition runs with the MP's claim anyway, and Vell survives by five votes without knowing how close it came or who was behind it. | 0 |

Credibility outcome adjustment (#50): Exposed +2, Survived 0, Shelved 0, Sidelined −2, Burned −2.

---

## Postmortem script

> **Day 1.** LANTERN walked in with a gift and a condition. He told you about IRON HARVEST, which was true and cost Kordav nothing: the operation had been blown for three months. The Vell allegation came from "colleagues in the Bureau," and a planning officer doesn't see the Bureau's agent files.
>
> **Day 2.** If you pressed him for details, room 412 came from a newspaper: *The Kalsa Courier* printed it three weeks before he walked in. His question about who could vouch for him was the second job he'd been sent to do: find out who we have in the ministry. And if you read the Bureau's headquarters net, you saw a recall that never happened. Kordav put it where it thought we were listening.
>
> **Day 3.** The ledger was real paper telling a forged story. Every payment matched a trip anyone could look up. Real agents get paid on trips nobody announces.
>
> **Day 4.** The deadline was Kordav's, not Elsin's. The MP heard about "a defector" from the only people who knew besides us.
>
> **Day 5.** A man kidnapped by Western intelligence asked to record a press statement for the morning of the vote. Kordav stayed silent for four days, then announced a kidnapping. The Bureau's office in the neutral capital never so much as changed a code.

**Lessons:**

1. A walk-in's verifiable details prove access, not intent. Ask what they cost the other side.
2. Check claims against access: what could he actually have seen?
3. Count origins. A detail that's already in print isn't corroboration.
4. Watch how the other side reacts, everywhere you can. Damage control is hard to fake on every channel at once.
5. The adversary knows some of what you collect. Ask what it expects you to hear.
6. Collection can be seen too. Asking the wrong source the wrong question can burn it.

---

## Designer notes (critic hat)

**Does it play differently from Crisis 01?** (the Phase 2 gate)

| | Crisis 01 | Crisis 02 |
| --- | --- | --- |
| Question | What is an army doing? | Is one man telling the truth? |
| Decision | Move troops | Share intelligence with an ally, or warn it |
| Truth | Shifts on Day 3 | Fixed; how visible it is changes |
| HUMINT | Always honest | The main channel of deception, volunteered and under questioning |
| Collection | Standing stream plus tasked extras | Push the public, pull the secret (#51). Tasking finds the diagnostic, can walk into staged traffic, and can burn your own source. |
| Customer | Military commander | Political official |

**Fairness check (#51 rules):**

| Pulled plant | Tell in its own text | Cross-check reachable the same day | Paths |
| --- | --- | --- | --- |
| C-10 room 412 | Can't say how he knows | R-1-03 (push), C-03 (OSINT, 1 point) | 2 |
| C-06 staged recall | Admin net, routine precedence, names its targets | C-01 (SIGINT), C-02 (OSINT), C-07 (SIGINT), C-11 (re-task) | 4 |

The diagnostic ("no damage control") has two tasking paths: C-01 (SIGINT, 3 points) and C-02 (OSINT, 1 point). C-07 supports it. No single bad tasking locks a player out.

**Dominant-strategy check** (paper estimate: calls plus ending, before evidence, doubts and burned sources; with credibility #50):

| Strategy | Ending | Total |
| --- | --- | --- |
| Best play: H2 Low, H2 Medium, then H2 High from Day 3 | Exposed | **+17** |
| Paranoid: H2 High every day | Shelved (Day 1 counter rebuffed, credibility Discounted, so Day 5 High acts as Medium and no warning goes) | **+15** |
| Fooled by the staged recall, then recovers: H2 Low, H1 Medium on Day 2, H2 High from Day 3 | Exposed, credibility Questioned (withdrew the caveat) | **+13** |
| Never above Medium on H2 | Shelved | **+9** |
| Always hedge (Low) | Shelved, credibility Discounted | **+5** |
| "He's a fabricator" (H3 Medium every day) | Shelved | **−10** |
| Cautious believer (H1 Medium every day) | Sidelined | **−13** |
| Trust the walk-in (H1 High every day) | Burned | **−25** |

**Watch for:**

- **"Always assume a dangle" is still close (+15 vs +17).** Credibility widened the gap by one point, because the rebuffed counter now leaves Marlowe discounting Day 5. Evidence widens it further: a paranoid player who never tasks has fewer true items to cite. The real fix is still a genuine walk-in in a later crisis (parking lot).
- **Nine plants out of about 36 possible items** (7 push, 2 pull). A deception crisis, but watch whether testers find it exhausting.
- **C-06 is the hardest plant in either crisis.** Its tells are procedural (net and precedence), which an intel-trained player will catch and a newcomer may not. It's fair because four same-day cross-checks contradict it, and C-11 exposes it to anyone who re-tasks. If testers call it unfair, add a line to MERIDIAN's access: "Compromise traffic normally goes on the Bureau's secure channel."
- **Burning FINCH has to feel fair.** The warnings are LANTERN's question on Day 2, FINCH's own access text ("a dangerous place to ask questions") and the cheaper OSINT alternative (C-08). FINCH gives the stronger evidence; that's the trade.
- **Free Liaison:** only one liaison target, and it can be collected once, so it can't dominate.

**Engine needs before building** (Phase 2, step 4):

- The customer's actions here aren't a ladder like company and battalion. The engine needs **named states with transitions** (shared, caveated, restricted, countered, ended), plus ending conditions such as "ever reached" (Burned) and "first reached on day N" (Exposed or Survived).
- **Per-target cost and delay:** debriefing is HUMINT at 2 points, next day; FINCH is HUMINT at 3 points, two days.
- **Burn on first tasking** (FINCH), and **debrief targets that close** when the debriefing is ended (H3).
- **Ordered results per target** (C-06, then C-11 on the headquarters net). The v0.7 engine already resolves the first uncollected result in its window, so this is data only.
- **Credibility triggers:** the rebuffed early counter (event) and withdrawing a caveat (reply). Both fit the v0.8 format.
- **Map:** the neutral capital (embassy, Bureau office), Kordav's capital (Bureau headquarters, LANTERN's home), and Kalsa (parliament, Hotel Sorel). Target pins for the three SIGINT targets and the family.
