"""House-style wording for each crisis (#82, #83). The builders hold structure and rules; the text here replaces their wording
just before the file is written. SPOILERS: the text files hold each scenario's answers. See docs/style-guide.md."""
import importlib

def apply(crisis):
    try: T = importlib.import_module("text_" + crisis["id"].replace("-", "_")).TEXT
    except ModuleNotFoundError: return crisis
    R = {r["id"]: r for r in crisis["reports"]}
    for k in ("briefing", "policyNote", "opening", "frozenText", "vars", "replyByDay"):
        if k in T: crisis[k] = T[k]
    crisis["customer"].update(T.get("customer", {}))
    for k, v in T.get("replies", {}).items(): assert k in crisis["replies"], k; crisis["replies"][k] = v
    for t in crisis["credibility"]["triggers"]:
        if t["id"] in T.get("triggers", {}): t["note"] = T["triggers"][t["id"]]
    if "credSummary" in T: crisis["credibility"]["summary"] = T["credSummary"]
    S = {s["id"]: s for s in crisis["sources"]}
    for k, v in T.get("sources", {}).items():
        assert k in S, k
        if isinstance(v, str): S[k]["access"] = v
        else: S[k].update(v)
    for k, v in T.get("items", {}).items(): assert k in R, k; R[k]["text"] = v
    for k, vs in T.get("textBy", {}).items():
        assert len(vs) == len(R[k]["textBy"]), k
        for tb, v in zip(R[k]["textBy"], vs): tb["text"] = v
    for k, vs in T.get("append", {}).items():
        assert len(vs) == len(R[k]["append"]), k
        for ap, v in zip(R[k]["append"], vs): ap["text"] = v
    for k, v in T.get("itemNotes", {}).items(): R[k]["postmortemNote"] = v
    N = {(n["analyst"], n["item"]): n for n in crisis.get("notes", [])}
    for k, v in T.get("notes", {}).items():
        assert k in N, k
        if isinstance(v, str): N[k]["text"] = v
        else: N[k]["text"], N[k]["why"] = v
    for a in crisis.get("analysts", []):
        if a["id"] in T.get("analysts", {}): a["reveal"] = T["analysts"][a["id"]]
    E = {e["id"]: e for e in crisis["endings"]}
    for k, v in T.get("endings", {}).items(): assert k in E, k; E[k]["text"] = v
    for k, v in T.get("changedBy", {}).items(): assert k in E, k; E[k]["changedBy"] = v
    P = crisis["postmortem"]
    if "script" in T:
        assert len(T["script"]) == len(P["script"])
        for s, v in zip(P["script"], T["script"]): s["text"] = v
    for k in ("lessons", "answer", "openQuestion"):
        if k in T: P[k] = T[k]
    for c, v in zip(P.get("callouts", []), T.get("callouts", [])): c["text"] = v
    for b, v in zip(crisis["collection"].get("burnRules", []), T.get("burn", [])): b["text"] = v
    for e in crisis["events"]:
        ev = T.get("events", {}).get(e["id"])
        if not ev: continue
        if "note" in ev: e["note"] = ev["note"]
        for o in e.get("outcomes", []):
            if o.get("flag") in ev.get("outcomes", {}): o.update(ev["outcomes"][o["flag"]])
    for d in crisis["dailyUpdates"]:
        if d["day"] in T.get("updates", {}): d["text"] = T["updates"][d["day"]]
    if "epilogue" in T: crisis["epilogue"]["texts"].update(T["epilogue"])
    for t in crisis["targets"]:
        if t["id"] in T.get("fallback", {}): t["fallback"] = T["fallback"][t["id"]]
    return crisis
