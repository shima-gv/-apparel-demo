# -*- coding: utf-8 -*-
"""1枚目と2枚目を再生成"""
import sys
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image
from pathlib import Path

OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/fashion_images")

WIDTH_INCH = 4.0
HEIGHT_INCH = 5.0

# 1枚目: 室内→外に変更
prompt_01 = """A candid, lifestyle fashion photograph capturing a natural outdoor moment.

CRITICAL COMPOSITION:
- The sweater is the main focus - fills most of the frame
- Upper body/torso shot, head partially cropped or at very top of frame
- Sweater should be prominently displayed and clearly visible

CRITICAL IMAGE REQUIREMENTS:
- Photorealistic photograph with natural, editorial feel
- NO text, NO borders, NO frames
- Image fills entire canvas edge-to-edge

MODEL:
- Italian male model, late 20s to early 30s
- Warm friendly smile, light stubble
- Natural wavy dark brown hair

THE FEATURED OUTFIT:
- Sage green cotton knit sweater (crew neck, slightly oversized, relaxed fit)
- The knit texture should be clearly visible

SCENE & BACKGROUND:
- OUTDOOR: Standing on a sunny terrace or rooftop with city view in soft focus
- Morning golden hour light, warm tones
- Architectural elements slightly blurred in background

POSE & MOMENT:
- Leaning casually against a railing, hands in pockets
- Relaxed genuine smile, looking slightly off camera
- Capturing a moment of enjoying the view

PHOTOGRAPHY STYLE:
- Lifestyle editorial photography
- Natural warm lighting
- Magazine quality but candid feel
"""

# 2枚目: 服にもっとフォーカス
prompt_02 = """A fashion photograph with strong focus on the knitwear sweater.

CRITICAL COMPOSITION:
- The sweater MUST fill at least 70% of the frame
- CLOSE-UP upper body shot - from chest to just above the head
- Head should be cropped at forehead level or higher
- The sweater texture, buttons, and details must be clearly visible
- This is a PRODUCT-focused shot, not a portrait

CRITICAL IMAGE REQUIREMENTS:
- Photorealistic photograph
- NO text, NO borders, NO frames
- Image fills entire canvas edge-to-edge

MODEL:
- Italian male model, late 20s to early 30s
- Sharp features, clean shaven, dark hair
- Only lower face/chin area may be visible

THE FEATURED OUTFIT:
- Cream white waffle knit henley sweater with 3 buttons
- Buttons partially undone showing a hint of collarbone
- The waffle texture MUST be sharp and detailed

SCENE & BACKGROUND:
- OUTDOOR: European cafe terrace, but heavily blurred (bokeh)
- Warm afternoon light creating soft shadows on the knit
- Background is just colors and shapes, not distracting

POSE & MOMENT:
- One hand raised near chest, touching the sweater
- Natural pose that shows off the fabric and fit
- Relaxed confident stance

PHOTOGRAPHY STYLE:
- Fashion product photography with lifestyle context
- Shallow depth of field - sweater in sharp focus
- The sweater is the star of this image
"""

# 既存ファイルを削除して再生成
for fname, prompt in [("theme1_spring_01", prompt_01), ("theme1_spring_02", prompt_02)]:
    old_file = OUTPUT_DIR / f"{fname}.png"
    if old_file.exists():
        old_file.unlink()
    
    print(f"{fname} を再生成中...")
    result = generate_partial_image(
        prompt=prompt,
        width_inch=WIDTH_INCH,
        height_inch=HEIGHT_INCH,
        output_dir=str(OUTPUT_DIR),
        filename=fname
    )
    
    if result:
        print(f"  ✅ 成功: {result}")
    else:
        print(f"  ❌ 失敗: {fname}")

print("\n完了！")
