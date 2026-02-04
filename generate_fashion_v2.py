# -*- coding: utf-8 -*-
"""
テーマ1「清涼感のある、私だけの春の装い」- 改良版
- アスペクト比: 4:5（少し縦を削る）
- 構図: 上着に注目、顔は頭の天辺が上端、ズボンはカット
- 服タイプ統一: 春向けライトニット（クルーネック）の色違い
- モデル: イタリア人男性
"""
import sys
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image
from pathlib import Path

# 出力ディレクトリ
OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/fashion_images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 既存ファイルを削除
for f in OUTPUT_DIR.glob("theme1_spring_*.png"):
    f.unlink()

# アスペクト比 4:5（縦長だが少し縦を削る）
WIDTH_INCH = 4.0
HEIGHT_INCH = 5.0

# テーマ1用の服タイプ: 春向けライトコットンニット（クルーネック）
# 5色のバリエーション
VARIATIONS = [
    {
        "filename": "theme1_spring_01",
        "color": "ペールミント（淡いミントグリーン）",
        "texture": "細かいリブ編み、軽やかなコットン素材",
        "model_hair": "ダークブラウンのウェーブがかった髪、少し長め",
        "model_feature": "彫りの深い顔立ち、軽い無精髭",
        "background": "柔らかいベージュの壁、春の自然光",
    },
    {
        "filename": "theme1_spring_02",
        "color": "スカイブルー（明るい水色）",
        "texture": "滑らかなハイゲージニット、薄手",
        "model_hair": "黒髪のショートヘア、きれいに整えた",
        "model_feature": "シャープな顎のライン、端正な顔立ち",
        "background": "白い壁、クリーンな自然光",
    },
    {
        "filename": "theme1_spring_03",
        "color": "オフホワイト（生成り色）",
        "texture": "ざっくりしたローゲージニット、立体感のある編み目",
        "model_hair": "ライトブラウンの髪、自然なパーマ",
        "model_feature": "柔らかい表情、親しみやすい雰囲気",
        "background": "淡いグレーの背景、ソフトな光",
    },
    {
        "filename": "theme1_spring_04",
        "color": "ラベンダー（淡い紫）",
        "texture": "ミドルゲージのリブニット、程よい厚み",
        "model_hair": "ダークブラウンのストレート、センターパート",
        "model_feature": "知的な印象、落ち着いた表情",
        "background": "コンクリートの壁、都会的な雰囲気",
    },
    {
        "filename": "theme1_spring_05",
        "color": "サーモンピンク（くすんだピンク）",
        "texture": "細身のフィットしたニット、上質なコットン",
        "model_hair": "黒髪でやや長め、ナチュラルなスタイリング",
        "model_feature": "力強い眉、男らしい顔立ち",
        "background": "暖かみのあるベージュ、柔らかい影",
    },
]

def create_fashion_prompt(v):
    """ファッション画像生成用のプロンプトを作成"""
    prompt = f"""A high-end fashion photography focusing on a spring knitwear sweater.

CRITICAL COMPOSITION REQUIREMENTS:
- The sweater/top is the HERO of this image - it must be prominently displayed
- Frame: The model's head should be cropped at the top (only showing from forehead or top of head down)
- The bottom of the frame should cut off at the waist or upper hip area - NO pants visible
- The sweater fills most of the frame, showing texture and color clearly
- Upper body/torso shot only

CRITICAL IMAGE REQUIREMENTS:
- Photorealistic photograph, NOT illustration
- NO text, NO borders, NO frames, NO margins
- Image fills entire canvas edge-to-edge

MODEL:
- Italian male model, late 20s to early 30s
- {v['model_hair']}
- {v['model_feature']}
- Natural relaxed pose, hands may be in pockets or relaxed at sides

THE FEATURED PRODUCT - Spring Light Cotton Knit Sweater (Crew Neck):
- Color: {v['color']}
- Texture: {v['texture']}
- Style: Classic crew neck, relaxed fit, perfect for spring layering
- The knit texture and color should be clearly visible and attractive

BACKGROUND:
- {v['background']}
- Shallow depth of field, background slightly blurred to emphasize the sweater

PHOTOGRAPHY STYLE:
- Professional fashion editorial photography
- Soft, flattering lighting that shows fabric texture
- Magazine quality, sharp focus on the clothing
- The sweater is the star - composition emphasizes it
"""
    return prompt

def main():
    print("=" * 60)
    print("テーマ1: 清涼感のある、私だけの春の装い")
    print("服タイプ: 春向けライトコットンニット（クルーネック）× 5色")
    print("=" * 60)
    
    for i, v in enumerate(VARIATIONS, 1):
        print(f"\n[{i}/5] {v['color']} を生成中...")
        
        prompt = create_fashion_prompt(v)
        
        result = generate_partial_image(
            prompt=prompt,
            width_inch=WIDTH_INCH,
            height_inch=HEIGHT_INCH,
            output_dir=str(OUTPUT_DIR),
            filename=v['filename']
        )
        
        if result:
            print(f"  ✅ 成功: {result}")
        else:
            print(f"  ❌ 失敗: {v['filename']}")
    
    print("\n" + "=" * 60)
    print(f"完了！出力先: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
