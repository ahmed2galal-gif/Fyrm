// Converts an SVG background into JPG and WebP raster images at multiple sizes
// Usage: node scripts/svg-to-raster.js images/bckgrd-generated.svg

const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

async function run(src) {
  if (!fs.existsSync(src)) {
    console.error('Source not found:', src);
    process.exit(1);
  }
  const dir = path.dirname(src);
  const base = path.basename(src, path.extname(src));

  const sizes = [
    { name: base + '-large', width: 1920, height: 1080 },
    { name: base + '-medium', width: 1280, height: 720 },
    { name: base + '-small', width: 640, height: 360 }
  ];

  for (const s of sizes) {
    const outJpg = path.join(dir, s.name + '.jpg');
    const outWebp = path.join(dir, s.name + '.webp');
    console.log(`Generating ${outJpg} and ${outWebp}...`);
    await sharp(src, { density: 300 })
      .resize(s.width, s.height, { fit: 'cover' })
      .jpeg({ quality: 80, progressive: true })
      .toFile(outJpg);
    await sharp(src, { density: 300 })
      .resize(s.width, s.height, { fit: 'cover' })
      .webp({ quality: 75 })
      .toFile(outWebp);
  }
  console.log('Done. Files created in', dir);
}

const src = process.argv[2] || 'images/bckgrd-generated.svg';
run(src).catch(err => { console.error(err); process.exit(1); });