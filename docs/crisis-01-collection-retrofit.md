# Crisis 01 · Collection retrofit (Phase 2, paper)

*SPOILERS. Paper design for adding collection tasking to Crisis 01 (#45). Nothing built. Uses the Phase 2 rules in `claude/phase-2-design.md` and the v0.6 call (hypothesis plus Low, Medium or High confidence).*

## What changes in the crisis

| Change | Why |
| --- | --- |
| **R-4-01 splits in two.** Standing imagery keeps only the Ostrel half: *"About half of 12th Mechanized Brigade's vehicles are gone. 31st Mechanized Brigade is still at Ostrel."* The Dolan forest half (bridging vehicles, field hospital) becomes **collection-only**. | Phase 2 authoring rule 4: at least one diagnostic item is only reachable through collection. Standing coverage still tells you something left; tasking tells you where it went. |
| **R-5-03 splits the same way.** Standing imagery keeps the Ostrel ceremony and "no snow cover" line. "Bridging within 2 km of the river" becomes collection-only. | Keeps the snow-photo cross-check (R-5-05) in the base stream, so that plant stays beatable without collection |
| **CIRRANE's standing coverage is Ostrel only.** Dolan and the railhead are outside it unless you task them. | Gives IMINT tasking a real job |
| **Budget: 4 points a day.** Costs as in the design doc: OSINT 1, Liaison 0, IMINT 2, SIGINT 3, HUMINT 3. HUMINT takes 2 days, everything else arrives next morning. | Starting values to tune |

A player who never tasks collection can still get to H2: KESTREL's Day 3 report, the comms going dark and the half-empty Ostrel all point there. What they lose is the clear picture of Dolan, so High on Day 4 becomes a harder call. That's the point.

## PIRs and targets

| PIR | Question shown to the player | Targets |
| --- | --- | --- |
| PIR 1 | Are 4th Army units moving toward the border outside the exercise area? | Dolan crossing and forest, Ostrel railhead |
| PIR 2 | Has Kordav's leadership authorized action against Tarsk? | 4th Army HQ, Kordav defence ministry |
| PIR 3 | Is Kordav preparing to cross the Veyl (bridging, medical, fuel)? | Dolan crossing and forest, Varn depot |

Each target is a map area, so tapping it on the map opens the same tasking picker.

## Collection results

"Tasked on" is the day you spend the points. Results arrive the next morning (HUMINT: two mornings later). Every combination not listed returns the fallback line at the bottom.

| ID | Discipline · target | Tasked on | Arrives | Kind | Text | What it really was |
| --- | --- | --- | --- | --- | --- | --- |
| C-01 | IMINT · Dolan forest | Day 1–2 | Day 2–3 | True | "Dolan forest: fresh vehicle tracks and a cleared strip along the treeline. No vehicles present." | The staging area being prepared. An early indicator that nothing in the base stream shows. |
| C-02 | IMINT · Dolan forest | Day 3 | Day 4 | True, **diagnostic** | "Dolan forest: about 30 bridging vehicles (77th Engineer Regiment) and a tented facility consistent with a field medical unit, 8 km from the crossing." | The Dolan half of the old R-4-01 |
| C-03 | IMINT · Dolan forest | Day 4 | Day 5 | True, diagnostic | "Dolan staging area: about 40% more vehicles than yesterday. Bridging vehicles have moved to within 2 km of the river. The field medical facility has grown." | The Dolan half of the old R-5-03 |
| C-04 | IMINT · Ostrel railhead | Day 3–4 | Day 4–5 | True | "Ostrel railhead: no rail cars staged and no loading activity." | Cross-check against the "going home" plants (R-4-02, R-4-03, R-5-05) |
| C-05 | SIGINT · 4th Army HQ | Day 1–2 | Day 2–3 | True | "HQ net: the 'northern option' planning cell has moved to 24-hour manning." | Planning intensifying. On Day 2 tasking it also hints at the authorization before the walkout. |
| C-06 | SIGINT · 4th Army HQ | Day 3+ | Day 4+ | Noise | "The HQ nets you were watching have gone quiet. Traffic has moved to a net we don't cover." | **Risk: target went dark** after the 0400 switch. Spending 3 points here after Day 2 buys a confirmation of R-3-04 and nothing more. |
| C-07 | OSINT · Kordav defence ministry | Day 2+ | Day 3+ | True | "The ministry has quietly cancelled the defence minister's foreign trip planned for the 21st." | The minister expects to be busy after the 20th |
| C-08 | OSINT · Ostrel railhead | Day 2+ | Day 3+ | True | "Rail enthusiast forums: no military trains timetabled out of Ostrel before the 23rd." | Cheap cross-check against "home by the 20th" |
| C-09 | HUMINT · KESTREL (Varn depot) | Day 1 | Day 3 | True | "Two officers asked the depot for fuel for 'heavy vehicles' at a site the depot doesn't supply, north of Ostrel." | Fuel for the bridging column. Arrives with R-3-02, strengthening Day 3. |
| C-10 | HUMINT · KESTREL (Varn depot) | Day 2 | Day 4 | True | "The 'contingency' account now covers rations for 3,000 people for 10 days." | Sustainment for an operation, not an exercise ending on the 20th |
| C-11 | HUMINT · KESTREL, tasked on two consecutive days | — | — | — | **Risk: source burned.** KESTREL misses the next meeting and goes quiet. R-5-04 never arrives. | The postmortem explains: a clerk asking questions two days running gets noticed. |
| C-12 | Liaison · WREN (any target) | Any | Next day | Noise (Days 1–3), true (Day 4–5) | Days 1–3: "Elsin's service is certain the attack is imminent and asks again for the battalion." Days 4–5: "Elsin's border police report engineers at the riverbank opposite Dolan." | Free, and always pushing Elsin's agenda. True once the facts catch up with it. |

**Fallback** for anything not listed: *"Nothing significant."* That's true, and it still tells you something: the place you looked was quiet.

## Planted items reachable through collection

None in Crisis 01. The plants stay in the base stream so the retrofit only adds information. Crisis 02 is where tasking itself carries risk from the adversary.

## The collection you didn't do (postmortem lines)

Shown for each day in the postmortem, after the items:

| Day | Line |
| --- | --- |
| 1 | "Imagery of Dolan forest would have shown a cleared strip with no vehicles yet: somewhere being prepared." |
| 2 | "SIGINT on 4th Army HQ would have shown the 'northern option' cell going to 24-hour manning." |
| 3 | "Imagery of Dolan forest would have found the bridging vehicles and the field hospital a day before anyone else." |
| 4 | "Imagery of the Ostrel railhead would have shown nothing loading: nobody was going home on the 20th." |
| 5 | "Imagery of Dolan would have shown the bridging within 2 km of the river." |

## Balance expectations (to check in `tools/simulate.js` once built)

| Strategy | Expected |
| --- | --- |
| Best play with collection (task Dolan imagery on Day 3) | Deterred, higher score than today's best because the Day 4 call is easier to justify |
| Best calls, no collection at all | Still possible to reach Deterred with High on Day 4, but on thinner evidence. Testers' confidence choices will show whether that feels fair. |
| Tasking KESTREL every day | KESTREL burned. Loses R-5-04 and costs points. |
| Spending SIGINT on HQ after Day 2 | Wasted 3 points |
