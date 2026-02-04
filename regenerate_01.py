# -*- coding: utf-8 -*-
"""1枚目のみ再生成"""
import sys
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image
from pathlib import Path

OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/fashion_images")

# 既存ファイルを削除
old_file = OUTPUT_DIR / "theme1_spring_01.png"
if old_file.exists():
    old_file.unlink()

WIDTH_INCH = 3.0
HEIGHT_INCH = 5.33

prompt = """Generate a photorealistic fashion photograph. This must be a real photograph, NOT an illustration, NOT a drawing, NOT anime style.

CRITICAL: 
- Photorealistic photograph ONLY
- NO text anywhere in the image
- NO borders or frames
- NO illustrations or drawings
- The image must fill the entire canvas edge to edge

SUBJECT:
- Japanese male model in his early 20s
- Short textured hair, youthful and fresh appearance
- Slim athletic build

CLOTHING (the featured product):
- Light mint green cotton knit sweater (thin, crew neck)
- White wide tapered pants
- White sneakers

SETTING:
- Cherry blossom lined path in full bloom
- Petals falling gently
- Soft spring afternoon sunlight

POSE:
- Walking naturally, glancing back over shoulder
- Relaxed genuine smile

PHOTOGRAPHY STYLE:
- Professional fashion editorial photography
- Natural lighting
- Full body shot
- Sharp focus, high resolution
- Magazine quality
"""

print("1枚目を再生成中...")
result = generate_partial_image(
    prompt=prompt,
    width_inch=WIDTH_INCH,
    height_inch=HEIGHT_INCH,
    output_dir=str(OUTPUT_DIR),
    filename="theme1_spring_01"
)

if result:
    print(f"✅ 成功: {result}")
else:
    print("❌ 失敗")
