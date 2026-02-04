# -*- coding: utf-8 -*-
"""5枚目のみ再生成"""
import sys
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image
from pathlib import Path

OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/fashion_images")

# 既存ファイルを削除
old_file = OUTPUT_DIR / "theme1_spring_05.png"
if old_file.exists():
    old_file.unlink()

WIDTH_INCH = 4.0
HEIGHT_INCH = 5.0

prompt = """A high-end fashion photography focusing on a spring knitwear sweater.

CRITICAL COMPOSITION REQUIREMENTS:
- The sweater/top is the HERO of this image - it must be prominently displayed
- Frame: The model's head should be cropped at the top (only showing from forehead or top of head down)
- The bottom of the frame should cut off at the waist or upper hip area - NO pants visible
- The sweater fills most of the frame, showing texture and color clearly
- Upper body/torso shot only
- PORTRAIT ORIENTATION (taller than wide)

CRITICAL IMAGE REQUIREMENTS:
- Photorealistic photograph, NOT illustration
- NO text, NO borders, NO frames, NO margins
- Image fills entire canvas edge-to-edge
- Aspect ratio: 4:5 (portrait/vertical)

MODEL:
- Italian male model, late 20s to early 30s
- Dark wavy hair, slightly long, natural styling
- Strong eyebrows, masculine handsome features
- Natural relaxed pose, hands may be in pockets or relaxed at sides

THE FEATURED PRODUCT - Spring Light Cotton Knit Sweater (Crew Neck):
- Color: Salmon Pink (muted dusty pink tone)
- Texture: Fine gauge knit, fitted silhouette, premium cotton
- Style: Classic crew neck, relaxed fit, perfect for spring layering
- The knit texture and color should be clearly visible and attractive

BACKGROUND:
- Warm beige tones, soft shadows
- Shallow depth of field, background slightly blurred to emphasize the sweater

PHOTOGRAPHY STYLE:
- Professional fashion editorial photography
- Soft, flattering lighting that shows fabric texture
- Magazine quality, sharp focus on the clothing
- The sweater is the star - composition emphasizes it
"""

print("5枚目を再生成中...")
result = generate_partial_image(
    prompt=prompt,
    width_inch=WIDTH_INCH,
    height_inch=HEIGHT_INCH,
    output_dir=str(OUTPUT_DIR),
    filename="theme1_spring_05"
)

if result:
    print(f"✅ 成功: {result}")
else:
    print("❌ 失敗")
