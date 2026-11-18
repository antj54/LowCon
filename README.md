# Intel Cell Sim

A phone-first daily strategy game. You lead a small intelligence analysis cell: each day you read incoming reporting, decide what to believe, and brief a commander with a judgment and a confidence level. The world reacts, and the truth comes out in a postmortem.

Working title options: *Low Confidence*, *The Daily Brief*, *Indications & Warning*, *Tradecraft*.

## Status

**Phase 1 · First playable.** One 5-day crisis (Crisis 01, *Exercise or Operation?*) with a morning read-in, a situation map, an inbox with accept-or-doubt grading, a daily brief, and a postmortem with the real unit positions.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | The engine: one self-contained page (markup, styles, script). Holds no crisis content. |
| `crises/*.json` | Crisis data files. The engine loads one at start. Format v0.3. |
| `docs/` | Design doc, decisions log, crisis content and the Crisis 01 packet and answer key (spoilers), mirrored from the claude.ai project. |
| `tools/simulate.js` | Runs the real engine headlessly and prints the ending and score for a set of fixed strategies. Use it after any change to scoring, policy or content. |

## Run it

The page fetches its crisis file, so serve the folder rather than opening the file directly:

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

Progress saves in the browser. When published as a claude.ai artifact, it also saves to the player's account.

## Check balance

```sh
node tools/simulate.js
```

Expected for Crisis 01: best play ends **Deterred**, "always worst case" and "never above Moderate" end in **Standoff**, and trusting the official line, "just signaling" and always hedging end **Seized**. Doubting everything should score below doubting nothing.

## Setting

A real map in the early 2030s with fictional countries, leaders, units and companies. Kordav, Elsin, the Veyl, Tarsk, Ostrel, Dolan and Varn are stand-in names. No real people are depicted.
