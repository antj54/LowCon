# Crisis 07: The Vote in Kalsa · GM key and postmortem (paper)

**SPOILERS FOR THIS SCENARIO AND FOR THE CAMPAIGN. Anthony: don't open this (#67, #68). It depends on `claude/story-key.md`.**

*Written for Act 3. Paper only. Player packet: `claude/crisis-07-player-packet.md`.*

---

## What this scenario is for

1. **Not everything is Kordav.** In Crises 02, 04, 05 and 06 the answer was Kordav or Kordav's channel. Here the government falls for its own reasons, and the right call is H1: the vote. "It's always Kordav" is the habit this scenario punishes.
2. **The adversary wants you to accuse it.** Kordav isn't engineering the fall. It's amplifying it, and its real aim is to get the alliance to say "Kordav" in public, so the vote becomes about foreign meddling and the new government owes the alliance nothing. Its plants are built to be repeated, and then debunked.
3. **Your own assessment, read back to you.** If the leak is still open, Kordav reads the evening note to Valde's office and feeds it back through "a source close to Valde": your own judgment, word for word, presented as corroboration. It's circular reporting, from the inside.
4. **Hands off, but not asleep.** The best ending needs a quiet channel to the opposition early, and a public commitment to respect the vote once the coalition has broken. Medium alone isn't enough.

## Ground truth

The truth is **H1 on every day.** The street is real but doesn't decide it; parliament does.

| Day | What's really happening | Best call |
| --- | --- | --- |
| 1 (26th) | Ekdal has spent three weeks in her constituency and has decided to leave. Kordav's embassy doubles its press staff to amplify. | H1 at Low |
| 2 (27th) | The protests grow on their own money. The Bureau posts a forged bank document "proving" Kordav funds National Renewal, meant to be repeated by the alliance and then exposed. | H1 at Medium |
| 3 (28th) | Ekdal leaves. The motion is tabled. The biggest protest, and the only violence. | H1 at High (Medium is defensible) |
| 4 (29th) | Ekdal and Kask negotiate. The Bureau posts recycled winter photos of "organisers at a Kordavan camp." | H1 at High |
| 5 (30th) | The deal is signed. The organisers call off the march. | H1 at High |

## Adversary plan

| Aim | How | Channels |
| --- | --- | --- |
| Make the alliance say "Kordav" in public | Plant evidence of Kordavan interference that can be debunked after the alliance repeats it | SOCIAL (the bank document, the camp photos) |
| Feed the alliance's own fears back to it | If LATTICE is open: read the evening note and play it back through a "source close to Valde" | EMBASSY's walk-up source (Appendix D) |
| Look the part | Double the embassy's press staff; KSB at full volume | KSB, Kordav's embassy |

**The meta-tell:** every piece of evidence of a Kordavan plot is either forged, ten years old, a thousandth of the money, or your own words.

## Sources (hidden values)

| Code name | True reliability | Controlled by Kordav | Notes |
| --- | --- | --- | --- |
| EMBASSY | 0.9 | No | Accurate, except the walk-up "source close to Valde" in Appendix D, who is the Bureau's |
| WREN | 0.85 | No | True and misleading once (R-3-04) |
| COURIER | 0.8 | No | Honest. The poll is the most important number in the scenario. |
| CWS | 0.9 | No | Straight |
| KSB | — | Yes | Noise and gloating |
| SOCIAL | 0.3 | Partly | Both fixed plants |
| HERON | 0.85 | No | The best source on Ekdal |
| MERIDIAN | 0.9 | No | Reads the Bureau's instruction, if tasked |

## Item key: push

| ID | Kind | Note |
| --- | --- | --- |
| R-1-01 | true | The grievance, from the record. "Has not been asked to by anyone" is true. |
| R-1-02 | true | Real anger, real buses |
| R-1-03 | noise | Gloating |
| R-1-04 | true | Amplification, not engineering |
| R-1-05 | clutter | The letterhead. Also the cross-check for R-2-03. |
| R-2-01 | true | Kask and Ekdal talk. It looks like a plot and is politics. |
| R-2-02 | true | The protests grow |
| R-2-03 | **planted** | The bank document |
| R-2-04 | true | Kask is anti-everyone |
| R-2-05 | true | The note, and its route. Cross-check for Appendix D. |
| R-3-01 | true, diagnostic | Ekdal leaves for her own reasons, on her own schedule |
| R-3-02 | true | The street at its peak. Tempts H2. |
| R-3-03 | noise | Gloating |
| R-3-04 | noise | True and meaningless: a youth exchange ten years ago |
| R-3-05 | true | The note |
| R-4-01 | true | The deal's price is domestic |
| R-4-02 | **planted** | The camp photos |
| R-4-03 | true, diagnostic | 61% want the task force to stay. A government that falls isn't a country leaving. |
| R-4-04 | clutter | The heat. Also the cross-check for R-4-02. |
| R-4-05 | true | The note |
| R-5-01 | true | "Review, not end" |
| R-5-02 | noise | Gloating |
| R-5-03 | true | The street stands down. H2 falls away. |
| R-5-04 | true | The note |
| D2a–D5a, D2b–D5b | **planted** | The Bureau's walk-up source. See below. Only if LATTICE is open. |
| D9 | true | The leaked private warning |

## Item key: pull

| ID | Tasking | Kind | What it tells you |
| --- | --- | --- | --- |
| C-01 | HERON, Days 1–2 | true, diagnostic | Ekdal decided on her own, and dislikes Kask |
| C-02 | HERON, Days 3–5 | true, diagnostic | The deal is domestic, and protects the task force for a year |
| C-03 | Protest funding | true, diagnostic | Real money, and a token Kordavan amount |
| C-04 | The bank document | true | It's a forgery, posted by a new account |
| C-05 | Bureau traffic | true, diagnostic | The Bureau's plan, in its own words: get the alliance to say "Kordav" in public |
| C-06 | Kask's finances | noise | Declared, and one grain importer. Tempting, and nothing. |
| C-07 | Security service on organisers | true | Local organisers. Costs nothing, unless LATTICE is open. |
| C-07K | (follow-up, LATTICE open) | true | The request was read, and used against Valde. Alliance −1. |
| C-08 | Whip count | true | It's arithmetic: the Highlands Party decides it |

## Planted items: the reasoning

### R-2-03 (Day 2, SOCIAL): the bank document

- **Tell:** "the letterhead of Elsin's Ministry of Finance."
- **Cross-check:** R-1-05, the day before: it has been the Ministry of Finance and Economy since last year. C-04 confirms it for one point.
- **Motive:** for the alliance to repeat it, and for Kask to wave the forgery on television the day after.

### R-4-02 (Day 4, SOCIAL): the camp photos

- **Tell:** winter coats and snow.
- **Cross-check:** R-4-04, the same day: Kalsa is at 29°C. It's May.
- **Motive:** the same. A public accusation that falls apart within a day is worth more to Kordav than any plot.

### D2a–D5a (LATTICE open, after an H3 brief): your judgment, word for word

- **Tell:** a source volunteers your own key judgment in your own words.
- **Cross-check:** the admin note the same morning (R-2-05, R-3-05, R-4-05, R-5-04), which quotes what the note to Valde's office said. The note crossed LATTICE.
- **Motive:** confirmation. It pushes a player who suspects a plot towards a public warning.

### D2b–D5b (LATTICE open, after an H1 or H2 brief): "the alliance has it wrong"

- **Tell:** the source answers a note it shouldn't have seen.
- **Cross-check:** the admin note, and C-01, C-02 or C-03 if collected.
- **Motive:** to change your mind. Kordav wants you at H3.

## The analysts

| Analyst | Notes | Right | How it went |
| --- | --- | --- | --- |
| Vasko | R-1-04, R-2-03, R-3-04, R-4-03, R-5-03 | 1 of 5 | After 06 he sees Kordav in everything. Right once, about the cancelled march. |
| Halden | R-2-03, R-4-02, a day late | 2 of 2 | The letterhead, and the snow. Both arrive the morning after you could have caught them. |
| Marrow | R-1-02, R-2-04, R-3-04, R-4-03 | 4 of 4 | She reads crowds and polls. Her best scenario. |

## Marlowe's actions and the endings

| Brief | What happens |
| --- | --- |
| H1 High | Public commitment and talks with Kask. On Days 1–2, Valde takes it as abandonment: credibility −1, and the talks start under a cloud. |
| H1 Medium | A quiet channel to the opposition |
| H2 High | The vote is postponed. Next morning the protests double and blame the alliance: credibility −1. |
| H2 Medium | A request for police restraint. Harmless. |
| H3 High | A public warning. Next morning Kask is on television with it: credibility −2. |
| H3 Medium | A private warning in the note. LATTICE open: KSB quotes it the next morning (D9), credibility −1. Link shut: Valde's police question organisers on it, and they tell the Courier, credibility −1. |
| Low | Nothing. Two days running costs credibility. |

**Events:** `talks` at the start of Day 5: if Marlowe has opened the quiet channel or made the public commitment by then, `talks: open`. `early`: a public commitment on Day 1 or 2.

**Endings** (first that fits):

| Condition | Ending | Points |
| --- | --- | --- |
| A public warning, ever | **Meddled.** The motion passes, and Kask's first speech as prime minister is about "the alliance choosing Elsin's government." He asks for the task force to be halved by the autumn. | −5 |
| The vote postponed, ever | **Postponed.** The vote happens a week late, after a week of riots blamed on the alliance. Kask wins it by more than he would have. | −3 |
| A private warning, ever | **Overheard.** Kask governs with a grudge, and Valde's last week is remembered as a hunt for a plot that wasn't there. | −2 |
| Public commitment at the end, made on Day 3 or later, with `talks: open` | **Hands off.** The motion passes. Kask's first call is to the embassy. The task force agreement is reviewed over the summer and survives with a new name. | +5 |
| Anything else without a warning or a postponement | **Kept out of it.** The motion passes. Kask's government is polite and distant, and the review takes a year. | +2 |

**Credibility:** starts from Marlowe's at the end of Crisis 06. Outcome: Hands off +1, Meddled −1.

## What it writes to the record

| Outcome | Alliance | Pressure | For Act 3 |
| --- | --- | --- | --- |
| Hands off | +1 | — | Kask's government talks to the alliance. Used in 08. |
| Kept out of it | 0 | — | Kask's government keeps its distance |
| Overheard | −1 | — | — |
| Postponed | −1 | +1 | — |
| Meddled | −2 | +1 | The task force is halved by the autumn. Used in 08 and 10. |
| C-07 tasked with LATTICE open | −1 | — | — |
| Any D-item cited | — | — | Case file: "Your own judgment came back to you from a source in Kalsa." |
| C-05 collected | — | — | Case file: "The Bureau wanted the alliance to say 'Kordav' in public." |

## Postmortem script

> **Day 1.** The Highlands Party gave Valde a week over a grievance its voters had carried all year. Kordav's embassy hired more press officers.
>
> **Day 2.** Kask and Ekdal talked. A bank document appeared on a letterhead that hasn't existed since last year.
>
> **Day 3.** Ekdal left the coalition. Forty thousand people came out, and the police used water cannon.
>
> **Day 4.** Photos of "organisers at a Kordavan camp" showed snow. It was 29°C in Kalsa. Most of Elsin wanted a new government and the same task force.
>
> **Day 5.** Ekdal and Kask signed. The march was called off.

**An open question** (Act 3 thread; facts only): none. The leak's status is already on the record.

**Lessons:**

1. Not everything bad is the adversary's doing. Sometimes it's just Tuesday in a coalition.
2. An adversary can want to be accused. Ask who gains from your statement, not just from the event.
3. Your own assessment, quoted back to you by someone who shouldn't have read it, isn't corroboration. It's a leak.
4. A government falling isn't a country leaving.
5. Hands off isn't the same as eyes shut.

---

## Designer notes (critic hat)

**Dominant-strategy check** (paper estimate: calls and ending; before evidence, doubts and burns):

| Strategy | Ending | Total |
| --- | --- | --- |
| Best play: H1 Low, Medium (quiet channel), then High from Day 3 | Hands off | **+17** |
| H1 High from Day 1 | Kept out of it (commitment on Day 1, so it isn't "Hands off") | **+17**, credibility −2 |
| Never above Medium on H1 | Kept out of it | **+11** |
| Always hedge (Low on H1) | Kept out of it | **+7**, credibility falls |
| The street: H2 Medium, then H2 High on Day 3 | Postponed | **−11** |
| Vasko's path: H3 Medium on Days 2–3, then H1 High | Overheard | **+1** |
| Always Kordav, H3 High | Meddled | **−25** |

**Watch for:**

- **H1 High from Day 1 ties best play on points.** It's a blind guess against the campaign's habit, since four of the last five answers were Kordav. It loses the best ending and two points of credibility. If testers find that too cheap, raise the cost of an early public commitment, not a freeze.
- **The echo items only exist if the leak is open,** so two players can see quite different scenarios. A player who closed the leak in 06 gets a quieter, more generic 07, which is the reward. Check that the closed-leak version still has enough to argue about. I think it does, with the bank document, the photos, R-3-04 and Vasko.
- **The poll (R-4-03) is the moral centre.** It says a government can fall without a country leaving. Don't bury it.
- **Reading load:** five items a day, plus one echo item if the leak is open. Lighter than 06.
- **"Not Kordav" right after "Kordav's channel"** risks feeling like a trick. It's fair only if the scenario makes the domestic story at least as vivid as the plot. The Highlands Party's grievance comes from the player's own record for that reason.

**Engine needs before building:**

- **A condition on the previous day's brief** (`when: {lastBrief: {hyp: [...]}}`) for the echo items, and text that quotes the player's own key judgment (the admin notes and the a-variants)
- **Record conditions on items:** earlier endings, Alliance on the record, story flags (`leak`, `wrongName`), all supported or nearly, from #74
- **Endings on a flag plus "made on Day 3 or later"** (`since`), supported
- **Events the morning after a state is entered** (postponed, public warning, private warning), supported (`onEnter`)
- **A follow-up only when LATTICE is open** (C-07K), supported (`then.when` with a record condition)
- **Codex entries** for Valde, Ekdal, Kask, the Highlands Party, National Renewal, HERON, Hollis and Ahrend
- **Map:** none. The Codex map shows Kalsa, and nothing moves.
