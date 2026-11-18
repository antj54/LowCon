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

// A plan is one entry per day: [hypothesis, likelihood, [evidence ids]].
function run(plan, doubt, cfg) {
  const handlers = {};
  const els = { app: { innerHTML: '' }, layer: { innerHTML: '' } };
  global.document = { getElementById: id => els[id] || null, addEventListener: (t, f) => { handlers[t] = f; }, hidden: false };
  global.window = { scrollTo() {} };
  global.localStorage = { getItem: () => null, setItem() {} };
  global.setInterval = () => 0;
  Object.defineProperty(globalThis, 'navigator', { value: {}, configurable: true, writable: true });
  global.fetch = async url => /config\.json$/.test(url)
    ? (cfg ? { ok: true, json: async () => cfg } : { ok: false, json: async () => ({}) })
    : { ok: true, json: async () => JSON.parse(JSON.stringify(crisis)) };
  eval(engine);
  const click = (act, ds = {}) => handlers.click({ target: { closest: () => ({ dataset: Object.assign({ act }, ds), classList: { contains: () => false } }) } });
  return new Promise(resolve => setTimeout(() => {
    click('start'); click('playahead');
    const calls = [];
    plan.forEach(([h, lik, ev], i) => {
      crisis.reports.filter(r => r.day === i + 1 && doubt(r)).forEach(r => click('flag', { id: r.id }));
      click('tab', { v: 'brief' });
      click('hyp', { v: h }); click('lik', { v: lik });
      (ev || []).forEach(id => click('ev', { id }));
      const conf = ((els.app.innerHTML.match(/Confidence, from your evidence<\/span><b>([^<]+)</) || [])[1] || '?');
      calls.push(`${h} ${lik} (${conf})`);
      click('confirmsend');
      if (cfg && cfg.playtest) {
        if (!/How was Day/.test(els.layer.innerHTML)) throw new Error('Playtest reaction sheet missing on day ' + (i + 1));
        click('react', { v: 'engaging' }); click('reactdone');
      }
    });
    if (cfg && cfg.playtest) { click('realism', { id: 'R-3-03' }); click('debrief', { q: 'sixth', v: 'yes' }); }
    const out = els.app.innerHTML; lastHtml = out; lastLayer = els.layer.innerHTML;
    const ending = (out.match(/<h2>([^<]+)<\/h2>/) || [])[1];
    const total = (out.match(/class="n">([^<]+)</) || [])[1];
    const parts = (out.match(/calls[^<]+/) || [])[0];
    resolve({ line: `${ending} ${total} | ${parts}`, calls });
  }, 50));
}

const none = () => false, plants = r => r.kind === 'planted', all = () => true;
const BEST = [
  ['H3', 'likely', ['R-1-01', 'R-1-02', 'R-1-04']],
  ['H3', 'likely', ['R-2-01', 'R-2-02']],
  ['H2', 'likely', ['R-3-02', 'R-3-04', 'R-3-01']],
  ['H2', 'very', ['R-4-01', 'R-3-02', 'R-4-04']],
  ['H2', 'very', ['R-5-03', 'R-5-04', 'R-4-01']],
];
const STRATEGIES = [
  ['Best play', BEST, none],
  ['Best play, doubt plants', BEST, plants],
  ['Best play, doubt everything', BEST, all],
  ['Very likely from Day 3', [BEST[0], BEST[1], ['H2', 'very', ['R-3-02', 'R-3-04', 'R-3-01']], BEST[3], BEST[4]], none],
  ['Very likely, thin evidence', [BEST[0], BEST[1], BEST[2], ['H2', 'very', ['R-4-01']], ['H2', 'very', ['R-5-03']]], none],
  ['Never above Likely', [BEST[0], BEST[1], BEST[2], ['H2', 'likely', ['R-4-01', 'R-3-02', 'R-4-04']], ['H2', 'likely', ['R-5-03', 'R-5-04']]], none],
  ['Always worst case', [['H2', 'almost', ['R-1-03', 'R-1-01']], ['H2', 'almost', ['R-2-01', 'R-2-03']], ['H2', 'almost', ['R-3-02', 'R-3-04']], ['H2', 'almost', ['R-4-01', 'R-4-04']], ['H2', 'almost', ['R-5-03', 'R-5-04']]], none],
  ['Trust the official line', Array(5).fill(['H1', 'likely', []]), none],
  ['"Just signaling"', Array(5).fill(['H3', 'likely', []]), none],
  ['Always hedge (roughly even)', [['H3', 'even', []], ['H3', 'even', []], ['H2', 'even', []], ['H2', 'even', []], ['H2', 'even', []]], none],
];

(async () => {
  console.log(`Crisis: ${crisis.title} (${path.relative(root, crisisPath)})`);
  for (const [name, plan, doubt] of STRATEGIES) {
    const r = await run(plan, doubt);
    console.log(name.padEnd(30), r.line);
    if (process.argv.includes('--calls')) console.log(' '.repeat(31) + r.calls.join(' · '));
  }
  const pt = await run(BEST, none, { playtest: true });
  console.log('Playtest build'.padEnd(30), pt.line, /Playtest debrief/.test(lastHtml) ? '| debrief shown' : '| DEBRIEF MISSING');
})();
