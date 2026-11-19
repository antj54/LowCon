#!/usr/bin/env python3
"""Builds crises/vote-in-kalsa.json (Crisis 07). SPOILERS: this file holds the scenario's answers."""
import json, os

def R(id, day, src, disc, grade, cred, text, kind, note, tells=(), reveal=None, via=False, diagnostic=False, when=None):
    r = {"id": id, "day": day, "sourceId": src, "discipline": disc, "sourceGrade": grade, "credibility": cred, "text": text, "kind": kind,
         "supports": [], "contradicts": [], "tells": list(tells), "postmortemNote": note}
    if reveal: r["reveal"] = {"tell": reveal[0], "crossCheck": {"ids": reveal[1], "text": reveal[2]}, "motive": reveal[3]}
    if via: r["via"] = "collection"
    if diagnostic: r["diagnostic"] = True
    if when: r["when"] = when
    return r

EMB, WR, CO, CWS, KSB, SOC, HER, MER, OS, ESS, ADM = ("S-EMBASSY", "S-WREN", "S-COURIER", "S-CWS", "S-KSB", "S-SOCIAL", "S-HERON", "S-MERIDIAN", "S-OSINT", "S-ESS", "S-ADMIN")
LEAK_OPEN = {"recordStory": {"crisis": "damage-assessment", "flag": "leak", "in": ["open"]}}
LEAK_NOT_OPEN = {"notRecordStory": {"crisis": "damage-assessment", "flag": "leak", "in": ["open"]}}
def W(**kw): return dict(kw)

NOTE = "Last night's alliance note to Valde's office, built from your brief, went {route}. It said: \"{kj:%d}.\""
reports = [
 # ---- Day 1 ----
 R("R-1-01", 1, EMB, "Diplomatic", "B", 2, "The Highlands Party has given Valde a week: a public inquiry into {grievance}, or it leaves the coalition. Ekdal told our political officer she \"has not decided anything, and has not been asked to by anyone.\" {majority} {vell}", "true",
   "The grievance came from your own record. \"Has not been asked to by anyone\" was true."),
 R("R-1-02", 1, CWS, "OSINT", "B", 1, "About 3,000 people protested outside parliament in Kalsa this afternoon over {grievance}. Peaceful. Many came in by bus from the north.", "true", "Real anger, and real buses."),
 R("R-1-03", 1, KSB, "OSINT", "D", 3, "KSB: \"Elsin's people tire of foreign soldiers, and of foreign winters.\"", "noise", "Gloating."),
 R("R-1-04", 1, WR, "Liaison", "B", 2, "{wren}: \"Kordav's embassy in Kalsa has doubled its press staff this month and is buying advertising on Elsin's news sites.\"", "true",
   "Amplification, not engineering."),
 R("R-1-05", 1, ADM, "Admin", "A", 1, "Elsin's Ministry of Finance and Economy, which was the Ministry of Finance until last year, regrets that its new letterhead is still delayed. Correspondence on the old paper remains valid until the stock runs out.", "clutter",
   "The letterhead. Also the cross-check for R-2-03."),
 # ---- Day 2 ----
 R("R-2-01", 2, EMB, "Diplomatic", "B", 2, "Kask and Ekdal met last night for the first time in two years. Both say it was about farm subsidies.", "true", "Politics, not a plot."),
 R("R-2-02", 2, CWS, "OSINT", "B", 1, "About 12,000 protesters in Kalsa, with tractors from the north. A window was broken at the agriculture ministry. Police made four arrests.", "true", "The protests grew on their own."),
 R("R-2-03", 2, SOC, "OSINT", "F", 3, "A \"leaked bank document\" circulates widely: on the letterhead of Elsin's Ministry of Finance, it records a transfer of 2 million from a Kordavan \"Agrarian Fund\" to National Renewal.", "planted",
   "The bank document.", tells=["old-name"],
   reveal=("The letterhead of the Ministry of Finance, which has been the Ministry of Finance and Economy since last year.",
           ["R-1-05"], "The ministry was renamed last year (R-1-05). For one point, C-04 adds an account format Elsin's banks don't use, and an account created on the 26th.",
           "For the alliance to repeat it, and for Kask to wave the forgery on television the day after.")),
 R("R-2-04", 2, CO, "OSINT", "C", 2, "Kask, in an interview: \"Elsin's future will be decided in Elsin. Not in Kordav, and not by the alliance.\"", "true", "Kask is anti-everyone."),
 R("R-2-05", 2, ADM, "Admin", "A", 1, NOTE % 1, "true", "The note, and the road it took."),
 R("R-2-06", 2, EMB, "Diplomatic", "B", 3, "A source close to Valde's office tells our embassy, unprompted, that {claim:1}.", "planted",
   "Your own judgment, read back to you.", tells=["your-words"], when=W(**LEAK_OPEN, lastBrief={"hyp": ["H3"]}),
   reveal=("A source volunteers your own key judgment, in your own words.", ["R-2-05"], "That wording went to Valde's office last night, over LATTICE (R-2-05).",
           "Confirmation. It pushes a player who suspects a plot towards saying so in public.")),
 R("R-2-07", 2, EMB, "Diplomatic", "B", 3, "A source close to Valde's office says the alliance \"has it wrong\": Kordav's money is behind the Highlands Party, and Ekdal has been bought.", "planted",
   "An answer to a note it shouldn't have seen.", tells=["answers-note"], when=W(**LEAK_OPEN, lastBrief={"hyp": ["H1", "H2"]}),
   reveal=("The source answers last night's note, which only went to Valde's office.", ["R-2-05"], "The note crossed LATTICE (R-2-05). HERON (C-01) shows Ekdal decided on her own.",
           "To change your mind. Kordav wants you at H3.")),
 # ---- Day 3 ----
 R("R-3-01", 3, EMB, "Diplomatic", "B", 1, "At noon Ekdal took the Highlands Party out of the coalition. A motion of no confidence has been tabled for the morning of the 31st.", "true",
   "Ekdal left for her own reasons, on her own schedule.", diagnostic=True),
 R("R-3-02", 3, CWS, "OSINT", "B", 1, "The largest protest yet, about 40,000. Police used water cannon near parliament. Thirty people were hurt, two of them police officers.", "true", "The street at its peak."),
 R("R-3-03", 3, KSB, "OSINT", "D", 3, "KSB: \"The alliance's man Valde turns water cannon on his own farmers.\"", "noise", "Gloating."),
 R("R-3-04", 3, WR, "Liaison", "B", 2, "{wren}: \"Two of the protest's organisers took part in a Kordav-funded youth exchange ten years ago.\"", "noise", "True, and meaningless."),
 R("R-3-05", 3, ADM, "Admin", "A", 1, NOTE % 2, "true", "The note."),
 R("R-3-06", 3, EMB, "Diplomatic", "B", 3, "The same source close to Valde's office says that {claim:2}, and that this is \"what everyone in the prime minister's office believes.\"", "planted",
   "Your own judgment, read back to you.", tells=["your-words"], when=W(**LEAK_OPEN, lastBrief={"hyp": ["H3"]}),
   reveal=("Your own key judgment again, word for word.", ["R-3-05"], "That wording went over LATTICE last night (R-3-05).", "Confirmation.")),
 R("R-3-07", 3, EMB, "Diplomatic", "B", 3, "The same source says Ekdal's press conference \"was written in Kordav's embassy.\"", "planted",
   "Bait.", tells=["answers-note"], when=W(**LEAK_OPEN, lastBrief={"hyp": ["H1", "H2"]}),
   reveal=("The source keeps answering the note.", ["R-3-05"], "The note crossed LATTICE (R-3-05). HERON (C-01, C-02) shows the decision was Ekdal's.", "To change your mind.")),
 # ---- Day 4 ----
 R("R-4-01", 4, EMB, "Diplomatic", "B", 2, "Valde won't resign; he'll face the vote. Kask and Ekdal are close to a deal. Her price is the inquiry and the agriculture ministry.", "true", "A domestic price."),
 R("R-4-02", 4, SOC, "OSINT", "F", 3, "Photos posted overnight claim to show the protest organisers \"at a Kordavan training camp.\" The men in the photos are in winter coats, and there is snow on the ground behind them.", "planted",
   "The camp photos.", tells=["wrong-season"],
   reveal=("Winter coats and snow, in May.", ["R-4-04"], "Kalsa reached 29°C the same day (R-4-04).", "A public accusation that falls apart within a day is worth more to Kordav than any plot.")),
 R("R-4-03", 4, CO, "OSINT", "C", 2, "A poll for the Courier: 58% want a new government. 61% want Task Force VEYL to stay.", "true",
   "A government falling isn't a country leaving.", diagnostic=True),
 R("R-4-04", 4, ADM, "Admin", "A", 1, "The embassy's air conditioning has failed in the heat. Kalsa reached 29°C today. Staff may remove their ties.", "clutter", "The heat. Also the cross-check for R-4-02."),
 R("R-4-05", 4, ADM, "Admin", "A", 1, NOTE % 3, "true", "The note."),
 R("R-4-06", 4, EMB, "Diplomatic", "B", 3, "The same source repeats that {claim:3}, and adds that \"the alliance should say so before it's too late.\"", "planted",
   "Your own judgment, read back to you, with advice.", tells=["your-words"], when=W(**LEAK_OPEN, lastBrief={"hyp": ["H3"]}),
   reveal=("Your own words again, now with a recommendation.", ["R-4-05"], "That wording went over LATTICE last night (R-4-05).", "To get the alliance to speak.")),
 R("R-4-07", 4, EMB, "Diplomatic", "B", 3, "The same source says Kordavan money is paying for the protesters' buses.", "planted",
   "Bait.", tells=["answers-note"], when=W(**LEAK_OPEN, lastBrief={"hyp": ["H1", "H2"]}),
   reveal=("The source answers the note again.", ["R-4-05"], "The note crossed LATTICE (R-4-05). The funding (C-03) is a farmers' union and a transport union.", "To change your mind.")),
 # ---- Day 5 ----
 R("R-5-01", 5, EMB, "Diplomatic", "B", 1, "Kask and Ekdal have signed a coalition agreement. Kask, at the signing: \"We will review the task force agreement. Review, not end.\"", "true", "Review, not end."),
 R("R-5-02", 5, KSB, "OSINT", "D", 3, "KSB: \"Tomorrow Elsin chooses: sovereignty, or occupation.\"", "noise", "Gloating."),
 R("R-5-03", 5, CWS, "OSINT", "B", 1, "The protest organisers have called off tomorrow's march \"to let parliament decide.\"", "true", "The street stood down."),
 R("R-5-04", 5, ADM, "Admin", "A", 1, NOTE % 4, "true", "The note."),
 R("R-5-05", 5, EMB, "Diplomatic", "B", 3, "The same source repeats that {claim:4}, and says the prime minister \"is waiting for the alliance to speak.\"", "planted",
   "Your own judgment, read back to you.", tells=["your-words"], when=W(**LEAK_OPEN, lastBrief={"hyp": ["H3"]}),
   reveal=("Your own words, a fourth time.", ["R-5-04"], "That wording went over LATTICE last night (R-5-04).", "To get the alliance to speak on the last day.")),
 R("R-5-06", 5, EMB, "Diplomatic", "B", 3, "The same source says Kask will expel the task force within a month of taking office.", "planted",
   "Bait.", tells=["answers-note"], when=W(**LEAK_OPEN, lastBrief={"hyp": ["H1", "H2"]}),
   reveal=("The source answers the note again.", ["R-5-04", "R-5-01"], "The note crossed LATTICE (R-5-04), and Kask said \"review, not end\" the same day (R-5-01).", "To change your mind.")),
 # ---- collection ----
 R("C-01", None, HER, "HUMINT", "C", 2, "HERON: Ekdal decided after three weeks of meetings in her own constituency, where nobody has forgiven anyone. She dislikes Kask, and says she will vote against Valde anyway.", "true",
   "Ekdal decided on her own.", via=True, diagnostic=True),
 R("C-02", None, HER, "HUMINT", "C", 2, "HERON: Ekdal's deal with Kask is the inquiry, the agriculture ministry and a promise not to touch the task force for a year. HERON has seen the draft. Nothing in it mentions Kordav or money.", "true",
   "A domestic deal that protects the task force.", via=True, diagnostic=True),
 R("C-03", None, OS, "OSINT", "B", 1, "Small donations, a farmers' union and a transport union pay for the buses. One account linked to a Kordavan grain trader gave about a thousandth of the total.", "true",
   "Real money, and a token Kordavan amount.", via=True, diagnostic=True),
 R("C-04", None, OS, "OSINT", "B", 1, "The letterhead uses the ministry's old name, dropped last year, and an account-number format Elsin's banks don't use. The document was first posted by an account created on the 26th.", "true",
   "A forgery.", via=True),
 R("C-05", None, MER, "SIGINT", "B", 2, "Bureau instruction to its Kalsa team: \"Amplify. Don't touch the vote; it will fall on its own. What we need is the alliance saying the word Kordav in public.\"", "true",
   "The Bureau's plan, in its own words.", via=True, diagnostic=True),
 R("C-06", None, OS, "OSINT", "B", 1, "National Renewal's donors are mostly Elsin businessmen. One is a grain importer who trades with Kordav. Everything is declared.", "noise",
   "Tempting, and nothing.", via=True),
 R("C-07", None, ESS, "Liaison", "B", 2, "Elsin's security service: the organisers are local, a farmers' union and a students' group. No foreign links found.", "true", "Local organisers.", via=True),
 R("C-07K", None, KSB, "OSINT", "D", 1, "KSB, in passing: \"Valde's police now investigate peaceful farmers at the alliance's request.\"", "true",
   "The request crossed LATTICE and was used against Valde.", via=True),
 R("C-08", None, OS, "OSINT", "B", 1, "With the Highlands Party, Valde survives any motion. Without it, a motion passes.", "true", "Arithmetic.", via=True, diagnostic=True),
]

levels = {"home": {"label": "nothing yet", "rank": 0}, "channel": {"label": "a quiet channel to the opposition", "rank": 0},
          "handsoff": {"label": "committed to respect the vote", "rank": 0}, "restraint": {"label": "urged police restraint", "rank": 0},
          "postpone": {"label": "asked for the vote to be postponed", "rank": 0}, "warnpriv": {"label": "warned Valde privately", "rank": 0},
          "warnpub": {"label": "warned publicly about Kordav", "rank": 0}}
HI, MED = ["high"], ["medium"]
policy = [
 {"if": {"hypothesis": "H1", "confidence": HI, "assetAt": "handsoff"}, "reply": "stands"},
 {"if": {"hypothesis": "H1", "confidence": HI, "days": [1, 2]}, "to": "handsoff", "reply": "handsoff_early", "sends": True},
 {"if": {"hypothesis": "H1", "confidence": HI}, "to": "handsoff", "reply": "handsoff", "sends": True},
 {"if": {"hypothesis": "H1", "confidence": MED, "assetAt": ["channel", "handsoff"]}, "reply": "stands"},
 {"if": {"hypothesis": "H1", "confidence": MED}, "to": "channel", "reply": "channel", "sends": True},
 {"if": {"hypothesis": "H2", "confidence": HI, "assetAt": "postpone"}, "reply": "stands"},
 {"if": {"hypothesis": "H2", "confidence": HI}, "to": "postpone", "reply": "postpone", "sends": True},
 {"if": {"hypothesis": "H2", "confidence": MED, "assetAt": "restraint"}, "reply": "stands"},
 {"if": {"hypothesis": "H2", "confidence": MED}, "to": "restraint", "reply": "restraint", "sends": True},
 {"if": {"hypothesis": "H3", "confidence": HI, "assetAt": "warnpub"}, "reply": "stands"},
 {"if": {"hypothesis": "H3", "confidence": HI}, "to": "warnpub", "reply": "warnpub", "sends": True},
 {"if": {"hypothesis": "H3", "confidence": MED, "assetAt": "warnpriv"}, "reply": "stands"},
 {"if": {"hypothesis": "H3", "confidence": MED}, "to": "warnpriv", "reply": "warnpriv", "sends": True},
 {"if": {}, "reply": "listen"}]
replies = {
 "handsoff": "I've said we'll work with whoever parliament chooses. Kask's people have asked for a meeting.",
 "handsoff_early": "I've said we'll work with whoever parliament chooses. Valde called. He wanted to know when we'd decided he was finished.",
 "channel": "The embassy has had coffee with Kask's foreign affairs man. Nothing promised.",
 "postpone": "I've asked Valde to postpone. He's thinking about it, which in Kalsa means yes.",
 "restraint": "The embassy has asked Elsin's police for restraint. Politely.",
 "warnpub": "I've said it in public: Kordav is interfering in Elsin's politics. The press here liked that very much.",
 "warnpriv": "Valde has it in tonight's note. He says he'll look into it.",
 "listen": "That's a shrug. Kalsa isn't waiting for us.",
 "stands": "That stands.", "frozen": "Not today.",
 "postponed_next": "Valde postponed. The organisers called it an alliance decision, and twice as many came out last night.",
 "backlash": "Kask spent the evening on television with my statement. He calls it \"the alliance choosing Elsin's government.\" The Courier agrees with him.",
 "overheard_ksb": "KSB led the news with it: \"The alliance whispers to Valde that his opponents are Kordav's.\" It quoted the note.",
 "overheard_police": "Valde's police questioned two of the organisers last night, on our warning. They've told the Courier."}
labels = {"handsoff": "Commits to respect the vote, and talks to the opposition", "handsoff_early": "Commits to respect the vote, before the coalition breaks",
 "channel": "Opens a quiet channel to the opposition", "postpone": "Asks Valde to postpone the vote", "restraint": "Urges police restraint",
 "warnpub": "Warns publicly about Kordav", "warnpriv": "Warns Valde privately", "listen": "Does nothing", "stands": "Nothing new. It stands", "frozen": "Can't act yet",
 "postponed_next": "The postponement backfires", "backlash": "The public warning backfires", "overheard_ksb": "The private warning is on Kordav's television", "overheard_police": "The private warning reaches the press"}

crisis = {
 "id": "vote-in-kalsa", "formatVersion": "1.3", "title": "The Vote in Kalsa", "crisisNumber": "07", "days": 5,
 "dayLabels": ["the 26th", "the 27th", "the 28th", "the 29th", "the 30th"],
 "placeholderNote": "Kordav, Elsin, Marrat and Pellaria are fictional countries. All politicians, parties and officials are fictional.",
 "adversary": "Kordav", "endingEyebrow": "Kalsa, the morning of the 31st", "frozenText": "",
 "vars": {
   "grievance": [{"when": {"recordEnding": {"crisis": "border-buildup", "in": ["seized"]}}, "text": "Tarsk Dam, and the government that lost it"},
                 {"when": {"recordEnding": {"crisis": "lights-out", "in": ["clean", "clean-cold"]}}, "text": "the January blackouts"},
                 {"when": {"recordFlag": {"crisis": "southern-line", "event": "tolen", "in": ["cut", "cut_far"]}}, "text": "Marrat's guards on the Southern Line"},
                 {"text": "food and fuel prices"}],
   "majority": [{"when": {"allianceAtLeast": 1}, "text": "Without the Highlands Party, Valde would be four votes short."},
                {"when": {"allianceAtMost": -1}, "text": "Without the Highlands Party, Valde would be one vote short, and two of his own members have stopped answering his calls."},
                {"text": "Without the Highlands Party, Valde would be two votes short."}],
   "vell": [{"when": {"recordEnding": {"crisis": "walk-in", "in": ["sidelined"]}}, "text": "Vell's replacement as Deputy Defence Minister, Dag Hollis, won't say whether he supports the task force."},
            {"when": {"recordEnding": {"crisis": "walk-in", "in": ["burned"]}}, "text": "Vell is still awaiting trial. His replacement, Dag Hollis, won't say whether he supports the task force."},
            {"when": {"recordEnding": {"crisis": "walk-in", "in": ["exposed", "survived", "shelved"]}}, "text": "Deputy Defence Minister Aron Vell is the coalition's loudest supporter of the task force."},
            {"text": ""}],
   "wren": [{"when": {"recordStory": {"crisis": "damage-assessment", "flag": "wrongName", "in": ["rhun"]}}, "text": "Lt. Col. N. Ahrend, who replaced Col. Rhun"},
            {"text": "Col. Rhun"}],
   "route": [{"when": LEAK_OPEN, "text": "over LATTICE"}, {"text": "by courier"}]},
 "briefing": {"dateLine": "Late May. Day 1 is the 26th.", "situation": [
   "Elsin's coalition government is in trouble. Prime Minister Henrik Valde governs with the Highlands Party, a rural party from the north led by Sanna Ekdal, and his majority is thin. Ekdal's voters are angry, and so are the crowds outside parliament.",
   "The opposition is led by Ruben Kask of National Renewal, who says Elsin should decide its own future \"without Kordav or the alliance.\" A government led by Kask would have to decide whether Task Force VEYL stays.",
   "Kordav's broadcaster is enjoying itself.",
   "The alliance keeps Valde's office informed about Kordavan activity in a short note each evening, drawn from your brief. Liaison requests go to Kalsa over LATTICE, unless the link is shut."]},
 "customer": {"name": "Under Secretary H. Marlowe", "short": "Marlowe", "pronouns": ["she", "her"], "role": "Under Secretary for alliance affairs", "callsign": "USEC ALLIANCE",
   "wants": "Is this Elsin's business, or Kordav's, and what should the alliance do?",
   "context": "Her public steps can't be undone, and some quiet ones may not stay quiet.",
   "tipLine": "High is public. Medium is quiet. Low changes nothing."},
 "opening": {"text": "Valde's government is in trouble. Tell me whose trouble it is.",
   "reassigned": "A new cell, and an old government in trouble. Tell me whose trouble it is.",
   "byTone": {"good": "You were right about the link when nobody wanted you to be. Now Kalsa is wobbling, and everyone in my building has a theory. I'd like yours.",
              "bad": "We got the last one wrong, and Kalsa remembers. This one is about Kalsa. Tell me whose business it is.",
              "warn": "Valde's government is in trouble. Tell me whose trouble it is."}},
 "asset": {"id": "stance", "name": "What the alliance has done", "levels": levels},
 "customerPolicy": policy,
 "policySummary": [
   {"brief": "H1 at High", "action": "Says publicly the alliance will work with whatever government parliament chooses, and opens talks with the opposition"},
   {"brief": "H1 at Medium", "action": "Quietly opens a channel to the opposition, through the embassy"},
   {"brief": "H2 at High", "action": "Asks Valde to postpone the vote until the streets are calm. Can't be undone."},
   {"brief": "H2 at Medium", "action": "Urges Elsin's police, through the embassy, to show restraint"},
   {"brief": "H3 at High", "action": "Warns publicly that Kordav is interfering in Elsin's politics. Can't be undone."},
   {"brief": "H3 at Medium", "action": "Warns Valde privately, in the evening note to his office"},
   {"brief": "Anything at Low", "action": "Nothing"}],
 "policyNote": "Her public steps can't be undone, and some quiet ones may not stay quiet.",
 "replyLabels": labels, "replies": replies,
 "events": [
   {"id": "postponed", "onEnter": "postpone", "effect": {}, "replyId": "postponed_next", "note": "", "points": 0},
   {"id": "backlash", "onEnter": "warnpub", "effect": {}, "replyId": "backlash", "note": "", "points": 0},
   {"id": "overheard-ksb", "onEnter": "warnpriv", "if": {"when": LEAK_OPEN}, "effect": {}, "replyId": "overheard_ksb", "note": "", "points": 0},
   {"id": "overheard-police", "onEnter": "warnpriv", "if": {"when": LEAK_NOT_OPEN}, "effect": {}, "replyId": "overheard_police", "note": "", "points": 0},
   {"id": "talks", "atStartOfDay": 5, "outcomes": [
     {"if": {"assetAt": ["channel", "handsoff"]}, "flag": "open", "points": 0, "title": "Talks with the opposition are open", "pointsLabel": "talks with the opposition"},
     {"if": {}, "flag": "closed", "points": 0, "title": "No talks with the opposition", "pointsLabel": "talks with the opposition"}]}],
 "hypotheses": [
   {"id": "H1", "short": "By the vote", "text": "The coalition is breaking over its own grievance, and parliament will bring the government down.", "claim": "the coalition is breaking over its own grievance, and parliament will bring the government down"},
   {"id": "H2", "short": "By the street", "text": "The protests will force the government out before parliament can.", "claim": "the protests will force the government out before parliament can"},
   {"id": "H3", "short": "Something planned", "text": "Kordav is engineering the fall, to get a government that will send the task force home.", "claim": "Kordav is engineering the fall, to get a government that will send the task force home"}],
 "groundTruth": [
   {"day": 1, "trueHypothesis": "H1", "bestCall": "H1 at Low", "state": "Ekdal has spent three weeks in her constituency and has decided to leave. Kordav's embassy doubles its press staff to amplify."},
   {"day": 2, "trueHypothesis": "H1", "bestCall": "H1 at Medium", "state": "The protests grow on their own money. The Bureau posts a forged bank document, meant to be repeated by the alliance and then exposed."},
   {"day": 3, "trueHypothesis": "H1", "bestCall": "H1 at High (Medium is defensible)", "state": "Ekdal leaves. The motion is tabled. The biggest protest, and the only violence."},
   {"day": 4, "trueHypothesis": "H1", "bestCall": "H1 at High", "state": "Ekdal and Kask negotiate. The Bureau posts recycled winter photos of organisers at a Kordavan camp."},
   {"day": 5, "trueHypothesis": "H1", "bestCall": "H1 at High", "state": "The deal is signed. The organisers call off the march."}],
 "adversaryPlan": [
   {"phase": "Make the alliance say \"Kordav\" in public", "days": [1, 2, 3, 4, 5], "wantsYouToBelieve": "H3", "summary": "Amplify a fall that would happen anyway, plant evidence that can be debunked, and, if the link is open, feed the alliance its own words.", "channels": [SOC, KSB, EMB]}],
 "sources": [
   {"id": EMB, "codeName": "EMBASSY", "discipline": "Diplomatic", "access": "Our embassy's political section in Kalsa", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": "partly", "postmortemNote": "Accurate, except the walk-up \"source close to Valde\", who was the Bureau's."},
   {"id": WR, "codeName": "WREN", "discipline": "Liaison", "access": "Elsin's military intelligence liaison desk. Politics isn't its brief, Kordav is.", "startingGrade": "B", "trueReliability": 0.85, "controlledByAdversary": False, "postmortemNote": "True, and once misleading."},
   {"id": CO, "codeName": "COURIER", "discipline": "OSINT", "access": "The Kalsa Evening Courier, Elsin's biggest paper", "startingGrade": "C", "trueReliability": 0.8, "controlledByAdversary": False, "postmortemNote": "The poll was the most important number in the scenario."},
   {"id": CWS, "codeName": "CWS", "discipline": "OSINT", "access": "Continental Wire Service", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Straight."},
   {"id": KSB, "codeName": "KSB", "discipline": "OSINT", "access": "Kordav State Broadcaster", "startingGrade": "D", "trueReliability": None, "controlledByAdversary": True, "postmortemNote": "Noise and gloating."},
   {"id": SOC, "codeName": "SOCIAL", "discipline": "OSINT", "access": "Forums and social media. Unvetted.", "startingGrade": "F", "trueReliability": 0.3, "controlledByAdversary": "partly", "postmortemNote": "Carried both forgeries."},
   {"id": HER, "codeName": "HERON", "discipline": "HUMINT", "access": "A staffer in the Highlands Party. New. Don't task her two days running.", "startingGrade": "C", "trueReliability": 0.85, "controlledByAdversary": False, "postmortemNote": "The best source on Ekdal."},
   {"id": MER, "codeName": "MERIDIAN", "discipline": "SIGINT", "access": "Tasked coverage only.", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "postmortemNote": "Reliable."},
   {"id": OS, "codeName": "OSINT cell", "discipline": "OSINT", "access": "", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""},
   {"id": ESS, "codeName": "Elsin security service", "discipline": "Liaison", "access": "", "startingGrade": "B", "trueReliability": 0.9, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""},
   {"id": ADM, "codeName": "Cell admin", "discipline": "Admin", "access": "", "startingGrade": "A", "trueReliability": 1, "controlledByAdversary": False, "rosterHidden": True, "postmortemNote": ""}],
 "reports": reports,
 "tellLabels": {"old-name": "Uses a name that changed last year", "wrong-season": "The wrong season", "your-words": "Your own words, coming back", "answers-note": "Answers a message it shouldn't have seen"},
 "scoring": {"call": {"low": [1, -1], "medium": [2, -2], "high": [3, -4]}, "evidence": {"true": 1, "noise": 0, "clutter": -1, "planted": -2}, "challenge": {"true": -1, "noise": 0, "clutter": 0, "planted": 1}, "maxEvidence": 3},
 "endings": [
   {"id": "meddled", "tone": "bad", "title": "Meddled", "points": -5, "if": {"everAt": "warnpub"},
    "text": "The motion passes, and Kask's first speech as prime minister is about \"the alliance choosing Elsin's government.\" He asks for the task force to be halved by the autumn.",
    "changedBy": "Saying nothing in public about Kordav. The fall was Elsin's own, and the accusation was what Kordav wanted."},
   {"id": "postponed", "tone": "bad", "title": "Postponed", "points": -3, "if": {"everAt": "postpone"},
    "text": "The vote happens a week late, after a week of riots blamed on the alliance. Kask wins it by more than he would have.",
    "changedBy": "Letting parliament vote. The street was standing down by the last day."},
   {"id": "overheard", "tone": "warn", "title": "Overheard", "points": -2, "if": {"everAt": "warnpriv"},
    "text": "Kask governs with a grudge, and Valde's last week is remembered as a hunt for a plot that wasn't there.",
    "changedBy": "Not warning Valde about a plot that wasn't there. A private warning doesn't stay private when someone else is reading the note."},
   {"id": "hands-off", "tone": "good", "title": "Hands off", "points": 5, "if": {"assetAt": "handsoff", "since": [3, 4, 5], "flag": {"event": "talks", "in": ["open"]}},
    "text": "The motion passes. Kask's first call is to the embassy. The task force agreement is reviewed over the summer, and survives with a new name."},
   {"id": "kept-out", "tone": "warn", "title": "Kept out of it", "points": 2, "default": True,
    "text": "The motion passes. Kask's government is polite and distant, and the review takes a year.",
    "changedBy": "A quiet channel to the opposition before the last day, and a public commitment to respect the vote once the coalition had broken."}],
 "dailyUpdates": [
   {"day": 1, "text": "A confidence motion against Valde's government is being talked about in the corridors. Nothing has been tabled."},
   {"day": 2, "text": "The protests are growing."},
   {"day": 3, "text": "Ekdal has called a press conference for noon."},
   {"day": 4, "text": "The vote is two days away."},
   {"day": 5, "text": "Parliament votes tomorrow morning."}],
 "postmortem": {
   "script": [
     {"days": [1], "text": "The Highlands Party gave Valde a week over a grievance its voters had carried all year. Kordav's embassy hired more press officers."},
     {"days": [2], "text": "Kask and Ekdal talked. A bank document appeared on a letterhead that hasn't existed since last year."},
     {"days": [3], "text": "Ekdal left the coalition. Forty thousand people came out, and the police used water cannon."},
     {"days": [4], "text": "Photos of organisers at a Kordavan camp showed snow, on a 29-degree day. Most of Elsin wanted a new government and the same task force."},
     {"days": [5], "text": "Ekdal and Kask signed. The march was called off."}],
   "lessons": [
     "Not everything bad is the adversary's doing. Sometimes it's just a coalition.",
     "An adversary can want to be accused. Ask who gains from your statement, not only from the event.",
     "Your own assessment, quoted back to you by someone who shouldn't have read it, isn't corroboration. It's a leak.",
     "A government falling isn't a country leaving.",
     "Hands off isn't the same as eyes shut."],
   "missedCollection": {
     "1": "HERON: Ekdal had already decided, on her own.",
     "2": "Bureau traffic about Kalsa (SIGINT): the Bureau's plan, in its own words.",
     "3": "HERON again (not two days running): the deal is domestic.",
     "4": "The protests' funding (OSINT, one point).",
     "5": "Nothing tasked today could arrive in time."},
   "callouts": [
     {"title": "That source was quoting you", "if": {"cited": ["R-2-06", "R-3-06", "R-4-06", "R-5-05", "R-2-07", "R-3-07", "R-4-07", "R-5-06"]},
      "text": "The \"source close to Valde's office\" was the Bureau, reading the evening note over LATTICE and answering it. Its words were your own, or a reply to them."}]},
 "pirs": [
   {"id": "PIR 1", "question": "Why is the coalition breaking?", "targets": ["heron", "whip-count"]},
   {"id": "PIR 2", "question": "Who is behind the protests?", "targets": ["funding", "security-service"]},
   {"id": "PIR 3", "question": "What is Kordav doing?", "targets": ["bureau-traffic", "kask-finances", "document"]}],
 "targets": [
   {"id": "heron", "name": "HERON, in the Highlands Party", "disciplines": ["HUMINT"], "fallback": "HERON had nothing new."},
   {"id": "whip-count", "name": "The whip count for a confidence vote", "disciplines": ["OSINT"], "until": 4},
   {"id": "funding", "name": "The protests' funding", "disciplines": ["OSINT"], "until": 4},
   {"id": "security-service", "name": "Ask Elsin's security service about the organisers", "disciplines": ["Liaison"], "until": 4},
   {"id": "bureau-traffic", "name": "Bureau traffic about Kalsa", "disciplines": ["SIGINT"], "until": 4},
   {"id": "kask-finances", "name": "Kask's party finances", "disciplines": ["OSINT"], "until": 4},
   {"id": "document", "name": "The \"Kordav money\" document", "disciplines": ["OSINT"], "from": 2, "until": 4}],
 "collection": {"budget": 5, "costs": {"HUMINT": 3, "SIGINT": 3, "OSINT": 1, "Liaison": 0}, "delays": {},
   "sources": {"HUMINT": HER, "SIGINT": MER, "OSINT": OS, "Liaison": ESS}, "fallback": "Nothing significant at {target}.",
   "note": "Liaison requests go to Kalsa over LATTICE, unless the link is shut.",
   "burnRules": [{"sourceId": HER, "discipline": "HUMINT", "consecutiveDays": 2, "text": "HERON has stopped answering.",
     "postmortem": "HERON was tasked two days running. A party staffer who keeps slipping out to make calls during a coalition crisis gets noticed."}],
   "burnPoints": -2},
 "collectionResults": [
   {"id": "C-01", "discipline": "HUMINT", "target": "heron", "from": 1, "to": 2},
   {"id": "C-02", "discipline": "HUMINT", "target": "heron", "from": 3, "to": 5},
   {"id": "C-03", "discipline": "OSINT", "target": "funding", "from": 1, "to": 4},
   {"id": "C-04", "discipline": "OSINT", "target": "document", "from": 2, "to": 4},
   {"id": "C-05", "discipline": "SIGINT", "target": "bureau-traffic", "from": 1, "to": 4},
   {"id": "C-06", "discipline": "OSINT", "target": "kask-finances", "from": 1, "to": 4},
   {"id": "C-07", "discipline": "Liaison", "target": "security-service", "from": 1, "to": 4, "then": {"id": "C-07K", "after": 1, "when": LEAK_OPEN}},
   {"id": "C-08", "discipline": "OSINT", "target": "whip-count", "from": 1, "to": 4}],
 "credibility": {"start": 3, "min": 0, "max": 5, "bonusAt": 5,
   "levels": [
     {"id": "trusted", "label": "Trusted", "min": 3, "text": "She acts on your confidence as given, with your full collection budget."},
     {"id": "questioned", "label": "Questioned", "min": 2, "budgetDelta": -1, "text": "Her office trims your collection: 1 point less a day."},
     {"id": "discounted", "label": "Discounted", "min": 0, "budgetDelta": -2, "caution": 1, "text": "2 points less a day, and she treats your confidence as one step lower."}],
   "triggers": [
     {"id": "early", "on": "reply", "reply": "handsoff_early", "delta": -1, "rule": "She commits to the vote before the coalition has broken", "note": "Credibility −1. Valde wanted to know when we'd decided he was finished."},
     {"id": "postponed", "on": "event", "eventId": "postponed", "delta": -1, "rule": "A postponement she asked for backfires", "note": "Credibility −1."},
     {"id": "backlash", "on": "event", "eventId": "backlash", "delta": -2, "rule": "A public warning she made on your word backfires", "note": "Credibility −2."},
     {"id": "overheard-ksb", "on": "event", "eventId": "overheard-ksb", "delta": -1, "rule": "A private warning becomes public", "note": "Credibility −1."},
     {"id": "overheard-police", "on": "event", "eventId": "overheard-police", "delta": -1, "rule": "A private warning becomes public", "note": "Credibility −1."},
     {"id": "hedging", "on": "streak", "confidence": "low", "days": 2, "delta": -1, "rule": "Low confidence two days running (each further Low day too)", "note": "Credibility −1. \"Kalsa isn't waiting for us.\""}],
   "outcome": {"hands-off": 1, "meddled": -1},
   "summary": "Marlowe can see what her statements cause. She can't see whether you're right about who's behind it."},
 "board": {"pinsPerDay": 3},
 "record": {"grades": []},
 "story": {
   "values": [
     {"value": "alliance", "delta": 1, "if": {"ending": "hands-off"}},
     {"value": "alliance", "delta": -1, "if": {"ending": ["overheard", "postponed"]}},
     {"value": "alliance", "delta": -2, "if": {"ending": "meddled"}},
     {"value": "pressure", "delta": 1, "if": {"ending": ["postponed", "meddled"]}},
     {"value": "alliance", "delta": -1, "if": {"collected": "C-07K"}}],
   "flags": [
     {"flag": "kask", "value": "talks", "if": {"ending": "hands-off"}},
     {"flag": "kask", "value": "distant", "if": {"ending": "kept-out"}},
     {"flag": "kask", "value": "grudge", "if": {"ending": ["overheard", "postponed"]}},
     {"flag": "kask", "value": "halved", "if": {"ending": "meddled"}}],
   "caseFile": [
     {"tag": "own-words", "text": "Your own judgment came back to you from a source in Kalsa.", "if": {"cited": ["R-2-06", "R-3-06", "R-4-06", "R-5-05", "R-2-07", "R-3-07", "R-4-07", "R-5-06"]}},
     {"tag": "say-kordav", "text": "The Bureau wanted the alliance to say \"Kordav\" in public.", "if": {"collected": "C-05"}}]},
 "analysts": [
   {"id": "vasko", "name": "Imre Vasko", "specialty": "Regional analyst", "reveal": "Anchors on his first theory. After the damage assessment he saw Kordav in everything. Right once, about the cancelled march."},
   {"id": "halden", "name": "Noor Halden", "specialty": "Technical analyst (signals, imagery, forensics)", "reveal": "Slow but careful. Never wrong. The letterhead and the snow, each a day late."},
   {"id": "marrow", "name": "Tess Marrow", "specialty": "Open-source analyst", "extra": True, "reveal": "She reads crowds and polls, and was right every time. Her best scenario."}],
}
def N(a, item, text, right, why, after=0): return {"analyst": a, "item": item, "after": after, "text": text, "right": right, "why": why}
crisis["notes"] = [
 N("marrow", "R-1-02", "Three thousand on a weekday is real anger. Nobody pays people to stand in the rain for that.", 1, "Real anger."),
 N("vasko", "R-1-04", "Doubling the press staff is how it starts.", 0, "It's how amplifying starts."),
 N("vasko", "R-2-03", "There's the money.", 0, "A forgery."),
 N("marrow", "R-2-04", "Kask's line is anti-everyone. Kordav won't like that as much as it thinks it does.", 1, "Review, not end."),
 N("halden", "R-2-03", "The letterhead says Ministry of Finance. It hasn't been called that since last year.", 1, "The tell.", 1),
 N("vasko", "R-3-04", "Ten years ago. They plan long.", 0, "A youth exchange."),
 N("marrow", "R-3-04", "A youth exchange ten years ago isn't a recruitment.", 1, "It wasn't."),
 N("vasko", "R-4-03", "Polls lie in May.", 0, "This one didn't."),
 N("marrow", "R-4-03", "Sixty-one percent want the task force to stay. That's the number.", 1, "It was."),
 N("halden", "R-4-02", "There's snow on the ground in that photo. It's May.", 1, "The tell.", 1),
 N("vasko", "R-5-03", "If they're calling off the march, they think they've already won in parliament.", 1, "They had.")]

# ---------- sanity ----------
ids = {r["id"] for r in reports}
assert len(ids) == len(reports)
assert all(cr["id"] in ids for cr in crisis["collectionResults"]) and all(n["item"] in ids for n in crisis["notes"]) and "C-07K" in ids
assert all(i in ids for r in reports if r.get("reveal") for i in r["reveal"]["crossCheck"]["ids"]) and all(r.get("reveal") for r in reports if r["kind"] == "planted")
tids = {t["id"] for t in crisis["targets"]}
assert tids == {t for p in crisis["pirs"] for t in p["targets"]} and all(cr["target"] in tids for cr in crisis["collectionResults"])
keys = {r["reply"] for r in policy} | {"frozen"} | {e["replyId"] for e in crisis["events"] if e.get("replyId")}
assert keys <= set(replies) and keys <= set(labels)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "crises", "vote-in-kalsa.json")
with open(out, "w") as f: json.dump(crisis, f, indent=2, ensure_ascii=False); f.write("\n")
print("wrote", os.path.normpath(out), len(reports), "reports")
