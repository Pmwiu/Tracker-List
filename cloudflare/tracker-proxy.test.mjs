// 零依赖单元测试：node --test cloudflare/tracker-proxy.test.mjs
import test from 'node:test';
import assert from 'node:assert';
import {
  pruneBuckets, noteRoute, normalize, resolveRepoPath,
  cacheControlFor, fetchWithTimeout, contentType,
} from './tracker-proxy.js';

test('pruneBuckets removes expired and caps size', () => {
  const m = new Map();
  const now = 1_000_000;
  m.set('a', { windowStart: now - 100_000, count: 5 }); // expired
  m.set('b', { windowStart: now - 10, count: 1 });       // fresh
  let size = pruneBuckets(m, now, 60_000, 100);
  assert.strictEqual(size, 1);
  assert.ok(!m.has('a'));
  assert.ok(m.has('b'));
  // cap: add many fresh, force prune to max
  for (let i = 0; i < 10; i++) m.set('k' + i, { windowStart: now, count: 1 });
  size = pruneBuckets(m, now, 60_000, 3);
  assert.ok(size <= 3, `expected <=3 got ${size}`);
});

test('noteRoute caps distinct routes into other', () => {
  const r = {};
  for (let i = 0; i < 5; i++) noteRoute(r, 'p' + i, 3);
  // first 3 distinct recorded, then overflow -> other
  assert.strictEqual(r.p0, 1);
  assert.ok(r.other >= 1);
  assert.ok(Object.keys(r).length <= 4); // 3 + other
});

test('normalize handles root and index', () => {
  assert.strictEqual(normalize('/'), 'index.html');
  assert.strictEqual(normalize('/Best.TXT'), 'best.txt');
  assert.strictEqual(normalize('/s'), 'index.html'); // 裸 /s 归首页（原设计）
  assert.strictEqual(normalize('/s/alive'), 's/alive');
});

test('resolveRepoPath maps aliases and dynamic', () => {
  assert.strictEqual(resolveRepoPath('best.txt'), 'trackers/trackers_alive.txt');
  assert.strictEqual(resolveRepoPath('p/udp.txt'), 'trackers/trackers_udp.txt');
  assert.strictEqual(resolveRepoPath('src/ngosang_best.txt'), 'trackers/trackers_ngosang_best.txt');
  assert.strictEqual(resolveRepoPath('foo'), 'docs/foo');
});

test('cacheControlFor: txt cached, html short', () => {
  assert.match(cacheControlFor('trackers/trackers_alive.txt'), /max-age=300/);
  assert.match(cacheControlFor('docs/index.html'), /max-age=60/);
});

test('contentType maps by extension', () => {
  assert.match(contentType('x.json'), /application\/json/);
  assert.match(contentType('x.html'), /text\/html/);
  assert.match(contentType('x.txt'), /text\/plain/);
});

test('fetchWithTimeout aborts a hanging fetch', async () => {
  const hanging = (u, opts) => new Promise((_, reject) => {
    opts.signal.addEventListener('abort', () => reject(new Error('aborted')));
  });
  await assert.rejects(() => fetchWithTimeout('http://x', 50, hanging), /aborted/);
});

test('fetchWithTimeout returns on success', async () => {
  const ok = async () => ({ status: 200 });
  const res = await fetchWithTimeout('http://x', 500, ok);
  assert.strictEqual(res.status, 200);
});
