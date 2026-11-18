#!/usr/bin/env python3
"""Builds crises/walk-in.json (Crisis 02). Content lives here so the long text stays readable; the engine only reads the JSON."""
import json, os
def R(id, day, src, disc, grade, cred, text, kind, note, supports=(), contradicts=(), tells=(), reveal=None, via=None, diagnostic=False):
    r = {"id": id, "day": day, "sourceId": src, "discipline": disc, "sourceGrade": grade, "credibility": cred, "text": text, "kind": kind,
         "supports": list(supports), "contradicts": list(contradicts), "tells": list(tells), "postmortemNote": note}
    if reveal: r["reveal"] = {"tell": reveal[0], "crossCheck": {"ids": reveal[1], "text": reveal[2]}, "motive": reveal[3]}
    if via: r["via"] = "collection"
    if diagnostic: r["diagnostic"] = True
    return r
ST, LN, FI, WR, ME, KSB, CWS, SOC, AD, SEC, OS = "S-STATION", "S-LANTERN", "S-FINCH", "S-WREN", "S-MERIDIAN", "S-KSB", "S-CWS", "S-SOCIAL", "S-ADMIN", "S-SECURITY", "S-OSINT"

reports = [
 # Day 1
 R("R-1-01", 1, ST, "HUMINT", "A", 1, "A man walked into the embassy at 0710 and asked for asylum. His Kordavan passport matches the officer he says he is: a major on the General Staff's planning directorate. He asked for asylum for himself only and said his wife \"will be fine.\" He asked that his presence be kept secret \"for my safety.\"", "true",
   "True. Two details matter later: he asked asylum for himself only (\"my wife will be fine\"), and he asked to be kept secret."),
 R("R-1-02", 1, LN, "HUMINT", "F", 3, "Volunteers that he served on the IRON HARVEST planning cell. Describes the \"northern option,\" the 0400 switch to contingency accounts and the staging area in Dolan forest.", "true",
   "True, and worthless to Kordav. IRON HARVEST was blown three months ago. Real information that costs the other side nothing is chickenfeed: true isn't the same as genuine.", supports=["H1", "H2"]),
 R("R-1-03", 1, LN, "HUMINT", "F", 3, "Volunteers that Deputy Defence Minister Vell has been a Kordavan agent for four years, and that he learned it from \"colleagues in the Bureau,\" Kordav's security service. Will give the details of Vell's meetings with his handler once his resettlement is guaranteed.", "planted",
   "The allegation, with a hook attached.", supports=["H1"], tells=["access-mismatch", "conditional-gift"],
   reveal=("He says he learned it from \"colleagues in the Bureau.\" A planning officer doesn't see the security service's agent files. And the gift comes with a condition: resettlement first.",
           ["R-1-01", "R-1-02"], "Both put him on the General Staff's planning directorate (R-1-01, R-1-02), which is military planning, not counterintelligence. Debriefing his access (C-12) or checking the ministry directory (C-08), if you tasked them, confirm it.",
           "Plant the claim on Day 1 and attach a hook, so we invest in him before we test him.")),
 R("R-1-04", 1, CWS, "OSINT", "B", 1, "Elsin's parliament will vote on the 12th on a no-confidence motion against Vell, architect of the task force agreement. The opposition calls him \"too close to foreign militaries.\"", "true",
   "Motive and timing: the vote is why LANTERN is here this week.", supports=["H2"]),
 R("R-1-05", 1, AD, "Admin", "A", 1, "The embassy's annual fire drill is on Thursday. The interview room is not a fire exit, whatever its current occupant may hope.", "clutter", "Fire drill."),
 # Day 2
 R("R-2-01", 2, ST, "HUMINT", "A", 2, "Second session. LANTERN's account of his career matches yesterday's almost word for word. The debriefers note he is \"unusually calm for a man who has just abandoned his country.\"", "true",
   "A rehearsed story told by a man with nothing to fear.", supports=["H2"]),
 R("R-2-02", 2, LN, "HUMINT", "F", 3, "Asks whether we have anyone in Kordav's defence ministry who could vouch for him, and offers the names of officers who \"know him well.\"", "planted",
   "The dangle's second job: find our sources.", supports=["H1"], tells=["fishing"],
   reveal=("A defector asking us who we have inside his own ministry.",
           ["R-1-03"], "A man who claims to know Bureau agent files (R-1-03) could prove himself with something only the Bureau knows. Instead, he asks us to show our hand.",
           "The Bureau was watching the ministry for whoever came asking about him. Tasking FINCH did exactly that.")),
 R("R-2-03", 2, KSB, "OSINT", "D", 1, "State TV runs a long segment on \"corruption\" in Elsin's defence ministry, naming Deputy Minister Vell. Nothing about any missing officer.", "true",
   "Kordav's media attacking the same man LANTERN accuses, the same day, and not looking for its missing officer.", supports=["H2"]),
 R("R-2-04", 2, CWS, "OSINT", "B", 1, "The neutral capital's metro workers strike tomorrow. Embassy staff are advised to work from home.", "clutter", "Metro strike."),
 # Day 3
 R("R-3-01", 3, WR, "Liaison", "B", 3, "Elsin's service has heard rumors that \"someone from Kordav\" is talking about \"a traitor in our ministry,\" and asks for details. WREN adds that \"some here have long doubted Vell.\"", "noise",
   "Elsin's anti-Vell faction repeating itself. It tells you what some in Kalsa want to hear, not what's true.", supports=["H1"], tells=["agenda-aligned"]),
 R("R-3-02", 3, LN, "HUMINT", "F", 3, "Produces his proof: a photocopy of a Bureau payment ledger listing an agent codenamed HERON, with payment dates that match Vell's trips abroad.", "planted",
   "Real paper, forged story.", supports=["H1"], tells=["only-public-dates"],
   reveal=("Every payment date matches one of Vell's trips abroad, and only the ones anybody could look up.",
           ["R-3-03"], "The station's analysis the same morning (R-3-03): every date is on Vell's public schedule, and none of his private travel appears. Real agents get paid on trips nobody announces. Debriefing the ledger (C-09), if you tasked it, adds that a planner had no way into the registry it came from.",
           "Genuine Bureau paper gets a forgery past a quick look.")),
 R("R-3-03", 3, ST, "HUMINT", "A", 1, "Document analysis of the ledger: the paper and stamps are genuine Bureau stock. Every date on it matches a trip on Vell's public ministry schedule. None matches his private travel.", "true",
   "The best item in the daily stream. Real agents get paid on trips nobody announces.", supports=["H2"], contradicts=["H1"]),
 R("R-3-04", 3, CWS, "OSINT", "B", 1, "Elsin's parliament has moved the no-confidence vote up from the 12th to the 10th.", "true",
   "The deadline LANTERN will lean on tomorrow.", supports=["H2"]),
 R("R-3-05", 3, SOC, "OSINT", "F", 3, "A viral video of a Kordavan general's wedding: forty minutes, three brass bands.", "clutter", "A wedding."),
 # Day 4
 R("R-4-01", 4, LN, "HUMINT", "F", 3, "Insists the allegation reach Elsin before the vote: \"After the vote it will be too late. He will purge the honest officers.\"", "planted",
   "Urgency on Kordav's timetable.", supports=["H1"], tells=["convenient-timing"],
   reveal=("The urgency is tied to a deadline only Kordav benefits from.",
           ["R-3-04", "R-1-04"], "The vote was moved up yesterday (R-3-04), and it was the reason for his timing from Day 1 (R-1-04).",
           "Force a decision before verification can catch up.")),
 R("R-4-02", 4, ST, "HUMINT", "A", 2, "LANTERN asks for resettlement \"for my family too,\" the first time he has raised them himself since Day 1.", "true",
   "His story about his family changes once the pressure is on. On Day 1 she would \"be fine.\"", supports=["H2"]),
 R("R-4-03", 4, SOC, "OSINT", "F", 2, "An Elsin opposition MP posts that \"a Kordavan officer who has defected to an allied service\" has evidence against Vell.", "planted",
   "The backup route for the smear.", supports=["H1"], tells=["leak-origin"],
   reveal=("The MP knows about \"a Kordavan officer who has defected to an allied service.\"",
           ["R-3-01", "R-1-01"], "Elsin's own service only had a rumor about \"someone from Kordav\" (R-3-01), and LANTERN asked us to keep him secret (R-1-01). If nothing left our building, nobody on our side said \"defector.\" Only LANTERN's side could have. (If the allegation had already been passed to Elsin, the leak could be theirs.)",
           "A backup plan. The smear lands even if we never share anything.")),
 R("R-4-04", 4, KSB, "OSINT", "D", 1, "State TV repeats its Vell segment, now with \"questions about his foreign contacts.\"", "true",
   "The media campaign building toward the vote.", supports=["H2"]),
 R("R-4-05", 4, SEC, "Admin", "A", 1, "The phishing campaign is back: \"Updated_Per_Diem_Rates_v2.xlsm\". The rates have still not gone up.", "clutter", "Still phishing."),
 # Day 5
 R("R-5-01", 5, KSB, "OSINT", "D", 1, "State TV reports that a Kordavan officer was \"kidnapped by Western intelligence\" in a neutral capital, and names LANTERN.", "planted",
   "Four days of silence, then a kidnapping.", supports=["H1"], tells=["convenient-timing"],
   reveal=("Four days of silence about a missing officer, then a kidnapping story the day before the vote.",
           ["R-2-03", "R-4-04"], "State TV spent those days attacking Vell and never mentioned LANTERN (R-2-03, R-4-04). If you tasked the embassy (C-07), it was told to keep its distance.",
           "Make the defection look real just in time for LANTERN to go public.")),
 R("R-5-02", 5, ST, "HUMINT", "A", 1, "LANTERN asks to record a statement for the press, to be released \"tomorrow morning.\"", "true",
   "STATION reported it straight, and it's the last tell: a man who asked to be kept secret for his safety (R-1-01) now wants a press statement on the morning of the vote. The smear's final delivery route.", supports=["H2"], contradicts=["H1"]),
 R("R-5-03", 5, WR, "Liaison", "B", 2, "The opposition's motion now cites \"allied intelligence.\" Elsin's service asks whether we've shared anything with anyone.", "true",
   "If anything we passed ended up in the motion, this is where it shows."),
 R("R-5-04", 5, CWS, "OSINT", "B", 1, "The metro strike is over.", "clutter", "Metro strike over."),
 # Collection results
 R("C-12", None, ST, "HUMINT", "A", 2, "Debrief, on his access. Asked what his directorate does day to day, LANTERN describes exercise planning, movement tables and fuel allocations, in detail and accurately. Asked how a planning officer comes to know the contents of Bureau agent files, he says: \"People talk. You hear things at dinners.\"", "true",
   "Expert on his own job, vague on the Bureau's. \"People talk\" is not access.", supports=["H2", "H3"], contradicts=["H1"], via=True),
 R("C-10", None, LN, "HUMINT", "F", 3, "Debrief, on the Vell details. LANTERN says Vell met his Bureau handler at the Hotel Sorel in Kalsa, room 412, on 14 March. Asked how he knows the room number, he can't say. \"It was known.\"", "planted",
   "The dangle's prepared detail, held back for when the debriefers pressed.", supports=["H1"], tells=["access-mismatch", "circular-origin"], via=True,
   reveal=("An exact room number he can't say how he knows.",
           ["R-1-03", "C-03"], "A planning officer has no route to that detail (R-1-03). And it was already in print: The Kalsa Courier ran it three weeks ago (C-03, Elsin's press, 1 point on any day). One origin, dressed up as two.",
           "A dangle is briefed with a prepared detail for when the debriefers push for specifics. Precision sounds like access. Kordav didn't need to know we'd ask: every debriefer does.")),
 R("C-13", None, ST, "HUMINT", "A", 2, "Debrief, on his family. Asked about his wife, LANTERN repeats that she \"will be fine\" because she \"knows nothing about my work.\" Asked whether the Bureau will question her, he says it \"doesn't bother the families of planning officers.\"", "true",
   "A man unafraid for his wife. A real defector knows exactly what the Bureau does to families.", supports=["H2"], contradicts=["H1"], via=True),
 R("C-09", None, ST, "HUMINT", "A", 2, "Debrief, on the ledger. Asked how he got it out, LANTERN says he photographed it in the Bureau's central registry. Asked how a General Staff planner got into the registry, he says a friend signed him in. He won't name the friend.", "true",
   "A planner can't walk into the Bureau's registry, and a friend who signs him in has a name. The ledger was handed to him.", supports=["H2"], contradicts=["H1"], via=True),
 R("C-04", None, FI, "HUMINT", "B", 2, "FINCH: LANTERN is known in the ministry as a mid-level planning officer, \"nowhere near counterintelligence files.\" FINCH asks why we're asking, and mentions that someone else asked him about LANTERN's friends last week.", "true",
   "Confirms the access mismatch. The \"someone else\" was the Bureau's watch on the ministry, and this meeting was seen. FINCH is gone.", supports=["H2", "H3"], contradicts=["H1"], via=True),
 R("C-08", None, OS, "OSINT", "B", 1, "The ministry's published staff directory lists LANTERN's name under the General Staff planning directorate, logistics branch. The Bureau is a separate service with its own directory; his name isn't in it.", "true",
   "The cheap version of FINCH's answer: a logistics planner, and the Bureau is a different service. One point, and nobody burned.", supports=["H2", "H3"], contradicts=["H1"], via=True),
 R("C-06", None, ME, "SIGINT", "B", 2, "Bureau headquarters to its office in the neutral capital, administrative net, routine precedence: \"Suspend contact with all persons known to [LANTERN's true name]. Officers KARSA, DOVIN and TREL to return to the capital for consultations.\"", "planted",
   "Staged for MERIDIAN. Reliable channel, planted content.", supports=["H1"], contradicts=["H2"], tells=["wrong-channel", "too-on-message"], via=True,
   reveal=("A real compromise order goes out on a service's secure operational channel at the highest precedence. This one went on the administrative net, at routine precedence, and names the officers it's recalling. It reads like a press release for an audience of one.",
           ["C-01", "C-02", "C-07", "C-11"], "The office's own traffic shows every officer still at post and nothing changed (C-01). His family isn't questioned (C-02). The embassy is told to stay out of it (C-07). Task the headquarters net again and the recall is never mentioned (C-11). Any one of these, all available the same day, says the recall never happened.",
           "The strongest sign of a genuine defection is the other side's damage control. Kordav couldn't fake it everywhere, so it faked it where it thought we were listening: it has assumed its administrative net is read ever since IRON HARVEST was blown.")),
 R("C-11", None, ME, "SIGINT", "B", 2, "Bureau headquarters administrative net: routine traffic only. Nothing further about LANTERN. The recall of KARSA, DOVIN and TREL isn't mentioned again.", "true",
   "The staged recall was a one-off. Real damage control generates traffic for days.", supports=["H2"], contradicts=["H1"], via=True),
 R("C-01", None, ME, "SIGINT", "B", 2, "Bureau office in the neutral capital: its own traffic is routine. Every officer on its duty roster is still at post, and nobody has been called home. No change to codes or procedures since LANTERN walked in. One circular from headquarters reminds staff of \"media discipline this week.\"", "true",
   "The diagnostic item: no damage control. If an officer with the access LANTERN claims had really defected, this office would be pulling people home and changing codes. Nobody moves, nothing changes, and headquarters is thinking about the media.", supports=["H2"], contradicts=["H1", "H3"], via=True, diagnostic=True),
 R("C-07", None, ME, "SIGINT", "B", 2, "Kordav's embassy: routine traffic. Its security officer has been told to \"keep distance from the matter.\" No sign of any effort to find anyone.", "true",
   "Kordav's embassy is under orders to stay hands-off. Nobody is looking for him.", supports=["H2"], contradicts=["H1"], via=True),
 R("C-02", None, OS, "OSINT", "B", 2, "His wife's accounts are posting normally: a school concert on the 6th, a weekend at the lake being planned. No sign she's been questioned or stopped from traveling.", "true",
   "The diagnostic by the cheap route. A real defector's family gets questioned and stopped from traveling. His goes to the lake.", supports=["H2"], contradicts=["H1", "H3"], via=True, diagnostic=True),
 R("C-03", None, OS, "OSINT", "B", 1, "Three weeks ago The Kalsa Courier, an opposition paper, ran an unsourced story: Vell met \"a foreign businessman\" at the Hotel Sorel, room 412, on 14 March.", "true",
   "The origin of \"room 412.\" It was in print three weeks before LANTERN walked in.", supports=["H2", "H3"], contradicts=["H1"], via=True),
 R("C-05", None, WR, "Liaison", "B", 2, "Elsin confirms Vell was at the Hotel Sorel on 14 March, at a meeting with a defence contractor logged by his own office. WREN adds that \"some here have long doubted him.\"", "true",
   "The meeting happened, logged and innocent. WREN's last line is its faction talking.", supports=["H2", "H3"], via=True),
]

crisis = {
 "id": "walk-in", "formatVersion": "0.9", "title": "The Walk-in", "crisisNumber": "02", "days": 5,
 "dayLabels": ["the 5th", "the 6th", "the 7th", "the 8th", "the 9th"],
 "placeholderNote": "Kordav and Elsin are fictional countries. All leaders, officials, services and newspapers are fictional.",
 "adversary": "Kordav", "endingEyebrow": "The vote", "frozenText": "Kalsa has asked us to stay out of it. Nothing can go to Elsin today.",
 "briefing": {"dateLine": "Day 1 is the 5th, three months after IRON HARVEST.", "situation": [
   "Your cell now supports Under Secretary H. Marlowe, who handles the alliance's relationship with Elsin.",
   "At 0710 this morning, a man walked into our embassy in a neutral capital and asked for asylum. He says he's a major on the planning directorate of Kordav's General Staff. He has been given the cryptonym LANTERN.",
   "Elsin's parliament is about to vote on a no-confidence motion against Deputy Defence Minister Aron Vell, who negotiated the task force agreement and is Kordav's least favorite politician in Kalsa.",
   "This crisis works differently. Public reporting, and whatever LANTERN chooses to volunteer, reach you every day. Everything secret arrives only if you task it: questioning him, signals intelligence, your own sources. And Kordav knows some of what you can collect."]},
 "customer": {"name": "Under Secretary H. Marlowe", "short": "Marlowe", "pronouns": ["she", "her"], "role": "Under Secretary for alliance affairs", "callsign": "USEC ALLIANCE",
   "wants": "What do we do with what LANTERN is telling us? She acts as far as your confidence supports.",
   "context": "Careful, political and allergic to surprises. Anything she passes to Kalsa is hard to take back, and the full allegation can't be taken back at all.",
   "tipLine": "High gets the full action. Medium gets a cautious one, and Low keeps everything in the building."},
 "asset": {"id": "lantern", "name": "LANTERN's reporting", "levels": {
   "home": {"label": "kept in the building", "rank": 0}, "caveated": {"label": "caveated warning passed to Elsin", "rank": 1},
   "shared": {"label": "full allegation passed to Elsin", "rank": 2}, "restricted": {"label": "sharing stopped", "rank": 0},
   "countered": {"label": "Elsin warned of a Kordavan smear", "rank": 0}, "ended": {"label": "debriefing ended", "rank": 0}}},
 "customerPolicy": [
   {"if": {"assetAt": "shared"}, "reply": "shared_stands"},
   {"if": {"hypothesis": "H1", "confidence": ["medium", "high"], "assetAt": "countered"}, "to": "restricted", "reply": "withdraw_warning"},
   {"if": {"hypothesis": "H1", "confidence": ["high"]}, "to": "shared", "reply": "share_full", "sends": True},
   {"if": {"hypothesis": "H1", "confidence": ["medium"], "assetAt": "caveated"}, "reply": "caveat_stands"},
   {"if": {"hypothesis": "H1", "confidence": ["medium"]}, "to": "caveated", "reply": "share_caveat", "sends": True},
   {"if": {"assetAt": "countered"}, "reply": "counter_stands"},
   {"if": {"hypothesis": "H2", "confidence": ["high"]}, "to": "countered", "reply": "counter", "sends": True},
   {"if": {"hypothesis": ["H2", "H3"], "confidence": ["medium"], "assetAt": "ended"}, "reply": "end_stands"},
   {"if": {"hypothesis": "H3", "confidence": ["high"], "assetAt": "ended"}, "reply": "end_stands"},
   {"if": {"hypothesis": "H2", "confidence": ["medium"], "assetAt": "restricted"}, "reply": "restrict_stands"},
   {"if": {"hypothesis": "H2", "confidence": ["medium"]}, "to": "restricted", "reply": "restrict"},

   {"if": {"hypothesis": "H3", "confidence": ["medium", "high"]}, "to": "ended", "reply": "end"},
   {"if": {"assetAt": "caveated"}, "reply": "caveat_stands"},
   {"if": {"assetAt": "ended"}, "reply": "end_stands"},
   {"if": {}, "reply": "listen"}],
 "policySummary": [
   {"brief": "H1 at High", "action": "Passes LANTERN's full allegation and his evidence to Elsin. This can't be undone."},
   {"brief": "H1 at Medium", "action": "Passes Elsin a caveated warning: \"single-source, unverified reporting about your deputy defence minister\""},
   {"brief": "H2 at High", "action": "Treats LANTERN as hostile and warns Elsin that Kordav is running a smear against Vell. Withdraws a caveated warning if one was sent."},
   {"brief": "H2 at Medium", "action": "Stops all sharing and keeps LANTERN in debriefing, but tells Elsin nothing. Withdraws a caveated warning if one was sent."},
   {"brief": "H3 at Medium or High", "action": "Ends the debriefing and refuses resettlement. You can't question him after that."},
   {"brief": "Any hypothesis at Low", "action": "Keeps listening. Nothing new leaves the building."}],
 "policyNote": "What reaches Kalsa is hard to take back.",
 "replyLabels": {
   "share_full": "Passes the full allegation and the evidence to Elsin", "share_caveat": "Passes Elsin a caveated warning about Vell",
   "caveat_stands": "Leaves the caveated warning in place", "shared_stands": "Nothing. The allegation is already with Elsin",
   "counter": "Warns Elsin that Kordav is running a smear", "counter_stands": "Leaves the smear warning in place",
   "restrict": "Stops all sharing and keeps him in the room", "restrict_stands": "Keeps sharing stopped and tells Elsin nothing",
   "end": "Ends the debriefing and refuses resettlement", "end_stands": "Nothing. The debriefing is over",
   "withdraw_warning": "Withdraws the smear warning and stops sharing", "listen": "Keeps listening. Nothing leaves the building",
   "frozen": "Can't send anything to Elsin yet. Keeps listening", "rebuff": "Withdraws the warning. Kalsa asks us to stay out of it"},
 "replies": {
   "share_full": "I've passed it to Kalsa in full, ledger and all. If this is wrong, it's the most expensive thing I've ever signed. Make sure it isn't.",
   "share_caveat": "I've told Elsin's minister we have single-source, unverified reporting about Vell. He asked what that means. I said it means be careful. He said nobody in politics has ever followed that advice.",
   "caveat_stands": "The caveat stands. Kalsa keeps asking what's behind it, and I keep saying I'll know when you do.",
   "shared_stands": "It's with Kalsa and it isn't coming back. Whatever you tell me now is for the file.",
   "counter": "I've told Kalsa that Kordav is running a smear against Vell and that our walk-in is part of it. Their minister went very quiet, then thanked me. I've just called an ally's star witness a liar, so I hope you're right.",
   "counter_stands": "The warning stands. Keep building the file; they'll want it after the vote.",
   "restrict": "We stop sharing and keep him in the room. If he's a plant, I want to know what else he was sent to say. If you want me to say it to Kalsa, I need more than medium confidence.",
   "restrict_stands": "Still nothing leaving the building, and he's still talking. Medium doesn't get a call to Kalsa.",
   "end": "We've ended the debriefing. He's been told there will be no resettlement. He took it remarkably well, which I'm choosing not to think about.",
   "end_stands": "The debriefing is over. He's someone else's paperwork now.",
   "withdraw_warning": "I've withdrawn the warning I gave Kalsa. Their minister asked if we make a habit of this. I said not usually.",
   "listen": "We keep listening. Nothing leaves this building.",
   "frozen": "Kalsa asked us to stay out of it, and for now we are. Nothing goes to them. Keep him talking.",
   "rebuff": "You wanted me to call a defector a plant after one interview. I did. Kalsa thinks we're protecting Vell for our own reasons, and they've asked us to stay out of it. For three days, we will."},
 "events": [{"id": "early-counter-rebuffed", "atStartOfDay": 2, "if": {"movedTo": {"state": "countered", "days": [1]}},
   "effect": {"assetTo": "home", "freezeBriefDays": [2, 3, 4]}, "replyId": "rebuff", "note": "The warning is withdrawn. Nothing can go to Elsin for three days.", "points": -5, "pointsLabel": "rebuffed warning"}],
 "hypotheses": [
   {"id": "H1", "short": "Genuine defector", "text": "LANTERN is who he says he is, and his reporting is authentic.", "claim": "LANTERN is a genuine defector and his reporting on Vell is authentic"},
   {"id": "H2", "short": "Dangle", "text": "Kordav sent him to feed us deception.", "claim": "LANTERN was sent by Kordav to feed us deception about Vell"},
   {"id": "H3", "short": "Fabricator", "text": "He's acting alone, for money and resettlement, and stitched his story together from what he could find.", "claim": "LANTERN is a fabricator acting alone for resettlement"}],
 "groundTruth": [
   {"day": 1, "trueHypothesis": "H2", "bestCall": "H2 at Low", "state": "LANTERN is a real mid-level planning officer, recruited by the Bureau for one job. He walked in on orders. The aim: smear Vell before the vote, and see who we ask about him."},
   {"day": 2, "trueHypothesis": "H2", "bestCall": "H2 at Medium", "state": "The Bureau watches the defence ministry for anyone asking about LANTERN, and puts a staged recall on the headquarters net it assumes we read. \"Room 412\" comes from a story the Bureau planted in The Kalsa Courier three weeks ago."},
   {"day": 3, "trueHypothesis": "H2", "bestCall": "H2 at High", "state": "The ledger is delivered: genuine Bureau paper, with entries forged from Vell's public schedule. Elsin's opposition, working alongside Kordav's media campaign, gets the vote moved up."},
   {"day": 4, "trueHypothesis": "H2", "bestCall": "H2 at High", "state": "The Bureau leaks \"a defector with evidence\" to an opposition MP, so the smear lands even if we keep quiet."},
   {"day": 5, "trueHypothesis": "H2", "bestCall": "H2 at High", "state": "State TV announces a \"kidnapping,\" and LANTERN asks to go public on the morning of the vote."}],
 "adversaryPlan": [
   {"phase": "Hook", "days": [1, 2], "wantsYouToBelieve": "H1", "summary": "A walk-in with true but worthless information, an allegation with a condition, and prepared detail for when we press.", "channels": [LN, KSB]},
   {"phase": "Proof and pressure", "days": [3, 4, 5], "wantsYouToBelieve": "H1", "summary": "A forged ledger on real paper, a deadline, a leak to the opposition and a kidnapping story. A staged recall sits on the net Kordav assumes we read.", "channels": [LN, KSB, SOC, ME]}],
 "sources": [
   {"id": LN, "codeName": "LANTERN", "discipline": "HUMINT (walk-in)", "access": "Says he's a major on Kordav's General Staff planning directorate. No track record. What he volunteers reaches you every day; what you want to test, you have to ask.", "startingGrade": "F", "trueReliability": None, "controlledByAdversary": True, "postmortemNote": "A real officer on a Bureau assignment. His one true gift, IRON HARVEST, was chickenfeed. Accurate about his own job, vague about everything else."},
   {"id": ST, "codeName": "STATION", "discipline": "HUMINT handling", "access": "Our station in the neutral capital. Runs the debriefing and reports what happens in the room.", "startingGrade": "A", "trueReliability": 1, "controlledByAdversary": False, "postmortemNote": "Reported exactly what happened in the room, including the things LANTERN wanted reported."},
   {"id": FI, "codeName": "FINCH", "discipline": "HUMINT", "access": "A source inside Kordav's defence ministry for six years. Reliable. A meeting takes two days to arrange, and the ministry is a dangerous place to be seen asking questions.", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Honest. The Bureau was watching for whoever asked about LANTERN, so his first meeting on this was his last."},
   {"id": WR, "codeName": "WREN", "discipline": "Liaison", "access": "Elsin's military intelligence. Pushes what it wants us to see, and answers requests. Some of its officers have long distrusted Vell.", "startingGrade": "B", "trueReliability": 0.6, "controlledByAdversary": False, "postmortemNote": "Not controlled, but some of its officers wanted Vell gone and kept saying so."},
   {"id": ME, "codeName": "MERIDIAN", "discipline": "SIGINT", "access": "Tasked coverage only: the Bureau's headquarters administrative net (read since last year; Kordav has had reason to suspect it since IRON HARVEST was blown), the Bureau's office in the neutral capital, and Kordav's embassy there.", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "A reliable channel. Kordav suspected the headquarters net was read and staged one message on it. The office's own traffic was genuine."},
   {"id": KSB, "codeName": "KSB", "discipline": "OSINT", "access": "Kordav State Broadcaster and official channels", "startingGrade": "D", "trueReliability": None, "controlledByAdversary": True, "postmortemNote": "Ran the media side of the smear."},
   {"id": CWS, "codeName": "CWS", "discipline": "OSINT", "access": "Continental Wire Service", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Straight reporting throughout."},
   {"id": SOC, "codeName": "SOCIAL", "discipline": "OSINT", "access": "Social media monitoring. Accounts unvetted.", "startingGrade": "F", "trueReliability": 0.3, "controlledByAdversary": "partly", "postmortemNote": "Carried the MP's planted claim, and a wedding."},
   {"id": AD, "codeName": "Embassy admin", "discipline": "Admin", "access": "", "startingGrade": "A", "trueReliability": 1, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""},
   {"id": SEC, "codeName": "Security office", "discipline": "Admin", "access": "", "startingGrade": "A", "trueReliability": 1, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""},
   {"id": OS, "codeName": "OSINT cell", "discipline": "OSINT", "access": "", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""}],
 "reports": reports,
 "tellLabels": {"access-mismatch": "The reporter couldn't have known this", "conditional-gift": "The gift comes with a condition", "fishing": "Asks us to show our hand",
   "only-public-dates": "Matches only what anyone could look up", "convenient-timing": "Timing that's too convenient", "leak-origin": "Only the other side could have leaked it",
   "out-of-pattern": "Breaks his own pattern", "agenda-aligned": "Lines up with the reporter's own agenda", "circular-origin": "Already in print: one origin",
   "wrong-channel": "Wrong net and precedence for this kind of order", "too-on-message": "Says exactly what the adversary wants you to hear"},
 "scoring": {"call": {"low": [1, -1], "medium": [2, -2], "high": [3, -4]}, "evidence": {"true": 1, "noise": 0, "clutter": -1, "planted": -2}, "challenge": {"true": -1, "noise": 0, "clutter": 0, "planted": 1}, "maxEvidence": 3},
 "endings": [
   {"id": "burned", "tone": "bad", "title": "Burned", "points": -5, "if": {"everAt": "shared"}, "text": "Elsin arrests Vell on the morning of the vote. Six months later the ledger is exposed as a forgery built from his public schedule. Nobody in Kalsa trusts allied intelligence again. Kordav couldn't have bought a better outcome."},
   {"id": "sidelined", "tone": "bad", "title": "Sidelined", "points": -3, "if": {"assetAt": "caveated"}, "text": "The caveat leaked within a day and is quoted in the opposition's speech. Vell resigns \"to clear his name.\" Elsin's reformers lose their best voice, and Kordav never fired a shot."},
   {"id": "exposed", "tone": "good", "title": "Exposed", "points": 5, "if": {"assetAt": "countered", "since": [1, 2, 3, 4]}, "text": "Elsin's defence minister stands up in parliament with your warning: Kordav is running a smear, and its \"defector\" was sent. The motion fails by forty votes. LANTERN's statement never airs. Two Bureau officers are quietly recalled from the neutral capital, for real this time."},
   {"id": "survived", "tone": "warn", "title": "Survived", "points": 1, "if": {"assetAt": "countered"}, "text": "Your warning reaches Kalsa the night before the vote. The motion fails by three. Vell keeps his job and loses his reputation."},
   {"id": "shelved", "tone": "warn", "title": "Shelved", "points": 0, "default": True, "text": "You kept it to yourself. The opposition runs with the MP's claim anyway, and Vell survives by five votes without knowing how close it came or who was behind it."}],
 "dailyUpdates": [
   {"day": 1, "text": "Elsin's parliament will vote on a no-confidence motion against Deputy Defence Minister Aron Vell on the 12th."},
   {"day": 2, "text": "Debriefing continues. Elsin's opposition steps up its attacks on Vell."},
   {"day": 3, "text": "The no-confidence vote has been moved up to the 10th."},
   {"day": 4, "text": "Elsin's coalition partners say they'll decide how to vote \"on the evidence.\" The vote is the day after tomorrow."},
   {"day": 5, "text": "The vote is tomorrow morning."}],
 "postmortem": {
   "script": [
     {"days": [1], "text": "LANTERN walked in with a gift and a condition. He told you about IRON HARVEST, which was true and cost Kordav nothing: the operation had been blown for three months. The Vell allegation came from \"colleagues in the Bureau,\" and a planning officer doesn't see the Bureau's agent files."},
     {"days": [2], "text": "If you pressed him for details, room 412 came from a newspaper: The Kalsa Courier printed it three weeks before he walked in. His question about who could vouch for him was the second job he'd been sent to do: find out who we have in the ministry. And if you read the Bureau's headquarters net, you saw a recall that never happened. Kordav put it where it thought we were listening."},
     {"days": [3], "text": "The ledger was real paper telling a forged story. Every payment matched a trip anyone could look up. Real agents get paid on trips nobody announces."},
     {"days": [4], "text": "The deadline was Kordav's, not Elsin's. The MP heard about \"a defector\" from the only people who knew besides us."},
     {"days": [5], "text": "A man kidnapped by Western intelligence asked to record a press statement for the morning of the vote. Kordav stayed silent for four days, then announced a kidnapping. The Bureau's office in the neutral capital never so much as changed a code."}],
   "lessons": [
     "A walk-in's verifiable details prove access, not intent. Ask what they cost the other side.",
     "Check claims against access: what could he actually have seen?",
     "Count origins. A detail that's already in print isn't corroboration.",
     "Watch how the other side reacts, everywhere you can. Damage control is hard to fake on every channel at once.",
     "The adversary knows some of what you collect. Ask what it expects you to hear.",
     "Collection can be seen too. Asking the wrong source the wrong question can burn it."],
   "missedCollection": {
     "1": "The Bureau's office in the neutral capital (SIGINT) or LANTERN's family (OSINT): either shows that Kordav isn't doing any damage control.",
     "2": "Elsin's press (OSINT, 1 point): the newspaper story that \"room 412\" came from.",
     "3": "Questioning LANTERN on the ledger: he can't explain how a planner got into the Bureau's registry.",
     "4": "Anything still untasked on Kordav's reaction. It's the last tasking that can arrive before the vote.",
     "5": "Nothing tasked today could arrive in time."}},
 "pirs": [
   {"id": "PIR 1", "question": "Is LANTERN who he says he is, with the access he claims?", "targets": ["d-access", "finch", "ministry"]},
   {"id": "PIR 2", "question": "How is Kordav reacting to his disappearance?", "targets": ["bureau-hq", "bureau-office", "embassy", "family", "d-family"]},
   {"id": "PIR 3", "question": "Where does the allegation against Vell come from?", "targets": ["d-vell", "d-ledger", "press", "travel"]}],
 "targets": [
   {"id": "d-access", "name": "Question LANTERN: his access", "disciplines": ["HUMINT"], "closedWhen": "ended", "fallback": "The session on this went over old ground. Nothing new."},
   {"id": "d-vell", "name": "Question LANTERN: the Vell details", "disciplines": ["HUMINT"], "closedWhen": "ended", "fallback": "The session on this went over old ground. Nothing new."},
   {"id": "d-family", "name": "Question LANTERN: his family", "disciplines": ["HUMINT"], "closedWhen": "ended", "fallback": "The session on this went over old ground. Nothing new."},
   {"id": "d-ledger", "name": "Question LANTERN: the ledger", "disciplines": ["HUMINT"], "from": 3, "closedWhen": "ended", "fallback": "The session on this went over old ground. Nothing new."},
   {"id": "finch", "name": "FINCH, inside Kordav's defence ministry", "disciplines": ["HUMINT"], "cost": {"HUMINT": 3}, "delay": {"HUMINT": 2}, "source": {"HUMINT": FI}, "fallback": "No meeting with FINCH could be arranged in time."},
   {"id": "ministry", "name": "Kordav defence ministry, public records", "disciplines": ["OSINT"]},
   {"id": "bureau-hq", "name": "Bureau headquarters administrative net", "disciplines": ["SIGINT"]},
   {"id": "bureau-office", "name": "Bureau office in the neutral capital", "disciplines": ["SIGINT"]},
   {"id": "embassy", "name": "Kordav's embassy in the neutral capital", "disciplines": ["SIGINT"]},
   {"id": "family", "name": "LANTERN's family", "disciplines": ["OSINT"]},
   {"id": "press", "name": "Elsin's press", "disciplines": ["OSINT"]},
   {"id": "travel", "name": "Vell's travel records, via WREN", "disciplines": ["Liaison"]}],
 "collection": {"budget": 5, "costs": {"OSINT": 1, "Liaison": 0, "SIGINT": 3, "HUMINT": 2}, "delays": {},
   "sources": {"SIGINT": ME, "OSINT": OS, "HUMINT": ST, "Liaison": WR}, "fallback": "Nothing significant from {target}.",
   "note": "Questioning LANTERN is HUMINT at 2 points. A meeting with FINCH costs 3 and takes two days.",
   "burnRules": [{"sourceId": FI, "discipline": "HUMINT", "onFirstTasking": True,
     "text": "FINCH didn't come to the meeting. His signal site hasn't been serviced.",
     "readIn": "FINCH has reported, and has since missed his safety signal.",
     "postmortem": "The Bureau was watching the ministry for whoever came asking about LANTERN, which is what LANTERN's question on Day 2 was for. FINCH's meeting was seen. The ministry's public directory would have answered the same question for 1 point."}],
   "burnPoints": -2},
 "collectionResults": [
   {"id": "C-12", "discipline": "HUMINT", "target": "d-access", "from": 1, "to": 4},
   {"id": "C-10", "discipline": "HUMINT", "target": "d-vell", "from": 1, "to": 3},
   {"id": "C-13", "discipline": "HUMINT", "target": "d-family", "from": 1, "to": 3},
   {"id": "C-09", "discipline": "HUMINT", "target": "d-ledger", "from": 3, "to": 4},
   {"id": "C-04", "discipline": "HUMINT", "target": "finch", "from": 1, "to": 3},
   {"id": "C-08", "discipline": "OSINT", "target": "ministry", "from": 1, "to": 4},
   {"id": "C-06", "discipline": "SIGINT", "target": "bureau-hq", "from": 1, "to": 4},
   {"id": "C-11", "discipline": "SIGINT", "target": "bureau-hq", "from": 2, "to": 4},
   {"id": "C-01", "discipline": "SIGINT", "target": "bureau-office", "from": 1, "to": 4},
   {"id": "C-07", "discipline": "SIGINT", "target": "embassy", "from": 1, "to": 4},
   {"id": "C-02", "discipline": "OSINT", "target": "family", "from": 1, "to": 4},
   {"id": "C-03", "discipline": "OSINT", "target": "press", "from": 1, "to": 4},
   {"id": "C-05", "discipline": "Liaison", "target": "travel", "from": 1, "to": 4}],
 "credibility": {"start": 3, "min": 0, "max": 5,
   "levels": [
     {"id": "trusted", "label": "Trusted", "min": 3, "text": "She acts on your confidence as given, with your full collection budget."},
     {"id": "questioned", "label": "Questioned", "min": 2, "budgetDelta": -1, "text": "Her office trims your collection: 1 point less a day."},
     {"id": "discounted", "label": "Discounted", "min": 0, "budgetDelta": -2, "caution": 1, "text": "2 points less a day, and she treats your confidence as one step lower: High gets the Medium action, Medium the Low one."}],
   "triggers": [
     {"id": "rebuffed", "on": "event", "eventId": "early-counter-rebuffed", "delta": -2, "rule": "A warning she sent on your word is rebuffed", "note": "Credibility −2. She called an ally's witness a liar on your word after one interview, and Kalsa shut the door."},
     {"id": "withdrew-caveat", "on": "leave", "state": "caveated", "notTo": ["shared"], "delta": -1, "rule": "She has to withdraw a warning she passed on your word", "note": "Credibility −1. She had to withdraw the caveated warning she passed on your word. \"Their minister asked if we make a habit of this.\""},
     {"id": "withdrew-warning", "on": "leave", "state": "countered", "delta": -1, "rule": "She has to withdraw a smear warning", "note": "Credibility −1. She had to take back a warning to an ally."},
     {"id": "hedging", "on": "streak", "confidence": "low", "days": 2, "delta": -1, "rule": "Low confidence two days running (each further Low day too)", "note": "Credibility −1. Low again. \"If I wanted maybe, I'd read the newspapers.\""}],
   "outcome": {"exposed": 2, "survived": 0, "shelved": 0, "sidelined": -2, "burned": -2},
   "summary": "Marlowe can't see whether you're right until it's over. She can see when she has to take something back, and when you won't commit."},
 "board": {"pinsPerDay": 3},
}
# ---------- map: three capitals, drawn as a schematic ----------
EMB_L, EMB_S, KEMB, BOFF = (240, 62), (240, 102), (350, 52), (388, 100)      # neutral capital
BHQ, MIN, TV, HOME = (70, 262), (180, 256), (96, 350), (204, 338)             # Kordav's capital
PARL, SOREL, PRESS = (440, 272), (534, 292), (472, 348)                       # Kalsa
PINS = {
 "R-1-01": (EMB_S, "Walk-in at 0710, asks asylum"), "R-1-02": (EMB_L, "Describes IRON HARVEST"), "R-1-03": (EMB_L, "Alleges Vell is an agent"), "R-1-04": (PARL, "No-confidence vote set"),
 "R-2-01": (EMB_S, "Same story, unusually calm"), "R-2-02": (MIN, "Asks who can vouch for him"), "R-2-03": (TV, "State TV names Vell"),
 "R-3-01": (PARL, "Rumors of a traitor"), "R-3-02": (EMB_L, "Produces a ledger"), "R-3-03": (EMB_S, "Ledger matches public trips only"), "R-3-04": (PARL, "Vote moved up"),
 "R-4-01": (EMB_L, "Insists: before the vote"), "R-4-02": (HOME, "Now asks about his family"), "R-4-03": (PRESS, "MP posts about a defector"), "R-4-04": (TV, "State TV repeats the segment"),
 "R-5-01": (TV, "Kidnapping story"), "R-5-02": (EMB_S, "Wants a press statement"), "R-5-03": (PARL, "Motion cites allied intelligence"),
 "C-12": (EMB_L, "Questioned on his access"), "C-10": (EMB_L, "Gives room 412"), "C-09": (EMB_L, "Questioned on the ledger"), "C-13": (HOME, "Unworried about his wife"),
 "C-04": (MIN, "FINCH on LANTERN's job"), "C-08": (MIN, "Ministry directory"), "C-06": (BHQ, "Recall order on the admin net"), "C-11": (BHQ, "Recall never mentioned again"),
 "C-01": (BOFF, "Office traffic routine"), "C-07": (KEMB, "Embassy told to keep distance"), "C-02": (HOME, "Family life as normal"), "C-03": (PRESS, "Room 412 in print weeks ago"), "C-05": (SOREL, "Hotel meeting logged")}
for r in reports:
    if r["id"] in PINS: (x, y), label = PINS[r["id"]]; r["pin"] = {"x": x, "y": y, "label": label}
TPIN = {"d-access": EMB_L, "d-vell": EMB_L, "d-family": EMB_L, "d-ledger": EMB_L, "finch": MIN, "ministry": MIN, "bureau-hq": BHQ, "bureau-office": BOFF, "embassy": KEMB, "family": HOME, "press": PRESS, "travel": SOREL}
for t in crisis["targets"]: t["pin"] = {"x": TPIN[t["id"]][0], "y": TPIN[t["id"]][1]}
def site(name, xy, lx, ly): return {"name": name, "x": xy[0], "y": xy[1], "type": "town", "lx": xy[0] + lx, "ly": xy[1] + ly}
crisis["map"] = {
 "viewBox": [0, 0, 600, 420], "title": "Schematic of the three capitals",
 "caption": "Three capitals, not to scale. Reporting will be plotted here as it arrives.",
 "truthNote": "Red diamonds are what the Bureau was really doing on Day {day}.",
 "border": "M340,420 L322,350 L350,286 L318,206 L420,168 L500,100 L522,0",
 "areas": [{"d": "M118,0 L150,96 L258,154 L318,206 L420,168 L500,100 L522,0 Z", "label": "NEUTRAL STATE", "lx": 434, "ly": 20}],
 "zones": [{"x": 212, "y": 28, "w": 208, "h": 100, "label": "Neutral capital"}, {"x": 28, "y": 228, "w": 242, "h": 156, "label": "Kordav's capital"}, {"x": 404, "y": 236, "w": 178, "h": 140, "label": "Kalsa"}],
 "regions": [{"name": "KORDAV", "x": 40, "y": 412}, {"name": "ELSIN", "x": 452, "y": 408}],
 "places": [site("Our embassy", EMB_L, -22, 62), site("", EMB_S, 0, 0), site("Kordav embassy", KEMB, -34, -10), site("Bureau office", BOFF, -30, 20),
            site("Bureau HQ", BHQ, -30, -12), site("Defence ministry", MIN, -34, 20), site("State TV", TV, -24, 20), site("LANTERN's home", HOME, -48, 20),
            site("Parliament", PARL, -28, 20), site("Hotel Sorel", SOREL, -40, -12), site("Press", PRESS, -14, 20)],
 "legend": "Plots reporting as it arrives, not confirmed fact. Dashed pins are items you doubted. Dashed rings are today's taskings."}
U = lambda label, xy, dx=0, dy=-26: {"label": label, "x": xy[0] + dx, "y": xy[1] + dy}
truth_units = {
 1: [U("Bureau case officers", BOFF, 6, 34)],
 2: [U("Bureau case officers", BOFF, 6, 34), U("Ministry watch", MIN, 48, 36), U("Staged recall", BHQ, 0, 38)],
 3: [U("Ministry watch", MIN, 48, 36), U("Forged ledger", BHQ, 0, 38)],
 4: [U("Ministry watch", MIN, 48, 36), U("Leak to the MP", PARL, 40, 34)],
 5: [U("Kidnap script", TV, 34, -32), U("Statement rehearsed", EMB_S, 70, 8)]}
for g in crisis["groundTruth"]: g["units"] = truth_units[g["day"]]

# sanity: every result id has a report, every reveal id exists, every target is in a PIR
ids = {r["id"] for r in reports}
assert all(cr["id"] in ids for cr in crisis["collectionResults"])
assert all(i in ids for r in reports if r.get("reveal") for i in r["reveal"]["crossCheck"]["ids"])
tids = {t["id"] for t in crisis["targets"]}
assert tids == {t for p in crisis["pirs"] for t in p["targets"]} and all(cr["target"] in tids for cr in crisis["collectionResults"])
assert all(r["reveal"] for r in reports if r["kind"] == "planted")
keys = {r["reply"] for r in crisis["customerPolicy"]} | {"frozen", "rebuff"}
assert keys <= set(crisis["replies"]) and keys <= set(crisis["replyLabels"]), keys - set(crisis["replies"])
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "crises", "walk-in.json")
with open(out, "w") as f: json.dump(crisis, f, indent=2, ensure_ascii=False); f.write("\n")
print("wrote", os.path.normpath(out), len(reports), "reports,", sum(r["kind"] == "planted" for r in reports), "planted")
