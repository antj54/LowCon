#!/usr/bin/env node
// Strategy regression check for Low Confidence.
// Runs the real engine from index.html headlessly against a crisis file and
// prints the ending and score for a set of fixed strategies.
// Usage: node tools/simulate.js [crises/border-buildup.json]
'use strict';
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const crisisPath = path.resolve(root, process.argv.slice(2).find(a => !a.startsWith('--')) || 'crises/border-buildup.json');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const engine = (html.match(/<script>([\s\S]*)<\/script>/) || [])[1];
if (!engine) { console.error('No inline engine script found in index.html'); process.exit(1); }
const crisis = JSON.parse(fs.readFileSync(crisisPath, 'utf8'));
let lastHtml = '', lastLayer = '';

// A plan is one entry per day: [hypothesis, confidence, [evidence ids], [[discipline, target] taskings]].
// Evidence affects points only. Taskings resolve overnight like the real game.
// opts.board(day, click) pins and marks items before the brief. opts.reloadAfter reboots the engine
// from saved storage after that day's brief, the way a player closing and reopening the page would.
function boot(cfg, storage) {
  const handlers = {};
  const els = { app: { innerHTML: '' }, layer: { innerHTML: '' } };
  global.document = { getElementById: id => els[id] || null, addEventListener: (t, f) => { handlers[t] = f; }, hidden: false };
  global.window = { scrollTo() {} };
  global.localStorage = { getItem: k => (k in storage ? storage[k] : null), setItem: (k, v) => { storage[k] = String(v); } };
  global.setInterval = () => 0;
  global.setTimeout = (f, ms) => (ms === 0 || ms === 50 ? realSetTimeout(f, ms) : 0);
  Object.defineProperty(globalThis, 'navigator', { value: {}, configurable: true, writable: true });
  global.fetch = async url => /config\.json$/.test(url)
    ? (cfg ? { ok: true, json: async () => cfg } : { ok: false, json: async () => ({}) })
    : { ok: true, json: async () => JSON.parse(JSON.stringify(crisis)) };
  eval(engine);
  const click = (act, ds = {}) => handlers.click({ target: { closest: () => ({ dataset: Object.assign({ act }, ds), classList: { contains: () => false } }) } });
  return new Promise(resolve => realSetTimeout(() => resolve({ click, els }), 20));
}
const realSetTimeout = setTimeout;

async function run(plan, doubt, cfg, opts = {}) {
  const storage = {};
  let { click, els } = await boot(cfg, storage);
  click('start'); click('playahead');
  const calls = [];
  for (let i = 0; i < plan.length; i++) {
    const [h, conf, ev, tasks] = plan[i];
    crisis.reports.filter(r => r.day === i + 1 && doubt(r)).forEach(r => click('flag', { id: r.id }));
    (tasks || []).forEach(([disc, target]) => click('task', { disc, target }));
    if (opts.board) opts.board(i + 1, click);
    click('tab', { v: 'brief' });
    click('hyp', { v: h }); click('conf', { v: conf });
    (ev || []).forEach(id => click('ev', { id }));
    if (opts.expectNudge && opts.expectNudge[i + 1] && !els.app.innerHTML.includes(opts.expectNudge[i + 1])) throw new Error('Board nudge missing on day ' + (i + 1) + ': ' + opts.expectNudge[i + 1]);
    calls.push(`${h} ${conf}`);
    click('confirmsend');
    if (cfg && cfg.playtest) {
      if (!/How was Day/.test(els.layer.innerHTML)) throw new Error('Playtest reaction sheet missing on day ' + (i + 1));
      click('react', { v: 'engaging' }); click('reactdone');
    }
    if (opts.reloadAfter && opts.reloadAfter.includes(i + 1)) ({ click, els } = await boot(cfg, storage));
  }
  if (cfg && cfg.playtest) { click('realism', { id: 'R-3-03' }); click('debrief', { q: 'sixth', v: 'yes' }); }
  const out = els.app.innerHTML; lastHtml = out; lastLayer = els.layer.innerHTML;
  const ending = (out.match(/<h2>([^<]+)<\/h2>/) || [])[1];
  const total = (out.match(/class="n">([^<]+)</) || [])[1];
  const parts = (out.match(/calls[^<]+/) || [])[0];
  return { line: `${ending} ${total} | ${parts}`, calls, total, html: out };
}

// Board use for the "with board" check: pin the day's diagnostic items and mark them like a careful analyst.
const BOARD_MARKS = {
  1: { 'R-1-01': 'ccc', 'R-1-02': 'ici' },
  2: { 'R-2-01': 'icc', 'C-01': 'ici' },
  3: { 'R-3-02': 'ici', 'C-05': 'ici' },
  4: { 'C-02': 'ici' },
  5: { 'C-03': 'ici' },
};
const CYCLE = { c: 1, i: 2, n: 3 };
function useBoard(day, click) {
  Object.entries(BOARD_MARKS[day] || {}).forEach(([id, marks]) => {
    click('bpin', { id });
    [...marks].forEach((m, k) => { for (let n = 0; n < CYCLE[m]; n++) click('mark', { id, h: 'H' + (k + 1) }); });
  });
}

const none = () => false, plants = r => r.kind === 'planted', all = () => true;
const BEST = [
  ['H3', 'medium', ['R-1-01', 'R-1-02', 'R-1-04']],
  ['H3', 'medium', ['R-2-01', 'R-2-02']],
  ['H2', 'medium', ['R-3-02', 'R-3-04', 'R-3-01']],
  ['H2', 'high', ['R-4-01', 'R-3-02', 'R-4-04']],
  ['H2', 'high', ['R-5-03', 'R-5-04', 'R-4-01']],
];
const COLLECT = [
  ['H3', 'medium', ['R-1-01', 'R-1-02', 'R-1-04'], [['IMINT', 'dolan']]],
  ['H3', 'medium', ['R-2-01', 'R-2-02', 'C-01'], [['SIGINT', 'hq'], ['OSINT', 'railhead']]],
  ['H2', 'medium', ['R-3-02', 'R-3-04', 'C-05'], [['IMINT', 'dolan'], ['IMINT', 'railhead']]],
  ['H2', 'high', ['C-02', 'R-3-02', 'R-4-04'], [['IMINT', 'dolan']]],
  ['H2', 'high', ['C-03', 'C-04', 'R-5-04']],
];
const STRATEGIES = [
  ['Best play, no collection', BEST, none],
  ['Best play with collection', COLLECT, none],
  ['Collection, doubt plants', COLLECT, plants],
  ['Collection, doubt everything', COLLECT, all],
  ['High from Day 3, with collection', [COLLECT[0], COLLECT[1], ['H2', 'high', ['R-3-02', 'R-3-04', 'C-05'], [['IMINT', 'dolan']]], COLLECT[3], COLLECT[4]], none],
  ['Burn KESTREL (HUMINT twice)', [['H3', 'medium', ['R-1-01'], [['HUMINT', 'depot']]], ['H3', 'medium', ['R-2-01'], [['HUMINT', 'depot']]], BEST[2], BEST[3], ['H2', 'high', ['R-5-03', 'R-4-01']]], none],
  ['Never above Medium', [COLLECT[0], COLLECT[1], COLLECT[2], ['H2', 'medium', ['C-02', 'R-3-02', 'R-4-04'], [['IMINT', 'dolan']]], ['H2', 'medium', ['C-03', 'C-04']]], none],
  ['Always worst case', [['H2', 'high', ['R-1-03', 'R-1-01']], ['H2', 'high', ['R-2-01', 'R-2-03']], ['H2', 'high', ['R-3-02', 'R-3-04']], ['H2', 'high', ['R-4-01', 'R-4-04']], ['H2', 'high', ['R-5-03', 'R-5-04']]], none],
  ['Trust the official line', Array(5).fill(['H1', 'medium', []]), none],
  ['"Just signaling"', Array(5).fill(['H3', 'medium', []]), none],
  ['Always hedge (Low)', [['H3', 'low', []], ['H3', 'low', []], ['H2', 'low', []], ['H2', 'low', []], ['H2', 'low', []]], none],
];

(async () => {
  console.log(`Crisis: ${crisis.title} (${path.relative(root, crisisPath)})`);
  let ref;
  for (const [name, plan, doubt] of STRATEGIES) {
    const r = await run(plan, doubt);
    if (plan === COLLECT && doubt === none) ref = r;
    console.log(name.padEnd(30), r.line);
    if (process.argv.includes('--calls')) console.log(' '.repeat(31) + r.calls.join(' · '));
  }
  const b = await run(COLLECT, none, null, { board: useBoard, expectNudge: { 2: 'H2</b> is the least contradicted', 3: 'H2</b> is the least contradicted' } });
  const boardOk = b.total === ref.total && /Your board/.test(b.html);
  console.log('Collection + board (unscored)'.padEnd(30), b.line, boardOk ? '| same score, board in postmortem' : '| BOARD CHANGED THE SCORE OR IS MISSING');
  const rl = await run(COLLECT, none, null, { board: useBoard, reloadAfter: [1, 2, 3, 4] });
  console.log('Reload after every day'.padEnd(30), rl.line, rl.total === ref.total && /Your board/.test(rl.html) ? '| matches, save survives reload' : '| RELOAD CHANGED THE RESULT');
  const pt = await run(COLLECT, none, { playtest: true });
  console.log('Playtest build'.padEnd(30), pt.line, /Playtest debrief/.test(lastHtml) ? '| debrief shown' : '| DEBRIEF MISSING');
  if (!boardOk || rl.total !== ref.total) process.exitCode = 1;
})();
