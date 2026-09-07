// Запусти: node export_node.js
// Нужен: npm install puppeteer (установит свой Chromium)
const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  const file = 'file://' + path.resolve(__dirname, 'index.html');
  await page.goto(file, { waitUntil: 'networkidle0' });
  await page.emulateMediaType('print');
  try { await page.waitForFunction('document.fonts.ready', { timeout: 4000 }); } catch(e){}
  await new Promise(r => setTimeout(r, 800));
  await page.pdf({
    path: path.resolve(__dirname, 'Медиацентр_презентация+кейсы.pdf'),
    width: '1280px',
    height: '720px',
    printBackground: true,
    preferCSSPageSize: true,
  });
  await browser.close();
  console.log('✅ PDF готов: Mediacentr_presentation.pdf');
})();
