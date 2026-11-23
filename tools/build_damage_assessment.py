#!/usr/bin/env python3
"""Builds crises/damage-assessment.json (Crisis 06). SPOILERS: this file holds the campaign's answer."""
import json, os

def R(id, day, src, disc, grade, cred, text, kind, note, tells=(), reveal=None, via=False, diagnostic=False, when=None, textBy=None, append=None):
    r = {"id": id, "day": day, "sourceId": src, "discipline": disc, "sourceGrade": grade, "credibility": cred, "text": text, "kind": kind,
         "supports": [], "contradicts": [], "tells": list(tells), "postmortemNote": note}
    if reveal: r["reveal"] = {"tell": reveal[0], "crossCheck": {"ids": reveal[1], "text": reveal[2]}, "motive": reveal[3]}
    if via: r["via"] = "collection"
    if diagnostic: r["diagnostic"] = True
    if when: r["when"] = when
    if textBy: r["textBy"] = textBy
    if append: r["append"] = append
    return r

ASM, WR, VS, VET, COR, KSB, SOC, CPR, MER, LAB, OS, WATCH, EVET, ADM = ("S-ASSESS", "S-WREN", "S-VEYLSTAFF", "S-VETTING", "S-CORVANE", "S-KSB", "S-SOCIAL", "S-CPR", "S-MERIDIAN", "S-LAB", "S-OSINT", "S-WATCH", "S-EVETTING", "S-ADMIN")
SHIP = lambda *e: {"recordEnding": {"crisis": "missing-shipment", "in": list(e)}}
LIGHTS = lambda *e: {"recordEnding": {"crisis": "lights-out", "in": list(e)}}
LINK_STATES = ["shut", "couriers"]

DELIVERY = "LATTICE's original terminals were shipped to Kalsa four years ago through Halsk, by the forwarder Tessaly Freight. They arrived 36 hours late, seals intact, and were signed for without query."
LETTER_O = "Appendix to part five: the lab's last comparison. The attackers' list spells one server \"PCS-O6\", with a letter O. The five paper copies print a zero. Only the electronic copy, lodged over LATTICE, has the O."

reports = [
 # ---- Day 1 ----
 R("R-1-01", 1, ASM, "Security", "B", 2, "Part one: the Veyl, last spring. Kordav staged a radio call on 12th Brigade's net, the one net we were reading. Outside your cell, the fact that we read it appeared in one place: the daily assessments General Halvorsen shared with Kalsa, over LATTICE. KESTREL's identity was never written down outside the cell, and nobody has come near KESTREL.", "true",
   "The pattern, part one. What leaked had gone to Kalsa over LATTICE; what stayed in the cell never did.",
   textBy=[{"when": {"burnedOnRecord": "KESTREL"}, "text": "Part one: the Veyl, last spring. Kordav staged a radio call on 12th Brigade's net, the one net we were reading. Outside your cell, the fact that we read it appeared in one place: the daily assessments General Halvorsen shared with Kalsa, over LATTICE. KESTREL went quiet last spring after he was met on two days running. The assessment puts that down to how often he was met, not to anything written down."}]),
 R("R-1-02", 1, ASM, "Security", "B", 2, "Part two: the Walk-in. The Bureau staged its recall on its headquarters admin net, the net it believed we read. Two weeks earlier, a product sourced from that net went to Kalsa over LATTICE. FINCH was found because the Bureau watched the ministry door, not because of anything we wrote.", "true",
   "The pattern, part two. FINCH's loss has its own, human explanation."),
 R("R-1-03", 1, ASM, "Security", "B", 2, "Part three: the Southern Line. Someone knew where the guard company was. Its movement order went through Elsin's Southern Command, where Marrat's advisers sit. The assessment treats this one as explained.", "true",
   "The explained leak: real, local and human, and not this one."),
 R("R-1-04", 1, WR, "Liaison", "B", 2, "Col. Rhun: \"I know whose desk this assessment is circling. Send me something by hand. Anything. Then watch what Kordav does with it.\"", "true",
   "Rhun volunteered for the hand test. Suspicion was the mistake."),
 R("R-1-05", 1, CPR, "OSINT", "C", 3, "An essay in the Continental Policy Review: \"Kordav needs no spy in Kalsa. The alliance moves the same way every time, and announces it in press releases.\"", "noise",
   "Half right. We are predictable, but a staged call on one specific net isn't a guess."),
 R("R-1-06", 1, ADM, "Admin", "A", 1, "The security officer asks staff not to discuss the assessment in the canteen. The canteen has asked the security officer the same.", "clutter", "The canteen."),
 # case-file head starts
 R("R-1-07", 1, COR, "Commercial", "B", 2, DELIVERY, "true", "Your case file gave you the 36-hour detour on Day 1.", diagnostic=True, when={"noticed": "same-delay"}),
 R("R-1-08", 1, ASM, "Security", "B", 2, LETTER_O, "true", "Your case file gave you the letter O on Day 1.", diagnostic=True, when={"noticed": "letter-o"}),
 R("R-1-09", 1, ASM, "Security", "B", 2, "Your note from Lights Out stands: a request to Kalsa's registry, sent over LATTICE, was on Kordav's television the next day.", "true", "A liaison request heard in Kordav.", when={"noticed": "registry-heard"}),
 R("R-1-10", 1, ASM, "Security", "B", 2, "Your note from the Missing Shipment stands: a request to Halsk's port police, sent through Kalsa over LATTICE, reached Tessaly before the police did.", "true", "Another liaison request heard on the other side.", when={"noticed": "tipped-off"}),
 R("R-1-11", 1, ASM, "Security", "B", 2, "Your doubt about the Grey Ledger chat log is confirmed: it was a forgery.", "true", "The forgery that pointed at Rhun.", when={"noticed": "not-rhun"}),
 # ---- Day 2 ----
 R("R-2-01", 2, ASM, "Security", "B", 2, "Part four: the Missing Shipment. The forty replacement terminals for LATTICE's Kalsa end went missing in Halsk for three days last autumn.", "true",
   "The terminals. If they were sent back in Crisis 04, the lab's finding is here.",
   append=[{"when": SHIP("sent-back"), "text": "Corvane took them back. Six weeks later an independent lab opened one: inside was a component that isn't on Corvane's build list. It has found the same component in every unit it has opened since."},
           {"when": SHIP("passed"), "text": "Corvane's engineers inspected them for three weeks, found nothing wrong, and they went in over the new year."},
           {"when": SHIP("installed"), "text": "They have been in the ministry's communications room since the 8th of that month."}]),
 R("R-2-02", 2, VET, "Security", "B", 2, "Vetting has flagged unreported foreign travel by T. Marrow, your open-source analyst, in the week before she joined the cell.", "true",
   "True, and it means nothing: she joined in the Southern Line, after the first two leaks.", when={"onTeam": "marrow"}),
 R("R-2-03", 2, KSB, "OSINT", "D", 3, "Kordav's broadcaster, citing \"reports in Elsin's own press\" (the Kalsa Evening Courier, 22 January): the alliance's leak is \"a colonel in Kalsa who has had enough of Elsin's foreign masters.\"", "planted",
   "Circular reporting.", tells=["circular"],
   reveal=("It cites an Elsin paper, and names it.",
           ["R-2-04"], "The Courier's 22 January story gave Kordav's broadcaster as its source (R-2-04). The broadcaster is quoting itself through an ally's paper.",
           "Circular reporting turns one Bureau claim into two that look independent.")),
 R("R-2-04", 2, ASM, "Security", "B", 2, "Part five: Lights Out. The attackers' target list was built from issue 7 of the network diagram: five paper copies and one electronic copy lodged over LATTICE. The \"leaked chat log\" naming the liaison office was a forgery: it matches no message Grey Ledger has ever sent. The Kalsa Evening Courier's story of 22 January, \"a traitor in the liaison office,\" gave Kordav's broadcaster as its source.", "true",
   "The diagram and the forgery. The cross-check for R-2-03.",
   append=[{"when": LIGHTS("clean", "clean-cold"), "text": "In March the lab finished with Corvane's January images: they carried a remote-management component that isn't on Corvane's published build list."},
           {"when": LIGHTS("lights-on"), "text": "Corvane's January images have run the grid's control servers since the 15th of January."}]),
 R("R-2-05", 2, KSB, "OSINT", "D", 3, "Last week, within hours, Kordav's broadcaster reported that the alliance \"has announced\" a new signals team for Kalsa.", "noise",
   "Looks like a link leak and isn't: \"has announced.\" It was in a press release."),
 R("R-2-06", 2, ADM, "Admin", "A", 1, "The building's secure room has a new lock. Nobody has been issued the new key.", "clutter", "The lock."),
 # ---- Day 3 ----
 R("R-3-01", 3, COR, "Commercial", "B", 2, DELIVERY, "true", "LATTICE's own terminals took the same detour through Halsk as last autumn's.", diagnostic=True, when={"notNoticed": "same-delay"}),
 R("R-3-02", 3, VS, "Liaison", "B", 2, "Maj. T. Arle: \"My distribution lists were long because the general wants everyone to read you. They're down to eleven names. For the record, I was on leave for all of January.\"", "true",
   "Arle, clearing himself. His copy of the diagram was still sealed in the registry."),
 R("R-3-03", 3, SOC, "OSINT", "F", 3, "A Kordavan defence forum posts \"a page of Task Force VEYL's internal distribution list, courtesy of a friend on the general's staff.\" The page lists the task force's press office, its public enquiries desk and its visitors' centre.", "planted",
   "A secret list that isn't secret.", tells=["nothing-secret"],
   reveal=("Everything on the page is public: a press office, an enquiries desk and a visitors' centre.",
           ["R-3-05"], "The page is from last summer's press pack, still on the task force's website (R-3-05).",
           "To spread the hunt to our own side, so it widens instead of narrowing.")),
 R("R-3-04", 3, WR, "Liaison", "B", 2, "Col. Rhun: \"My service has gone back over everything that reached my desk this year. What came to me on paper never went anywhere that I can find. I can't say that about everything that came to me.\"", "true",
   "Rhun, carefully, and right."),
 R("R-3-05", 3, ADM, "Admin", "A", 1, "Public affairs reminds staff that last summer's press pack is still on the task force's website, including the page of public contact addresses it was asked to take down.", "clutter",
   "The press pack. Also the cross-check for R-3-03."),
 # ---- Day 4 ----
 R("R-4-01", 4, VS, "Liaison", "B", 1, "The revised Veyl contingency plan went to Kalsa at 0900 over LATTICE.", "true", "How the plan went.",
   textBy=[{"when": {"flag": {"event": "plan", "in": ["safe"]}}, "text": "The revised Veyl contingency plan went to Kalsa at 0900, by courier."}]),
 R("R-4-02", 4, ASM, "Security", "B", 2, LETTER_O, "true", "The letter O: the attackers' map was the electronic copy.", diagnostic=True, when={"notNoticed": "letter-o"}),
 R("R-4-03", 4, KSB, "OSINT", "D", 3, "Kordav's broadcaster: \"Our friends in Elsin's liaison service keep us better informed than the alliance knows.\"", "planted",
   "The boast.", tells=["unverifiable", "too-on-message"],
   reveal=("It names nothing that could be checked, and says exactly what the Bureau needs said.",
           ["R-2-04"], "The last time Kordav pointed at that office, it was with a forgery (R-2-04). A marked item sent by hand to Rhun, or over the link to a desk she never sees, settles it.",
           "A mole hunt protects an implant.")),
 R("R-4-04", 4, COR, "Commercial", "B", 2, "Corvane asks, stiffly, whether the alliance means to keep using its terminals, and reminds everyone that its seals have never been broken.", "noise",
   "Seals tell you about seals."),
 R("R-4-05", 4, ADM, "Admin", "A", 1, "The new key to the secure room has been issued. The lock has been changed again.", "clutter", "The key."),
 # ---- Day 5 ----
 R("R-5-01", 5, ASM, "Security", "A", 1, "The assessment is due for signature today. Elsin's minister has asked to read it before the alliance acts.", "true", "The deadline."),
 R("R-5-02", 5, WR, "Liaison", "B", 2, "Col. Rhun has asked for a transfer, \"effective on the alliance's decision, whichever it is.\"", "true",
   "Not guilt. A career that was over either way."),
 R("R-5-03", 5, KSB, "OSINT", "D", 3, "Kordav's broadcaster: \"The alliance is hunting itself. We wish it luck.\"", "noise", "Gloating."),
 R("R-5-04", 5, ADM, "Admin", "A", 1, "The secure room is now open to anyone. Facilities say this is temporary.", "clutter", "The room."),
 # ---- collection ----
 R("C-01", None, WATCH, "Test", "B", 1, "Nothing about the Brennick depot has turned up anywhere: no Kordavan broadcast, no Bureau traffic, no activity near the depot.", "true",
   "Silent. Rhun the person doesn't pass things on.", via=True, diagnostic=True),
 R("C-02", None, WATCH, "Test", "B", 1, "Kordav's broadcaster ran a piece on \"alliance engineers prowling the north signals annex, according to our friends in Elsin's liaison service.\" Only the version sent over LATTICE to Col. Rhun's desk named the annex.", "true",
   "The trap. It surfaced, and couldn't tell Rhun from the link. The broadcaster's attribution was the Bureau framing her.", via=True),
 R("C-03", None, WATCH, "Test", "B", 1, "Bureau traffic refers to \"the engineers' visit to pumping station 4.\" Only the version sent over LATTICE to Director Brandt's office named pumping station 4. It went nowhere near Col. Rhun's desk.", "true",
   "The test that settles it: over the link, to a desk Rhun never sees.", via=True, diagnostic=True),
 R("C-04", None, WATCH, "Test", "B", 1, "Nothing about the Mirren road bridge has turned up anywhere.", "true", "Silent. Clears our side.", via=True),
 R("C-05", None, WATCH, "Test", "B", 1, "Nothing about the Saule ferry has turned up anywhere.", "true", "Silent. Clears your cell.", via=True),
 R("C-06", None, LAB, "Technical", "B", 1, "The lab has opened one of the ministry's LATTICE terminals. Inside is a component that isn't on Corvane's build list, fitted before the terminal was ever installed.", "true",
   "The component. The second road to the answer.", via=True, diagnostic=True,
   textBy=[{"when": SHIP("sent-back"), "text": "The lab has opened one of the ministry's LATTICE terminals. Inside is a component that isn't on Corvane's build list: the same component the independent lab found in the terminals Elsin sent back."}]),
 R("C-07", None, OS, "OSINT", "B", 1, "Four days in her mother's town, the week before she joined. A death notice in the local paper. Her declaration was filed nine days late.", "true", "A funeral.", via=True),
 R("C-08", None, COR, "Commercial", "B", 2, DELIVERY, "true", "The 36-hour detour, early.", via=True, diagnostic=True),
 R("C-09", None, MER, "SIGINT", "B", 2, "Bureau traffic calls its Kalsa reporting \"the long line.\" It arrives on a schedule, like a delivery. No officer, meeting, payment or cover name for a person is ever mentioned with it.", "true",
   "A channel, on a schedule, with no person attached.", via=True, diagnostic=True),
 R("C-09Q", None, MER, "SIGINT", "B", 2, "Bureau traffic calls its Kalsa reporting \"the long line.\" No officer, meeting, payment or cover name for a person is ever mentioned with it. Since the alliance changed how it sends things: \"The long line has gone quiet.\"", "true",
   "It went quiet when the link did.", via=True, diagnostic=True),
 R("C-10", None, EVET, "Liaison", "B", 2, "Elsin's vetting office: Col. Rhun's contacts, finances and travel are clean. They would like to know why the alliance is asking.", "true",
   "Clean. And Elsin was asked to vet its own colonel.", via=True),
 R("C-10K", None, KSB, "OSINT", "D", 1, "KSB, in passing: \"The alliance is now vetting its own friends in Kalsa.\"", "true",
   "The request crossed LATTICE and was on Kordav's television the next morning.", via=True),
]

levels = {"home": {"label": "nothing yet", "rank": 0}, "restrict-rhun": {"label": "routine traffic only to Rhun's desk", "rank": 0},
          "restrict-arle": {"label": "Halvorsen's lists cut to named readers", "rank": 0}, "couriers": {"label": "sensitive traffic by courier", "rank": 0},
          "noleak": {"label": "assessment closed: no leak", "rank": 0}, "remove-rhun": {"label": "Col. Rhun removed", "rank": 0},
          "remove-arle": {"label": "Maj. Arle relieved", "rank": 0}, "shut": {"label": "LATTICE shut", "rank": 0}}
PROOF = ["C-02", "C-03", "C-06"]
REMOVED = ["remove-rhun", "remove-arle"]
HI = ["high"]
policy = [
 {"if": {"assetAt": "shut"}, "reply": "done"},
 {"if": {"hypothesis": "H3", "confidence": HI, "assetAt": REMOVED}, "to": "shut", "reply": "shut_apology", "sends": True},
 {"if": {"hypothesis": "H3", "confidence": HI, "collected": PROOF}, "to": "shut", "reply": "shut", "sends": True},
 {"if": {"hypothesis": "H3", "confidence": HI}, "to": "shut", "reply": "shut_bare", "sends": True},
 {"if": {"hypothesis": "H1", "confidence": HI, "assetAt": "remove-rhun"}, "reply": "stands"},
 {"if": {"hypothesis": "H1", "confidence": HI, "collected": PROOF}, "to": "remove-rhun", "reply": "remove_rhun", "sends": True},
 {"if": {"hypothesis": "H1", "confidence": HI}, "to": "remove-rhun", "reply": "remove_rhun_bare", "sends": True},
 {"if": {"hypothesis": "H2", "confidence": HI, "assetAt": "remove-arle"}, "reply": "stands"},
 {"if": {"hypothesis": "H2", "confidence": HI, "collected": PROOF}, "to": "remove-arle", "reply": "remove_arle", "sends": True},
 {"if": {"hypothesis": "H2", "confidence": HI}, "to": "remove-arle", "reply": "remove_arle_bare", "sends": True},
 {"if": {"assetAt": REMOVED}, "reply": "stands"},
 {"if": {"hypothesis": "H1", "confidence": ["medium"], "assetAt": "restrict-rhun"}, "reply": "stands"},
 {"if": {"hypothesis": "H1", "confidence": ["medium"]}, "to": "restrict-rhun", "reply": "restrict_rhun", "sends": True},
 {"if": {"hypothesis": "H2", "confidence": ["medium"], "assetAt": "restrict-arle"}, "reply": "stands"},
 {"if": {"hypothesis": "H2", "confidence": ["medium"]}, "to": "restrict-arle", "reply": "restrict_arle", "sends": True},
 {"if": {"hypothesis": "H3", "confidence": ["medium"], "assetAt": "couriers"}, "reply": "stands"},
 {"if": {"hypothesis": "H3", "confidence": ["medium"]}, "to": "couriers", "reply": "couriers", "sends": True},
 {"if": {"hypothesis": "H4", "confidence": ["medium", "high"], "assetAt": "noleak"}, "reply": "stands"},
 {"if": {"hypothesis": "H4", "confidence": ["medium", "high"]}, "to": "noleak", "reply": "noleak", "sends": True},
 {"if": {}, "reply": "listen"}]
BARE = " Kalsa asked what it rests on. I said your judgment."
replies = {
 "remove_rhun": "Kalsa has agreed to move Col. Rhun. Their minister did not enjoy it, and nor did I.",
 "remove_arle": "Arle is relieved, and your vetting case is suspended pending review. The general would like to discuss it with you.",
 "shut": "The link is off. We're back to couriers and the telephone for a month at least. Kalsa's minister asked whether we've lost our minds. I showed him the test.",
 "restrict_rhun": "Rhun's desk gets routine traffic only, as of tonight. She'll notice.",
 "restrict_arle": "The general's lists are down to named readers.",
 "couriers": "Sensitive traffic goes by courier from tonight. The link carries the weather and the canteen menu.",
 "noleak": "Closed. No leak. I hope you're right, because I've said so in writing.",
 "listen": "That's a shrug. I need more than a shrug.",
 "stands": "That stands.",
 "done": "The link is off. Whatever you think now, that's done.",
 "shut_apology": "I've shut the link. I've also had to tell Kalsa that the person I asked them to remove was not the problem.",
 "frozen": "Not today."}
replies["remove_rhun_bare"] = replies["remove_rhun"] + BARE
replies["remove_arle_bare"] = replies["remove_arle"] + BARE
replies["shut_bare"] = "The link is off. We're back to couriers and the telephone for a month at least. Kalsa's minister asked whether we've lost our minds." + BARE
labels = {"remove_rhun": "Asks Elsin to remove Col. Rhun", "remove_rhun_bare": "Asks Elsin to remove Col. Rhun, on your word", "remove_arle": "Relieves Maj. Arle",
 "remove_arle_bare": "Relieves Maj. Arle, on your word", "shut": "Shuts LATTICE", "shut_bare": "Shuts LATTICE, on your word", "shut_apology": "Shuts LATTICE, and apologises to Kalsa",
 "restrict_rhun": "Sends Rhun's desk routine traffic only", "restrict_arle": "Cuts Halvorsen's lists to named readers", "couriers": "Moves sensitive traffic to couriers",
 "noleak": "Closes the assessment: no leak", "listen": "Does nothing", "stands": "Nothing new. It stands", "done": "Nothing more: the link is already shut", "frozen": "Can't act yet"}

crisis = {
 "id": "damage-assessment", "formatVersion": "1.3", "title": "The Damage Assessment", "crisisNumber": "06", "days": 5,
 "dayLabels": ["the 14th", "the 15th", "the 16th", "the 17th", "the 18th"],
 "placeholderNote": "Kordav, Elsin and Marrat are fictional countries. All officials, companies and systems are fictional.",
 "adversary": "Kordav", "endingEyebrow": "Kalsa, the 18th", "frozenText": "",
 "briefing": {"dateLine": "April. Day 1 is the 14th.", "situation": [
   "For a year Kordav has kept knowing things it shouldn't: which nets we read, what we'd shared with Kalsa, when. Under Secretary Marlowe has opened a damage assessment, and your cell is running it. Her security staff have pulled together what leaked and how each thing travelled. It reaches you a part at a time.",
   "The alliance's traffic with Elsin goes on as usual while the assessment runs: most of it over LATTICE, the secure terminal link between the alliance and Elsin's ministries, maintained by Corvane Systems.",
   "You can send marked items: a notice that Corvane engineers will visit a site on the 24th. Each version names a different site, and only that version names it. Then you watch for the site to turn up on the other side. A test's result takes two days.",
   "A deadline you know about: General Halvorsen's revised Veyl contingency plan goes to Kalsa at 0900 on the 17th, by whatever channel is open to it that morning."]},
 "customer": {"name": "Under Secretary H. Marlowe", "short": "Marlowe", "pronouns": ["she", "her"], "role": "Under Secretary for alliance affairs, with General Halvorsen copied", "callsign": "USEC ALLIANCE",
   "wants": "Who or what is reading us, and what does she do about it?",
   "context": "Her High actions can't be undone. If she acts against an ally's colonel or an ally's link, Kalsa will ask what it rests on, and she'd like something to show them.",
   "tipLine": "High removes a person or shuts the link, and can't be undone. Medium restricts. Low changes nothing."},
 "opening": {"text": "We'll do this properly. Somebody has been reading us for a year. Tell me who.",
   "reassigned": "A new cell, on the oldest question in the building. Fine. Who has been reading us?",
   "byTone": {"good": "You sent the terminals back when everyone else wanted them in. Now I'd like to know who has been reading us, and I'd like the same nerve.",
              "warn": "We'll do this properly. Somebody has been reading us for a year. Tell me who.",
              "bad": "I've signed things on your reading before. This one I'll read twice. Who is it?"}},
 "asset": {"id": "action", "name": "What she has done", "levels": levels},
 "customerPolicy": policy,
 "policySummary": [
   {"brief": "H1 at High", "action": "Asks Elsin to remove Col. Rhun from the liaison desk. Can't be undone."},
   {"brief": "H1 at Medium", "action": "Stops sending anything sensitive to Rhun's desk"},
   {"brief": "H2 at High", "action": "Relieves Maj. Arle, and suspends anyone in your cell with an open vetting flag. Can't be undone."},
   {"brief": "H2 at Medium", "action": "Cuts Halvorsen's distribution to named readers"},
   {"brief": "H3 at High", "action": "Shuts LATTICE for at least a month. Can't be undone."},
   {"brief": "H3 at Medium", "action": "Moves sensitive traffic to couriers. The link carries routine traffic only."},
   {"brief": "H4 at Medium or High", "action": "Closes the assessment: no leak"},
   {"brief": "Anything at Low", "action": "Nothing"}],
 "policyNote": "She'd like something to show Kalsa before she takes a step that can't be undone.",
 "replyLabels": labels, "replies": replies,
 "events": [{"id": "plan", "atStartOfDay": 4, "outcomes": [
   {"if": {"assetAt": LINK_STATES}, "flag": "safe", "points": 0, "title": "The plan went by courier", "pointsLabel": "the Veyl plan"},
   {"if": {}, "flag": "leaked", "points": 0, "title": "The plan went over LATTICE", "pointsLabel": "the Veyl plan"}]}],
 "hypotheses": [
   {"id": "H1", "short": "Someone in Elsin's service", "text": "A person on the Kalsa side is passing on what we share. Most suspicion points at Col. Rhun's liaison desk.", "claim": "a person in Elsin's service is passing on what we share"},
   {"id": "H2", "short": "Someone on our side", "text": "A person in the task force or in your own cell.", "claim": "a person on our own side is passing on what we share"},
   {"id": "H3", "short": "The link", "text": "LATTICE itself is compromised. No person is involved.", "claim": "LATTICE itself is compromised"},
   {"id": "H4", "short": "No leak", "text": "Kordav reads our behaviour, not our traffic.", "claim": "there is no leak, and Kordav reads our behaviour"}],
 "groundTruth": [
   {"day": 1, "trueHypothesis": "H3", "bestCall": "H3 at Low (Medium with a full case file)", "state": "Every leak so far had crossed LATTICE to Kalsa. That fits Rhun and the link equally."},
   {"day": 2, "trueHypothesis": "H3", "bestCall": "H3 at Medium", "state": "The terminals and the diagram ran through the link again. Kordav's broadcaster recycles its January story about a colonel."},
   {"day": 3, "trueHypothesis": "H3", "bestCall": "H3 at High, with a test in hand", "state": "LATTICE's own terminals took the same 36-hour detour through Halsk four years ago."},
   {"day": 4, "trueHypothesis": "H3", "bestCall": "H3 at High", "state": "The Veyl plan goes to Kalsa at 0900. The Bureau points at Rhun's office again."},
   {"day": 5, "trueHypothesis": "H3", "bestCall": "H3 at High", "state": "Rhun asks for a transfer. The assessment is signed."}],
 "adversaryPlan": [
   {"phase": "Blame a person", "days": [1, 2, 3, 4, 5], "wantsYouToBelieve": "H1", "summary": "A mole hunt protects an implant. Point at Rhun, and spread the hunt to our own side.", "channels": [KSB, SOC]}],
 "sources": [
   {"id": ASM, "codeName": "ASSESSMENT", "discipline": "Security", "access": "Marlowe's security staff, compiling the record of what leaked", "startingGrade": "B", "trueReliability": 0.95, "controlledByAdversary": False, "postmortemNote": "Accurate. Drew no conclusion, deliberately."},
   {"id": WR, "codeName": "WREN", "discipline": "Liaison", "access": "Elsin's military intelligence liaison desk, Col. E. Rhun", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Innocent, angry, and right."},
   {"id": VS, "codeName": "VEYL STAFF", "discipline": "Liaison", "access": "Halvorsen's staff, Maj. T. Arle", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Innocent and sloppy."},
   {"id": VET, "codeName": "VETTING", "discipline": "Security", "access": "The alliance's vetting office", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "A true fact with a false implication."},
   {"id": COR, "codeName": "CORVANE", "discipline": "Commercial", "access": "Corvane Systems, which built and maintains LATTICE", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Honest. It didn't know what was in its own terminals."},
   {"id": KSB, "codeName": "KSB", "discipline": "OSINT", "access": "Kordav State Broadcaster", "startingGrade": "D", "trueReliability": None, "controlledByAdversary": True, "postmortemNote": "Pointed at Rhun's office for the third time this year."},
   {"id": SOC, "codeName": "SOCIAL", "discipline": "OSINT", "access": "Forums and social media. Unvetted.", "startingGrade": "F", "trueReliability": 0.3, "controlledByAdversary": "partly", "postmortemNote": "Carried the press-pack page."},
   {"id": CPR, "codeName": "CPR", "discipline": "OSINT", "access": "Continental Policy Review, a journal of opinion", "startingGrade": "C", "trueReliability": 0.6, "controlledByAdversary": False, "postmortemNote": "Half right."},
   {"id": MER, "codeName": "MERIDIAN", "discipline": "SIGINT", "access": "Tasked coverage only.", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Reliable."},
   {"id": LAB, "codeName": "IPC LAB", "discipline": "Technical", "access": "Director Brandt's forensic team, on loan", "startingGrade": "B", "trueReliability": 0.95, "controlledByAdversary": False, "postmortemNote": "Reliable."},
   {"id": OS, "codeName": "OSINT cell", "discipline": "OSINT", "access": "", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""},
   {"id": WATCH, "codeName": "Test watch", "discipline": "Test", "access": "", "startingGrade": "B", "trueReliability": 1, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""},
   {"id": EVET, "codeName": "Elsin vetting", "discipline": "Liaison", "access": "", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""},
   {"id": ADM, "codeName": "Cell admin", "discipline": "Admin", "access": "", "startingGrade": "A", "trueReliability": 1, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""}],
 "reports": reports,
 "tellLabels": {"circular": "Circular reporting: the source traces back to the reporter", "nothing-secret": "Nothing in it is actually secret", "unverifiable": "Names nothing that could be checked", "too-on-message": "Says exactly what someone needs said"},
 "scoring": {"call": {"low": [1, -1], "medium": [2, -2], "high": [3, -4]}, "evidence": {"true": 1, "noise": 0, "clutter": -1, "planted": -2}, "challenge": {"true": -1, "noise": 0, "clutter": 0, "planted": 1}, "maxEvidence": 3},
 "endings": [
   {"id": "closed", "tone": "good", "title": "Closed", "points": 5, "if": {"assetAt": "shut", "everReply": "shut", "notEverAt": REMOVED, "flag": {"event": "plan", "in": ["safe"]}},
    "text": "The link goes dark. Kalsa's minister is furious for a week and then asks, privately, to see the lab report. Corvane's chairman flies to Kalsa again."},
   {"id": "closed-late", "tone": "good", "title": "Closed, after the plan went", "points": 3, "if": {"assetAt": "shut", "everReply": "shut", "notEverAt": REMOVED},
    "text": "The link goes dark, a day after the most useful thing it ever carried.",
    "changedBy": "Moving sensitive traffic to couriers (the link at Medium), or shutting the link, before 0900 on the 17th."},
   {"id": "closed-word", "tone": "warn", "title": "Closed, on your word", "points": 2, "if": {"assetAt": "shut", "notEverAt": REMOVED},
    "text": "The link goes dark. Kalsa's minister asks what it rests on, and is told: judgment. Elsin remembers that.",
    "changedBy": "A result to show Kalsa when the link was shut: a marked item that came out the other side, or the lab's look inside a terminal."},
   {"id": "closed-price", "tone": "warn", "title": "Closed, at a price", "points": 0, "if": {"assetAt": "shut"},
    "text": "The link goes dark, and Marlowe writes to Kalsa about the person she asked them to remove.",
    "changedBy": "Not removing anyone first. The test that separates a person from the road they sit on goes over the link to a desk that person never sees, or by hand to the person."},
   {"id": "wrong-name", "tone": "bad", "title": "The wrong name", "points": -5, "if": {"everAt": REMOVED},
    "text": "The removal goes ahead. The leaks go on.",
    "changedBy": "Testing the road separately from the person at the end of it, before anything that couldn't be undone."},
   {"id": "narrowed", "tone": "warn", "title": "Narrowed", "points": -2, "if": {"assetAt": "couriers"},
    "text": "The sensitive traffic is safe and the link stays up. Kordav keeps reading the rest.",
    "changedBy": "The same call at High, once a result was in hand."},
   {"id": "case-closed", "tone": "bad", "title": "Case closed", "points": -3, "if": {"assetAt": "noleak"},
    "text": "No leak, in writing. The leaks go on.",
    "changedBy": "Any marked item sent over the link: one that came out the other side means there is a leak."},
   {"id": "inquiry", "tone": "bad", "title": "An inquiry", "points": -3, "default": True,
    "text": "It sits for a year and decides nothing.",
    "changedBy": "A call she could act on."}],
 "dailyUpdates": [
   {"day": 1, "text": "Marlowe has opened a damage assessment. The alliance's traffic with Elsin goes on as usual while it runs."},
   {"day": 2, "text": "Elsin's minister has asked to be told before the alliance acts on the assessment."},
   {"day": 3, "text": "Halvorsen's revised Veyl contingency plan goes to Kalsa at 0900 tomorrow."},
   {"day": 4, "text": "", "byFlag": {"event": "plan", "texts": {"safe": "The Veyl contingency plan went to Kalsa at 0900, by courier.", "leaked": "The Veyl contingency plan went to Kalsa at 0900, over LATTICE."}}},
   {"day": 5, "text": "The assessment is due for signature today."}],
 "postmortem": {
   "script": [
     {"days": [1], "text": "The assessment laid out the first two leaks. Each time, what leaked had gone to Kalsa over LATTICE, and nothing that stayed in the cell ever did. Rhun offered to be tested."},
     {"days": [2], "text": "The terminals and the diagram: both ran through the link again. Kordav's broadcaster repeated its own January story, through an Elsin paper that had quoted it."},
     {"days": [3], "text": "Four years ago LATTICE's own terminals took the same 36-hour detour through Halsk as last autumn's. A forum offered a secret list that was a page from a press pack."},
     {"days": [4], "text": "The plan went to Kalsa, by courier or over the link. Kordav's broadcaster pointed at Rhun's office for the third time this year."},
     {"days": [5], "text": "Rhun asked for a transfer."}],
   "lessons": [
     "Test the road separately from the person at the end of it.",
     "A pattern with no motive is still a pattern.",
     "An ally's paper quoting your adversary's broadcaster is still your adversary's broadcaster.",
     "The suspect with the worst manner isn't, for that reason, the suspect.",
     "Before you act against an ally, have something you can show them."],
   "missedCollection": {
     "1": "A marked item over LATTICE to a desk Rhun never sees (Director Brandt's office): it would have come out the other side.",
     "2": "A marked item by hand to Rhun: it would never have surfaced.",
     "3": "The lab's look inside a LATTICE terminal.",
     "4": "The lab, if you hadn't asked yet. Tests sent today would arrive too late.",
     "5": "Nothing tasked today could arrive in time."},
   "callouts": [
     {"title": "Your tests already answered it", "if": {"allOf": [{"collected": "C-01"}, {"collected": "C-02"}]}, "text": "Same desk, two roads. The copy you sent Rhun by hand never surfaced; the copy you sent her over the link did. If she were passing things on, both would have leaked. What leaked was the road."},
     {"title": "Your test answered it", "if": {"allOf": [{"collected": "C-03"}]}, "text": "The copy you sent over the link to Director Brandt's office, a desk Rhun never sees, surfaced in Bureau traffic. No person sat on both ends of that road. Only the link did."}],
   "answer": "The leak was LATTICE. Its terminals were altered in Halsk four years ago, during a day and a half nobody asked about, and the Bureau has read everything that crossed the link since. Only what crossed the link ever leaked. Nothing that stayed in the cell ever did. Nobody betrayed anyone. A procurement officer signed for a late delivery without asking why it was late."},
 "pirs": [
   {"id": "PIR 1", "question": "Does a marked item reach Kordav, and by which road?", "targets": ["test-hand-rhun", "test-link-rhun", "test-link-ipc", "test-arle", "test-cell"]},
   {"id": "PIR 2", "question": "Who could be passing it on?", "targets": ["vetting-rhun", "marrow-travel"]},
   {"id": "PIR 3", "question": "Could the link itself be the problem?", "targets": ["delivery-history", "lab-terminal", "bureau-traffic"]}],
 "targets": [
   {"id": "test-hand-rhun", "name": "Test: by hand to Rhun's desk", "disciplines": ["Test"], "until": 3},
   {"id": "test-link-rhun", "name": "Test: over LATTICE to Rhun's desk", "disciplines": ["Test"], "until": 3, "closedWhen": "shut", "closedText": "The link was shut before the item went."},
   {"id": "test-link-ipc", "name": "Test: over LATTICE to Director Brandt's Infrastructure Protection Cell", "disciplines": ["Test"], "until": 3, "closedWhen": "shut", "closedText": "The link was shut before the item went."},
   {"id": "test-arle", "name": "Test: to Maj. Arle's distribution (stays on our side)", "disciplines": ["Test"], "until": 3},
   {"id": "test-cell", "name": "Test: kept inside your own cell", "disciplines": ["Test"], "until": 3},
   {"id": "vetting-rhun", "name": "Ask Elsin's vetting office about Col. Rhun", "disciplines": ["Liaison"], "until": 4, "fallback": "Elsin's vetting office has nothing to add."},
   {"id": "marrow-travel", "name": "Marrow's travel", "disciplines": ["OSINT"], "until": 4, "when": {"onTeam": "marrow"}},
   {"id": "delivery-history", "name": "LATTICE's delivery history", "disciplines": ["OSINT"], "until": 2},
   {"id": "lab-terminal", "name": "Have the lab open a LATTICE terminal", "disciplines": ["Technical"], "from": 3, "until": 4},
   {"id": "bureau-traffic", "name": "Bureau traffic about Kalsa", "disciplines": ["SIGINT"], "until": 4}],
 "collection": {"budget": 5, "costs": {"Test": 3, "Technical": 2, "SIGINT": 3, "OSINT": 1, "Liaison": 0}, "delays": {"Test": 2},
   "sources": {"Test": WATCH, "Technical": LAB, "SIGINT": MER, "OSINT": OS, "Liaison": EVET}, "fallback": "Nothing significant at {target}.",
   "note": "Liaison requests go to Kalsa over LATTICE, unless the link is shut. A test over LATTICE can't be sent once the link is shut, including on the day you shut it.",
   "burnRules": [], "burnPoints": -2},
 "collectionResults": [
   {"id": "C-01", "discipline": "Test", "target": "test-hand-rhun", "from": 1, "to": 3},
   {"id": "C-02", "discipline": "Test", "target": "test-link-rhun", "from": 1, "to": 3},
   {"id": "C-03", "discipline": "Test", "target": "test-link-ipc", "from": 1, "to": 3},
   {"id": "C-04", "discipline": "Test", "target": "test-arle", "from": 1, "to": 3},
   {"id": "C-05", "discipline": "Test", "target": "test-cell", "from": 1, "to": 3},
   {"id": "C-06", "discipline": "Technical", "target": "lab-terminal", "from": 3, "to": 4},
   {"id": "C-07", "discipline": "OSINT", "target": "marrow-travel", "from": 1, "to": 4},
   {"id": "C-08", "discipline": "OSINT", "target": "delivery-history", "from": 1, "to": 2},
   {"id": "C-09", "discipline": "SIGINT", "target": "bureau-traffic", "from": 1, "to": 4, "when": {"notAssetAt": LINK_STATES}},
   {"id": "C-09Q", "discipline": "SIGINT", "target": "bureau-traffic", "from": 1, "to": 4, "when": {"assetAt": LINK_STATES}},
   {"id": "C-10", "discipline": "Liaison", "target": "vetting-rhun", "from": 1, "to": 4, "then": {"id": "C-10K", "after": 1, "when": {"notAssetAt": "shut"}}}],
 "credibility": {"start": 3, "min": 0, "max": 5, "bonusAt": 5,
   "levels": [
     {"id": "trusted", "label": "Trusted", "min": 3, "text": "She acts on your confidence as given, with your full collection budget."},
     {"id": "questioned", "label": "Questioned", "min": 2, "budgetDelta": -1, "text": "Her office trims your collection: 1 point less a day."},
     {"id": "discounted", "label": "Discounted", "min": 0, "budgetDelta": -2, "caution": 1, "text": "2 points less a day, and she treats your confidence as one step lower: High gets the Medium step."}],
   "triggers": [
     {"id": "nothing-to-show", "on": "reply", "reply": ["shut_bare", "remove_rhun_bare", "remove_arle_bare"], "delta": -1, "rule": "She takes a step that can't be undone with nothing to show Kalsa yet", "note": "Credibility −1. \"Kalsa asked what it rests on. I said your judgment.\""},
     {"id": "apology", "on": "reply", "reply": "shut_apology", "delta": -2, "rule": "She has to apologise to Kalsa for a removal she made on your word", "note": "Credibility −2. She wrote to Kalsa about the person she asked them to remove."},
     {"id": "reopened", "on": "leave", "state": ["noleak"], "delta": -1, "rule": "She has to reopen an assessment she closed", "note": "Credibility −1. \"I closed this in writing. Now I'm reopening it in writing.\""},
     {"id": "hedging", "on": "streak", "confidence": "low", "days": 2, "delta": -1, "rule": "Low confidence two days running (each further Low day too)", "note": "Credibility −1. \"That's a shrug again.\""}],
   "outcome": {"closed": 1, "closed-late": 1, "closed-word": 0, "closed-price": 0, "wrong-name": -1, "narrowed": 0, "case-closed": 0, "inquiry": 0},
   "summary": "Marlowe can see whether she had something to show Kalsa when she acted, whether she had to take anything back, and whether you'd commit. She can't see whether you're right."},
 "board": {"pinsPerDay": 3},
 "record": {"grades": []},
 "story": {
   "values": [
     {"value": "alliance", "delta": -1, "if": {"ending": ["closed", "closed-late", "closed-price"]}},
     {"value": "alliance", "delta": -2, "if": {"ending": "closed-word"}},
     {"value": "alliance", "delta": -1, "if": {"everAt": "remove-rhun"}},
     {"value": "alliance", "delta": -1, "if": {"collected": "C-10"}},
     {"value": "pressure", "delta": 1, "if": {"ending": ["wrong-name", "narrowed", "case-closed", "inquiry"]}},
     {"value": "pressure", "delta": 1, "if": {"flag": {"event": "plan", "in": ["leaked"]}}}],
   "flags": [
     {"flag": "leak", "value": "closed", "if": {"ending": ["closed", "closed-late", "closed-word", "closed-price"]}},
     {"flag": "leak", "value": "open", "if": {"ending": ["wrong-name", "narrowed", "case-closed", "inquiry"]}},
     {"flag": "named", "value": "link", "if": {"ending": ["closed", "closed-late", "closed-word", "closed-price"]}},
     {"flag": "wrongName", "value": "rhun", "if": {"everAt": "remove-rhun"}},
     {"flag": "wrongName", "value": "arle", "if": {"everAt": "remove-arle"}},
     {"flag": "marrowLost", "value": "yes", "if": {"everAt": "remove-arle"}}],
   "caseFile": [
     {"tag": "link-test", "text": "A marked item sent over the link to a desk Rhun never sees turned up in Bureau traffic.", "if": {"collected": "C-03"}},
     {"tag": "hand-test", "text": "A marked item sent by hand to Rhun never turned up.", "if": {"collected": "C-01"}},
     {"tag": "component", "text": "The lab found a component inside a LATTICE terminal that isn't on Corvane's build list.", "if": {"collected": "C-06"}},
     {"tag": "vetting-heard", "text": "Your request about Rhun was on Kordav's television the next day.", "if": {"collected": "C-10K"}}]},
 "analysts": [
   {"id": "vasko", "name": "Imre Vasko", "specialty": "Regional analyst", "reveal": "Anchors on his first theory. The mole hunter, sincerely: right once, about Arle."},
   {"id": "halden", "name": "Noor Halden", "specialty": "Technical analyst (signals, imagery, forensics)", "reveal": "Slow but careful. Never wrong. Each note pointed at the test or tasking that settled it, a day after you could first have asked."},
   {"id": "marrow", "name": "Tess Marrow", "specialty": "Open-source analyst", "extra": True, "reveal": "Under suspicion herself, and right every time, including about herself."}],
}
def NOTE(a, item, text, right, why, after=0): return {"analyst": a, "item": item, "after": after, "text": text, "right": right, "why": why}
crisis["notes"] = [
 NOTE("vasko", "R-1-04", "She would say that. A professional leaks around a test, not through it.", 0, "She volunteered because she had nothing to hide."),
 NOTE("marrow", "R-1-05", "Predictable? We are. Predictable doesn't tell you which net to stage a call on.", 1, "Exactly the flaw in the no-leak case."),
 NOTE("halden", "R-1-01", "Both leaks in parts one and two travelled the same road to Kalsa. I'd like to know whether it's the person at the end of that road, or the road.", 1, "The question the scenario turns on.", 1),
 NOTE("marrow", "R-2-02", "It was my mother's funeral, and the form was late. Test me if you like. I'd test me.", 1, "It was, and a test of the cell stays silent."),
 NOTE("vasko", "R-2-03", "Even Kordav's own television says it's a colonel.", 0, "Kordav's television quoting itself."),
 NOTE("halden", "R-2-04", "Five paper copies and one electronic one. Only one of those six is a channel rather than a person.", 1, "The electronic one.", 1),
 NOTE("vasko", "R-3-02", "Arle's lists were a disgrace. A sloppy man isn't a spy.", 1, "Right, for once."),
 NOTE("marrow", "R-3-04", "That's a careful sentence. She isn't saying what went over the link.", 1, "She wasn't, and it was the point."),
 NOTE("halden", "R-3-01", "Thirty-six hours in Halsk, four years ago, for a box of terminals. I'd open one.", 1, "The lab did, and found it.", 1),
 NOTE("halden", "R-1-07", "Thirty-six hours in Halsk, four years ago, for a box of terminals. I'd open one.", 1, "The lab did, and found it.", 1),
 NOTE("vasko", "R-4-03", "There. They can't resist boasting.", 0, "A boast that names nothing."),
 NOTE("marrow", "R-4-03", "That's the third time this year Kordav's television has pointed at the same office. They do like that office.", 1, "They liked it because it wasn't the problem."),
 NOTE("vasko", "R-5-02", "A transfer request, before the decision. Interesting.", 0, "A career that was over either way.")]

crisis["ledger"] = {
 "title": "The assessment so far", "sub": "What leaked, and the road it took. Fills in as the parts arrive.",
 "rows": [
  {"after": "R-1-01", "tag": "01", "what": "That we read 12th Brigade's net", "road": "In the daily assessment, over LATTICE", "leaked": "reached Kordav", "yes": True},
  {"after": "R-1-01", "tag": "01", "what": "KESTREL's identity", "road": "Never left the cell", "leaked": "didn't leak"},
  {"after": "R-1-02", "tag": "02", "what": "That we read the Bureau's admin net", "road": "In a product sent over LATTICE", "leaked": "reached Kordav", "yes": True},
  {"after": "R-1-02", "tag": "02", "what": "FINCH", "road": "Never left the cell", "leaked": "found another way (the ministry was watched)"},
  {"after": "R-1-03", "tag": "03", "what": "Where the guard company was", "road": "Through Elsin's Southern Command", "leaked": "reached Marrat (explained)", "yes": True},
  {"after": "R-1-10", "tag": "04", "what": "Your port-police request", "road": "Through Kalsa, over LATTICE", "leaked": "reached Tessaly", "yes": True},
  {"after": "R-2-04", "tag": "05", "what": "The network diagram, issue 7", "road": "Five paper copies, one electronic copy over LATTICE", "leaked": "reached the attackers: which copy not known", "yes": True,
   "leakedBy": [{"after": ["R-1-08", "R-4-02"], "text": "reached the attackers: the electronic copy"}]},
  {"after": "R-1-09", "tag": "05", "what": "Your request to the registry", "road": "Over LATTICE", "leaked": "on Kordav's television next day", "yes": True},
  {"after": "C-10K", "tag": "06", "what": "Your request to vet Rhun", "road": "Over LATTICE", "leaked": "on Kordav's television next day", "yes": True}],
 "testsTitle": "Your tests",
 "tests": {"test-hand-rhun": {"road": "By hand", "desk": "Rhun's desk"}, "test-link-rhun": {"road": "Over LATTICE", "desk": "Rhun's desk"},
           "test-link-ipc": {"road": "Over LATTICE", "desk": "Brandt's office"}, "test-arle": {"road": "Our side only", "desk": "Arle's distribution"},
           "test-cell": {"road": "Inside the cell", "desk": "your cell"}},
 "results": {"C-01": "silent", "C-02": "surfaced", "C-03": "surfaced", "C-04": "silent", "C-05": "silent"}}
# ---------- sanity ----------
ids = {r["id"] for r in reports}
assert len(ids) == len(reports)
assert all(cr["id"] in ids for cr in crisis["collectionResults"]) and all(n["item"] in ids for n in crisis["notes"]) and "C-10K" in ids
assert all(i in ids for r in reports if r.get("reveal") for i in r["reveal"]["crossCheck"]["ids"]) and all(r.get("reveal") for r in reports if r["kind"] == "planted")
tids = {t["id"] for t in crisis["targets"]}
assert tids == {t for p in crisis["pirs"] for t in p["targets"]} and all(cr["target"] in tids for cr in crisis["collectionResults"])
keys = {r["reply"] for r in policy} | {"frozen"}
assert keys <= set(replies) and keys <= set(labels)
assert all(to in levels for to in [r.get("to") for r in policy if r.get("to")])
import house_text; house_text.apply(crisis)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "crises", "damage-assessment.json")
with open(out, "w") as f: json.dump(crisis, f, indent=2, ensure_ascii=False); f.write("\n")
print("wrote", os.path.normpath(out), len(reports), "reports")
