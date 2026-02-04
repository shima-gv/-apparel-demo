# -*- coding: utf-8 -*-
"""
テーマ1「清涼感のある、私だけの春の装い」のファッション画像を生成
nanabananapro.pyを使用
"""
import sys
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image
from pathlib import Path
import os

# 出力ディレクトリ
OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/fashion_images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 既存ファイルを削除
for f in OUTPUT_DIR.glob("theme1_spring_*.png"):
    f.unlink()

# スマホ向け縦長アスペクト比（9:16）
WIDTH_INCH = 3.0
HEIGHT_INCH = 5.33  # 約9:16比率

# テーマ1: 清涼感のある、私だけの春の装い
THEME = "清涼感のある、私だけの春の装い - 軽やかな素材×爽やかカラーで春先を先取り"

# 5つの異なるコーディネート・モデル・シーン
VARIATIONS = [
    {
        "filename": "theme1_spring_01",
        "model": "20代前半の日本人男性、短めのマッシュヘア、爽やかで若々しい印象、細身体型",
        "outfit": "淡いミントグリーンのコットンニット（薄手、クルーネック）と白のワイドテーパードパンツ、白スニーカー",
        "scene": "桜並木の遊歩道、満開の桜、花びらが舞う",
        "pose": "自然に歩きながら少し振り返る、リラックスした笑顔",
    },
    {
        "filename": "theme1_spring_02",
        "model": "30代前半の日本人男性、センターパートの黒髪、知的で落ち着いた印象、標準体型",
        "outfit": "白いオープンカラーシャツ（リネン素材）とベージュのチノパン、ブラウンレザーローファー",
        "scene": "白い壁のおしゃれなカフェテラス、観葉植物が見える",
        "pose": "椅子に座ってコーヒーカップを持つ、穏やかな表情",
    },
    {
        "filename": "theme1_spring_03",
        "model": "20代後半の日本人男性、ウェーブのかかったミディアムヘア、アーティスティックな雰囲気",
        "outfit": "ライトブルーのストライプシャツ（袖をロールアップ）とネイビーのアンクルパンツ、白キャンバススニーカー",
        "scene": "海沿いの遊歩道、青い海と空が背景、白い手すり",
        "pose": "手すりにもたれて遠くを見つめる、風で髪がなびく",
    },
    {
        "filename": "theme1_spring_04",
        "model": "30代の日本人男性、短髪でスポーティな印象、がっしりした体格",
        "outfit": "オフホワイトのヘンリーネックTシャツ（七分袖）とカーキのジョガーパンツ、グレースニーカー",
        "scene": "緑豊かな公園、木漏れ日が差す芝生エリア",
        "pose": "芝生に座って足を伸ばす、リラックスした自然体",
    },
    {
        "filename": "theme1_spring_05",
        "model": "20代半ばの日本人男性、きれいめな黒髪ショート、モデル体型で背が高い",
        "outfit": "ペールピンクのオーバーサイズTシャツとグレーのスラックス、白レザースニーカー",
        "scene": "シンプルなコンクリートの壁、都会的なミニマル背景",
        "pose": "壁に軽くもたれて正面を見る、クールで自信のある表情",
    },
]

def create_fashion_prompt(variation):
    """ファッション画像生成用のプロンプトを作成"""
    prompt = f"""A high-quality fashion photography, editorial style photo for a fashion magazine.

CRITICAL REQUIREMENTS:
- Generate ONLY the photograph itself, NO text, NO borders, NO frames, NO margins, NO captions
- The image must be a pure photograph filling the entire canvas edge-to-edge
- Photorealistic, professional fashion photography quality

MODEL:
{variation['model']}

OUTFIT (the product being featured):
{variation['outfit']}

SCENE/BACKGROUND:
{variation['scene']}

POSE:
{variation['pose']}

STYLE:
- Professional fashion magazine photography
- Natural lighting appropriate for the scene
- The outfit/clothing is the hero product and should be clearly visible and attractive
- Full body or 3/4 body shot
- High resolution, sharp focus on the model and clothing
- Theme: {THEME}

STRICTLY FORBIDDEN:
- Any text, titles, captions, or typography
- Any borders, frames, margins, or white space around the image
- Any graphic design elements or overlays
- The photo must fill 100% of the image area
"""
    return prompt

def main():
    print("=" * 50)
    print("テーマ1: 清涼感のある、私だけの春の装い")
    print("5枚のファッション画像を生成します")
    print("=" * 50)
    
    for i, variation in enumerate(VARIATIONS, 1):
        print(f"\n[{i}/5] {variation['scene']} を生成中...")
        
        prompt = create_fashion_prompt(variation)
        
        result = generate_partial_image(
            prompt=prompt,
            width_inch=WIDTH_INCH,
            height_inch=HEIGHT_INCH,
            output_dir=str(OUTPUT_DIR),
            filename=variation['filename']
        )
        
        if result:
            print(f"  ✅ 成功: {result}")
        else:
            print(f"  ❌ 失敗: {variation['filename']}")
    
    print("\n" + "=" * 50)
    print(f"完了！出力先: {OUTPUT_DIR}")
    print("=" * 50)

if __name__ == "__main__":
    main()
