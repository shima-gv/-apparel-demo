# -*- coding: utf-8 -*-
"""桜の背景画像を生成"""
import sys
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image
from pathlib import Path

OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/fashion_images")

# テーマヘッダー用の横長画像
WIDTH_INCH = 8.0
HEIGHT_INCH = 2.0

prompt = """A beautiful cherry blossom (sakura) photograph for use as a background overlay.

REQUIREMENTS:
- Soft, dreamy cherry blossoms in full bloom
- Delicate pink petals, some falling gently
- Soft focus, bokeh effect on background
- Light and airy atmosphere
- Gentle spring sunlight filtering through
- Color palette: soft pinks, whites, hints of pale green
- Ethereal and romantic mood

STYLE:
- Photorealistic but with a soft, dreamy quality
- Would work well as a semi-transparent overlay
- Not too busy - leaves space for text overlay
- Horizontal/landscape orientation

NO text, NO borders, pure photography.
"""

print("桜の背景画像を生成中...")
result = generate_partial_image(
    prompt=prompt,
    width_inch=WIDTH_INCH,
    height_inch=HEIGHT_INCH,
    output_dir=str(OUTPUT_DIR),
    filename="theme1_sakura_bg"
)

if result:
    print(f"✅ 成功: {result}")
else:
    print("❌ 失敗")
