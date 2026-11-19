#!/usr/bin/env python3
"""Builds crises/southern-line.json (Crisis 03). Content lives here so the long text stays readable; the engine only reads the JSON."""
import json, os
def R(id, day, src, disc, grade, cred, text, kind, note, tells=(), reveal=None, via=False, diagnostic=False, when=None, tag=None):
    r = {"id": id, "day": day, "sourceId": src, "discipline": disc, "sourceGrade": grade, "credibility": cred, "text": text, "kind": kind,
         "supports": [], "contradicts": [], "tells": list(tells), "postmortemNote": note}
    if reveal: r["reveal"] = {"tell": reveal[0], "crossCheck": {"ids": reveal[1], "text": reveal[2]}, "motive": reveal[3]}
    if via: r["via"] = "collection"
    if diagnostic: r["diagnostic"] = True
    if when: r["when"] = when
    if tag: r["callbackTag"] = tag
    return r
WR, ESC, ROOK, MAG, KES, FIN, MER, CIR, MNA, FR, CWS, SOC, OS, ADM = ("S-WREN", "S-ESC", "S-ROOK", "S-MAGPIE", "S-KESTREL", "S-FINCH", "S-MERIDIAN", "S-CIRRANE", "S-MNA", "S-FRONT", "S-CWS", "S-SOCIAL", "S-OSINT", "S-ADMIN")
NEW_TRICK = {"notFooled": ["recycled-photo", "staged-signals"]}
OLD_PHOTO = {"fooled": "recycled-photo", "notFooled": ["staged-signals"]}
OLD_SIGNALS = {"fooled": "staged-signals"}
CAUGHT = {"flag": {"event": "tolen", "in": ["caught"]}}
NOT_CAUGHT = {"flagNot": {"event": "tolen", "in": ["caught"]}}

reports = [
 # ---------- Day 1 ----------
 R("R-1-01", 1, ESC, "Liaison", "B", 2, "Valve housing 22, Sarn valley: a small charge, placed by someone who knew which housing to pick. Flow was restored in nine hours. No sign of military explosive: it was a quarrying charge of the kind sold up and down the valley. Marrat's advisers have offered forensic help.", "true",
   "A cheap local charge and a nine-hour repair: an attack designed to be noticed. It also contradicts any talk of special forces instructors."),
 R("R-1-02", 1, WR, "Liaison", "C", 3, "Elsin's service says Marrat's intelligence officers have met Commander Oro twice this month and are paying the Front. No sourcing is given. WREN adds that Southern Command \"should never have let Marrat's advisers through the door.\"", "true",
   "The genuine item that looks like noise. It has the same surface as WREN's alarm over Tarsk: no sourcing, and an axe to grind. The difference is that this time there was sourcing to be had. Asking for it was free."),
 R("R-1-03", 1, FR, "OSINT", "E", 3, "Communiqué, signed by Commander Davin Oro: the Front claims the valve \"for the fields taken for the compressor station, and for every promise made since.\" It says: \"We answer to the valley.\"", "true",
   "Oro means every word. It's what he believes, even while he takes Marrat's money."),
 R("R-1-04", 1, MNA, "OSINT", "D", 2, "Marrat News Agency, citing \"security sources\": Kordavan special forces instructors have been in the Sarn valley since the winter.", "planted",
   "The start of the Kordav story.", tells=["no-detail", "only-one-chain"],
   reveal=("Unnamed \"security sources,\" no place, no number and no date, from the state outlet of the country offering to sell Elsin the cure.",
           ["R-1-01"], "The charge was a quarrying charge sold up and down the valley, placed by someone who knew the housing (R-1-01). Special forces instructors don't teach that.",
           "Start the Kordav story on Day 1, before anyone has looked.")),
 R("R-1-05", 1, ADM, "Admin", "A", 1, "The Southern Line outage did not affect task force fuel. The canteen's gas range is a separate fault and is being investigated with less urgency.", "clutter", "The canteen."),
 # ---------- Day 2 ----------
 R("R-2-01", 2, ESC, "Liaison", "B", 2, "A second forensic sweep at valve housing 22, assisted by Marrat's advisers, recovered a detonator fragment with Kordavan factory markings. The first sweep, by Elsin's own engineers, found none.", "planted",
   "Southern Command reported the find accurately. The fragment was the plant.", tells=["found-by-beneficiary"],
   reveal=("Elsin's engineers swept the site and found nothing. The fragment appeared on a second sweep, in the hands of the advisers whose government benefits.",
           ["R-1-01", "C-07"], "The first report describes a quarrying charge (R-1-01). The lot number, for one point, traces to a batch Kordav sold to Marrat's mining ministry (C-07).",
           "Physical evidence outranks talk. Southern Command reported it honestly, which is why it arrived graded B.")),
 R("R-2-02", 2, ROOK, "Liaison", "D", 3, "Marrat's liaison officer shares a transcript of what he says is an intercepted call: a Kordavan officer tells \"our valley friends\" to \"take the river crossing next.\" Translated text only. No date, no audio.", "planted",
   "False about who, true about where.", tells=["no-raw-material", "knows-too-much"],
   reveal=("Translated text only, with no date and no audio. And it names the next target. How would Marrat's liaison officer know what the Front will hit next?",
           ["R-1-04", "R-2-01"], "Three items in two days point at Kordav (R-1-04, R-2-01 and this one), and all three came through Marrat's hands. If you tasked Kordav's own nets (C-08), they were talking about a fuel spur at Varn.",
           "To have Kordav blamed in advance for an attack Marrat had already scheduled. The target it names was real, which was the most useful thing in it.")),
 R("R-2-03", 2, CWS, "OSINT", "B", 1, "At the talks, Marrat offers border guard units to protect the Southern Line \"at no cost for the first year.\" Elsin's opposition calls it \"an occupation with the invoice to follow.\"", "true",
   "Motive, stated in public."),
 R("R-2-04", 2, SOC, "OSINT", "F", 3, "Valley residents post about the Front's new pickup trucks: \"the boys never had money for those before.\"", "true",
   "Someone is paying. It rules against the Front acting alone, and can't say who."),
 R("R-2-05", 2, ADM, "Admin", "A", 1, "Kalsa's hotels are full for the talks. The task force's visiting auditors are in a hostel and have asked that this be recorded.", "clutter", "The auditors."),
 # ---------- Day 3 ----------
 R("R-3-01", 3, ESC, "Liaison", "B", 2, "Marrat's advisers asked to inspect the guard post at Tolen bridge \"for the pact survey,\" spent an hour there, and have left for the holiday. The post is six border police.", "true",
   "A reconnaissance of the target by the people who chose it, and an alibi for the night."),
 R("R-3-02", 3, WR, "Liaison", "C", 3, "\"Our people say something is planned in the south within two days. We asked Southern Command to reinforce Tolen. They say Marrat's advisers think it unnecessary.\"", "true",
   "WREN was right again, and gave the timing."),
 R("R-3-03", 3, SOC, "OSINT", "F", 3, "An account called \"Valley Truth\" posts a photo of a payment order on Kordav 4th Army letterhead, made out to \"Sarn auxiliaries.\" The sum is in Marrat crowns.", "planted",
   "A forged payment order.", tells=["wrong-currency"], when=NEW_TRICK, tag="forged-document",
   reveal=("A Kordavan army order that pays in Marrat crowns.",
           ["C-02", "C-17"], "MAGPIE says the Front is paid in new Marrat crowns by \"a cousin from across the river\" (C-02). The account is ten days old and its first followers work for Marrat's news agency (C-17).",
           "One more push before the raid. It was a new trick: nothing on your record told Marrat that an old one would work on you.")),
 R("R-3-03P", 3, SOC, "OSINT", "F", 3, "An account called \"Valley Truth\" posts a photo captioned \"Kordavan instructors in the Sarn valley.\" Six men in 4th Army field uniform stand beside a truck. A water tower is visible behind them.", "planted",
   "A photo from somewhere else.", tells=["recycled-media"], when=OLD_PHOTO, tag="recycled-photo",
   reveal=("The water tower. It stands at the Ostrel training area, 300 km away in Kordav: this is a press photo from IRON HARVEST.",
           ["C-17", "C-10"], "The account is ten days old and its first followers work for Marrat's news agency (C-17). Kordav's southern crossings show no military traffic at all (C-10).",
           "They tried this because it worked on you last time: you cited an old photo as evidence in Crisis 01. The other side keeps notes too.")),
 R("R-3-04", 3, FR, "OSINT", "E", 3, "Communiqué: \"The valley will be heard before any pact is signed.\"", "true", "Timing: before the signing."),
 R("R-3-05", 3, ADM, "Admin", "A", 1, "Because of the holiday in Marrat, the border market at Tolen is closed tomorrow. The welfare trip is cancelled. Refunds will take the usual six weeks.", "clutter", "The market. The holiday mattered; the refund didn't."),
 # ---------- Day 4 ----------
 R("R-4-01", 4, CWS, "OSINT", "B", 1, "Elsin's government says it will sign the security pact with Marrat on the 20th. A minister says last night \"settled the argument.\"", "true",
   "The public result of the night.", when=NOT_CAUGHT),
 R("R-4-01C", 4, CWS, "OSINT", "B", 1, "Elsin has postponed the pact talks after \"equipment of foreign military origin\" was recovered at Tolen. Marrat says the radios were stolen from a depot last year.", "true",
   "The public result of the night.", when=CAUGHT),
 R("R-4-02", 4, FR, "OSINT", "E", 3, "Communiqué, signed by Oro: \"We did not bleed for the valley to hand it to Marrat's border guards in place of the capital's engineers. The compressor that took our fields still stands.\"", "true",
   "The break, in Oro's own words, and the next target named."),
 R("R-4-03", 4, ROOK, "Liaison", "D", 3, "Marrat \"regrets the violence, has no contact with any armed group, and urges calm on all sides.\"", "noise",
   "A denial. False about last week, true about today, and no use either way."),
 R("R-4-04", 4, WR, "Liaison", "C", 3, "\"Marrat is still running them, and last night proves it. Expect a second attempt at Tolen.\"", "noise",
   "WREN had stopped looking. It was right for three days and assumed it still was.", tells=["agenda-aligned"]),
 R("R-4-05", 4, ADM, "Admin", "A", 1, "The canteen's gas range has been fixed. It was the regulator.", "clutter", "The regulator."),
 # ---------- Day 5 ----------
 R("R-5-01", 5, ROOK, "Liaison", "D", 3, "Marrat's liaison officer warns Southern Command that \"the Oro faction\" will attack the Sarn compressor station at dawn tomorrow, coming up the quarry road. He repeats that Marrat's guards could be there by nightfall.", "true",
   "True, from the adversary. Marrat knew Oro's plans because it trained his people, and it warned Elsin because a rogue militia sells the pact better than a tame one. The motive was self-serving and the content was right. Those are separate questions."),
 R("R-5-02", 5, FR, "OSINT", "E", 3, "Statement from \"the Front's political office\": the Front \"has suspended operations pending the outcome of talks.\"", "planted",
   "One quiet night was all they needed.", tells=["unsigned", "new-voice"],
   reveal=("The Front has never had a \"political office,\" and every earlier statement was signed by Oro.",
           ["R-4-02", "R-5-04"], "Yesterday Oro said the compressor still stands (R-4-02). Last night strangers photographed the quarry road gate (R-5-04). If you tasked imagery of the valley, eight vehicles were in the quarry (C-16).",
           "Oro's people planted it. One quiet night was all they needed.")),
 R("R-5-03", 5, WR, "Liaison", "C", 3, "\"ROOK's warning is a trick to get Marrat's guards into the valley. Ignore it.\"", "noise",
   "WREN, wrong, for the same reason it was right on Day 1.", tells=["agenda-aligned"]),
 R("R-5-04", 5, ESC, "Liaison", "B", 2, "The night shift at the Sarn compressor station reports strangers photographing the quarry road gate yesterday evening.", "true",
   "Oro's people looking over their route."),
 R("R-5-05", 5, ADM, "Admin", "A", 1, "The auditors have left. Their report notes that the hostel was \"adequate.\"", "clutter", "Adequate."),
 # ---------- Collection results ----------
 R("C-01", None, WR, "Liaison", "C", 2, "WREN sends a border police surveillance log: two meetings between Oro and three men at a roadside café near Tolen, on dated evenings this month. The men arrived in a car with Marrat diplomatic plates. Photographs attached.", "true",
   "What turned WREN's claim into evidence. It cost nothing to ask.", via=True, diagnostic=True),
 R("C-02", None, MAG, "HUMINT", "C", 2, "MAGPIE: the Front has started paying for fuel in new Marrat crown notes, in sequence. \"A cousin from across the river\" handles their money now.", "true",
   "Marrat's money, in sequence.", via=True, diagnostic=True),
 R("C-03", None, MAG, "HUMINT", "C", 2, "MAGPIE: the Front bought 400 litres of diesel this morning and paid in crowns. The driver said they are \"going south tonight or tomorrow.\"", "true",
   "Timing and direction: south, tonight or tomorrow.", via=True),
 R("C-04", None, MAG, "HUMINT", "C", 2, "MAGPIE: the cousin from across the river is gone. The fighters say they haven't been paid, and that Oro smashed the new handset on the yard wall. The talk at the pumps is all about the compressor.", "true",
   "The money stopped and Oro broke the handset. The break.", via=True, diagnostic=True),
 R("C-18", None, MER, "SIGINT", "B", 2, "The Front's radios: encrypted traffic on new handsets, as on other days. One call was made in the clear, in Kordavan-accented speech: \"Tell the valley friends. Kessa next.\"", "planted",
   "Staged for MERIDIAN, again.", tells=["out-of-pattern", "too-on-message"], via=True, when=OLD_SIGNALS, tag="staged-signals",
   reveal=("Every other Front call that week was encrypted. The one call in the clear names a target in a foreign accent.",
           ["R-3-01", "R-3-02"], "Marrat's advisers had just looked over Tolen, not Kessa (R-3-01), and WREN's people expected something in the south (R-3-02). If you tasked the Tolen approaches, the raiding party was already there (C-12).",
           "They tried this because it worked on you last time: you cited a staged message as evidence. The other side keeps notes too.")),
 R("C-05", None, MER, "SIGINT", "B", 2, "The Front has moved onto encrypted handsets of a model issued to Marrat's border guard. Traffic rises every evening.", "true",
   "Marrat's kit.", via=True),
 R("C-06", None, MER, "SIGINT", "B", 2, "The encrypted handsets have been silent since last night. The Front is back on open citizens'-band sets. Words heard: \"quarry,\" \"before the signing.\"", "true",
   "The break, and the target.", via=True),
 R("C-07", None, OS, "OSINT", "B", 1, "Trade registry: the lot number on the fragment belongs to a batch that Kordav's state factory exported to Marrat's mining ministry six years ago.", "true",
   "The fragment was Kordav-made and Marrat-owned. One point.", via=True),
 R("C-08", None, MER, "SIGINT", "B", 2, "Two 4th Army staff officers discuss \"the southern pipeline problem\" and what \"our friends in the valley\" will charge to fix \"the Varn spur.\"", "noise",
   "The tidy item that was nothing. B-graded, on topic, and about Kordav's own fuel spur at Varn and what the contractors would charge. Varn is KESTREL's depot, 300 km inside Kordav.", via=True),
 R("C-09", None, KES, "HUMINT", "B", 2, "KESTREL: no unusual issues from the depot and nothing drawn for special units. Half the staff are on leave. They are laughing about being blamed for a pipeline in someone else's country.", "true",
   "Kordav cleared from the depot floor. You had him because you didn't burn him.", via=True),
 R("C-10", None, CIR, "IMINT", "B", 2, "Kordav's southern border crossings: normal civilian traffic at both. No military vehicles south of the garrison line.", "true",
   "The weaker way to clear Kordav.", via=True),
 R("C-11", None, FIN, "HUMINT", "B", 2, "FINCH: the ministry is drafting a protest note to Elsin about the detonator story. Nobody there had heard of the Sarn Valley Front before last week.", "true",
   "Kordav cleared from the ministry. You had him because you didn't burn him.", via=True),
 R("C-12", None, CIR, "IMINT", "B", 2, "Tolen bridge approaches: two pickup trucks under camouflage nets in an orchard 4 km south of the bridge. A boat is drawn up on the Marrat bank.", "true",
   "The raiding party, waiting.", via=True),
 R("C-13", None, CIR, "IMINT", "B", 2, "Night passes show pickup trucks fording from the Marrat side at an unofficial ford 6 km from Tolen, and returning before dawn.", "true",
   "The supply route from Marrat.", via=True),
 R("C-14", None, CIR, "IMINT", "B", 2, "The ford: no crossings for two nights. The track down to it hasn't been used.", "true",
   "The route went dead: the break.", via=True),
 R("C-15", None, CIR, "IMINT", "B", 2, "The Front's camp at the upper farm: about 40 fighters and six vehicles, four of them new.", "true",
   "More fighters and newer vehicles than a valley could pay for.", via=True),
 R("C-16", None, CIR, "IMINT", "B", 1, "The camp at the upper farm is empty. Eight vehicles are parked in the disused quarry, 3 km from the compressor station.", "true",
   "The column at the quarry: where the last attack would come from.", via=True, diagnostic=True),
 R("C-17", None, OS, "OSINT", "B", 1, "The \"Valley Truth\" account was created ten days ago. It writes Elsin's language with Marrat spellings. Its first followers were Marrat News Agency staff accounts.", "true",
   "Marrat's account.", via=True),
]

SITES = {"tolen": ("Tolen bridge", "H3"), "kessa": ("the Kessa pumping station", "H2"), "sarn": ("the Sarn compressor station", "H1")}
policy, replies, labels, levels = [], {}, {}, {"home": {"label": "in reserve", "rank": 0}}
for sid, (sname, hyp) in SITES.items():
    levels[sid + "_p"] = {"label": "one platoon at " + sname, "rank": 1}
    levels[sid + "_c"] = {"label": "at " + sname + " in full", "rank": 2}
    policy += [
      {"if": {"hypothesis": hyp, "confidence": ["high"], "assetAt": sid + "_c"}, "reply": "already"},
      {"if": {"hypothesis": hyp, "confidence": ["high"]}, "to": sid + "_c", "reply": "company_" + sid},
      {"if": {"hypothesis": hyp, "confidence": ["medium"], "assetAt": [sid + "_p", sid + "_c"]}, "reply": "already"},
      {"if": {"hypothesis": hyp, "confidence": ["medium"]}, "to": sid + "_p", "reply": "platoon_" + sid}]
    replies["company_" + sid] = "The company's going to " + sname + ". Southern Command will know by lunchtime, and so will everyone who drinks coffee there."
    replies["platoon_" + sid] = "One platoon to " + sname + ", quietly. Nobody at Southern Command needs to know why. If you want the company there, give me more than medium."
    labels["company_" + sid] = "Moves the full guard company to " + sname
    labels["platoon_" + sid] = "Sends one platoon to " + sname + ", quietly"
policy.append({"if": {}, "reply": "listen"})
replies.update({"already": "They're already there. Keep building the picture.", "listen": "Noted. The company stays where it is.",
  "tolen_caught": "Seven prisoners and a box of radios nobody in that valley could afford. Good.",
  "tolen_displaced": "They went round us. I'd like to know who told them where we were.",
  "tolen_held": "A platoon holds a bridge. It doesn't take prisoners.",
  "tolen_cut_far": "I guarded the wrong end of the country.",
  "tolen_cut": "Flow stops for four days. The pact talks won't."})
labels.update({"already": "Nothing new. The force is already there", "listen": "Changes nothing", "tolen_caught": "Caught the raid at Tolen", "tolen_displaced": "Was at Tolen; the raid went elsewhere",
  "tolen_held": "Platoon drove off the raid at Tolen", "tolen_cut_far": "Was at Kessa when Tolen was cut", "tolen_cut": "Had nothing at Tolen when it was cut"})

crisis = {
 "id": "southern-line", "formatVersion": "1.1", "title": "The Southern Line", "crisisNumber": "03", "days": 5,
 "dayLabels": ["the 14th", "the 15th", "the 16th", "the 17th", "the 18th"],
 "placeholderNote": "Kordav, Elsin and Marrat are fictional countries. All leaders, groups, units and outlets are fictional.",
 "adversary": "Marrat", "endingEyebrow": "Dawn, the 19th",
 "briefing": {"dateLine": "Day 1 is the 14th, the following spring.", "situation": [
   "Your cell is back with Gen. R. Halvorsen and Task Force VEYL.",
   "The Southern Line is Elsin's gas pipeline. It runs from the Kessa pumping station in the north, through the Sarn valley, to the Tolen bridge on the border with Marrat, Elsin's southern neighbour. The task force buys its fuel off the same network.",
   "Three nights ago a small explosion damaged a valve housing in the Sarn valley. A local militia, the Sarn Valley Front, has claimed it. Its commander is Davin Oro, a farmer whose land was taken for the Sarn compressor station.",
   "This week Elsin and Marrat open talks on a pipeline security pact. Marrat is offering its border guards to protect the line, and already has \"advisers\" at Elsin's Southern Command.",
   "Public reporting, and whatever Elsin's services, Marrat's liaison officer and the Front choose to say, reach you every day. Everything else you task."]},
 "customer": {"name": "Gen. R. Halvorsen", "short": "Halvorsen", "pronouns": ["he", "his"], "role": "Commander, Task Force VEYL", "callsign": "CDR TF VEYL",
   "wants": "Who is behind the Front, and so where does he put the guard company? He has one, and it can only be in one place.",
   "context": "He reasons from who to where. If the Front is acting alone, he expects it to hit the Sarn compressor station, the thing it resents. If Kordav is behind it, the Kessa pumping station, which feeds the task force. If Marrat, the Tolen bridge, where a cut is spectacular, easy to repair and right beside the guards Marrat wants to sell.",
   "tipLine": "High moves the whole company to the site that goes with your hypothesis. Medium sends one platoon there, quietly. Low changes nothing."},
 "opening": {"text": "One company, three places it might be needed, and a liaison officer from Marrat who keeps offering to help. Tell me whose militia this is.",
   "byTone": {"good": "Last time you were right when it was hard to be. Don't make me regret remembering that.",
              "warn": "Last time you got there, and you got there late. I need you earlier.",
              "bad": "I lost a dam on your reading. I'm told you've improved. Show me."}},
 "asset": {"id": "guard", "name": "Guard company", "levels": levels},
 "customerPolicy": policy,
 "policySummary": [
   {"brief": "H1 (acting alone)", "action": "He guards the Sarn compressor station"},
   {"brief": "H2 (Kordav's proxy)", "action": "He guards the Kessa pumping station"},
   {"brief": "H3 (Marrat's proxy)", "action": "He guards the Tolen bridge"},
   {"brief": "…at High", "action": "The full company goes there. Southern Command will know, and Marrat has advisers at Southern Command."},
   {"brief": "…at Medium", "action": "One platoon goes there, quietly. If the company was out somewhere else, the rest returns to reserve."},
   {"brief": "…at Low", "action": "Nothing changes"}],
 "policyNote": "A platoon is discreet. A company is not.",
 "replies": replies, "replyLabels": labels,
 "events": [{"id": "tolen", "atStartOfDay": 4, "pointsLabel": "the night at Tolen", "outcomes": [
   {"if": {"assetAt": "tolen_c", "since": [3]}, "flag": "caught", "points": 4, "title": "Caught", "replyId": "tolen_caught",
    "note": "The Front's raiding party crossed at 0340 and walked into the company. Seven fighters were captured, with encrypted radios of a military pattern. The bridge is untouched."},
   {"if": {"assetAt": "tolen_c"}, "flag": "displaced", "points": -2, "title": "Displaced", "replyId": "tolen_displaced",
    "note": "Nothing came to Tolen. At 0410 the valve yard at Dessa, forty kilometres north, was blown instead. Someone knew the company was at the bridge."},
   {"if": {"assetAt": "tolen_p"}, "flag": "held", "points": 1, "title": "Driven off", "replyId": "tolen_held",
    "note": "The platoon drove the raiders off after a short fight. One pier is scorched and the line is intact. Nobody was captured."},
   {"if": {"assetAt": "kessa_c"}, "flag": "cut_far", "points": -3, "title": "Cut", "replyId": "tolen_cut_far",
    "note": "Tolen bridge was cut at 0345. The company was three hundred kilometres away."},
   {"if": {}, "flag": "cut", "points": -3, "title": "Cut", "replyId": "tolen_cut",
    "note": "Tolen bridge was cut at 0345. The six border police were not harmed, and were not much help."}]}],
 "epilogue": {"event": "tolen", "texts": {
   "caught": "The pact is dead. Elsin sends Marrat's advisers home with their radios.",
   "held": "Elsin signs a thinner pact in the autumn. Marrat's guards get the southern third of the line.",
   "displaced": "Elsin signs a thinner pact in the autumn. Marrat's guards get the southern third of the line.",
   "cut": "Elsin signs on the 20th. Marrat's guards are on the line within the month, protecting it from a militia Marrat built.",
   "cut_far": "Elsin signs on the 20th. Marrat's guards are on the line within the month, protecting it from a militia Marrat built."}},
 "hypotheses": [
   {"id": "H1", "short": "Acting alone", "text": "The Front is a local militia with a local grievance. Nobody is running it.", "claim": "the Sarn Valley Front is acting alone"},
   {"id": "H2", "short": "Kordav's proxy", "text": "Kordav is paying and directing the Front to hurt Elsin and the task force.", "claim": "Kordav is paying and directing the Sarn Valley Front"},
   {"id": "H3", "short": "Marrat's proxy", "text": "Marrat is paying and directing the Front to frighten Elsin into the pact.", "claim": "Marrat is paying and directing the Sarn Valley Front"}],
 "sources": [
   {"id": WR, "codeName": "WREN", "discipline": "Liaison", "access": "Elsin's military intelligence. Pushes what it wants us to see, and answers requests. It distrusts Marrat's advisers and says so often.", "startingGrade": "C", "trueReliability": 0.7, "controlledByAdversary": False, "postmortemNote": "Right on Days 1 and 3, for good reasons it didn't share until asked. Wrong on Days 4 and 5, because it had stopped looking."},
   {"id": ESC, "codeName": "ESC", "discipline": "Liaison", "access": "Elsin's Southern Command: incident and forensic reporting. Marrat's advisers work in the building.", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Honest reporting from a building with Marrat's advisers in it. It reported the planted detonator accurately."},
   {"id": ROOK, "codeName": "ROOK", "discipline": "Liaison", "access": "Marrat's liaison officer at Southern Command. Speaks for Marrat.", "startingGrade": "D", "trueReliability": None, "controlledByAdversary": True, "postmortemNote": "Lied on Day 2, said nothing on Day 4, and told the truth on Day 5 because by then it suited him."},
   {"id": MAG, "codeName": "MAGPIE", "discipline": "HUMINT", "access": "A fuel trader in the Sarn valley who sells to the Front. Sees their money and their vehicles, not their plans. New. Every meeting is a risk: don't task him two days running.", "startingGrade": "C", "trueReliability": 0.85, "controlledByAdversary": False, "postmortemNote": "He saw money and vehicles, and his three reports were the spine of the scenario."},
   {"id": KES, "codeName": "KESTREL", "discipline": "HUMINT", "access": "Clerk at Kordav's 4th Army depot in Varn. Meetings take two days.", "startingGrade": "C", "trueReliability": 0.85, "controlledByAdversary": False, "postmortemNote": "If you still had him, he cleared Kordav from the depot floor."},
   {"id": FIN, "codeName": "FINCH", "discipline": "HUMINT", "access": "Inside Kordav's defence ministry. Meetings take two days.", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "If you still had him, he cleared Kordav from the ministry."},
   {"id": MER, "codeName": "MERIDIAN", "discipline": "SIGINT", "access": "Tasked coverage only: the Front's radios, or Kordav's 4th Army nets.", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "A reliable channel. Its intercept of Kordav's staff officers was accurate and about something else."},
   {"id": CIR, "codeName": "CIRRANE", "discipline": "IMINT", "access": "Tasked coverage only.", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "It showed what was there, including the nothing at Kessa."},
   {"id": MNA, "codeName": "MNA", "discipline": "OSINT", "access": "Marrat News Agency, Marrat's state outlet", "startingGrade": "D", "trueReliability": None, "controlledByAdversary": True, "postmortemNote": "Started the Kordav story."},
   {"id": FR, "codeName": "FRONT", "discipline": "OSINT", "access": "The Sarn Valley Front's own statements", "startingGrade": "E", "trueReliability": None, "controlledByAdversary": "partly", "postmortemNote": "Oro's signed communiqués were honest about what he wanted. The unsigned one wasn't."},
   {"id": CWS, "codeName": "CWS", "discipline": "OSINT", "access": "Continental Wire Service", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Straight reporting."},
   {"id": SOC, "codeName": "SOCIAL", "discipline": "OSINT", "access": "Social media monitoring. Accounts unvetted.", "startingGrade": "F", "trueReliability": 0.3, "controlledByAdversary": "partly", "postmortemNote": "\"Valley Truth\" was Marrat's."},
   {"id": OS, "codeName": "OSINT cell", "discipline": "OSINT", "access": "", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""},
   {"id": ADM, "codeName": "Task force admin", "discipline": "Admin", "access": "", "startingGrade": "A", "trueReliability": 1, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""}],
 "reports": reports,
 "tellLabels": {"no-detail": "No place, number or date", "only-one-chain": "Only the adversary's channels carry it", "found-by-beneficiary": "Found by the people who benefit",
   "no-raw-material": "No date, no audio, translation only", "knows-too-much": "Knows something its source couldn't", "wrong-currency": "A detail from the wrong country",
   "recycled-media": "Old media from somewhere else", "unsigned": "Not signed by the usual voice", "new-voice": "A voice that didn't exist last week",
   "agenda-aligned": "Lines up with the reporter's own agenda", "out-of-pattern": "Breaks the sender's own pattern", "too-on-message": "Says exactly what the adversary wants you to hear"},
 "scoring": {"call": {"low": [1, -1], "medium": [2, -2], "high": [3, -4]}, "evidence": {"true": 1, "noise": 0, "clutter": -1, "planted": -2}, "challenge": {"true": -1, "noise": 0, "clutter": 0, "planted": 1}, "maxEvidence": 3},
 "groundTruth": [
   {"day": 1, "trueHypothesis": "H3", "bestCall": "H3 at Low", "state": "Marrat's intelligence service has been paying and equipping the Front for a month. The valve was a rehearsal. The aim: frighten Elsin into a pact that puts Marrat's guards on the line. Marrat is also laying a trail that points at Kordav."},
   {"day": 2, "trueHypothesis": "H3", "bestCall": "H3 at Medium", "state": "Marrat's advisers plant a Kordav-made detonator fragment and hand over a forged transcript. The next target is already chosen: Tolen bridge."},
   {"day": 3, "trueHypothesis": "H3", "bestCall": "H3 at High", "state": "The advisers look over Tolen's guard post and leave for the holiday. The raid goes in that night."},
   {"day": 4, "trueHypothesis": "H1", "bestCall": "H1 at Medium", "state": "Marrat cuts the Front loose: the paymaster leaves and the money stops. Oro, who was promised his land back, turns on Marrat and plans his own attack on the thing he actually hates."},
   {"day": 5, "trueHypothesis": "H1", "bestCall": "H1 at High", "state": "Oro's column gathers at the quarry. Marrat learns of it through its old contacts and warns Elsin, truthfully, because a rogue militia is the best advertisement its guards could have. The attack on the compressor station is set for dawn on the 19th."}],
 "adversaryPlan": [
   {"phase": "Blame Kordav", "days": [1, 2, 3], "wantsYouToBelieve": "H2", "summary": "Marrat's news agency, its advisers' forensics, its liaison officer's transcript and a new social media account all point at Kordav.", "channels": [MNA, ROOK, SOC]},
   {"phase": "Never involved", "days": [4, 5], "wantsYouToBelieve": "H1", "summary": "Marrat denies everything, and on Day 5 tells the truth because it suits. Oro's people fake a stand-down.", "channels": [ROOK, FR]}],
 "endings": [
   {"id": "held", "tone": "good", "title": "Held", "points": 3, "if": {"assetAt": "sarn_c"}, "text": "Oro's column comes up the quarry road at first light and meets a company that has been waiting since dusk. It's over in ten minutes. Oro is taken alive, still asking about his fields."},
   {"id": "damaged", "tone": "warn", "title": "Damaged", "points": 0, "if": {"assetAt": "sarn_p"}, "text": "The platoon holds the control building. The cooling plant burns. The line is down for three weeks."},
   {"id": "burning", "tone": "bad", "title": "Burning", "points": -3, "default": True, "text": "The compressor station is alight by sunrise and the line is down for the summer. The task force goes onto trucked fuel."}],
 "dailyUpdates": [
   {"day": 1, "text": "Three nights ago an explosion damaged a valve housing in the Sarn valley. Pact talks between Elsin and Marrat open tomorrow."},
   {"day": 2, "text": "Pact talks open in Kalsa. No attacks overnight."},
   {"day": 3, "text": "Talks continue. Tomorrow is a public holiday in Marrat."},
   {"day": 4, "text": "It is a public holiday in Marrat.", "byFlag": {"event": "tolen", "texts": {
      "caught": "A raid on Tolen bridge was caught overnight. Seven fighters are in custody.", "held": "A raid on Tolen bridge was driven off overnight.",
      "displaced": "The valve yard at Dessa was blown overnight. Tolen bridge was not attacked.", "cut": "Tolen bridge was cut overnight. The Southern Line is down.", "cut_far": "Tolen bridge was cut overnight. The Southern Line is down."}}},
   {"day": 5, "text": "The pact's future is being argued in Kalsa. The Sarn valley has been quiet for two nights."}],
 "postmortem": {
   "script": [
     {"days": [1], "text": "WREN told you who was behind it, in one unsourced sentence with a grudge attached. It looked exactly like the alarm it raised over Tarsk, and that time it was guessing. This time it had a surveillance log, and all you had to do was ask. Marrat's news agency told you it was Kordav. It had nothing."},
     {"days": [2], "text": "A detonator turned up on the second sweep, found by the people selling the pact. A transcript with no date and no audio named the next target. Everything that pointed at Kordav had passed through Marrat's hands first."},
     {"days": [3], "text": "The advisers looked over a six-man guard post and went on holiday. MAGPIE's diesel went south. A platoon could be there without anyone knowing. A company arriving that day was a surprise; a company sitting there since the 14th was an announcement."},
     {"days": [4], "text": "The money stopped. Oro, who had been promised his fields, said so in public and named what he'd burn. WREN, right for three days, didn't notice the answer had changed."},
     {"days": [5], "text": "Marrat's liaison officer told the truth, because the truth had started to suit him. WREN called it a trick. The Front's \"political office\" said the fighting was over. Eight vehicles were already in the quarry."}],
   "lessons": [
     "A weakness is a reason to check, not a reason to doubt. Ask for the sourcing.",
     "A tell is something you can point to in the item. A feeling about the source isn't one.",
     "Ask whose hands each item passed through. Three items from one hand are one item.",
     "A source that was right yesterday is not right today because of it.",
     "An adversary can tell you the truth. Judge the content and the motive separately.",
     "When a sponsor lets go of a proxy, the proxy doesn't stop. It goes after what it wanted in the first place.",
     "Being right too visibly is a way of being wrong."],
   "missedCollection": {
     "1": "WREN's sourcing (free): the surveillance log behind its claim.",
     "2": "The detonator's markings (1 point), or MAGPIE on who is paying the Front.",
     "3": "Imagery of the Tolen approaches, or MAGPIE: either would have shown the raid was tonight.",
     "4": "MAGPIE, the Front's radios or the ford: each shows Marrat has let go.",
     "5": "Nothing tasked today could arrive in time."}},
 "pirs": [
   {"id": "PIR 1", "question": "Who is paying and equipping the Front?", "targets": ["wren-sourcing", "magpie", "front-radios", "detonator", "valley-truth"]},
   {"id": "PIR 2", "question": "Is Kordav involved?", "targets": ["kordav-nets", "kestrel", "finch", "kordav-crossings"]},
   {"id": "PIR 3", "question": "Where and when is the next attack?", "targets": ["tolen-approaches", "ford", "sarn-valley", "kessa"]}],
 "targets": [
   {"id": "wren-sourcing", "name": "Ask WREN for its sourcing", "disciplines": ["Liaison"], "fallback": "WREN has nothing more to send."},
   {"id": "magpie", "name": "MAGPIE, the fuel trader", "disciplines": ["HUMINT"], "fallback": "MAGPIE had nothing new."},
   {"id": "front-radios", "name": "The Front's radios", "disciplines": ["SIGINT"]},
   {"id": "detonator", "name": "The detonator's markings", "disciplines": ["OSINT"], "from": 2},
   {"id": "valley-truth", "name": "The \"Valley Truth\" account", "disciplines": ["OSINT"], "from": 3, "when": {"notFooled": ["staged-signals"]}},
   {"id": "kordav-nets", "name": "Kordav 4th Army nets", "disciplines": ["SIGINT"]},
   {"id": "kestrel", "name": "KESTREL, at the Varn depot", "disciplines": ["HUMINT"], "delay": {"HUMINT": 2}, "source": {"HUMINT": KES}, "fallback": "No meeting with KESTREL could be arranged in time."},
   {"id": "finch", "name": "FINCH, in Kordav's ministry", "disciplines": ["HUMINT"], "delay": {"HUMINT": 2}, "source": {"HUMINT": FIN}, "fallback": "No meeting with FINCH could be arranged in time."},
   {"id": "kordav-crossings", "name": "Kordav's southern border crossings", "disciplines": ["IMINT"]},
   {"id": "tolen-approaches", "name": "Tolen bridge approaches", "disciplines": ["IMINT"]},
   {"id": "ford", "name": "The ford on the Marrat border", "disciplines": ["IMINT"]},
   {"id": "sarn-valley", "name": "Sarn valley and the quarry", "disciplines": ["IMINT"]},
   {"id": "kessa", "name": "Kessa pumping station", "disciplines": ["IMINT"]}],
 "collection": {"budget": 5, "costs": {"OSINT": 1, "Liaison": 0, "IMINT": 2, "SIGINT": 3, "HUMINT": 3}, "delays": {},
   "sources": {"IMINT": CIR, "SIGINT": MER, "OSINT": OS, "HUMINT": MAG, "Liaison": WR}, "fallback": "Nothing significant at {target}.",
   "note": "MAGPIE reports the next morning. A meeting with KESTREL or FINCH takes two days.",
   "burnRules": [{"sourceId": MAG, "discipline": "HUMINT", "consecutiveDays": 2, "text": "MAGPIE didn't come. His yard is shut.",
     "postmortem": "MAGPIE was tasked two days running. A fuel trader who meets a stranger twice in two days gets noticed by his customers, and his customers were the Front."}],
   "burnPoints": -2},
 "collectionResults": [
   {"id": "C-01", "discipline": "Liaison", "target": "wren-sourcing", "from": 1, "to": 3},
   {"id": "C-02", "discipline": "HUMINT", "target": "magpie", "from": 1, "to": 2},
   {"id": "C-03", "discipline": "HUMINT", "target": "magpie", "from": 3, "to": 3},
   {"id": "C-04", "discipline": "HUMINT", "target": "magpie", "from": 4, "to": 4},
   {"id": "C-18", "discipline": "SIGINT", "target": "front-radios", "from": 3, "to": 3, "when": OLD_SIGNALS},
   {"id": "C-05", "discipline": "SIGINT", "target": "front-radios", "from": 1, "to": 3},
   {"id": "C-06", "discipline": "SIGINT", "target": "front-radios", "from": 4, "to": 4},
   {"id": "C-07", "discipline": "OSINT", "target": "detonator", "from": 2, "to": 4},
   {"id": "C-08", "discipline": "SIGINT", "target": "kordav-nets", "from": 1, "to": 4},
   {"id": "C-09", "discipline": "HUMINT", "target": "kestrel", "from": 1, "to": 3},
   {"id": "C-10", "discipline": "IMINT", "target": "kordav-crossings", "from": 1, "to": 4},
   {"id": "C-11", "discipline": "HUMINT", "target": "finch", "from": 1, "to": 3},
   {"id": "C-12", "discipline": "IMINT", "target": "tolen-approaches", "from": 3, "to": 3},
   {"id": "C-13", "discipline": "IMINT", "target": "ford", "from": 1, "to": 3},
   {"id": "C-14", "discipline": "IMINT", "target": "ford", "from": 4, "to": 5},
   {"id": "C-15", "discipline": "IMINT", "target": "sarn-valley", "from": 1, "to": 3},
   {"id": "C-16", "discipline": "IMINT", "target": "sarn-valley", "from": 4, "to": 5},
   {"id": "C-17", "discipline": "OSINT", "target": "valley-truth", "from": 3, "to": 4}],
 "credibility": {"start": 3, "min": 0, "max": 5, "bonusAt": 5,
   "levels": [
     {"id": "trusted", "label": "Trusted", "min": 3, "text": "He acts on your confidence as given, with your full collection budget."},
     {"id": "questioned", "label": "Questioned", "min": 2, "budgetDelta": -1, "text": "His staff trims your collection: 1 point less a day."},
     {"id": "discounted", "label": "Discounted", "min": 0, "budgetDelta": -2, "caution": 1, "text": "2 points less a day, and he treats your confidence as one step lower: High gets the platoon, Medium gets nothing."}],
   "triggers": [
     {"id": "turned-round", "on": "leave", "state": ["tolen_c", "kessa_c", "sarn_c"], "days": [1, 2, 3], "delta": -1, "rule": "He has to move the company away from a site with nothing to show for it", "note": "Credibility −1. \"So not there after all. I've turned a hundred and twenty people round on your word.\""},
     {"id": "went-round", "on": "flag", "event": "tolen", "flag": "displaced", "delta": -1, "rule": "An attack goes around a force he placed on your word", "note": "Credibility −1. The raid went around a company he placed on your word."},
     {"id": "wrong-end", "on": "flag", "event": "tolen", "flag": "cut_far", "delta": -2, "rule": "He guards the wrong end of the country on your word", "note": "Credibility −2. He had the company at Kessa on your word when Tolen was cut."},
     {"id": "bridge-held", "on": "flag", "event": "tolen", "flag": "held", "delta": 1, "rule": "A force he placed on your word stops an attack (this one raises it)", "note": "Credibility +1. The platoon he sent on your word held the bridge."},
     {"id": "raid-caught", "on": "flag", "event": "tolen", "flag": "caught", "delta": 1, "rule": "A force he placed on your word catches an attack (this one raises it)", "note": "Credibility +1. The company he sent on your word caught the raid."},
     {"id": "hedging", "on": "streak", "confidence": "low", "days": 2, "delta": -1, "rule": "Low confidence two days running (each further Low day too)", "note": "Credibility −1. Low again. \"I asked for a call, not a forecast.\""}],
   "outcome": {"held": 1, "damaged": 0, "burning": -1},
   "summary": "Halvorsen can't see whether you're right until it's over. He can see when a move comes to nothing, and when you won't commit."},
 "board": {"pinsPerDay": 3},
 "record": {"grades": [{"codeName": "WREN", "to": "B", "reason": "right about Marrat when it counted"}]},
 "analysts": [
   {"id": "vasko", "name": "Imre Vasko", "specialty": "Regional analyst", "reveal": "Anchors on his first theory. His first note was the best advice in the scenario: ask WREN for its sourcing. Then the detonator handed him a theory, Kordav, and he read everything after it that way, through two changes of the truth."},
   {"id": "halden", "name": "Noor Halden", "specialty": "Technical analyst (signals, imagery, forensics)", "reveal": "Slow but careful. Never wrong. Her note on the Tolen reconnaissance arrived the morning after the raid."},
   {"id": "marrow", "name": "Tess Marrow", "specialty": "Open-source analyst", "reveal": "Overconfident. \"Home-grown, full stop\" was wrong for three days and right by accident on the fourth. She authenticated a fake on Day 3. Her last note was sharp."}],
}
def NOTE(a, item, text, right, why, after=0): return {"analyst": a, "item": item, "after": after, "text": text, "right": right, "why": why}
crisis["notes"] = [
 NOTE("vasko", "R-1-02", "WREN has cried wolf before. But the border police down there keep good logs. Worth asking where this came from.", 1, "The best advice of the scenario."),
 NOTE("marrow", "R-1-03", "Classic local-grievance language. This is home-grown, full stop.", 0, "The language was Oro's own. The money wasn't."),
 NOTE("vasko", "R-2-01", "There's your Kordav link.", 0, "The plant handed him a theory, and he kept it."),
 NOTE("halden", "R-1-01", "A quarrying charge and a nine-hour repair. Whoever did this wanted a headline, not an outage.", 1, "An attack built to be noticed.", 1),
 NOTE("marrow", "R-3-03", "Letterhead checks out against open sources. Genuine.", 0, "She checked the letterhead and missed the currency."),
 NOTE("marrow", "R-3-03P", "Uniforms and vehicle match Kordav's 4th Army. Genuine.", 0, "The uniforms were real. So was the water tower at Ostrel behind them."),
 NOTE("halden", "R-2-01", "Fragments don't turn up on a second sweep that the first one missed. Ask who was holding the bag.", 1, "The detonator, a day after it arrived.", 1),
 NOTE("vasko", "R-4-02", "Posturing. Kordav will have them back in line by the weekend.", 0, "Anchored. Kordav was never in it."),
 NOTE("halden", "R-3-01", "An hour at a six-man guard post is a reconnaissance, not a survey.", 1, "Right, and it arrived the morning after the raid.", 1),
 NOTE("vasko", "R-5-01", "Marrat is guessing. The real threat is still in the north.", 0, "Anchored to the end."),
 NOTE("marrow", "R-5-02", "First statement from a \"political office\" in the Front's history, and Oro didn't sign it. I wouldn't hang a hat on it.", 1, "Sharp, and right."),
 NOTE("halden", "C-08", "\"The Varn spur.\" Varn is a Kordavan depot. They're talking about their own plumbing.", 1, "The tidy intercept, read properly.", 1)]

# ---------- map: the line from Kessa to Tolen ----------
KESSA, DESSA, V22, SARN, QUARRY, FARM, TOLEN, FORD, HQ, BASE, XING = (176, 128), (244, 186), (300, 226), (338, 262), (394, 236), (212, 294), (436, 352), (372, 372), (500, 228), (522, 112), (120, 132)
PINS = {
 "R-1-01": (V22, "Valve housing 22 blown"), "R-1-02": (TOLEN, "Marrat officers said to meet Oro"), "R-1-03": (FARM, "The Front claims the valve"), "R-1-04": (FARM, "Kordavan instructors alleged"),
 "R-2-01": (V22, "Detonator fragment found"), "R-2-02": (HQ, "Transcript from Marrat's liaison"), "R-2-04": (FARM, "New pickup trucks"),
 "R-3-01": (TOLEN, "Advisers inspect the guard post"), "R-3-02": (TOLEN, "WREN: something planned in the south"), "R-3-03": (HQ, "Payment order posted"), "R-3-03P": (FARM, "Photo of 'instructors'"),
 "R-4-02": (SARN, "Oro: the compressor still stands"), "R-4-04": (TOLEN, "WREN: expect a second attempt"),
 "R-5-01": (SARN, "ROOK: attack at dawn by the quarry road"), "R-5-02": (FARM, "Front 'suspends operations'"), "R-5-04": (QUARRY, "Strangers at the quarry road gate"),
 "C-01": (TOLEN, "Surveillance log: café meetings"), "C-02": (FARM, "Paid in Marrat crowns"), "C-03": (FARM, "Diesel bought, going south"), "C-04": (FARM, "Paymaster gone"),
 "C-05": (FARM, "Marrat-pattern handsets"), "C-06": (FARM, "Handsets silent, open sets back"), "C-18": (KESSA, "Call in the clear names Kessa"), "C-10": (XING, "Crossings normal"),
 "C-12": (TOLEN, "Pickups in the orchard"), "C-13": (FORD, "Night crossings at the ford"), "C-14": (FORD, "Ford unused"), "C-15": (FARM, "40 fighters, new vehicles"), "C-16": (QUARRY, "Eight vehicles in the quarry")}
for r in reports:
    if r["id"] in PINS: (x, y), label = PINS[r["id"]]; r["pin"] = {"x": x, "y": y, "label": label}
TPIN = {"magpie": FARM, "front-radios": FARM, "tolen-approaches": TOLEN, "ford": FORD, "sarn-valley": QUARRY, "kessa": KESSA, "kordav-crossings": XING, "wren-sourcing": TOLEN}
for t in crisis["targets"]:
    if t["id"] in TPIN: t["pin"] = {"x": TPIN[t["id"]][0], "y": TPIN[t["id"]][1]}
def site(name, xy, lx, ly, typ="town"): return {"name": name, "x": xy[0], "y": xy[1], "type": typ, "lx": xy[0] + lx, "ly": xy[1] + ly}
F = lambda xy, label, small=False, dx=0, dy=-24: {"x": xy[0] + dx, "y": xy[1] + dy, "label": label, "small": small}
reserve = F(BASE, "Guard Coy", dy=30)
forces = {"home": [reserve]}
for sid, xy, dx, dy in (("tolen", TOLEN, 0, -46), ("kessa", KESSA, -6, 40), ("sarn", SARN, -12, 46)):
    forces[sid + "_p"] = [F(xy, "1 Pl", True, dx, dy), F(BASE, "Guard Coy (-)", dy=30)]
    forces[sid + "_c"] = [F(xy, "Guard Coy", False, dx, dy)]
crisis["map"] = {
 "viewBox": [0, 0, 600, 420], "title": "Map of the Southern Line", "caption": "The Southern Line, from Kessa to Tolen. Reporting will be plotted here as it arrives.",
 "truthNote": "Red diamonds are what was really behind the Front on Day {day}.",
 "scaleKm": 50, "scaleUnits": 50,
 "border": "M0,420 L0,148 L96,140 L170,96 L214,40 L236,0",
 "areas": [{"d": "M0,340 C110,348 220,372 330,384 C410,390 470,356 600,366 L600,420 L0,420 Z", "label": "MARRAT", "lx": 60, "ly": 400}],
 "river": {"name": "Tolen", "d": "M0,340 C110,348 220,372 330,384 C410,390 470,356 600,366", "lx": 130, "ly": 344, "rot": 6},
 "lines": [{"d": "M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d" % (KESSA + DESSA + V22 + SARN + TOLEN), "label": "Southern Line", "lx": 196, "ly": 168}],
 "regions": [{"name": "KORDAV", "x": 14, "y": 60}, {"name": "ELSIN", "x": 420, "y": 60}],
 "places": [site("Kessa pumping station", KESSA, -40, -12, "depot"), site("Dessa valve yard", DESSA, 12, 4), site("Valve 22", V22, 10, -6), site("Sarn compressor", SARN, 12, 16, "depot"),
            site("Quarry", QUARRY, 10, -6), site("Upper farm", FARM, -34, 20), site("Tolen bridge", TOLEN, 76, 4, "crossing"), site("Ford", FORD, -34, -8),
            site("Southern Command", HQ, -44, 20), site("Task force base", BASE, -44, -12), site("Kordav crossings", XING, -76, 20)],
 "offmap": [{"text": "Kalsa 200 km", "x": 470, "y": 20}],
 "forces": forces,
 "legend": "Plots reporting as it arrives, not confirmed fact. Dashed pins are items you doubted. Dashed rings are today's taskings."}
U = lambda label, xy, dx=0, dy=30: {"label": label, "x": xy[0] + dx, "y": xy[1] + dy}
truth = {1: [U("Marrat paymaster", FARM, -10, 34)], 2: [U("Marrat paymaster", FARM, -10, 34), U("Evidence planted", V22, 48, -28)],
         3: [U("Marrat paymaster", FARM, -10, 34), U("Raiding party", TOLEN, 78, -44)], 4: [U("Oro's column", QUARRY, 44, -22)], 5: [U("Oro's column", QUARRY, 44, -22)]}
for g in crisis["groundTruth"]: g["units"] = truth[g["day"]]

# ---------- sanity ----------
ids = {r["id"] for r in reports}
assert all(cr["id"] in ids for cr in crisis["collectionResults"])
assert all(i in ids for r in reports if r.get("reveal") for i in r["reveal"]["crossCheck"]["ids"])
assert all(r.get("reveal") for r in reports if r["kind"] == "planted")
tids = {t["id"] for t in crisis["targets"]}
assert tids == {t for p in crisis["pirs"] for t in p["targets"]} and all(cr["target"] in tids for cr in crisis["collectionResults"])
keys = {r["reply"] for r in policy} | {o["replyId"] for e in crisis["events"] for o in e["outcomes"]}
assert keys <= set(replies) and keys <= set(labels), keys - set(labels)
assert all(n["item"] in ids for n in crisis["notes"]) and all(r["to"] in levels for r in policy if "to" in r)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "crises", "southern-line.json")
with open(out, "w") as f: json.dump(crisis, f, indent=2, ensure_ascii=False); f.write("\n")
print("wrote", os.path.normpath(out), len(reports), "reports,", sum(r["kind"] == "planted" for r in reports), "planted incl. variants")
