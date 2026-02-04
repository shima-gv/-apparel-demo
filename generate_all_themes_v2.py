# -*- coding: utf-8 -*-
"""
9テーマ × 5枚 = 45枚の画像を生成（修正版）
- 縦長を強制
- モデルを毎回変える
"""
import sys
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image
from pathlib import Path

OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/fashion_images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 既存のtheme*ファイルを削除
for f in OUTPUT_DIR.glob("theme*_*.png"):
    f.unlink()
    print(f"削除: {f.name}")

WIDTH_INCH = 4.0
HEIGHT_INCH = 5.0

# モデルのバリエーション（45種類）
MODEL_VARIATIONS = [
    # テーマ1（5人）
    {"hair": "ロングヘア、ゆるいウェーブ、ダークブラウン", "face": "丸顔、柔らかい印象、ナチュラルメイク", "build": "小柄で華奢"},
    {"hair": "ボブカット、内巻き、黒髪", "face": "面長、知的な印象、赤リップ", "build": "すらっとした体型"},
    {"hair": "ポニーテール、明るめブラウン", "face": "卵型、親しみやすい笑顔", "build": "標準体型"},
    {"hair": "セミロング、ストレート、アッシュブラウン", "face": "シャープな顎、クールビューティー", "build": "モデル体型、背が高い"},
    {"hair": "ショートボブ、パーマ、ダークブラウン", "face": "丸みのある頬、可愛らしい印象", "build": "ふんわり柔らかい体型"},
    # テーマ2（5人）
    {"hair": "ロング、センターパート、黒髪ストレート", "face": "凛とした表情、切れ長の目", "build": "スレンダー"},
    {"hair": "ミディアム、外ハネ、ハイライト入り", "face": "健康的な肌、ナチュラルメイク", "build": "健康的な体型"},
    {"hair": "アップスタイル、きちんとまとめた", "face": "品のある顔立ち、薄めメイク", "build": "華奢で上品"},
    {"hair": "ゆるふわロング、明るいベージュブラウン", "face": "愛嬌のある表情", "build": "ほどよい肉付き"},
    {"hair": "ショートヘア、ボーイッシュ", "face": "中性的な魅力、ナチュラル", "build": "スポーティ"},
    # テーマ3（5人）
    {"hair": "ロング、毛先カール、チョコレートブラウン", "face": "大きな目、フェミニン", "build": "女性らしい曲線"},
    {"hair": "ミディアム、レイヤーカット、ナチュラルブラウン", "face": "小顔、整った顔立ち", "build": "スタイル抜群"},
    {"hair": "ハーフアップ、前髪あり、黒髪", "face": "優しい目元、ほんのりチーク", "build": "小柄だがバランス良い"},
    {"hair": "ウェーブロング、グラデーションカラー", "face": "ハーフっぽい顔立ち", "build": "長身スレンダー"},
    {"hair": "まとめ髪、後れ毛あり", "face": "落ち着いた大人の雰囲気", "build": "しなやかな体型"},
    # テーマ4（5人）
    {"hair": "サイドに流したロング、艶のある黒髪", "face": "色白、透明感", "build": "華奢で儚げ"},
    {"hair": "ふわふわカール、明るいブラウン", "face": "笑顔が印象的", "build": "健康的でヘルシー"},
    {"hair": "ストレートロング、前髪なし", "face": "知的でクール", "build": "モデル体型"},
    {"hair": "ミディアムボブ、エアリー", "face": "ナチュラルビューティー", "build": "ほどよく女性らしい"},
    {"hair": "お団子ヘア、おくれ毛", "face": "元気で活発な印象", "build": "スポーティで引き締まった"},
    # テーマ5（5人）
    {"hair": "リラックスウェーブ、キャラメルブラウン", "face": "日焼け肌、健康的", "build": "アクティブな体型"},
    {"hair": "編み込み、ナチュラルブラウン", "face": "穏やかな表情", "build": "柔らかい印象"},
    {"hair": "風になびくロング、ライトブラウン", "face": "自由奔放な雰囲気", "build": "すらりと長い手足"},
    {"hair": "ハットをかぶって、見える髪は黒髪", "face": "ミステリアス", "build": "スタイリッシュ"},
    {"hair": "三つ編み、ダークブラウン", "face": "素朴で親しみやすい", "build": "健康的"},
    # テーマ6（5人）
    {"hair": "ゆるふわロング、ピンクブラウン", "face": "女性らしい柔らかさ", "build": "華奢"},
    {"hair": "ストレートロング、艶やか黒髪", "face": "凛とした美しさ", "build": "スレンダー"},
    {"hair": "ミディアム、くびれカール", "face": "愛らしい表情", "build": "小柄で可愛らしい"},
    {"hair": "アップスタイル、華やか", "face": "エレガント", "build": "すらっとした"},
    {"hair": "ショートボブ、シャープ", "face": "モード感", "build": "スタイリッシュ"},
    # テーマ7（5人）
    {"hair": "ナチュラルロング、朝のまとまり", "face": "すっぴんに近いナチュラル", "build": "自然体"},
    {"hair": "ゆるく束ねた髪", "face": "眠そうだけど可愛い", "build": "柔らかい"},
    {"hair": "ボブ、寝起き風", "face": "ほんのり赤い頬", "build": "小柄"},
    {"hair": "サイドテール、カジュアル", "face": "フレッシュな印象", "build": "健康的"},
    {"hair": "ハーフアップ、ラフ", "face": "リラックスした表情", "build": "ナチュラル"},
    # テーマ8（5人）
    {"hair": "アップスタイル、エレガント、黒髪", "face": "華やかなメイク", "build": "スレンダーで長身"},
    {"hair": "巻き髪ロング、ゴージャス", "face": "大人の色気", "build": "女性らしい曲線美"},
    {"hair": "シニヨン、きちんと", "face": "知的で上品", "build": "すらりとした"},
    {"hair": "ダウンスタイル、艶やか", "face": "落ち着いた美しさ", "build": "バランスの良い"},
    {"hair": "ポニーテール、洗練された", "face": "クールビューティー", "build": "モデル体型"},
    # テーマ9（5人）
    {"hair": "ナチュラルロング、ブラウン", "face": "親しみやすい笑顔", "build": "健康的"},
    {"hair": "お団子、カジュアル", "face": "元気で明るい", "build": "アクティブ"},
    {"hair": "ミディアム、ふんわり", "face": "柔らかい表情", "build": "女性らしい"},
    {"hair": "ショートカット、爽やか", "face": "ボーイッシュな可愛さ", "build": "スポーティ"},
    {"hair": "ロング、風になびく", "face": "自然体の美しさ", "build": "しなやか"},
]

# 9テーマの定義
THEMES = [
    {
        "id": 1,
        "name": "休日のカフェで過ごす、とろみブラウス",
        "item_type": "とろみブラウス",
        "focus": "tops",
        "variations": [
            {"color": "アイボリー", "detail": "Vネック、フレンチスリーブ、さらりとした落ち感", "scene": "テラス席のカフェ、コーヒーカップとグリーン", "pose": "テーブルに肘をついてリラックス"},
            {"color": "ダスティピンク", "detail": "ボウタイリボン、透け感のあるシフォン", "scene": "白い壁のおしゃれなカフェ外観前", "pose": "歩きながら振り返る"},
            {"color": "ペールブルー", "detail": "スタンドカラー、袖にギャザー", "scene": "緑の見えるオープンカフェ", "pose": "立ってメニューを見る"},
            {"color": "ミントグリーン", "detail": "ドロップショルダー、裾にスリット", "scene": "街角のカフェテラス", "pose": "椅子の背に手を置いて"},
            {"color": "ラベンダー", "detail": "パフスリーブ、バックボタン", "scene": "レンガの壁のカフェ外", "pose": "カップを持って立つ"},
        ]
    },
    {
        "id": 2,
        "name": "信頼感を纏う、春のオフィスジャケット",
        "item_type": "テーラードジャケット",
        "focus": "tops",
        "variations": [
            {"color": "ベージュ", "detail": "ノーカラー、一つボタン、リネン混素材", "scene": "モダンなオフィスビルのエントランス外", "pose": "颯爽と歩く姿"},
            {"color": "ネイビー", "detail": "クラシックなテーラード、ゴールドボタン", "scene": "ビジネス街の並木道", "pose": "資料を抱えて歩く"},
            {"color": "グレージュ", "detail": "ダブルブレスト、ややオーバーサイズ", "scene": "コンクリートの都会的な広場", "pose": "ジャケットの前を軽く持つ"},
            {"color": "オフホワイト", "detail": "ショールカラー、七分袖", "scene": "緑のあるビジネス街の歩道", "pose": "腕を組んで微笑む"},
            {"color": "カーキ", "detail": "サファリ風、ベルト付き", "scene": "モダンビルの前", "pose": "バッグを持って立つ"},
        ]
    },
    {
        "id": 3,
        "name": "街歩きが楽しくなる、こなれデニム",
        "item_type": "デニムパンツ",
        "focus": "bottoms",
        "variations": [
            {"color": "ライトブルー", "detail": "ハイウエスト、ストレートレッグ、裾カットオフ", "scene": "石畳のショッピングストリート", "pose": "歩きながら振り返る"},
            {"color": "インディゴ", "detail": "ワイドレッグ、センタープレス", "scene": "レンガ造りの路地", "pose": "壁にもたれて立つ"},
            {"color": "ウォッシュブルー", "detail": "テーパード、アンクル丈", "scene": "カラフルな店が並ぶ通り", "pose": "バッグを持って歩く"},
            {"color": "ミディアムブルー", "detail": "フレア、ヴィンテージ風加工", "scene": "公園近くの遊歩道", "pose": "足を交差させて立つ"},
            {"color": "ブリーチ", "detail": "スリムストレート、膝ダメージ", "scene": "アートギャラリー前の広場", "pose": "ポケットに手を入れて"},
        ]
    },
    {
        "id": 4,
        "name": "風に揺れる、春のプリーツスカート",
        "item_type": "プリーツスカート",
        "focus": "bottoms",
        "variations": [
            {"color": "ペールピンク", "detail": "ロング丈、細かいプリーツ、サテン光沢", "scene": "桜並木の遊歩道", "pose": "風でスカートがなびく"},
            {"color": "ミントグリーン", "detail": "ミモレ丈、ランダムプリーツ", "scene": "花壇のある公園", "pose": "歩きながらスカートを押さえる"},
            {"color": "ラベンダー", "detail": "マキシ丈、シフォン素材", "scene": "川沿いの遊歩道", "pose": "手すりに手を置いて"},
            {"color": "アイボリー", "detail": "ミディ丈、アコーディオンプリーツ", "scene": "白い建物の前", "pose": "優雅に歩く"},
            {"color": "スカイブルー", "detail": "Aライン、ウエストリボン", "scene": "海が見える丘", "pose": "髪を押さえながら"},
        ]
    },
    {
        "id": 5,
        "name": "旅先で映える、リラックスワイドパンツ",
        "item_type": "ワイドパンツ",
        "focus": "bottoms",
        "variations": [
            {"color": "ベージュ", "detail": "リネン素材、ハイウエスト、ゆったりシルエット", "scene": "リゾート風の石畳広場", "pose": "サングラスをかけて歩く"},
            {"color": "オリーブ", "detail": "カーゴ風ポケット、ドローストリング", "scene": "古い街並み、レンガの壁", "pose": "マップを持って立つ"},
            {"color": "テラコッタ", "detail": "センタープレス、きれいめ素材", "scene": "ヨーロッパ風の広場", "pose": "噴水の前で立つ"},
            {"color": "オフホワイト", "detail": "プリーツ入り、エレガントな落ち感", "scene": "海辺のプロムナード", "pose": "帽子を押さえて"},
            {"color": "ネイビー", "detail": "セーラーパンツ風、ゴールドボタン", "scene": "港町の風景", "pose": "手すりにもたれて"},
        ]
    },
    {
        "id": 6,
        "name": "一枚で決まる、春のワンピース",
        "item_type": "ワンピース",
        "focus": "full",
        "variations": [
            {"color": "花柄（白地にピンク）", "detail": "フレアスリーブ、ミディ丈、ウエストマーク", "scene": "花が咲く庭園", "pose": "花を眺めながら歩く"},
            {"color": "ペールイエロー", "detail": "シャツワンピース、前ボタン、ベルト付き", "scene": "菜の花が見える丘", "pose": "風を受けて立つ"},
            {"color": "ミントブルー", "detail": "ティアードスカート、ノースリーブ", "scene": "湖のほとり", "pose": "遠くを見つめる"},
            {"color": "コーラルピンク", "detail": "Aラインシルエット、パフスリーブ", "scene": "カラフルな街角", "pose": "ショップの前で振り返る"},
            {"color": "ライラック", "detail": "プリーツスカート部分、シンプルトップ", "scene": "美術館の前の広場", "pose": "階段を上る姿"},
        ]
    },
    {
        "id": 7,
        "name": "肌寒い朝の、軽やかカーディガン",
        "item_type": "カーディガン",
        "focus": "tops",
        "variations": [
            {"color": "クリーム", "detail": "ローゲージ、ざっくり編み、ロング丈", "scene": "朝の公園の遊歩道", "pose": "カーディガンを羽織りながら"},
            {"color": "ダスティローズ", "detail": "ショート丈、パール風ボタン", "scene": "朝のカフェテラス前", "pose": "コーヒーを持って微笑む"},
            {"color": "グレー", "detail": "オーバーサイズ、ドロップショルダー", "scene": "川沿いの朝の散歩道", "pose": "歩きながら前を閉める"},
            {"color": "セージグリーン", "detail": "ミドル丈、ポケット付き", "scene": "緑の多い住宅街の道", "pose": "ポケットに手を入れて"},
            {"color": "ペールブルー", "detail": "透かし編み、繊細な模様", "scene": "朝の海辺の遊歩道", "pose": "風で髪がなびく"},
        ]
    },
    {
        "id": 8,
        "name": "ディナーに映える、上品セットアップ",
        "item_type": "セットアップ",
        "focus": "full",
        "variations": [
            {"color": "ブラック", "detail": "ノーカラージャケット+テーパードパンツ、サテン素材", "scene": "高級レストラン前のテラス", "pose": "エレガントに立つ"},
            {"color": "ボルドー", "detail": "ショールカラー+ワイドパンツ", "scene": "ホテルの前庭", "pose": "クラッチバッグを持って"},
            {"color": "ネイビー", "detail": "ダブルジャケット+スラックス", "scene": "夜景が見えるテラス", "pose": "手すりに手を置いて"},
            {"color": "ベージュ", "detail": "ロングジャケット+スカート", "scene": "モダンなバーの外観前", "pose": "入り口に向かって歩く"},
            {"color": "チャコール", "detail": "ケープ風ジャケット+パンツ", "scene": "イルミネーションの通り", "pose": "歩きながら微笑む"},
        ]
    },
    {
        "id": 9,
        "name": "公園散歩の、柔らかコットンニット",
        "item_type": "コットンニット",
        "focus": "tops",
        "variations": [
            {"color": "オートミール", "detail": "クルーネック、リラックスフィット、リブ編み", "scene": "新緑の公園の小道", "pose": "散歩している姿"},
            {"color": "ペールピンク", "detail": "ボートネック、七分袖", "scene": "芝生の広場", "pose": "ピクニックの準備をする"},
            {"color": "ミントグリーン", "detail": "Vネック、サイドスリット", "scene": "桜の木の下", "pose": "桜を見上げる"},
            {"color": "ラベンダー", "detail": "モックネック、ゆったりシルエット", "scene": "池のほとりのベンチ付近", "pose": "歩きながら"},
            {"color": "スカイブルー", "detail": "ヘンリーネック、ボタンディテール", "scene": "遊歩道", "pose": "音楽を聴きながら歩く"},
        ]
    },
]

def create_prompt(theme, variation, model_idx):
    """プロンプト生成"""
    focus = theme["focus"]
    model = MODEL_VARIATIONS[model_idx]
    
    if focus == "tops":
        composition = """
- The top is the main focus - fills most of the frame
- Upper body shot, head may be partially cropped at top or showing full face
- The garment texture and details must be clearly visible
- Show from chest area down to waist/hip"""
    elif focus == "bottoms":
        composition = """
- The pants/skirt is the main focus - fills most of the frame  
- Shot from waist down to below knee or ankle
- Upper body may be partially visible, face may or may not be visible
- The fabric texture and silhouette must be clearly visible"""
    else:
        composition = """
- Full body or 3/4 body shot showing the complete outfit
- The outfit coordination is the focus
- Show from head to at least below knee"""

    prompt = f"""A candid, lifestyle fashion photograph for a Japanese women's fashion brand.

CRITICAL - IMAGE ORIENTATION:
- MUST be PORTRAIT orientation (taller than wide)
- Aspect ratio 4:5 (vertical/portrait)
- DO NOT generate landscape/horizontal image

CRITICAL COMPOSITION:{composition}

CRITICAL IMAGE REQUIREMENTS:
- Photorealistic photograph with natural, editorial feel
- NO text, NO borders, NO frames, NO margins
- Image fills entire canvas edge-to-edge
- OUTDOOR setting only

MODEL - UNIQUE FOR THIS IMAGE:
- Japanese woman in her early 30s
- Hair: {model['hair']}
- Face/Makeup: {model['face']}
- Body type: {model['build']}
- Each image features a DIFFERENT model

THE FEATURED ITEM - {theme["item_type"]}:
- Color: {variation["color"]}
- Details: {variation["detail"]}
- The texture, color, and design must be clearly visible

SCENE & BACKGROUND (OUTDOOR):
- {variation["scene"]}
- Natural lighting, outdoor setting
- Background has depth but doesn't distract

POSE & MOMENT:
- {variation["pose"]}
- Natural, candid moment
- Genuine expression

PHOTOGRAPHY STYLE:
- Japanese fashion magazine quality
- Soft, flattering natural light
- Slightly warm color grading
"""
    return prompt

def main():
    total = sum(len(t["variations"]) for t in THEMES)
    count = 0
    model_idx = 0
    
    print("=" * 60)
    print(f"9テーマ × 5枚 = {total}枚の画像を生成します（修正版）")
    print("=" * 60)
    
    for theme in THEMES:
        print(f"\n【テーマ{theme['id']}】{theme['name']}")
        print("-" * 50)
        
        for i, variation in enumerate(theme["variations"], 1):
            count += 1
            filename = f"theme{theme['id']}_{i:02d}"
            
            print(f"  [{count}/{total}] {variation['color']} を生成中...")
            
            prompt = create_prompt(theme, variation, model_idx)
            model_idx += 1
            
            result = generate_partial_image(
                prompt=prompt,
                width_inch=WIDTH_INCH,
                height_inch=HEIGHT_INCH,
                output_dir=str(OUTPUT_DIR),
                filename=filename
            )
            
            if result:
                print(f"    ✅ 成功")
            else:
                print(f"    ❌ 失敗")
    
    print("\n" + "=" * 60)
    print(f"完了！出力先: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
