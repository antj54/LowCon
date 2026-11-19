# Low Confidence

*Working title. Project name: Intel Cell Sim.*

A phone-first daily strategy game. You lead a small intelligence analysis cell: each day you read incoming reporting, decide what to believe, and brief a commander with a judgment and a confidence level. The world reacts, and the truth comes out in a postmortem.

## Status

**Phase 2 · Core systems.** Crisis 01 (*Exercise or Operation?*) is playable with a morning read-in, a situation map, an inbox with doubting, collection tasking, a hypotheses board (ACH-lite, unscored), credibility with the customer, a daily brief (hypothesis plus Low/Medium/High confidence) and a postmortem with the real unit positions. Crisis 02 (*The Walk-in*) is playable from the crisis picker. Phase 3 has started: a service record and carry-over between scenarios. Analyst notes are in both scenarios. Next: Crisis 03 as data.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | The engine: one self-contained page (markup, styles, script). Holds no crisis content. |
| `crises/*.json` | Crisis data files. The engine loads one at start. Format v0.3. |
| `config/playtest.json` | Published as `config.json` in the playtest build. Turns on playtest mode and opens each next day immediately (`playAheadDefault`): results sync to a shared `playtests/<tester>` record, plus one-tap reactions, a per-item realism flag, an end-of-crisis debrief and an owner-only Testers tab. With no `config.json`, the engine runs as the normal build. |
| `docs/` | Design doc, decisions log, crisis content and the Crisis 01 packet and answer key (spoilers), mirrored from the claude.ai project. |
| `tools/simulate.js` | Runs the real engine headlessly and prints the ending and score for a set of fixed strategies. Use it after any change to scoring, policy or content. |

## Run it

The page fetches its crisis file, so serve the folder rather than opening the file directly:

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

Progress saves in the browser. When published as a claude.ai artifact, it also saves to the player's account.

## Builds

| Build | Files published | Storage rules |
| --- | --- | --- |
| Main | `index.html`, `crises/` | `{db:{}, user:{}}` |
| Playtest | `index.html`, `crises/`, `config/playtest.json` as `config.json` | `playtests` readable by Editors and the owner, each tester writes only their own record; `meta` owner-only (holds `meta/owner`, which marks the owner for the Testers tab); `user` with the `profile` scope |

Testers need write access to save: Contributor if they're in the owner's organization, otherwise an email invite as Editor (and no public link).

## Check balance

```sh
node tools/simulate.js                        # Crisis 01
node tools/simulate.js crises/walk-in.json    # Crisis 02
python3 tools/build_walk_in.py                # regenerate crises/walk-in.json after editing its content
```

Expected for Crisis 01: best play ends **Deterred**, with or without collection. Burning KESTREL costs a source and points. "Never above Medium" and "always worst case" end in **Standoff**. Trusting the official line, "just signaling" and always hedging end **Seized**. Doubting everything scores below doubting nothing. Add `--calls` to see each day's call. The last line runs the playtest build and checks the reaction sheet and debrief appear.

## Setting

Fictional countries placed in real regions, in the early 2030s. All leaders, units and companies are fictional. No real people are depicted.
