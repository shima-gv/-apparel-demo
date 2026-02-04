# -*- coding: utf-8 -*-
"""
9テーマ × 5枚 = 45枚の画像を生成
30代日本人女性・春向け
"""
import sys
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image
from pathlib import Path

OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/fashion_images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH_INCH = 4.0
HEIGHT_INCH = 5.0

# 9テーマの定義
THEMES = [
    # テーマ1: ブラウス（トップス）
    {
        "id": 1,
        "name": "休日のカフェで過ごす、とろみブラウス",
        "item_type": "とろみブラウス",
        "focus": "tops",
        "variations": [
            {"color": "アイボリー", "detail": "Vネック、フレンチスリーブ、さらりとした落ち感", "scene": "テラス席のカフェ、コーヒーカップとグリーン", "pose": "テーブルに肘をついてリラックス"},
            {"color": "ダスティピンク", "detail": "ボウタイリボン、透け感のあるシフォン", "scene": "白い壁のおしゃれなカフェ内", "pose": "本を手に持ちながら微笑む"},
            {"color": "ペールブルー", "detail": "スタンドカラー、袖にギャザー", "scene": "窓際の席、自然光が差し込む", "pose": "窓の外を眺める横顔"},
            {"color": "ミントグリーン", "detail": "ドロップショルダー、裾にスリット", "scene": "緑の見えるオープンカフェ", "pose": "椅子に座って足を組む"},
            {"color": "ラベンダー", "detail": "パフスリーブ、バックボタン", "scene": "レンガ調の落ち着いたカフェ", "pose": "カップを両手で持つ仕草"},
        ]
    },
    # テーマ2: ジャケット（トップス）
    {
        "id": 2,
        "name": "信頼感を纏う、春のオフィスジャケット",
        "item_type": "テーラードジャケット",
        "focus": "tops",
        "variations": [
            {"color": "ベージュ", "detail": "ノーカラー、一つボタン、リネン混素材", "scene": "モダンなオフィスビルのエントランス", "pose": "颯爽と歩く姿、バッグを持って"},
            {"color": "ネイビー", "detail": "クラシックなテーラード、ゴールドボタン", "scene": "ガラス張りの会議室前", "pose": "資料を抱えて立つ"},
            {"color": "グレージュ", "detail": "ダブルブレスト、ややオーバーサイズ", "scene": "コンクリートの都会的な建物", "pose": "ジャケットの前を軽く持つ"},
            {"color": "オフホワイト", "detail": "ショールカラー、七分袖", "scene": "緑のあるビジネス街", "pose": "腕を組んで微笑む"},
            {"color": "カーキ", "detail": "サファリ風、ベルト付き", "scene": "ブティック風のオフィス前", "pose": "ポケットに手を入れてリラックス"},
        ]
    },
    # テーマ3: デニム（ボトムス）
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
            {"color": "ブリーチ", "detail": "スリムストレート、膝ダメージ", "scene": "アートギャラリー前", "pose": "ポケットに手を入れて"},
        ]
    },
    # テーマ4: スカート（ボトムス）
    {
        "id": 4,
        "name": "風に揺れる、春のプリーツスカート",
        "item_type": "プリーツスカート",
        "focus": "bottoms",
        "variations": [
            {"color": "ペールピンク", "detail": "ロング丈、細かいプリーツ、サテン光沢", "scene": "桜並木の遊歩道", "pose": "風でスカートがなびく"},
            {"color": "ミントグリーン", "detail": "ミモレ丈、ランダムプリーツ", "scene": "花壇のある公園", "pose": "歩きながらスカートを押さえる"},
            {"color": "ラベンダー", "detail": "マキシ丈、シフォン素材", "scene": "川沿いの遊歩道", "pose": "手すりに手を置いて"},
            {"color": "アイボリー", "detail": "ミディ丈、アコーディオンプリーツ", "scene": "白い建物の前", "pose": "優雅に振り返る"},
            {"color": "スカイブルー", "detail": "Aライン、ウエストリボン", "scene": "海が見える丘", "pose": "髪を押さえながら"},
        ]
    },
    # テーマ5: ワイドパンツ（ボトムス）
    {
        "id": 5,
        "name": "旅先で映える、リラックスワイドパンツ",
        "item_type": "ワイドパンツ",
        "focus": "bottoms",
        "variations": [
            {"color": "ベージュ", "detail": "リネン素材、ハイウエスト、ゆったりシルエット", "scene": "リゾート風の石畳", "pose": "サングラスをかけて歩く"},
            {"color": "オリーブ", "detail": "カーゴ風ポケット、ドローストリング", "scene": "古い街並み、レンガの壁", "pose": "マップを見ながら"},
            {"color": "テラコッタ", "detail": "センタープレス、きれいめ素材", "scene": "ヨーロッパ風の広場", "pose": "ベンチに腰掛ける"},
            {"color": "オフホワイト", "detail": "プリーツ入り、エレガントな落ち感", "scene": "海辺のプロムナード", "pose": "帽子を押さえて"},
            {"color": "ネイビー", "detail": "セーラーパンツ風、ゴールドボタン", "scene": "港町の風景", "pose": "手すりにもたれて"},
        ]
    },
    # テーマ6: ワンピース（全身）
    {
        "id": 6,
        "name": "一枚で決まる、春のワンピース",
        "item_type": "ワンピース",
        "focus": "full",
        "variations": [
            {"color": "花柄（白地にピンク）", "detail": "フレアスリーブ、ミディ丈、ウエストマーク", "scene": "花が咲く庭園", "pose": "花を眺めながら歩く"},
            {"color": "ペールイエロー", "detail": "シャツワンピース、前ボタン、ベルト付き", "scene": "菜の花畑が見える丘", "pose": "風を受けて立つ"},
            {"color": "ミントブルー", "detail": "ティアードスカート、ノースリーブ", "scene": "湖のほとり", "pose": "座って遠くを見つめる"},
            {"color": "コーラルピンク", "detail": "Aラインシルエット、パフスリーブ", "scene": "カラフルな街角", "pose": "ショップの前で振り返る"},
            {"color": "ライラック", "detail": "プリーツスカート部分、シンプルトップ", "scene": "美術館の前", "pose": "階段を上る姿"},
        ]
    },
    # テーマ7: カーディガン（トップス）
    {
        "id": 7,
        "name": "肌寒い朝の、軽やかカーディガン",
        "item_type": "カーディガン",
        "focus": "tops",
        "variations": [
            {"color": "クリーム", "detail": "ローゲージ、ざっくり編み、ロング丈", "scene": "朝霧の公園", "pose": "カーディガンを羽織りながら"},
            {"color": "ダスティローズ", "detail": "ショート丈、パール風ボタン", "scene": "朝のカフェテラス", "pose": "コーヒーを持って微笑む"},
            {"color": "グレー", "detail": "オーバーサイズ、ドロップショルダー", "scene": "川沿いの朝の散歩道", "pose": "歩きながら前を閉める"},
            {"color": "セージグリーン", "detail": "ミドル丈、ポケット付き", "scene": "緑の多い住宅街", "pose": "ポケットに手を入れて"},
            {"color": "ペールブルー", "detail": "透かし編み、繊細な模様", "scene": "朝の海辺", "pose": "風で髪がなびく"},
        ]
    },
    # テーマ8: セットアップ（全身）
    {
        "id": 8,
        "name": "ディナーに映える、上品セットアップ",
        "item_type": "セットアップ",
        "focus": "full",
        "variations": [
            {"color": "ブラック", "detail": "ノーカラージャケット+テーパードパンツ、サテン素材", "scene": "高級レストラン前", "pose": "エレガントに立つ"},
            {"color": "ボルドー", "detail": "ショールカラー+ワイドパンツ", "scene": "ホテルのロビー", "pose": "クラッチバッグを持って"},
            {"color": "ネイビー", "detail": "ダブルジャケット+スラックス", "scene": "夜景が見えるテラス", "pose": "手すりに手を置いて"},
            {"color": "ベージュ", "detail": "ロングジャケット+スカート", "scene": "モダンなバーの入り口", "pose": "ドアを開けようとする"},
            {"color": "チャコール", "detail": "ケープ風ジャケット+パンツ", "scene": "イルミネーションの通り", "pose": "歩きながら微笑む"},
        ]
    },
    # テーマ9: ニット（トップス）
    {
        "id": 9,
        "name": "公園散歩の、柔らかコットンニット",
        "item_type": "コットンニット",
        "focus": "tops",
        "variations": [
            {"color": "オートミール", "detail": "クルーネック、リラックスフィット、リブ編み", "scene": "新緑の公園", "pose": "犬のリードを持って歩く"},
            {"color": "ペールピンク", "detail": "ボートネック、七分袖", "scene": "芝生の広場", "pose": "ピクニックシートに座る"},
            {"color": "ミントグリーン", "detail": "Vネック、サイドスリット", "scene": "桜の木の下", "pose": "桜を見上げる"},
            {"color": "ラベンダー", "detail": "モックネック、ゆったりシルエット", "scene": "池のほとりのベンチ", "pose": "ベンチに座って読書"},
            {"color": "スカイブルー", "detail": "ヘンリーネック、ボタンディテール", "scene": "遊歩道を歩く", "pose": "イヤホンをしながら歩く"},
        ]
    },
]

def create_prompt(theme, variation):
    """プロンプト生成"""
    focus = theme["focus"]
    
    if focus == "tops":
        composition = """
- The top/sweater is the main focus - fills most of the frame
- Upper body shot, head may be partially cropped at top
- The garment texture and details must be clearly visible"""
    elif focus == "bottoms":
        composition = """
- The pants/skirt is the main focus - fills most of the frame  
- Lower body to waist shot, may include some upper body
- Face may be cropped, focus is on the bottoms
- The fabric texture and silhouette must be clearly visible"""
    else:  # full
        composition = """
- Full body or 3/4 body shot showing the complete outfit
- The outfit coordination is the focus
- Model visible from head to below knee at minimum"""

    prompt = f"""A candid, lifestyle fashion photograph for a Japanese women's fashion brand.

CRITICAL COMPOSITION:{composition}

CRITICAL IMAGE REQUIREMENTS:
- Photorealistic photograph with natural, editorial feel
- NO text, NO borders, NO frames
- Image fills entire canvas edge-to-edge
- OUTDOOR setting

MODEL:
- Japanese woman in her early 30s
- Natural, approachable beauty
- Well-groomed, sophisticated but not overdone
- Hair styled naturally, may be tied up or down

THE FEATURED ITEM - {theme["item_type"]}:
- Color: {variation["color"]}
- Details: {variation["detail"]}
- The texture, color, and design details should be clearly visible

SCENE & BACKGROUND:
- {variation["scene"]}
- Natural lighting, outdoor setting
- Background has depth but doesn't distract from the clothing

POSE & MOMENT:
- {variation["pose"]}
- Natural, candid moment
- Genuine expression

PHOTOGRAPHY STYLE:
- Japanese fashion magazine quality (like CLASSY, Oggi, VERY)
- Soft, flattering natural light
- Slightly warm color grading
- Professional but approachable feel
"""
    return prompt

def main():
    total = sum(len(t["variations"]) for t in THEMES)
    count = 0
    
    print("=" * 60)
    print(f"9テーマ × 5枚 = {total}枚の画像を生成します")
    print("=" * 60)
    
    for theme in THEMES:
        print(f"\n【テーマ{theme['id']}】{theme['name']}")
        print("-" * 50)
        
        for i, variation in enumerate(theme["variations"], 1):
            count += 1
            filename = f"theme{theme['id']}_{i:02d}"
            
            # 既存ファイルがあればスキップ
            existing = OUTPUT_DIR / f"{filename}.png"
            if existing.exists():
                print(f"  [{count}/{total}] {variation['color']} - スキップ（既存）")
                continue
            
            print(f"  [{count}/{total}] {variation['color']} を生成中...")
            
            prompt = create_prompt(theme, variation)
            
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
