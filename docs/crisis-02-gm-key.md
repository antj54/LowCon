# Crisis 02: The Walk-in · GM key and postmortem (paper)

*SPOILERS. Open this only after you've sent your last brief from `claude/crisis-02-player-packet.md`. Written for Phase 2 (collection, v0.6 call: hypothesis plus Low, Medium or High confidence).*

---

## Ground truth

The truth never shifts: LANTERN is a dangle on every day. What changes is how much of the evidence shows it.

| Day | What's really happening | True hypothesis |
| --- | --- | --- |
| 1 (5th) | LANTERN is a real mid-level planning officer, recruited by the Bureau (Kordav's security service) for one job. He walked in on orders. The aim: smear Vell before the vote, and see who we ask about him. | **H2** |
| 2 (6th) | The Bureau watches the defence ministry for anyone asking about LANTERN. "Room 412" comes from a story the Bureau planted in *The Kalsa Courier* three weeks ago. | **H2** |
| 3 (7th) | The ledger is delivered: genuine Bureau paper, with entries forged from Vell's public schedule. Elsin's opposition, working alongside Kordav's media campaign, gets the vote moved up. | **H2** |
| 4 (8th) | The Bureau leaks "a defector with evidence" to an opposition MP, so the smear lands even if we keep quiet. | **H2** |
| 5 (9th) | State TV announces a "kidnapping," and LANTERN asks to go public on the morning of the vote. | **H2** |

## Adversary plan

| Objective | How | Channels |
| --- | --- | --- |
| **Make us believe H1** and pass the allegation to Elsin before the vote | A walk-in carrying true but worthless information about IRON HARVEST, then the allegation, then "proof," then urgency | LANTERN, KSB, *The Kalsa Courier* (planted three weeks earlier), an opposition MP |
| **Find our sources** | LANTERN asks who in the ministry could vouch for him. The Bureau watches who comes asking. | LANTERN's question (R-2-03), the Bureau's watch on the ministry |
| **Win anyway if we stay quiet** | Leak the "defector" to the opposition, and stage a press statement for vote morning | The opposition MP, KSB, LANTERN |

**The meta-tell:** everything LANTERN gave us that we could check was something Kordav had already lost. Nothing he gave us cost Kordav anything.

## Sources (hidden values)

| Code name | True reliability | Adversary-controlled? | Notes |
| --- | --- | --- | --- |
| LANTERN | — | **Yes** | A real officer on a Bureau assignment. His one true item, R-1-02, is chickenfeed. |
| STATION | 1.0 | No | Reports exactly what happens in the room |
| FINCH | 0.9 | No | Honest. Tasking him puts him at risk, because the Bureau is watching who asks about LANTERN. |
| WREN | 0.6 | No (biased) | Some of its officers want Vell gone, so it repeats the doubts |
| MERIDIAN | 0.9 | No | Kordav's embassy is under orders to stay hands-off, and that's the signal |
| KSB | — | Yes | Runs the media side of the smear |
| CWS | 0.9 | No | |
| SOCIAL | 0.3 | Partly | Carries the MP's planted claim |

---

## Item key

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
| R-2-02 | P | H1 | access-mismatch, circular-origin | See the reasoning below |
| R-2-03 | P | H1 | fishing | See the reasoning below |
| R-2-04 | T | H2 | — | Kordav's media attacking the same man LANTERN accuses, the same day |
| R-2-05 | T | H2 | — | Kordav isn't looking for its missing officer |
| R-2-06 | C | — | — | Metro strike |

### Day 3 (truth H2). Best call: H2 at High

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-3-01 | N | H1 | agenda-aligned | Elsin's anti-Vell faction repeating itself |
| R-3-02 | P | H1 | only-public-dates | See the reasoning below |
| R-3-03 | T | **H2** | — | **The best item in the base stream.** Real agents get paid on trips nobody announces. |
| R-3-04 | T | H2 | — | The deadline LANTERN will lean on tomorrow |
| R-3-05 | C | — | — | A wedding |

### Day 4 (truth H2). Best call: H2 at High

| ID | Kind | Supports | Tells | What it really was |
| --- | --- | --- | --- | --- |
| R-4-01 | P | H1 | convenient-timing | See the reasoning below |
| R-4-02 | T | H2 | — | His story about his family changes once someone asks about them |
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

### Collection results

| ID | Kind | What it really was |
| --- | --- | --- |
| C-01 | T, **diagnostic** | **No damage control.** If an officer with the access LANTERN claims had really defected, the Bureau would be recalling people and changing codes. It's routine traffic plus a reminder about "media discipline." Only reachable through SIGINT tasking (Phase 2 rule 4). |
| C-02 | T | A real defector's family gets questioned. His goes to the lake. |
| C-03 | T | The origin of "room 412." Makes R-2-02 circular. |
| C-04 | T, **risk** | Confirms the access mismatch: planning staff, nowhere near the Bureau's files. **FINCH is burned:** he misses his next meeting. FINCH's remark that "someone else asked about LANTERN's friends" was the warning. **−2 points**, and in Phase 3 FINCH stays gone. |
| C-05 | T | The Hotel Sorel meeting happened, logged and innocent. WREN's remark is its faction talking. |

---

## Planted items: the reasoning

### R-1-03 (Day 1, LANTERN): the allegation

- **What gave it away:** he says he learned it from "colleagues in the Bureau." A planning officer doesn't see the security service's agent files. And the gift comes with a condition: resettlement first.
- **Check it against R-1-01, R-1-02:** both put him on the General Staff's planning directorate, which is military planning, not counterintelligence.
- **Why Kordav planted it:** plant the claim on Day 1 and attach a hook, so we invest in him before we test him.

### R-2-02 (Day 2, LANTERN): room 412

- **What gave it away:** an exact room number he can't say how he knows.
- **Check it against R-1-03 and C-03:** a planning officer has no route to that detail (R-1-03). And it was already in print: *The Kalsa Courier* ran it three weeks ago (C-03, OSINT on Elsin's press, available from Day 2). One origin, now dressed up as two.
- **Why Kordav planted it:** precision sounds like access.

### R-2-03 (Day 2, LANTERN): "who can vouch for me?"

- **What gave it away:** a defector asking us who we have inside his own ministry.
- **Check it against R-1-03:** a man who claims to know Bureau agent files could prove himself with something only the Bureau knows. Instead, he asks us to show our hand.
- **Why Kordav planted it:** the dangle's second job was to find our sources. The Bureau was watching the ministry for whoever came asking about him. Tasking FINCH (C-04) did exactly that.

### R-3-02 (Day 3, LANTERN): the ledger

- **What gave it away:** every payment date matches one of Vell's trips abroad.
- **Check it against R-3-03:** all of those trips are on his public schedule, and none of his private travel is. Real agents get paid on trips nobody announces.
- **Why Kordav planted it:** genuine Bureau paper gets a forgery past a quick look.

### R-4-01 (Day 4, LANTERN): "before the vote"

- **What gave it away:** the urgency is tied to a deadline only Kordav benefits from.
- **Check it against R-3-04 and R-1-04:** the vote was moved up yesterday, and it was the reason for his timing from Day 1.
- **Why Kordav planted it:** force a decision before verification can catch up.

### R-4-03 (Day 4, SOCIAL): the MP's post

- **What gave it away:** the MP knows about "a Kordavan officer who has defected to an allied service."
- **Check it against R-3-01 and R-1-01:** Elsin's own service only had a rumor about "someone from Kordav" (R-3-01). LANTERN asked us to keep him secret (R-1-01). Nobody on our side said "defector." Only LANTERN's side could have. *If you passed the full allegation to Elsin, this tell doesn't hold, because the leak could be theirs. By then the crisis is lost anyway.*
- **Why Kordav planted it:** a backup plan. The smear lands even if we never share anything.

### R-5-01 (Day 5, KSB): the "kidnapping"

- **What gave it away:** four days of silence about a missing officer, then a kidnapping story the day before the vote.
- **Check it against R-2-04 and R-2-05:** state TV spent those days attacking Vell, not mentioning LANTERN, and Kordav's embassy was told to keep its distance.
- **Why Kordav planted it:** make the defection look real just in time for LANTERN to go public.

### R-5-02 (Day 5, STATION): the press statement

- **What gave it away:** a man who asked us to keep him secret for his safety now wants a press statement released on the morning of the vote.
- **Check it against R-1-01:** his first request was secrecy.
- **Why Kordav planted it:** the smear's last delivery route, timed for maximum effect.

---

## Marlowe's actions and the endings

**Actions** (see the player packet for her habits table):

| State | Triggered by | Reversible? |
| --- | --- | --- |
| Full allegation shared | H1 at High | **No.** Elsin acts within a day. |
| Caveated warning shared | H1 at Medium | Yes: withdrawn by any H2 call at Medium or High, at a credibility cost |
| Sharing stopped, LANTERN restricted | H2 at Medium | — |
| Smear warning sent (counter) | H2 at High | — |
| Debriefing ended | H3 at Medium or High | — |
| Early counter rebuffed | H2 at High on Day 1 | The warning is withdrawn. Nothing can go to Elsin on Days 2–4. Credibility hit. |

**Endings** (at the vote, the morning of the 10th):

| Condition | Ending | Points |
| --- | --- | --- |
| Full allegation shared at any point | **Burned.** Elsin arrests Vell on the morning of the vote. Six months later the ledger is exposed as a forgery built from his public schedule. Nobody in Kalsa trusts allied intelligence again. Kordav couldn't have bought a better outcome. | −5 |
| Caveated warning still in place at the vote | **Sidelined.** The caveat leaked within a day and is quoted in the opposition's speech. Vell resigns "to clear his name." Elsin's reformers lose their best voice, and Kordav never fired a shot. | −3 |
| Smear warning sent on Day 2, 3 or 4 | **Exposed.** Elsin's defence minister stands up in parliament with your warning: Kordav is running a smear, and its "defector" was sent. The motion fails by forty votes. LANTERN's statement never airs. Two Bureau officers are quietly recalled from the neutral capital. | +5 |
| Smear warning sent only on Day 5 (including after the early-counter freeze) | **Survived.** Your warning reaches Kalsa the night before the vote. The motion fails by three. Vell keeps his job and loses his reputation. | +1 |
| None of the above | **Shelved.** You kept it to yourself. The opposition runs with the MP's claim anyway, and Vell survives by five votes without knowing how close it came or who was behind it. | 0 |

---

## Postmortem script

> **Day 1.** LANTERN walked in with a gift and a condition. He told you about IRON HARVEST, which was true and cost Kordav nothing: the operation had been blown for three months. The Vell allegation came from "colleagues in the Bureau," and a planning officer doesn't see the Bureau's agent files.
>
> **Day 2.** Room 412 came from a newspaper. *The Kalsa Courier* printed it three weeks before he walked in. His question about who could vouch for him was the second job he'd been sent to do: find out who we have in the ministry.
>
> **Day 3.** The ledger was real paper telling a forged story. Every payment matched a trip anyone could look up. Real agents get paid on trips nobody announces.
>
> **Day 4.** The deadline was Kordav's, not Elsin's. The MP heard about "a defector" from the only people who knew besides us.
>
> **Day 5.** A man kidnapped by Western intelligence asked to record a press statement for the morning of the vote. Kordav stayed silent for four days, then announced a kidnapping. The Bureau's own traffic never so much as changed a code.

**Lessons:**

1. A walk-in's verifiable details prove access, not intent. Ask what they cost the other side.
2. Check claims against access: what could he actually have seen?
3. Count origins. A detail that's already in print isn't corroboration.
4. Watch how the other side reacts. A real defection triggers damage control, so silence is a tell.
5. Collection can be seen too. Asking the wrong source the wrong question can burn it.

---

## Designer notes (critic hat)

**Does it play differently from Crisis 01?** (the Phase 2 gate)

| | Crisis 01 | Crisis 02 |
| --- | --- | --- |
| Question | What is an army doing? | Is one man telling the truth? |
| Decision | Move troops | Share intelligence with an ally, or warn it |
| Truth | Shifts on Day 3 | Fixed; how visible it is changes |
| HUMINT | Always honest | The main channel of deception |
| Collection | Adds information | Can burn your own source |
| Customer | Military commander | Political official |

**Dominant-strategy check** (paper estimate: calls plus ending, before evidence and doubts):

| Strategy | Ending | Total |
| --- | --- | --- |
| Best play: H2 Low, H2 Medium, then H2 High from Day 3 | Exposed | **+17** |
| Paranoid: H2 High every day | Survived (Day 1 counter rebuffed, freeze, counter on Day 5) | **+16** |
| Never above Medium on H2 | Shelved | **+9** |
| Always hedge (Low) | Shelved | **+5** |
| "He's a fabricator" (H3 Medium every day) | Shelved | **−10** |
| Cautious believer (H1 Medium every day) | Sidelined | **−13** |
| Trust the walk-in (H1 High every day) | Burned | **−25** |

**Watch for:**

- **"Always assume a dangle" nearly ties best play (+16 vs +17).** The truth never shifts, so calling H2 at High every day earns full points on the calls, and only the ending punishes it. Fixes to choose from: make the early-counter credibility hit cost about 3 points, and, the real fix, include a genuine walk-in in a later crisis so that reflexive suspicion has a price across the campaign (parking lot). This mirrors Crisis 01, where "trust HUMINT" works.
- **Eight plants out of 25 base items** is heavy, but it's a deception crisis. Watch whether testers find it exhausting or satisfying.
- **Burning FINCH has to feel fair.** The warnings are LANTERN's question on Day 2 and FINCH's own remark that someone else had already asked about LANTERN. If testers call it a trap with no warning, add a line to the packet's FINCH entry: "the Bureau is known to watch for this."
- **The ledger relies on STATION's analysis (R-3-03)** being in the base stream. That's fine: C-01 is the collection-only diagnostic.

**Engine needs before building** (Phase 2):

- The customer's actions here aren't a ladder like company and battalion. The engine needs **named states with transitions** (shared, caveated, restricted, countered, ended), plus ending conditions such as "ever reached" (Burned) and "first reached on day N" (Exposed or Survived).
- **Source state:** FINCH can be burned by a tasking, and the postmortem needs to show it.
- **Credibility hooks:** the rebuffed early counter, and withdrawing something already shared.
- **Map:** the neutral capital (embassy), Kordav's capital (Bureau headquarters, LANTERN's home), and Kalsa (parliament, Hotel Sorel). Pins for R-1-01, R-2-02, R-2-04 and C-02.
