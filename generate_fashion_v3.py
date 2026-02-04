# -*- coding: utf-8 -*-
"""
テーマ1「清涼感のある、私だけの春の装い」- 改良版v3
- ポーズ・背景・シチュエーションにバリエーション
- 自然な日常の一コマを切り取ったような写真
- 色は自然な範囲でバリエーション（きれいに揃えすぎない）
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

# アスペクト比 4:5
WIDTH_INCH = 4.0
HEIGHT_INCH = 5.0

# 5つの多様なシチュエーション（同じ春向けニットだが、より自然なバリエーション）
VARIATIONS = [
    {
        "filename": "theme1_spring_01",
        "outfit": "淡いセージグリーンのコットンニット（クルーネック、ややオーバーサイズ）",
        "scene": "暖かみのある木目調の壁の前、観葉植物が横に見える",
        "pose": "両手を軽くポケットに入れて、少し体を傾けながらカメラ目線で微笑む",
        "situation": "自宅でくつろぐ休日の朝",
        "model_vibe": "ナチュラルで親しみやすい雰囲気、軽い無精髭",
    },
    {
        "filename": "theme1_spring_02",
        "outfit": "クリームホワイトのワッフルニット（ヘンリーネック、ボタン2つ開け）",
        "scene": "明るいカフェのテラス席、白いテーブルとコーヒーカップが見える",
        "pose": "椅子に座ってコーヒーカップを片手に持ち、窓の外を見ている横顔",
        "situation": "休日のカフェでゆったり過ごす時間",
        "model_vibe": "知的で落ち着いた印象、整った黒髪",
    },
    {
        "filename": "theme1_spring_03",
        "outfit": "くすんだブルーグレーのリブニット（モックネック、タイトフィット）",
        "scene": "石畳の路地、古いレンガの壁が背景、柔らかい午後の光",
        "pose": "歩きながら振り返る瞬間、片手でニットの裾を軽く持つ",
        "situation": "街を散策中のワンシーン",
        "model_vibe": "スタイリッシュで都会的、ウェーブのある髪",
    },
    {
        "filename": "theme1_spring_04",
        "outfit": "ナチュラルベージュのケーブルニット（Vネック、インナーに白Tシャツ）",
        "scene": "公園のベンチ付近、背景に桜や新緑がぼんやり見える",
        "pose": "ベンチの背もたれに腕を乗せて座り、足を組んでリラックス",
        "situation": "春の公園でのんびり過ごす午後",
        "model_vibe": "爽やかでスポーティ、短めの髪",
    },
    {
        "filename": "theme1_spring_05",
        "outfit": "淡いラベンダーグレーのカシミヤ混ニット（ラウンドネック、上質な光沢）",
        "scene": "モダンなアパートの窓際、自然光が差し込む、シンプルなインテリア",
        "pose": "窓枠に寄りかかり、腕を組んで外を眺める、思慮深い表情",
        "situation": "静かな朝のひととき",
        "model_vibe": "洗練された大人の雰囲気、ダークブラウンの髪",
    },
]

def create_fashion_prompt(v):
    """ファッション画像生成用のプロンプトを作成"""
    prompt = f"""A candid, lifestyle fashion photograph that captures a natural moment in daily life.

CRITICAL COMPOSITION:
- The sweater/top is the main focus but shot in a natural, unstaged way
- Frame: Head may be partially cropped at top, or full face visible depending on pose
- Show from chest/torso area, may include some hip area
- NOT a stiff product shot - capture movement and life

CRITICAL IMAGE REQUIREMENTS:
- Photorealistic photograph with natural, editorial feel
- NO text, NO borders, NO frames
- Image fills entire canvas edge-to-edge
- Looks like a real candid photograph, not overly posed

MODEL:
- Italian male model, late 20s to early 30s
- {v['model_vibe']}
- Expression and body language should feel genuine and relaxed

THE FEATURED OUTFIT:
{v['outfit']}
- The knit should look natural and lived-in, not perfectly pressed
- Show natural fabric texture and drape

SCENE & BACKGROUND:
{v['scene']}
- Background should have depth and interest, slightly out of focus
- Natural lighting appropriate to the scene

POSE & MOMENT:
{v['pose']}
- Capture a genuine moment: {v['situation']}
- Movement or action makes it feel alive

PHOTOGRAPHY STYLE:
- Lifestyle editorial photography
- Natural, warm lighting
- Slightly cinematic color grading
- Magazine quality but candid feel
- The kind of photo you'd see on a fashion brand's Instagram
"""
    return prompt

def main():
    print("=" * 60)
    print("テーマ1: 清涼感のある、私だけの春の装い（v3 - 自然なバリエーション）")
    print("=" * 60)
    
    for i, v in enumerate(VARIATIONS, 1):
        print(f"\n[{i}/5] {v['situation']} を生成中...")
        
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
