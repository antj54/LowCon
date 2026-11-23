# Crisis 09: The Back Channel · GM key (paper)

**SPOILERS FOR THIS SCENARIO AND THE CAMPAIGN. Anthony: don't open this (#67, #68).**

Player packet: `claude/crisis-09-player-packet.md`. This key holds both versions' items, so it is the script for running the paper game.

## What it's for

1. **The truth depends on the record.** If Kordav has gained little since Crisis 01, its leadership needs a way out and the offer is real. If it has gained a lot, the offer is cover for the 20th. The player can't know which from the offer itself.
2. **Words are a position.** Everything Ansel says is the same in both versions. Only what Kordav does differs. The test is to ask for something that costs them.
3. **The last clue.** With the leak open, Ansel knows the alliance's bottom line. The player gets one more chance to close it.
4. **Both mistakes are available.** Refusing a real offer and accepting a false one are each the worst ending of their version.

## Which version

**Pressure** on the record, summed over Crises 01 to 08. **3 or less: version G (genuine), truth H1.** **4 or more: version S (stall), truth H2.** H3 is wrong in both: the approach to Kask is ordinary diplomacy.

Best calls, both versions: Day 1 Low on the true hypothesis; Day 2 Medium; Day 3 High once a result is in hand (the token answer arrives Day 3 at the earliest); Days 4 and 5 High.

## Shared items (both versions)

| ID | Day | Source | Text | Kind |
| --- | --- | --- | --- | --- |
| R-1-01 to R-1-05 | 1 | | As in the packet | true, position, noise, noise, clutter |
| R-2-02 | 2 | ANSEL | "You want proof. I am the proof. I do not travel for pleasure at my age." | position |
| R-2-03 | 2 | EMBASSY | "Political section: Kask's office likes the gas price. It asks whether the alliance means to say yes or no." | true |
| R-3-03 | 3 | KSB | "State television runs a documentary on the Veyl: 'A river two peoples share.'" | noise |
| R-4-03 | 4 | EMBASSY | "Political section: Kask says that if the alliance refuses, Elsin will have to consider its own answer." | true (tempts H3) |
| R-5-01 | 5 | STATION | "Fifth meeting. Ansel says he flies home tomorrow, with an answer or without one." | true |
| Admin, Days 2–5 | | | "Last night's instruction went to Aubrec {route}." | true |

**Leak open, both versions:**

| ID | Day | Text | Kind |
| --- | --- | --- | --- |
| R-2-06 | 2 | STATION: "Second meeting. Ansel said he understood the alliance 'could live with the Dolan road, and not with Kalsa.' Station comment: that phrase is from the Under Secretary's instruction of the 22nd, which went over LATTICE. Nobody said it in the room." | true, diagnostic for the leak |
| R-2-07 | 2 | *If Rhun was removed in 06.* Liaison desk (Lt. Col. Ahrend): "Col. Rhun, now at the defence college, asks me to pass on one line: 'Ask him how he knew.'" | true |
| R-4-06 | 4 | *If the courier tasking was made on Day 2 or 3.* STATION: "Fourth meeting. Ansel asked twice what the alliance's position on dates was. He had not needed to ask before." | true |

**The courier tasking:** once made, the route reads "by courier" and stays so. If made by Day 3: record flag `leak: closed-late`; Marlowe shuts LATTICE after the scenario (epilogue line). If the leak is open and it is never made: Ansel's side knows Marlowe's final instruction; in version S a High on H2 still works, but the reinforcement's route is known (`north` is not upgraded).

## Version G (genuine): truth H1

| ID | Day | Source | Text | Kind |
| --- | --- | --- | --- | --- |
| G-2-01 | 2 | STATION | "Second meeting. Asked what Kordav would do first, Ansel said: 'Tell me what you need to see.' He took notes." | true |
| G-2-04 | 2 | CWS | "From Kordav's capital: the grain harvest has failed in two eastern provinces. The agriculture minister asks for 'every available hand.'" | true |
| G-3-01 | 3 | STATION | "Third meeting. Ansel left a letter. Document examination: the leadership's seal and paper, signed. It commits to demobilisation 'on agreement in principle.'" | true |
| G-3-02 | 3 | CWS | "Ostrel: our correspondent counted eleven trains of reservists leaving the station today and spoke to men carrying release papers." | true, diagnostic |
| G-4-01 | 4 | STATION | "Fourth meeting. Ansel says General Drask opposes the offer and has said so in cabinet. 'He will lose the argument if you answer by the 28th. Perhaps not after.'" | true |
| G-4-02 | 4 | SOCIAL | **Planted (by Drask's side):** "A Kordavan forum posts a 'General Staff timetable' for a crossing on the 20th of November. The reference number uses the retired format." Tell: the retired format (08's C-06, or the item says so). Cross-check: G-3-02, G-C-03. Motive: get the offer refused. | planted |
| G-5-02 | 5 | CWS | "Kordav's reservists from the farm districts are home. The rest stay 'pending the talks.'" | true |

Collection, version G: **token (G-C-01):** "Ansel returned with an answer: 6,000 farm-district reservists released on the 25th. CWS saw the trains." diagnostic. **FINCH (G-C-02):** "The leadership wants out. The harvest has failed in two provinces. The army, Drask above all, opposes it." diagnostic. **Envoy's instructions (G-C-03):** "'The pull-back is the substance. The rest can be traded.'" diagnostic. **Dolan (G-C-04):** "No change. The strip is overgrown. Bridging still on the square at Ostrel." **KESTREL (G-C-05):** "No contingency account. Fuel is being returned to stock." diagnostic. **Railhead (G-C-06):** "Loading under way. Reservists and one regular brigade." **Kordav's embassy in Kalsa (G-C-07):** "The ambassador is told to 'keep Kask warm, and not to undercut Ansel.'" clears H3. **Kask's office (G-C-08):** "Kask will follow the alliance's lead if it gives one this week."

Analysts, version G: Vasko on G-3-01, "Genuine paper. We have been here before with genuine paper." (½: fair caution, wrong conclusion). Marrow on G-3-02, "Eleven trains and a reporter who talked to the men. That isn't a press release." (1). Halden, a day late on G-4-02, "That reference format again. The same hand as the October directive." (1).

## Version S (stall): truth H2

| ID | Day | Source | Text | Kind |
| --- | --- | --- | --- | --- |
| S-2-01 | 2 | STATION | "Second meeting. Asked what Kordav would do first, Ansel said: 'First we need your answer in principle.'" | true |
| S-2-04 | 2 | CWS | "From Kordav's capital: the reservists' release, due on the 25th, is postponed 'pending the talks.'" | true |
| S-3-01 | 3 | STATION | "Third meeting. Ansel showed a letter and would not leave it. It was a photocopy. He asked again for an answer in principle, and would not discuss dates." | true, diagnostic-lite |
| S-3-02 | 3 | CWS | **Planted:** "Kordav has begun releasing reservists, defence sources say." Tell: "defence sources say," with no count and nobody seen. Cross-check: S-3-04 (the ministry's release in the same words), S-C-06. Callback tag `circular`. | planted |
| S-3-04 | 3 | KSB | "Defence ministry: Kordav 'has begun releasing reservists.'" | planted (the origin) |
| S-4-01 | 4 | STATION | "Fourth meeting. Ansel says there is no opposition to the offer in Kordav. Asked about General Drask, he changed the subject." | true |
| S-5-02 | 5 | CWS | "Kordav's reservists remain at their depots. Military traffic into Ostrel resumed last night." | true |

Collection, version S: **token (S-C-01):** "Ansel 'will convey the request.' No release by the 26th. He asked again for an answer in principle." diagnostic. **FINCH (S-C-02):** "The General Staff wrote the offer. The foreign ministry saw it the day Ansel left. He has been told to bring back an agreement in principle and no dates." diagnostic. **Envoy's instructions (S-C-03):** "'Obtain agreement in principle. Do not agree dates. Report daily.'" diagnostic. **Dolan (S-C-04):** "Dolan forest: fresh vehicle tracks and a newly cleared strip along the treeline. No vehicles present." diagnostic (01's C-01). **KESTREL (S-C-05):** "A contingency account was opened on the 21st. Blood products are on order for delivery by the 15th of November." diagnostic. **Railhead (S-C-06):** "No reservists leaving. Flatcars arriving loaded." **Kordav's embassy in Kalsa (S-C-07):** "The ambassador is told to 'keep Kask talking.'" **Kask's office (S-C-08):** as G.

Analysts, version S: Vasko on S-3-02, "Releasing reservists. That fits an offer made in good faith." (0). Marrow on S-3-01, "A photocopy he won't leave behind. I've had landlords do that." (1). Halden, a day late on S-3-02, "The wire and the ministry use the same sentence. That's one source." (1).

## Policy and endings

"Something to show": in G, any of G-C-01, 02, 03, 05 or G-3-02 cited; in S, any of S-C-01 to 05.

| Version | Condition | Ending | Points | For Crisis 10 |
| --- | --- | --- | --- | --- |
| G | H1 High with something to show | **The way out.** Agreement in principle on the 28th. | +5 | `deal: yes` |
| G | H1 High, nothing to show | **A leap.** It holds, and Kask learns of it from the television. | +2 | `deal: yes`, Alliance −1 |
| G | H2 High | **Refused.** The offer was real. Drask wins the argument. | −5 | `deal: no`, `misjudged`, Pressure +1 |
| G | H3 High | **Kalsa first.** Kask is grateful. The offer lapses on the 28th. | −2 | `deal: no`, Alliance +1 |
| G | otherwise | **Talks about talks.** Ansel flies home without an answer. | −3 | `deal: no` |
| S | H2 High with something to show | **Seen through.** The alliance reinforces. | +5 | `north: reinforced` |
| S | H2 High, nothing to show | **Refused, on your word.** Reinforcement is slower to come. | +2 | — |
| S | H2 Medium at the end | **Talk and watch.** | +1 | — |
| S | H1 High | **Pulled back.** The task force leaves the Tarsk sector on the 1st of November. | −5 | `north: open`, `misjudged`, Pressure +2 |
| S | H3 High | **Kalsa first.** A week is lost. | −2 | Alliance +1 |
| S | otherwise | **Talks about talks.** | −2 | — |

Credibility: starts from Marlowe's after 07. Nothing to show on an irreversible step −1; a reversal −1; Low two days running −1. Outcome +1 for the best ending of the version, −1 for the worst.

Case file: R-2-06 cited or the courier tasking made → "The envoy knew the alliance's bottom line before it was said in the room."

## Postmortem

States the version outright: "On your record, Kordav had gained [little / a great deal] since the Veyl. Its leadership [needed a way out / could afford to wait]."

Lessons: An envoy's words are a position. Ask for something that costs the other side, and watch whether it is paid. The same offer can be real or false depending on what the adversary already holds. A quiet adversary is not always preparing (G) / A quiet adversary may be preparing (S). If the other side knows your bottom line, find out how.

## Critic's notes

- **Two scenarios' worth of writing for one slot,** and each player sees half. It is the only place the campaign's values change the truth, so it earns it.
- **The token is nearly free and nearly decisive.** Its cost is time: asked on Day 1 it answers on Day 3. A player who never asks has paid collection instead.
- **Threshold at Pressure 4.** Worth checking against real records once Crisis 08 has been played: if nearly everyone lands on one side, move it.
- **Version G's plant comes from a faction, not the state.** It sets up Crisis 10.
