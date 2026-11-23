# Crisis 10: The Veyl · GM key (paper)

**SPOILERS FOR THE FINALE AND EVERY ENDING. Anthony: don't open this (#67, #68).**

Player packet: `claude/crisis-10-player-packet.md`. This key holds both versions and is the script for running the paper game.

## What it's for

1. **Crisis 01's question, with everything the player has learned.** What is an army doing, and what do I tell a commander who commits in proportion to my confidence?
2. **The record decides the board.** Which version, where the task force starts, which sources are left, whether orders can be read.
3. **Each version reverses a habit.** Version A (agreement): the state is honest and the danger is one general. "It's always Kordav" and "it's never Kordav" both fail. Version B (none): Kordav repeats October's show exactly, because it knows what convinced us. "It was a show last time" fails.
4. **The leak's last use.** If LATTICE is still open, the final orders are read. A courier fixes it for nothing, if the player thinks of it.

## Which version

**Version A** if Crisis 09 set `deal: yes`. **Version B** otherwise.

## Starting position

| `north` on the record | Days to get into position |
| --- | --- |
| `reinforced` (09, Seen through) | In position already: a Medium counts as a High for the outcome |
| `held` | One day: High by the Day 4 brief |
| `thinned`, `open`, or the task force halved (07) | Two days: High by the Day 3 brief |

## Version A: truth H1 on Days 1–2, H3 on Days 3–5

Kordav's leadership means to keep the agreement. On the night of the 16th General Drask decides to wreck it: 12th Brigade will "escort the observers" to Dolan on the 19th and seize the dam's access road at dawn, presenting his government with a fact. Best calls: H1 Low, H1 Medium, H3 Medium, H3 High, H3 High.

| ID | Day | Source | Text | Kind |
| --- | --- | --- | --- | --- |
| A-2-01 | 2 | STATION | "Ansel, by telephone: the leadership has signed the demobilisation order. Reservists entrain from the 18th." | true |
| A-2-02 | 2 | CWS | "Ostrel: empty troop trains are arriving at the station." | true |
| A-2-03 | 2 | SOCIAL | **Planted (Drask's side):** "A forum posts 'General Staff order: force the Veyl at Dolan, dawn, the 20th.' The reference number uses the retired format." Tell: the retired format, a third time. Cross-check: A-2-01, A-C-02. Motive: an open alliance defence, which Drask can call a breach. | planted |
| A-3-01 | 3 | CIRRANE | "Ostrel, standing pass. 12th Mechanized Brigade's vehicles are fuelled and formed in column on the Dolan road. The other two brigades are loading at the railhead." | true, diagnostic |
| A-3-02 | 3 | KSB | "State television: 12th Brigade will 'escort the observers to Dolan and supervise the handover.'" | true (the cover) |
| A-3-03 | 3 | EMBASSY | "Political section: the agreement text says nothing about an escort." | true |
| A-4-01 | 4 | WREN | "Border posts report 12th Brigade's reconnaissance company at the Dolan crossing, on Kordav's side, in daylight. Sourcing: the service's own observation." | true |
| A-4-02 | 4 | STATION | "Ansel, by telephone, sounding tired: 'Everything is proceeding. Do not read too much into uniforms.'" | position |
| A-4-03 | 4 | SOCIAL | **Planted:** "The same forum: 'the whole army crosses on the 20th.'" Tell: two of the three brigades are on trains (A-3-01, A-C-06). | planted |
| A-5-01 | 5 | CIRRANE | "Ostrel: two brigades gone by rail. 12th Brigade is no longer on the Dolan road. Not visible on this pass." | true |
| A-5-02 | 5 | KSB | "State television leads with the handover ceremony. General Drask will attend 'with his escort.'" | true |

Collection, version A: **Dolan forest (A-C-01):** "No bridging. On Day 4 and 5: 12th Brigade's lead battalion under the trees, 3 km from the crossing." **Bridging at Ostrel (A-C-02):** "Real vehicles, being loaded on flatcars." **KESTREL (A-C-03):** "The contingency account is closed. One request refused by the depot commander: combat fuel for 12th Brigade, signed by Drask's own staff and by nobody at Army level." diagnostic. **FINCH (A-C-04):** "The ministry believes 12th Brigade is entraining on the 19th. Nobody there knows of an escort." diagnostic. **4th Army HQ net (A-C-05):** "Drask's headquarters is passing orders to 12th Brigade on a brigade net. Nothing about them goes up to the General Staff." diagnostic. **Ansel on 12th Brigade (A-C-06), from Day 3:** "The station asked him. He did not know of any escort. He left the room to telephone and came back grey. He asked how sure we are." diagnostic. **PETREL (A-C-07):** "Grey Ledger has no contract this month." **HERON (A-C-08):** "Kask will sign on the 20th, and call up only if shots are fired." **WREN field hospitals (A-C-09):** "None forward of Ostrel." (If the leak is open: the same, and true. Nobody is planting through liaison in this version.)

Analysts, A: Vasko on A-3-02, "An escort for observers. That's a courtesy." (0). Marrow on A-3-03, "The agreement has no escort in it. So whose idea is it?" (1). Halden, a day late on A-2-03, "That reference format again. The same hand as October." (1); on A-3-01, "Two brigades to the railhead and one to the road. That isn't one army doing one thing." (1).

**Outcome, A** (position reached in time, per the table above):

| Final state | Result |
| --- | --- |
| H3 High in position | **held.** Drask's column meets a battalion on the access road, and a telephone call from his own capital. He is relieved by noon. |
| H2 High in position | **standoff.** The road is held. Kordav's leadership, shown an alliance army deployed in the open and Elsin calling up, backs its general after the fact. The agreement is dead. |
| H3 or H2 Medium, or High too late | **standoff.** The company holds the road for an hour. |
| H1, or Low | **lost.** Drask has the access road by 0700. His government keeps it. |

## Version B: truth H2 on all five days

No agreement. Kordav will cross at Dolan at dawn on the 20th. It repeats October's show, because October's show worked: the bridging on the square is now decoys, the real bridging is in Dolan forest, and reservists carry papers with a release date. Best calls: H2 Low, Medium, High from Day 3.

| ID | Day | Source | Text | Kind |
| --- | --- | --- | --- | --- |
| B-2-01 | 2 | CWS | **Planted (circular):** "Kordav's reservists will be released on the 22nd, defence sources say." Cross-check: B-2-02. | planted |
| B-2-02 | 2 | KSB | "Defence ministry: reservists 'will be released on the 22nd.'" | planted (origin) |
| B-2-03 | 2 | CWS | "Kordav's health ministry has postponed elective surgery at four hospitals 'for staff training.'" | true, diagnostic-lite (October: unchanged) |
| B-3-01 | 3 | CIRRANE | "Ostrel, standing pass. Bridging on the main square: about 40 vehicles, none has moved since October. No tracks lead to or from them." | true, diagnostic |
| B-3-02 | 3 | KSB | "State television: a parade at Ostrel on the 19th. The bridging will drive past the reviewing stand." | **planted** in effect: the parade is announced and never held. Kind: noise. |
| B-3-03 | 3 | SOCIAL | "Reservists post that phones were collected last night." | true |
| B-4-01 | 4 | WREN | "Border posts report nothing at Dolan." *If the leak is open and the liaison request was tasked:* "…nothing at Dolan, and the service is confident." | noise (they see the crossing, not the forest) |
| B-4-02 | 4 | MNA | "Marrat closes the Tolen crossing 'for the duration.'" | true |
| B-4-03 | 4 | CWS | "Military traffic into Ostrel has not stopped this time." | true (October: stopped on the 4th) |
| B-5-01 | 5 | CIRRANE | "Ostrel: 12th and 31st Brigades are gone from the training area. The bridging is still on the square." | true, diagnostic |
| B-5-02 | 5 | KSB | "State television: 'Kordav's patience has limits.'" | true (01's first words) |

Collection, version B: **Dolan forest (B-C-01):** "About 60 bridging vehicles under the trees, 4 km from the crossing, and a tented facility consistent with a field hospital." diagnostic. **Bridging at Ostrel, close look (B-C-02):** "The vehicles on the square cast no shadow under the chassis and have no tracks. Decoys." diagnostic. **KESTREL (B-C-03):** "Blood products went forward on the 14th. All issues moved to the contingency account at 0400 on the 15th." diagnostic. **FINCH (B-C-04):** "The order is signed. The 20th, at Dolan." diagnostic. **4th Army HQ net (B-C-05):** "Quiet since the 15th. Stations have moved to a net we don't cover." **Ansel (B-C-06):** "He is not answering the station's calls." **PETREL (B-C-07):** "Grey Ledger has a new contract: the same six boxes, at 0400 on the 20th." If collected, Brandt is warned (`grid: warned`); if Crisis 05 ended Lights on and it isn't collected, Kalsa goes dark at 0400 (epilogue line, Pressure +1). **HERON (B-C-08):** "Kask will call up the moment the general asks." **WREN field hospitals (B-C-09):** leak shut: "One, in Dolan forest, seen from the ridge post." diagnostic. **Leak open: planted,** "None forward of Ostrel," because the request crossed LATTICE and the answer was arranged. Tell: the same sentence, word for word, as October's R-5-03. Cross-check: B-C-01, B-C-03.

Analysts, B: Vasko on B-2-01, "A release date again. It was a show in October and they went home." (0). Marrow on B-2-03, "In October the hospitals didn't change a thing. Now four of them have." (1). Halden, a day late on B-3-01, "Forty vehicles that haven't moved in six weeks and leave no tracks. I'd want a closer look." (1).

**Outcome, B:**

| Final state | Result |
| --- | --- |
| H2 or H3 High in position, orders secure | **held.** Lead elements reach Dolan and find a battalion dug in. They stop. |
| The same, with LATTICE open and no courier | **standoff.** They knew where the battalion was, and bridged upstream of it. |
| Medium, or High too late | **standoff.** |
| H1, or Low | **lost.** Kordav holds the Tarsk sector by 0900. |

## The endings

**The world,** first that fits:

| Rule | Ending |
| --- | --- |
| `held` and Alliance on the record ≥ 0 | **The alliance holds.** Kordav stops at the river. Nobody announces a victory. The water talks reopen in Aubrec in the spring. |
| `held` and Alliance < 0 | **A cold peace.** Kordav stops at the river, and Kask thanks the alliance and asks it to leave by the summer. Elsin stays whole and goes its own way. |
| `standoff` and Pressure ≤ 3 | **A cold peace.** |
| `standoff` and Pressure ≥ 4 | **Partition.** Kordav keeps what it holds in the north. Marrat's guards stay in the south. The maps are redrawn by not being corrected. |
| `lost`, and Crisis 09 was misjudged, and Pressure ≥ 4 | **War.** The alliance answers. It is the thing the cell existed to prevent. |
| `lost` otherwise | **Partition.** |

**You,** first that fits:

| Rule | Ending |
| --- | --- |
| Reassigned, and never recovered | **A new cell.** A long record, and nobody reading it. |
| Removed Rhun or Arle in 06, and never closed the leak | **The wrong name.** The postmortem names what the person you named is doing now. |
| Closed the leak in 06 | **Vindicated.** You found it and were believed. |
| Closed it in 09 | **Vindicated, late.** |
| Final credibility 3 or more | **Trusted, and blind.** Your customers relied on you. The leak was never found. |
| Otherwise | **Doubted, and blind.** |

The closing screen is the world passage, then the "you" passage, then the campaign's totals. Three pairings get one extra line: *The alliance holds + The wrong name* ("The alliance held. Col. Rhun teaches at the defence college, and does not take the alliance's calls." / Arle equivalent); *War + Vindicated* ("You were right about the link, and it was not enough."); *The alliance holds + Vindicated* ("Halvorsen's note this time is three lines.").

## Record

Points: held +5, standoff 0, lost −5. Credibility outcome +2 / 0 / −2. The service record gets `world` and `you`, and the campaign is marked complete.

## Postmortem

States the version. Lessons, A: A government and its general are two actors. The agreement's text was a source: it had no escort in it. A forged order can be meant to make you defend too loudly. Lessons, B: Evidence that convinced you once can be staged once it is known. Compare with last time item by item: the hospitals had changed, the trains hadn't stopped, the vehicles hadn't moved. Check that your own orders travel by a road nobody else is reading.

## Critic's notes

- **Two versions, two days of shared text.** Day 1 is deliberately the same so the version isn't given away by the inbox.
- **Version B punishes the player who learned 08 too well,** which is the point, and Marrow says so on Day 1. It needs the comparison items (B-2-03, B-4-03) to be findable, or it is unfair.
- **A player who burned KESTREL, FINCH and PETREL** has imagery, signals and Ansel. Still two paths to the diagnostic in each version (imagery and signals in A; two imagery targets in B).
- **Sixteen bespoke endings are cut to four world passages, six "you" passages and three linking lines** (changes the story plan). Fewer words, same range.
- **War needs three things to go wrong.** It should be rare.
