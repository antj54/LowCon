# Crisis 01: Exercise or Operation? · GM key and postmortem (Phase 0)

*SPOILERS. Open this only after you've sent your Day 5 brief from `claude/crisis-01-player-packet.md`.*

---

## Ground truth

| Day | What's really happening | True hypothesis |
| --- | --- | --- |
| 1 (15th) | The exercise is real. Leadership enlarged it by 40% to gain leverage at the talks. 4th Army has drafted a contingency plan to seize Tarsk Dam (the "northern option"), but nobody has authorized it. | **H3** |
| 2 (16th) | The talks go badly. Contingency planning continues and is still not authorized. The delegation walks out that evening, after your brief. | **H3** |
| 3 (17th) | Leadership authorized the northern option overnight. Orders go out at 0400: medical support and fuel move to operational accounts, comms security tightens and the cover story starts. | **H2** |
| 4 (18th) | 12th Brigade's lead elements and 77th Engineer Regiment (bridging) leave Ostrel for a hidden staging area near the Dolan crossing. 31st Brigade stays behind at Ostrel as the visible "exercise." | **H2** |
| 5 (19th) | Final preparations. The bridging moves forward and the field hospital expands. The incursion is set for **dawn on the 20th**, the same day as the closing ceremony. | **H2** |

## Adversary plan

| Phase | Days | What Kordav wants you to believe | Channels |
| --- | --- | --- | --- |
| Signal | 1–2 | **H3.** A coercer wants to be seen. The threat is real messaging. | KSB, the delegation's rhetoric |
| Conceal | 3–5 | **H1.** Once the operation is authorized, a visible threat only invites a defense, so Kordav switches to "routine." | KSB statements, staged unencrypted voice on a net they know is covered, sockpuppet accounts, a recycled photo. CWS then picks up the KSB line, which makes the reporting circular. |

**The meta-tell:** a coercer who suddenly goes quiet the morning after talks collapse has stopped coercing.

## Sources (hidden values)

| Code name | True reliability | Adversary-controlled? | Notes |
| --- | --- | --- | --- |
| KESTREL | 0.85 | No | A straight arrow who stays within his access. His one bad item (R-2-05) is gossip he labels as gossip. |
| MERIDIAN | 0.9 | No (the channel) | The channel is reliable, but Kordav knows it's covered and stages one item on it (R-4-02). |
| CIRRANE | 0.9 | No | Shows what's there and what isn't. Can't show intent on its own. |
| WREN | 0.6 | No (biased) | Elsin raises the alarm every day to get the battalion moved. It's wrong on Days 1–2 and right on Day 4. |
| KSB | — | Yes | Accurate about what the state wants said. |
| CWS | 0.85 | No | Honest outlet that gets circular on Day 5. |
| SOCIAL | 0.3 | Partly | Mixes real noise with sockpuppets. |

---

## Item key

Kinds: **T** true · **N** noise · **P** planted · **C** clutter. The full reasoning for each planted item is in the next section.

### Day 1 (truth H3). Best call: H3 at Medium

| ID | Kind | Supports | Contradicts | Tells | What it really was |
| --- | --- | --- | --- | --- | --- |
| R-1-01 | T | H2, H3 | H1 | — | The scale-up was ordered for leverage. The **exercise account code** is the baseline that changes on Day 3. |
| R-1-02 | T | H3, H2 | H1 | — | The minister links the exercise to the talks in public. That's coercive signaling working as designed. |
| R-1-03 | N | H2 | — | no-sourcing, agenda-aligned | Elsin's standing request dressed up as an assessment. It turns out roughly right later, for no reason anyone had on Day 1. |
| R-1-04 | T | H1, H2, H3 | — | — | Fits every hypothesis, so it can't tell them apart. It's the baseline: note where things *aren't* (Dolan). |
| R-1-05 | C | — | — | different cause named in item | The refinery outage caused the queues. Military fuel comes from depot stocks, not the capital's pumps. |

### Day 2 (truth H3). Best call: H3 at Medium (H2 at Low is a defensible early warning)

| ID | Kind | Supports | Contradicts | Tells | What it really was |
| --- | --- | --- | --- | --- | --- |
| R-2-01 | T | H2, H3 | — | — | The contingency plan exists. **Plans aren't intent:** militaries draft options all the time. |
| R-2-02 | T | H3 | — | — | Pressure rhetoric aimed at the table. |
| R-2-03 | N | H2 | — | no-corroboration, agenda-aligned | Routine Kordavan border-guard patrols, misidentified. |
| R-2-04 | N | — | — | — | A collection gap. Not knowing is not evidence. |
| R-2-05 | N | H2 | — | source labels it as gossip | Reliable source, worthless item. **Grade the information, not just the source.** |
| R-2-06 | C | — | — | — | Fish. |

### Day 3 (truth H2). Best call: H2 at Medium or High

| ID | Kind | Supports | Contradicts | Tells | What it really was |
| --- | --- | --- | --- | --- | --- |
| R-3-01 | T | H2, H3 | H1 | — | The trigger. The northern option was authorized within hours. |
| R-3-02 | T | **H2** | H1, H3 | — | **The best item of the day, and squarely within KESTREL's access.** Exercises rarely push blood products forward, and operations are funded from different accounts than training. |
| R-3-03 | P | H1 | H3 | tone-shift, convenient-timing | See the reasoning below. |
| R-3-04 | T | H2 | H1 | — | Comms security tightened at 0400, the same time as KESTREL's account change. Two independent sources line up on the timing. |
| R-3-05 | C | — | — | location, National Day date | National Day parade rehearsal. |

### Day 4 (truth H2). Best call: H2 at High. **Diagnostic day.**

| ID | Kind | Supports | Contradicts | Tells | What it really was |
| --- | --- | --- | --- | --- | --- |
| R-4-01 | T | H2 | H1 | — | Standing imagery now covers Ostrel only (v0.7): half of 12th Brigade is gone. **The diagnostic moved to collection:** C-02, imagery tasked on Dolan forest on Day 3, finds the bridging vehicles and field hospital 8 km from the crossing, and confirms KESTREL's "field medical point" (R-3-02). |
| R-4-02 | P | H1 | — | out-of-pattern (unencrypted), too on-message | See the reasoning below. |
| R-4-03 | P | H1 | — | access-mismatch, new-account | See the reasoning below. |
| R-4-04 | T | H2 | — | — | The same alarmist source as Days 1–2, but now imagery corroborates it. Corroboration should move you, not tone. |
| R-4-05 | C | — | — | — | Don't open the spreadsheet. |

### Day 5 (truth H2). Best call: H2 at High

| ID | Kind | Supports | Contradicts | Tells | What it really was |
| --- | --- | --- | --- | --- | --- |
| R-5-01 | P | H1 | — | circular-origin | See the reasoning below. |
| R-5-02 | P | H1 | — | only-one-chain | See the reasoning below. |
| R-5-03 | T | H2 | H1 | — | Ostrel only (v0.7): the ceremony is real, and good deception wraps itself in true details. The bridging within 2 km of the river is collection-only (C-03). |
| R-5-04 | T | H2 | H1 | — | 12th Brigade is on a separate operational supply chain and has been compartmented. KESTREL reports the limits of what he knows honestly. |
| R-5-05 | P | H1 | — | recycled-media | See the reasoning below. |
| R-5-06 | C | — | — | — | Economics. |

---

## Planted items: the reasoning

Each planted item has a tell in its own text and at least one check against an item you already have by that day. Nothing here relies on the key alone.

### R-3-03 (Day 3, KSB)

- **What gave it away:** Two days running, Kordav tied IRON HARVEST to the talks: "patience has limits" (R-1-02) and "we did not come to wait forever" (R-2-02). The morning after the walkout, the same ministry calls it routine. A coercer whose talks just failed has every reason to turn the pressure up, not down.
- **Check it against R-3-02, R-3-04:** The same morning, KESTREL's depot pushed blood products forward and moved fuel to a "contingency" account at 0400 (R-3-02), and the logistics net went quiet at 0400 (R-3-04). A routine exercise needs neither.
- **Why Kordav planted it:** Once the operation was authorized, a visible threat only invited a defense. Kordav needed you to stop worrying, so it swapped the threat for "routine."

### R-4-02 (Day 4, MERIDIAN)

- **What gave it away:** 12th Brigade has used encrypted voice for the whole exercise. The one time it talks in the clear, it announces the cover story word for word. Real slips happen on routine chatter, not on the exact message the other side would want overheard.
- **Check it against R-4-01:** The same day, imagery shows half of 12th Brigade gone from Ostrel and a new concentration 8 km from the Dolan crossing (R-4-01). That's not a brigade loading for garrison.
- **Why Kordav planted it:** Kordav knew the net was covered. A reliable channel is the best place for a lie, because you trust the channel.

### R-4-03 (Day 4, SOCIAL)

- **What gave it away:** A conscript wouldn't know a brigade-wide order with an exact date. The account is three weeks old and posts only about IRON HARVEST, which fits an account set up before the exercise for this job.
- **Check it against R-4-01:** The post is about 31st Brigade, which imagery shows still at Ostrel (R-4-01). Even if 31st really does go home on the 20th, that tells you nothing about 12th Brigade, the one moving toward Dolan.
- **Why Kordav planted it:** Fill open sources with "going home" so the story seems to be everywhere.

### R-5-01 (Day 5, CWS)

- **What gave it away:** Its key phrase, "orderly return to permanent bases by the 20th," matches the ministry press release word for word. Unnamed "defence sources" repeating a press release are the press release.
- **Check it against R-5-02:** Read it next to the KSB release the same day (R-5-02): one origin, two items.
- **Why Kordav planted it:** CWS isn't lying. It repeated the ministry line, and Kordav got a second, more trusted voice for free.

### R-5-02 (Day 5, KSB)

- **What gave it away:** Every "going home" item in this crisis comes through a channel Kordav controls or can feed: its ministry (R-3-03, R-5-02), an unencrypted call on a net it knows is covered (R-4-02), a new social media account (R-4-03) and a wire report quoting the ministry (R-5-01). Nothing independent backs it.
- **Check it against R-5-03:** The same day, imagery shows bridging vehicles within 2 km of the river and the field hospital growing (R-5-03). Units heading back to base don't push bridging toward a border river.
- **Why Kordav planted it:** The closing ceremony is real (R-5-03 shows the stands going up). Kordav wrapped the lie around a true event so it would check out.

### R-5-05 (Day 5, SOCIAL)

- **What gave it away:** There's snow on the vehicles and on the ground.
- **Check it against R-5-03:** The same day, imagery reports no snow cover anywhere in the area (R-5-03). The photo isn't from this week.
- **Why Kordav planted it:** An old photo costs nothing and spreads faster than any statement. This one is from last year's end of exercise.

---

## Halvorsen's commitment (Phase 1 rules, v0.6)

He acts on hypothesis and confidence only. Evidence affects points, not what he does.


| Your brief | What he does |
| --- | --- |
| H2 at High | Moves all of 2nd Battalion to Tarsk (or sends the rest, if the lead company is already there) |
| H2 at Medium | Sends a reinforced lead company to Tarsk |
| H2 at Low | Raises readiness, no move |
| H3 / H1 | Holds / relaxes |
| H1 or H3 at Medium or High, with troops at Tarsk | Pulls everyone back |
| Any move on Day 1 or 2 | Day 3: everyone ordered back and moves frozen for the Day 3 and Day 4 briefs |

A company can watch the crossing. Only the full battalion can hold the dam.

## Endings

What's at Tarsk at dawn on the 20th, and when it got there:

| Status at dawn | Ending | Points |
| --- | --- | --- |
| Full battalion, in place after the Day 3 or Day 4 brief | **Deterred.** Kordavan lead elements reach Dolan at dawn and find a full battalion dug in on the far bank. They halt. By noon KSB announces that IRON HARVEST "concluded successfully." The ceremony goes ahead with the minister smiling through it. Nobody will ever credit you with a war that didn't happen. Halvorsen does. | +5 |
| Full battalion, but only after the Day 5 brief | **Standoff (late).** 2nd Battalion is still deploying when Kordavan engineers bridge the river. They take the dam's access road but not the dam. A tense week of negotiation follows under a much worse map. | +1 |
| Lead company only | **Standoff (thin).** The lead company holds the dam itself, but Kordavan engineers bridge the river at Dolan and take the access road behind it. The company is cut off but still on the dam when the talking starts again. | +1 |
| Nobody | **Seized.** Kordav holds Tarsk Dam by 0900 and frames it as "securing critical water infrastructure." The closing ceremony goes ahead. | −5 |

---

## Postmortem script (read after scoring)

> **Day 1–2.** Kordav wanted you to see a threat, and the threat was real: a coercion campaign for the talks. The "northern option" existed as a plan, but nobody had authorized it. Elsin was raising the alarm for its own reasons. If you warned at Low confidence, that's what warning is for. If you moved troops, Kordav got photos to wave at the table.
>
> **Day 3.** The walkout changed the answer overnight. KESTREL's account codes and blood products were the tell, and the comms going quiet matched his timing. The ministry calling the exercise "routine" the morning after talks collapsed was the loudest signal of the day, and it pointed the opposite way from what it said.
>
> **Day 4.** Imagery found the bridging vehicles and the field hospital in a forest 8 km from Dolan. With KESTREL's Day 3 report and Elsin's sighting, three disciplines pointed the same way: a day for high confidence. Medium got you a company, and a company can't hold a dam. The unencrypted radio call and the conscript post were staged for you.
>
> **Day 5.** Three "going home" items, all from one origin. The snow in the photo was last year's.

**Lessons this crisis teaches:**

1. Plans aren't intent.
2. Grade the information, not just the source.
3. When a coercer suddenly goes quiet, the threat may have become an operation.
4. Confidence moves forces. Under-calling a clear warning has a cost too.
5. Count origins, not reports.
6. Look for what's missing (Dolan on Day 1) as well as what's there.

---

## Designer notes (critic hat)

**Dominant-strategy check** (v0.7 engine with collection, `node tools/simulate.js --calls`; totals include evidence, doubts, burned sources and ending). Collection is the full plan in the retrofit doc; the simulator assumes perfect calls, so it understates what collection is worth to a human player:

| Strategy | Ending | Total |
| --- | --- | --- |
| Best play with collection (imagery on Dolan Days 1, 3, 4; SIGINT on HQ Day 2) | Deterred | **+32** (+38 doubting only the plants) |
| Best play, no collection | Deterred | **+31** |
| Best play with collection, using the board | Deterred | **+32** (unscored: same as without) |
| Best play with collection, page reloaded after every day | Deterred | **+32** (save check) |
| Burning KESTREL (HUMINT two days running) | Deterred | **+25** (−2 burn, R-5-04 lost) |
| High from Day 3, with collection | Deterred | **+33** |
| Best calls, citing no evidence on Days 4–5 | Deterred | **+26** |
| Best calls with collection, doubting everything | Deterred | **+26** |
| Never above Medium | Standoff (thin) | **+25** |
| Always worst case (H2 High every day) | Standoff (late) | **+10** |
| Trust the official line (H1 Medium every day) | Seized | **−15** |
| "It's just signaling" (H3 Medium every day) | Seized | **−7** |
| Always hedge (Low every day) | Seized | **0** |

**Playtest 1 (Anthony, not blind, had read this key):** right hypothesis every day, never called High, doubted 2 of 6 plants (both on Day 4), cited clutter once (R-1-05). Day 5 took 1 minute with no Day 5 plants doubted. The Day 1 time (28 min) was a timer bug, now fixed.

**Watch in playtest:**

- **Blind playtest still needed.** Difficulty, Day 5 tension and turn length can't be judged from a run by someone who knew the answers.
- **"Trust HUMINT" works here.** KESTREL is honest the whole way through. That's fine for a first crisis that teaches the basics, but a later crisis (the defector seed) needs to punish it.
- **Day 2 could be slow.** Clouds, gossip and fish make for a quiet day. Check the time it takes and whether the tension still builds.
- **Day 5 could feel like a victory lap** once Day 4's imagery lands. With the commitment rules, a player who stayed at Moderate on Day 4 still has a real Day 5 decision (upgrade to High or not). If it still feels decided, move the circular pair to Day 4.
- **R-3-03 has the softest tell.** A change in tone is a judgment call, not a fact. It's fair only because R-3-02 and R-3-04 contradict it the same morning. If playtesters call it unfair, add a harder tell to the item itself.
- **Fixed truth.** An early move doesn't change Kordav's behavior; only Halvorsen's freeze punishes it. Reactive truth goes in the parking lot.

**Playtest 2 (Syd, blind, v0.3 rules):** H2 Low, H1 Moderate, then H2 Moderate on Days 3–5, never High: Standoff (thin), +7. Doubted 1 of 6 plants (the snow photo), cited none. Engaging on Days 2–5, plants fair, realism off in places (flagged R-2-05, R-2-06, R-5-04, kept as is), turn length about right at ~2 min a day, unsure about a sixth day. Led to #38: likelihood plus derived confidence.

**Data format:** v0.7 is built in the game (`crises/border-buildup.json`): v0.7 adds `pirs`, `targets`, `collection`, `collectionResults` and `postmortem.missedCollection`; the hypotheses board (#49) needs no new content. Earlier: v0.6 keys `customerPolicy` and `scoring.call` on the player's confidence (`low`, `medium`, `high`), #46. v0.5 dropped derived confidence (#41). v0.4 added `hypotheses[].claim`, `likelihood` in `customerPolicy` conditions and likelihood-keyed `scoring.call`. New in v0.3: `asset.levels`, `customerPolicy[].level`, `policyNote`, `countdown`, `dailyUpdates`, `endings[].tone` and `endings[].if.since`, `map`, `reports[].pin`, and `groundTruth[].units` (shown only in the postmortem map).
