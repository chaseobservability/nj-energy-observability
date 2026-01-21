#!/usr/bin/env bash
set -euo pipefail

# === NJ Energy Observability: Render OG + icon assets from canonical SVG ===
# Canonical source:
#   docs/assets/svg/nj-outline.svg
#
# Outputs:
#   docs/assets/og/og-image.png            (1200x630 for iMessage/OG)
#   docs/assets/icons/favicon-16x16.png
#   docs/assets/icons/favicon-32x32.png
#   docs/assets/icons/favicon.ico          (multi-size)
#   docs/assets/icons/apple-touch-icon.png (180x180)

SVG="docs/assets/svg/nj-outline.svg"
OUT_OG_DIR="docs/assets/og"
OUT_ICON_DIR="docs/assets/icons"
TMP_DIR=".tmp_assets"

mkdir -p "$OUT_OG_DIR" "$OUT_ICON_DIR" "$TMP_DIR"

# --- 1) Create Open Graph image (1200x630) ---
# Render a large transparent PNG (keeps edges crisp)
inkscape "$SVG" --export-type=png --export-filename="$TMP_DIR/nj-outline-1024.png" --export-width=1024 --export-area-drawing
magick "$TMP_DIR/nj-outline-1024.png" -bordercolor none -border 80 "$TMP_DIR/nj-outline-1024-padded.png"

# Compose onto OG canvas (white background), scaled to fit
magick -size 1200x630 canvas:white \
  "$TMP_DIR/nj-outline-1024-padded.png" -resize 900x500 \
  -gravity center -composite \
  "$OUT_OG_DIR/og-image.png"

echo "Wrote $OUT_OG_DIR/og-image.png (1200x630)"

# --- 2) Generate Apple touch icon (180x180) ---
inkscape "$SVG" --export-type=png --export-filename="$TMP_DIR/nj-outline-256.png" --export-width=256 --export-area-drawing
magick "$TMP_DIR/nj-outline-256.png" -bordercolor none -border 20 "$TMP_DIR/nj-outline-256-padded.png"

magick -size 180x180 canvas:white \
  "$TMP_DIR/nj-outline-256-padded.png" -resize 120x120 \
  -gravity center -composite \
  "$OUT_ICON_DIR/apple-touch-icon.png"

echo "Wrote $OUT_ICON_DIR/apple-touch-icon.png (180x180)"

# --- 3) Generate favicons (PNG 16/32) ---
magick "$TMP_DIR/nj-outline-256-padded.png" -resize 28x28 -gravity center -background white \
  -extent 32x32 "$OUT_ICON_DIR/favicon-32x32.png"

magick "$TMP_DIR/nj-outline-256-padded.png" -resize 14x14 -gravity center -background white \
  -extent 16x16 "$OUT_ICON_DIR/favicon-16x16.png"

echo "Wrote $OUT_ICON_DIR/favicon-32x32.png and favicon-16x16.png"

# --- 4) Generate favicon.ico (multi-size) ---
magick "$OUT_ICON_DIR/favicon-16x16.png" "$OUT_ICON_DIR/favicon-32x32.png" \
  "$OUT_ICON_DIR/favicon.ico"

echo "Wrote $OUT_ICON_DIR/favicon.ico"

# --- 5) Cleanup ---
rm -rf "$TMP_DIR"
echo "Done."
