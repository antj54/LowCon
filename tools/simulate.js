#!/usr/bin/env node
// Strategy regression check for Intel Cell Sim.
// Runs the real engine from index.html headlessly against a crisis file and
// prints the ending and score for a set of fixed strategies.
// Usage: node tools/simulate.js [crises/border-buildup.json]
'use strict';
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const crisisPath = path.resolve(root, process.argv[2] || 'crises/border-buildup.json');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const engine = (html.match(/<script>([\s\S]*)<\/script>/) || [])[1];
if (!engine) { console.error('No inline engine script found in index.html'); process.exit(1); }
const crisis = JSON.parse(fs.readFileSync(crisisPath, 'utf8'));

function run(plan, doubt) {
  const handlers = {};
  const els = { app: { innerHTML: '' }, layer: { innerHTML: '' } };
  global.document = { getElementById: id => els[id] || null, addEventListener: (t, f) => { handlers[t] = f; }, hidden: false };
  global.window = { scrollTo() {} };
  global.localStorage = { getItem: () => null, setItem() {} };
  global.setInterval = () => 0;
  Object.defineProperty(globalThis, 'navigator', { value: {}, configurable: true, writable: true });
  global.fetch = async () => ({ ok: true, json: async () => JSON.parse(JSON.stringify(crisis)) });
  eval(engine);
  const click = (act, ds = {}) => handlers.click({ target: { closest: () => ({ dataset: Object.assign({ act }, ds), classList: { contains: () => false } }) } });
  return new Promise(resolve => setTimeout(() => {
    click('start'); click('playahead');
    plan.forEach(([h, c], i) => {
      crisis.reports.filter(r => r.day === i + 1 && doubt(r)).forEach(r => click('flag', { id: r.id }));
      click('hyp', { v: h }); click('conf', { v: c }); click('confirmsend');
    });
    const out = els.app.innerHTML;
    const ending = (out.match(/<h2>([^<]+)<\/h2>/) || [])[1];
    const total = (out.match(/class="n">([^<]+)</) || [])[1];
    const parts = (out.match(/calls[^<]+/) || [])[0];
    resolve(`${ending} ${total} | ${parts}`);
  }, 50));
}

const none = () => false, plants = r => r.kind === 'planted', all = () => true;
const STRATEGIES = [
  ['Best play', [['H3','moderate'],['H3','moderate'],['H2','moderate'],['H2','high'],['H2','high']], none],
  ['Best play, doubt plants', [['H3','moderate'],['H3','moderate'],['H2','moderate'],['H2','high'],['H2','high']], plants],
  ['Best play, doubt everything', [['H3','moderate'],['H3','moderate'],['H2','moderate'],['H2','high'],['H2','high']], all],
  ['Never above Moderate', [['H3','moderate'],['H3','moderate'],['H2','moderate'],['H2','moderate'],['H2','moderate']], none],
  ['Always worst case', Array(5).fill(['H2','high']), none],
  ['Trust the official line', Array(5).fill(['H1','moderate']), none],
  ['"Just signaling"', Array(5).fill(['H3','moderate']), none],
  ['Always hedge (Low)', [['H3','low'],['H3','low'],['H2','low'],['H2','low'],['H2','low']], none],
];

(async () => {
  console.log(`Crisis: ${crisis.title} (${path.relative(root, crisisPath)})`);
  for (const [name, plan, doubt] of STRATEGIES) console.log(name.padEnd(30), await run(plan, doubt));
})();
