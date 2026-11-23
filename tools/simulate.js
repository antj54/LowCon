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
  const file = u => { const f = path.join(root, u); return fs.existsSync(f) ? { ok: true, json: async () => JSON.parse(fs.readFileSync(f, 'utf8')) } : { ok: false, json: async () => ({}) }; };
  const conf = Object.assign({ playtest: false, unlockAll: true }, cfg || {});
  global.fetch = async url => /config\.json$/.test(url) ? { ok: true, json: async () => conf }
    : url === path.relative(root, crisisPath) ? { ok: true, json: async () => JSON.parse(JSON.stringify(crisis)) } : file(url);
  storage['intel-cell-sim:current'] = crisis.id;
  eval(engine);
  const click = (act, ds = {}) => handlers.click({ target: { closest: () => ({ dataset: Object.assign({ act }, ds), classList: { contains: () => false } }) } });
  return new Promise(resolve => realSetTimeout(() => resolve({ click, els }), 20));
}
const realSetTimeout = setTimeout;

async function run(plan, doubt, cfg, opts = {}) {
  const storage = Object.assign({}, opts.seed || {});
  let { click, els } = await boot(cfg, storage);
  click('start'); click('playahead');
  const calls = [], snaps = {};
  for (let i = 0; i < plan.length; i++) {
    const [h, conf, ev, tasks] = plan[i];
    if (opts.snap && i === 0) { snaps.day1 = els.app.innerHTML; click('tab', { v: 'collect' }); snaps.collect1 = els.app.innerHTML; click('tab', { v: 'inbox' }); }
    if (opts.snap && i === 2) snaps.day3 = els.app.innerHTML;
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
    if (opts.reloadAfter && opts.reloadAfter.includes(i + 1)) { ({ click, els } = await boot(cfg, storage)); if (!/Low Confidence/.test(els.app.innerHTML)) throw new Error('Main menu missing after reload'); click('continue'); }
  }
  if (cfg && cfg.playtest) { click('realism', { id: 'R-3-03' }); click('debrief', { q: 'sixth', v: 'yes' }); }
  const rec = JSON.parse(storage['intel-cell-sim:record'] || '{"runs":{}}').runs[crisis.id];
  if (!opts.seed && (!rec || !rec.ending)) throw new Error('Service record not written at the end of the run');
  const out = els.app.innerHTML; lastHtml = out; lastLayer = els.layer.innerHTML;
  const ending = (out.match(/<h2>([^<]+)<\/h2>/) || [])[1];
  const total = (out.match(/class="n">([^<]+)</) || [])[1];
  const parts = (out.match(/calls[^<]+/) || [])[0];
  const cred = ((out.match(/credline">Credibility: ([^<]+)</) || [])[1] || '').replace(/ after the outcome/, '').replace(/&gt;/g, '>');
  snaps.record = storage['intel-cell-sim:record'] || '';
  return Object.assign({ line: `${ending} ${total} | ${parts}`, calls, total, html: out, cred }, snaps);
}

const CYCLE = { c: 1, i: 2, n: 3 };
const boardUser = marks => (day, click) => {
  Object.entries(marks[day] || {}).forEach(([id, m]) => {
    click('bpin', { id });
    [...m].forEach((x, k) => { for (let n = 0; n < CYCLE[x]; n++) click('mark', { id, h: 'H' + (k + 1) }); });
  });
};
const none = () => false, plants = r => r.kind === 'planted', all = () => true;
const rep5 = x => Array(5).fill(x);

// ---------- Crisis 01: Exercise or Operation? ----------
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
// ---------- Crisis 02: The Walk-in ----------
const W_BEST = [
  ['H2', 'low', ['R-1-01', 'R-1-04'], [['OSINT', 'family'], ['OSINT', 'press'], ['SIGINT', 'bureau-office']]],
  ['H2', 'medium', ['C-01', 'C-02', 'R-2-01'], [['HUMINT', 'd-access'], ['HUMINT', 'd-vell'], ['OSINT', 'ministry']]],
  ['H2', 'high', ['R-3-03', 'C-01', 'C-12'], [['HUMINT', 'd-ledger'], ['SIGINT', 'embassy']]],
  ['H2', 'high', ['C-09', 'C-07', 'R-4-02'], [['Liaison', 'travel'], ['SIGINT', 'bureau-hq']]],
  ['H2', 'high', ['R-4-04', 'R-5-02', 'C-02']],
];
const W_PUSH = [
  ['H2', 'low', ['R-1-01', 'R-1-04']], ['H2', 'medium', ['R-2-01', 'R-2-03']], ['H2', 'high', ['R-3-03', 'R-3-04', 'R-2-01']],
  ['H2', 'high', ['R-4-02', 'R-4-04', 'R-3-03']], ['H2', 'high', ['R-5-02', 'R-3-03']],
];
// ---------- Crisis 03: The Southern Line ----------
const S_BEST = [
  ['H3', 'low', ['R-1-01', 'R-1-03'], [['Liaison', 'wren-sourcing'], ['HUMINT', 'magpie'], ['IMINT', 'ford']]],
  ['H3', 'medium', ['C-01', 'C-02', 'C-13'], [['OSINT', 'detonator'], ['IMINT', 'sarn-valley'], ['IMINT', 'kordav-crossings']]],
  ['H3', 'high', ['C-01', 'C-07', 'R-3-01'], [['HUMINT', 'magpie'], ['IMINT', 'tolen-approaches']]],
  ['H1', 'medium', ['R-4-02', 'C-03'], [['SIGINT', 'front-radios'], ['IMINT', 'sarn-valley']]],
  ['H1', 'high', ['C-06', 'C-16', 'R-5-01']],
];
const S_PUSH = [['H3', 'low', ['R-1-01', 'R-1-02']], ['H3', 'medium', ['R-2-03', 'R-2-04']], ['H3', 'high', ['R-3-01', 'R-3-02']], ['H1', 'medium', ['R-4-02']], ['H1', 'high', ['R-5-01', 'R-5-04', 'R-4-02']]];
// ---------- Crisis 04: The Missing Shipment ----------
const M_BEST = [
  ['H2', 'low', ['R-1-04', 'R-1-01'], [['IMINT', 'brask'], ['OSINT', 'maren-lys'], ['OSINT', 'tessaly-history']]],
  ['H2', 'medium', ['C-01', 'C-05', 'R-1-04'], [['SIGINT', 'tessaly-office'], ['OSINT', 'listing']]],
  ['H2', 'high', ['C-01', 'C-07', 'R-3-01'], [['SIGINT', 'brask-warehouse'], ['IMINT', 'halsk-sheds']]],
  ['H2', 'high', ['C-12', 'C-03', 'R-2-04'], [['HUMINT', 'gannet']]],
  ['H2', 'high', ['C-09', 'C-07', 'R-5-03']],
];
const M_PUSH = [['H2', 'low', ['R-1-04']], ['H2', 'medium', ['R-1-04', 'R-2-04']], ['H2', 'high', ['R-3-01', 'R-3-03', 'R-1-04']], ['H2', 'high', ['R-2-04', 'R-4-01', 'R-3-01']], ['H2', 'high', ['R-5-03', 'R-2-04']]];
// ---------- Crisis 05: Lights Out ----------
const L_BEST = [
  ['H2', 'low', ['R-1-03'], [['OSINT', 'wallet'], ['OSINT', 'release-history'], ['HUMINT', 'petrel']]],
  ['H2', 'high', ['C-01', 'C-02', 'C-09'], [['Technical', 'target-list'], ['SIGINT', 'negotiator']]],
  ['H2', 'high', ['C-04', 'C-06', 'R-3-03'], [['Liaison', 'registry'], ['OSINT', 'language']]],
  ['H2', 'high', ['C-01', 'R-4-02', 'C-08'], [['Technical', 'images'], ['HUMINT', 'petrel']]],
  ['H2', 'high', ['C-10', 'C-03', 'R-5-04']],
];
const L_PUSH = [['H2', 'low', ['R-1-03']], ['H2', 'medium', ['R-1-03', 'R-2-03']], ['H2', 'high', ['R-3-03', 'R-1-03', 'R-2-03']], ['H2', 'high', ['R-3-03', 'R-4-02']], ['H2', 'high', ['R-5-04', 'R-3-03']]];
const sCalls = calls => calls.map(([h, c]) => [h, c, []]);
// ---------- Crisis 06: The Damage Assessment ----------
const D_BEST = [
  ['H3', 'low', ['R-1-01', 'R-1-02'], [['Test', 'test-link-ipc'], ['OSINT', 'delivery-history'], ['OSINT', 'marrow-travel']]],
  ['H3', 'medium', ['R-2-04', 'R-2-01', 'C-08'], [['Test', 'test-hand-rhun'], ['OSINT', 'delivery-history']]],
  ['H3', 'high', ['C-03', 'R-3-01', 'R-2-04'], [['Technical', 'lab-terminal'], ['Test', 'test-cell']]],
  ['H3', 'high', ['C-01', 'C-06', 'C-03']],
  ['H3', 'high', ['C-05', 'C-03', 'C-06']],
];
const D_PUSH = [['H3', 'low', ['R-1-01']], ['H3', 'medium', ['R-2-04', 'R-1-01']], ['H3', 'medium', ['R-3-01', 'R-2-04']], ['H3', 'high', ['R-4-02', 'R-3-01', 'R-2-04']], ['H3', 'high', ['R-4-02', 'R-3-01']]];
// ---------- Crisis 07: The Vote in Kalsa ----------
const V_BEST = [
  ['H1', 'low', ['R-1-01', 'R-1-02'], [['HUMINT', 'heron'], ['OSINT', 'funding'], ['OSINT', 'whip-count']]],
  ['H1', 'medium', ['C-01', 'C-03', 'R-2-04'], [['SIGINT', 'bureau-traffic'], ['OSINT', 'document']]],
  ['H1', 'high', ['R-3-01', 'C-08', 'C-05'], [['HUMINT', 'heron']]],
  ['H1', 'high', ['C-02', 'R-4-03', 'R-4-01']],
  ['H1', 'high', ['R-5-01', 'C-02', 'R-4-03']],
];
const V_PUSH = [['H1', 'low', ['R-1-01']], ['H1', 'medium', ['R-2-04', 'R-1-01']], ['H1', 'high', ['R-3-01', 'R-2-04']], ['H1', 'high', ['R-4-03', 'R-4-01', 'R-3-01']], ['H1', 'high', ['R-5-01', 'R-4-03']]];
const SETS = {
  'vote-in-kalsa': {
    collect: V_BEST, marks: { 1: { 'R-1-01': 'cci' }, 2: { 'C-01': 'cii' } }, nudge: {},
    strategies: [
      ['Best play with collection', V_BEST, none],
      ['Collection, doubt plants', V_BEST, plants],
      ['Collection, doubt everything', V_BEST, all],
      ['Push only', V_PUSH, none],
      ['H1 High from Day 1', rep5(['H1', 'high', ['R-1-01']]), none],
      ['Never above Medium (H1)', rep5(['H1', 'medium', ['R-1-01']]), none],
      ['Always hedge (Low)', rep5(['H1', 'low', []]), none],
      ['The street: H2 Med, then High Day 3', [['H2', 'medium', ['R-1-02']], ['H2', 'medium', ['R-2-02']], ['H2', 'high', ['R-3-02']], ['H2', 'high', ['R-3-02']], ['H2', 'high', ['R-3-02']]], none],
      ["Vasko's path: H3 Med Days 2-3, then H1 High", [['H1', 'low', ['R-1-01']], ['H3', 'medium', ['R-2-03']], ['H3', 'medium', ['R-3-04']], ['H1', 'high', ['R-4-03']], ['H1', 'high', ['R-5-01']]], none],
      ['Always Kordav (H3 High)', rep5(['H3', 'high', ['R-2-03']]), none],
      ['Burn HERON (Days 1 and 2)', [['H1', 'low', ['R-1-01'], [['HUMINT', 'heron']]], ['H1', 'medium', ['C-01'], [['HUMINT', 'heron']]], V_PUSH[2], V_PUSH[3], V_PUSH[4]], none],
    ],
  },
  'damage-assessment': {
    collect: D_BEST, marks: { 1: { 'R-1-01': 'icic' }, 2: { 'R-2-04': 'icic' } }, nudge: {},
    strategies: [
      ['Best play with collection', D_BEST, none],
      ['Collection, doubt plants', D_BEST, plants],
      ['Collection, doubt everything', D_BEST, all],
      ['Push only (lab-free, Medium then High Day 4)', D_PUSH, none],
      ['Always the link (H3 High)', rep5(['H3', 'high', ['R-1-01']]), none],
      ['Never above Medium (H3)', rep5(['H3', 'medium', ['R-1-01']]), none],
      ['Late, no couriers (Low x3, High)', [['H3', 'low', ['R-1-01'], [['Test', 'test-link-ipc']]], ['H3', 'low', []], ['H3', 'low', ['C-03']], ['H3', 'high', ['C-03']], ['H3', 'high', ['C-03']]], none],
      ['The trap (link test to Rhun, then H1 High)', [['H1', 'low', ['R-1-01'], [['Test', 'test-link-rhun']]], ['H1', 'medium', ['R-2-03'], [['Test', 'test-hand-rhun']]], ['H1', 'high', ['C-02']], ['H3', 'high', ['C-01']], ['H3', 'high', ['C-01']]], none],
      ['Always Rhun (H1 High)', rep5(['H1', 'high', ['R-2-03']]), none],
      ['Always Arle (H2 High)', rep5(['H2', 'high', ['R-3-03']]), none],
      ['No leak (H4 Medium)', rep5(['H4', 'medium', ['R-1-05']]), none],
      ['Always hedge (Low)', rep5(['H3', 'low', []]), none],
      ['Vetting request, then couriers, then High', [['H3', 'low', ['R-1-01'], [['Liaison', 'vetting-rhun'], ['Test', 'test-link-ipc']]], ['H3', 'medium', ['C-10']], ['H3', 'high', ['C-03', 'C-10K']], ['H3', 'high', ['C-03']], ['H3', 'high', ['C-03']]], none],
    ],
  },
  'missing-shipment': {
    collect: M_BEST, marks: { 1: { 'R-1-04': 'ici' }, 2: { 'C-01': 'ici' } }, nudge: {},
    strategies: [
      ['Best play, push only', M_PUSH, none],
      ['Best play with collection', M_BEST, none],
      ['Collection, doubt plants', M_BEST, plants],
      ['Collection, doubt everything', M_BEST, all],
      ['Port police first, then SIGINT', [['H2', 'low', ['R-1-04'], [['Liaison', 'port-police'], ['IMINT', 'brask']]], ['H2', 'medium', ['C-01'], [['SIGINT', 'tessaly-office']]], M_PUSH[2], M_PUSH[3], M_PUSH[4]], none],
      ['Burn GANNET (Days 1 and 2)', [['H2', 'low', ['R-1-04'], [['HUMINT', 'gannet']]], ['H2', 'medium', ['C-08'], [['HUMINT', 'gannet']]], M_PUSH[2], M_PUSH[3], M_PUSH[4]], none],
      ['Always Kordav (H2 High)', rep5(['H2', 'high', ['R-1-04']]), none],
      ['Never above Medium', rep5(['H2', 'medium', ['R-1-04']]), none],
      ['Always hedge (Low)', rep5(['H2', 'low', []]), none],
      ['Relieved on Day 4', [M_PUSH[0], M_PUSH[1], M_PUSH[2], ['H1', 'medium', ['R-4-01', 'R-4-03']], ['H1', 'high', ['R-4-01', 'R-4-03']]], none],
      ['Theft all along (H3 Medium)', rep5(['H3', 'medium', ['R-2-02']]), none],
      ['Paperwork (H1 High)', rep5(['H1', 'high', ['R-1-02']]), none],
    ],
  },
  'lights-out': {
    collect: L_BEST, marks: { 1: { 'R-1-03': 'ici' }, 2: { 'C-01': 'ici' } }, nudge: {},
    strategies: [
      ['Best play, push only', L_PUSH, none],
      ['Fast, with collection', L_BEST, none],
      ['Collection, doubt plants', L_BEST, plants],
      ['Collection, doubt everything', L_BEST, all],
      ['Late (High from Day 4)', [L_PUSH[0], L_PUSH[1], ['H2', 'medium', ['R-3-03']], L_PUSH[3], L_PUSH[4]], none],
      ['Always Kordav (H2 High)', rep5(['H2', 'high', ['R-1-03']]), none],
      ['Paid Day 1, right from Day 3', [['H1', 'high', ['R-1-02']], ['H2', 'medium', ['R-2-03']], L_PUSH[2], L_PUSH[3], L_PUSH[4]], none],
      ['Burn PETREL (Days 1 and 2)', [['H2', 'low', ['R-1-03'], [['HUMINT', 'petrel']]], ['H2', 'medium', ['C-02'], [['HUMINT', 'petrel']]], L_PUSH[2], L_PUSH[3], L_PUSH[4]], none],
      ['Never above Medium', rep5(['H2', 'medium', ['R-1-03']]), none],
      ['Always hedge (Low)', rep5(['H2', 'low', []]), none],
      ['Crime all along (H1 Medium)', rep5(['H1', 'medium', ['R-1-02']]), none],
      ['Marrat (H3 Medium, then High)', [['H3', 'medium', []], ['H3', 'high', ['R-2-01']], ['H3', 'high', ['R-2-01']], ['H3', 'high', ['R-2-01']], ['H3', 'high', ['R-2-01']]], none],
      ['Crime at High (pays daily)', rep5(['H1', 'high', ['R-1-02']]), none],
    ],
  },
  'southern-line': {
    collect: S_BEST,
    marks: { 1: { 'R-1-02': 'iic', 'R-1-04': 'ici' }, 2: { 'C-01': 'iic' } },
    nudge: {},
    strategies: [
      ['Best play, push only', S_PUSH, none],
      ['Best play with collection', S_BEST, none],
      ['Collection, doubt plants', S_BEST, plants],
      ['Collection, doubt everything', S_BEST, all],
      ['H1 High already on Day 4', [S_BEST[0], S_BEST[1], S_BEST[2], ['H1', 'high', ['R-4-02', 'C-03'], S_BEST[3][3]], S_BEST[4]], none],
      ['Believe WREN at once', sCalls([['H3', 'high'], ['H3', 'high'], ['H3', 'high'], ['H1', 'medium'], ['H1', 'high']]), none],
      ['Never above Medium', sCalls([['H3', 'medium'], ['H3', 'medium'], ['H3', 'medium'], ['H1', 'medium'], ['H1', 'medium']]), none],
      ['Slow believer', sCalls([['H1', 'low'], ['H3', 'low'], ['H3', 'medium'], ['H1', 'low'], ['H1', 'high']]), none],
      ['Distrust WREN, suspect Kordav', sCalls([['H1', 'medium'], ['H2', 'medium'], ['H2', 'medium'], ['H1', 'medium'], ['H1', 'high']]), none],
      ['Burn MAGPIE (Days 1 and 2)', [S_BEST[0], ['H3', 'medium', ['C-01', 'C-02'], [['HUMINT', 'magpie']]], ['H3', 'high', ['C-01', 'R-3-01']], S_BEST[3], S_BEST[4]], none],
      ['Always hedge (Low)', sCalls([['H3', 'low'], ['H3', 'low'], ['H3', 'low'], ['H1', 'low'], ['H1', 'low']]), none],
      ['Always Marrat (H3 High)', rep5(['H3', 'high', []]), none],
      ['Local all along (H1 Medium)', rep5(['H1', 'medium', []]), none],
      ['Always Kordav (H2 Medium)', rep5(['H2', 'medium', ['R-2-01', 'R-2-02']]), none],
      ['Always Kordav (H2 High)', rep5(['H2', 'high', ['R-2-01', 'R-2-02']]), none],
    ],
  },
  'border-buildup': {
    collect: COLLECT,
    marks: { 1: { 'R-1-01': 'ccc', 'R-1-02': 'ici' }, 2: { 'R-2-01': 'icc', 'C-01': 'ici' }, 3: { 'R-3-02': 'ici', 'C-05': 'ici' }, 4: { 'C-02': 'ici' }, 5: { 'C-03': 'ici' } },
    nudge: { 2: 'H2</b> is the least contradicted', 3: 'H2</b> is the least contradicted' },
    strategies: [
      ['Best play, no collection', BEST, none],
      ['Best play with collection', COLLECT, none],
      ['Collection, doubt plants', COLLECT, plants],
      ['Collection, doubt everything', COLLECT, all],
      ['High from Day 3, with collection', [COLLECT[0], COLLECT[1], ['H2', 'high', ['R-3-02', 'R-3-04', 'C-05'], [['IMINT', 'dolan']]], COLLECT[3], COLLECT[4]], none],
      ['Burn KESTREL (HUMINT twice)', [['H3', 'medium', ['R-1-01'], [['HUMINT', 'depot']]], ['H3', 'medium', ['R-2-01'], [['HUMINT', 'depot']]], BEST[2], BEST[3], ['H2', 'high', ['R-5-03', 'R-4-01']]], none],
      ['Never above Medium', [COLLECT[0], COLLECT[1], COLLECT[2], ['H2', 'medium', ['C-02', 'R-3-02', 'R-4-04'], [['IMINT', 'dolan']]], ['H2', 'medium', ['C-03', 'C-04']]], none],
      ['Always worst case', [['H2', 'high', ['R-1-03', 'R-1-01']], ['H2', 'high', ['R-2-01', 'R-2-03']], ['H2', 'high', ['R-3-02', 'R-3-04']], ['H2', 'high', ['R-4-01', 'R-4-04']], ['H2', 'high', ['R-5-03', 'R-5-04']]], none],
      ['Trust the official line', rep5(['H1', 'medium', []]), none],
      ['"Just signaling"', rep5(['H3', 'medium', []]), none],
      ['Hedge early, then commit', [['H3', 'low', ['R-1-01']], ['H3', 'low', ['R-2-01']], ['H2', 'low', ['R-3-02']], ['H2', 'high', ['R-4-01', 'R-3-02', 'R-4-04']], ['H2', 'high', ['R-5-03', 'R-5-04']]], none],
      ['Early mover, then right', [['H2', 'high', ['R-1-01']], ['H3', 'medium', ['R-2-01']], ['H2', 'high', ['R-3-02', 'R-3-04']], ['H2', 'high', ['R-4-01', 'R-4-04']], ['H2', 'high', ['R-5-03', 'R-5-04']]], none],
      ['Flip-flop (company, then back)', [BEST[0], BEST[1], BEST[2], ['H3', 'medium', ['R-4-04']], ['H2', 'high', ['R-5-03', 'R-5-04']]], none],
      ['Always hedge (Low)', [['H3', 'low', []], ['H3', 'low', []], ['H2', 'low', []], ['H2', 'low', []], ['H2', 'low', []]], none],
    ],
  },
  'walk-in': {
    collect: W_BEST,
    marks: { 1: { 'R-1-03': 'cci' }, 2: { 'C-01': 'ici', 'C-02': 'ici' }, 3: { 'R-3-03': 'ici' } },
    nudge: { 2: 'H2</b> is the least contradicted', 3: 'H2</b> is the least contradicted' },
    strategies: [
      ['Best play, push only', W_PUSH, none],
      ['Best play with collection', W_BEST, none],
      ['Collection, doubt plants', W_BEST, plants],
      ['Collection, doubt everything', W_BEST, all],
      ['Paranoid (H2 High daily)', rep5(['H2', 'high', ['R-1-01']]), none],
      ['Paranoid, full evidence', [['H2', 'high', ['R-1-01', 'R-1-04', 'R-1-02']], ['H2', 'high', ['R-2-01', 'R-2-03', 'R-1-04']], ['H2', 'high', ['R-3-03', 'R-3-04', 'R-2-01']], ['H2', 'high', ['R-4-02', 'R-4-04', 'R-3-03']], ['H2', 'high', ['R-5-02', 'R-3-03', 'R-4-04']]], none],
      ['Fooled by staged recall', [['H2', 'low', ['R-1-01'], [['SIGINT', 'bureau-hq'], ['HUMINT', 'd-vell']]], ['H1', 'medium', ['C-06', 'C-10']], W_PUSH[2], W_PUSH[3], W_PUSH[4]], none],
      ['Burn FINCH on Day 1', [['H2', 'low', ['R-1-01'], [['HUMINT', 'finch'], ['OSINT', 'family'], ['OSINT', 'press']]], W_PUSH[1], ['H2', 'high', ['R-3-03', 'C-04', 'C-02']], W_PUSH[3], W_PUSH[4]], none],
      ['Never above Medium', W_PUSH.map(x => ['H2', x[1] === 'high' ? 'medium' : x[1], x[2]]), none],
      ['Always hedge (Low)', rep5(['H2', 'low', []]), none],
      ['"He\'s a fabricator"', rep5(['H3', 'medium', []]), none],
      ['Cautious believer (H1 Medium)', rep5(['H1', 'medium', ['R-1-03']]), none],
      ['Trust the walk-in (H1 High)', rep5(['H1', 'high', ['R-1-03', 'R-1-02']]), none],
      ['Believer who recovers Day 4', [['H1', 'medium', []], ['H1', 'medium', []], ['H1', 'medium', []], ['H2', 'high', ['R-3-03']], ['H2', 'high', ['R-3-03']]], none],
    ],
  },
};

(async () => {
  const set = SETS[crisis.id];
  if (!set) { console.error('No strategies for crisis ' + crisis.id); process.exit(1); }
  console.log(`Crisis: ${crisis.title} (${path.relative(root, crisisPath)})`);
  let ref;
  for (const [name, plan, doubt] of set.strategies) {
    const r = await run(plan, doubt);
    if (plan === set.collect && doubt === none) ref = r;
    console.log(name.padEnd(32), r.line, '| cred ' + r.cred);
    if (process.argv.includes('--calls')) console.log(' '.repeat(33) + r.calls.join(' · '));
  }
  const useBoard = boardUser(set.marks);
  const b = await run(set.collect, none, null, { board: useBoard, expectNudge: set.nudge });
  const boardOk = b.total === ref.total && /Your board/.test(b.html);
  console.log('Collection + board (unscored)'.padEnd(32), b.line, boardOk ? '| same score, board in postmortem' : '| BOARD CHANGED THE SCORE OR IS MISSING');
  const rl = await run(set.collect, none, null, { board: useBoard, reloadAfter: [1, 2, 3, 4] });
  console.log('Reload after every day'.padEnd(32), rl.line, rl.total === ref.total && /Your board/.test(rl.html) ? '| matches, save survives reload' : '| RELOAD CHANGED THE RESULT');
  if (crisis.id === 'walk-in') {
    const prior = tone => ({ 'intel-cell-sim:record': JSON.stringify({ v: 2, runs: { 'border-buildup': { id: 'border-buildup', title: 'Exercise or Operation?', customer: 'Gen. R. Halvorsen', cred: tone === 'good' ? 5 : 1, tone, burned: [], fooled: [], tested: [], grades: [{ codeName: 'WREN', to: 'C', reason: 'test' }], at: '2026-01-01' } } }) });
    for (const tone of ['good', 'bad']) {
      const r = await run(set.collect, none, null, { seed: prior(tone) });
      const want = tone === 'good' ? 'Trusted (4)' : 'Questioned (2)';
      console.log(('Carry-in: Crisis 01 ended ' + tone).padEnd(32), r.line, '| cred ' + r.cred, r.cred.startsWith(want) ? '| starts as expected' : '| WRONG START, wanted ' + want);
      if (!r.cred.startsWith(want)) process.exitCode = 1;
    }
  }
  if (crisis.id === 'southern-line') {
    const rec = (cred, tone, extra) => ({ 'intel-cell-sim:record': JSON.stringify({ v: 2, voided: {}, runs: { 'border-buildup': Object.assign({ id: 'border-buildup', title: 'Exercise or Operation?', customer: 'Gen. R. Halvorsen', cred, tone, burned: [], fooled: [], tested: [], grades: [], at: '2026-01-01' }, extra || {}) } }) });
    const cases = [
      ['Record: Deterred, credibility 5', rec(5, 'good'), r => r.cred.startsWith('Trusted (5)') && /counting on the same/.test(r.day1) && /6 of 6 points/.test(r.collect1)],
      ['Record: Seized, credibility 1', rec(1, 'bad'), r => r.cred.startsWith('Discounted (1)') && /lost a dam/.test(r.day1)],
      ['Record: KESTREL burned', rec(3, 'warn', { burned: ['KESTREL'] }), r => /data-target="kestrel"[^>]*disabled/.test(r.collect1)],
      ['Record: cited the snow photo', rec(3, 'warn', { fooled: ['recycled-photo'] }), r => /water tower/.test(r.html) && !/Marrat crowns\./.test(r.day3)],
      ['Old record: reassigned after 01', rec(0, 'bad', { reassigned: true }), r => r.cred.startsWith('Discounted (1)') && !/fresh pair of eyes/.test(r.day1) && /Tess Marrow/.test(r.html)],
      ['Record: reassigned after 02', { 'intel-cell-sim:record': JSON.stringify({ v: 2, voided: {}, runs: {
          'border-buildup': { id: 'border-buildup', title: 'Exercise or Operation?', customer: 'Gen. R. Halvorsen', cred: 4, tone: 'good', burned: [], fooled: [], tested: [], grades: [], at: '2026-01-01' },
          'walk-in': { id: 'walk-in', title: 'The Walk-in', customer: 'Under Secretary H. Marlowe', cred: 0, tone: 'bad', reassigned: true, burned: [], fooled: [], tested: [], grades: [], at: '2026-01-02' } } }) },
        r => r.cred.startsWith('Discounted (1)') && /fresh pair of eyes/.test(r.day1) && !/Tess Marrow/.test(r.html) && /Imre Vasko/.test(r.html)],
      ['Record: cited staged signals', rec(3, 'warn', { fooled: ['staged-signals'] }), r => !/Valley Truth/.test(r.day3)],
    ];
    for (const [name, seed, ok] of cases) {
      const r = await run(set.collect, none, null, { seed, snap: true });
      const good = ok(r);
      console.log(name.padEnd(32), r.line, '| cred ' + r.cred, good ? '| as expected' : '| NOT AS EXPECTED');
      if (!good) process.exitCode = 1;
    }
  }
  if (crisis.id === 'vote-in-kalsa') {
    const seed = { 'intel-cell-sim:record': JSON.stringify({ v: 2, voided: {}, runs: { 'damage-assessment': { id: 'damage-assessment', title: 'The Damage Assessment', customer: 'Under Secretary H. Marlowe', cred: 4, tone: 'bad', ending: 'wrong-name', burned: [], fooled: [], tested: [], grades: [], at: '2026-01-06', story: { alliance: -2, pressure: 1, caseFile: [], flags: { leak: 'open', wrongName: 'rhun' } } } } }) };
    const h3 = [['H3', 'medium', ['R-1-04']], ['H3', 'medium', ['R-2-06']], ['H3', 'high', ['R-3-06']], ['H3', 'high', []], ['H3', 'high', []]];
    const r = await run(h3, none, null, { seed, snap: true });
    const ok = /over LATTICE/.test(r.day3) && /tells our embassy, unprompted/.test(r.html + r.day3) && /Ahrend/.test(r.day1) && /quoting you/.test(r.html);
    console.log('Leak open: echoes and route'.padEnd(32), r.line, ok ? '| as expected' : '| NOT AS EXPECTED');
    if (!ok) process.exitCode = 1;
  }
  if (crisis.id === 'border-buildup') {
    const hedge = set.strategies.find(x => /Always hedge/.test(x[0]));
    const r = await run(hedge[1], none);
    const ok = !/Posting notice/.test(r.html) && /"reassigned":false/.test(r.record) && /"cred":1/.test(r.record);
    console.log('Zero credibility in Scenario 01'.padEnd(32), r.line, ok ? '| not reassigned, carries over as 1' : '| NO REASSIGNMENT RULE');
    if (!ok) process.exitCode = 1;
  }
  const pt = await run(set.collect, none, { playtest: true });
  console.log('Playtest build'.padEnd(32), pt.line, /Playtest debrief/.test(lastHtml) ? '| debrief shown' : '| DEBRIEF MISSING');
  if (!boardOk || rl.total !== ref.total) process.exitCode = 1;
})();
