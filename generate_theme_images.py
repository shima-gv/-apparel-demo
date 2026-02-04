# -*- coding: utf-8 -*-
"""
テーマ別背景画像生成スクリプト
nanabananapro.pyを使用して9つのテーマの背景画像を生成
"""

import sys
import os
from pathlib import Path

# nanabananapro.pyのパスを追加
sys.path.insert(0, "/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ALL_GROWTH VERSE/99_島作成資料格納場所/95.cursor_settings/gv_pptx_skills")

from nanabananapro import generate_partial_image

# 出力ディレクトリ
OUTPUT_DIR = Path("/Users/shima/Library/CloudStorage/OneDrive-株式会社GROWTHVERSE/ドキュメント/サイト作成/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 9つのテーマ定義
THEMES = [
    {
        "id": 1,
        "name": "休日のカフェで過ごす、とろみブラウス",
        "category": "ブラウス",
        "focus": "トップス",
        "filename": "theme1_cafe_bg",
        "prompt": """春のカフェテラスの雰囲気を表現した背景画像。
柔らかい日差しが差し込む窓辺、淡いピンクと白の桜の花びら、
温かみのあるベージュとクリーム色のトーン。
コーヒーカップや観葉植物のシルエットを薄く配置。
リラックスした休日の穏やかな雰囲気。"""
    },
    {
        "id": 2,
        "name": "信頼感を纏う、春のオフィスジャケット",
        "category": "ジャケット",
        "focus": "トップス",
        "filename": "theme2_office_bg",
        "prompt": """洗練されたオフィスの雰囲気を表現した背景画像。
モダンなビルの窓から見える都会の景色、
ネイビーとグレーを基調としたクリーンなトーン。
薄く桜の花びらが舞う春らしさを添えて。
プロフェッショナルで信頼感のある印象。"""
    },
    {
        "id": 3,
        "name": "街歩きが楽しくなる、こなれデニム",
        "category": "デニムパンツ",
        "focus": "ボトムス",
        "filename": "theme3_street_bg",
        "prompt": """おしゃれな街並みを表現した背景画像。
レンガの壁、カフェの看板、石畳の道。
インディゴブルーとテラコッタの温かみのある色調。
春の陽気な雰囲気、街路樹の新緑が薄く見える。
カジュアルでこなれた都会的な印象。"""
    },
    {
        "id": 4,
        "name": "風に揺れる、春のプリーツスカート",
        "category": "プリーツスカート",
        "focus": "ボトムス",
        "filename": "theme4_breeze_bg",
        "prompt": """春風が吹く公園の雰囲気を表現した背景画像。
桜並木、花びらが風に舞う様子。
ピンク、ラベンダー、ミントグリーンの柔らかいパステルトーン。
軽やかで女性らしい、エレガントな印象。
風のそよぎを感じる動きのある表現。"""
    },
    {
        "id": 5,
        "name": "旅先で映える、リラックスワイドパンツ",
        "category": "ワイドパンツ",
        "focus": "ボトムス",
        "filename": "theme5_travel_bg",
        "prompt": """リゾートや旅先の雰囲気を表現した背景画像。
青い空と海、ヤシの木のシルエット、白い砂浜。
ターコイズブルー、サンドベージュ、白の爽やかな色調。
開放感とリラックス感、太陽の光。
旅行気分を高める非日常的な印象。"""
    },
    {
        "id": 6,
        "name": "一枚で決まる、春のワンピース",
        "category": "ワンピース",
        "focus": "全身",
        "filename": "theme6_garden_bg",
        "prompt": """華やかなガーデンパーティーの雰囲気を表現した背景画像。
満開の花々、チューリップ、バラ、春の草花。
ピンク、コーラル、クリームイエローの華やかな色調。
柔らかい日差し、フェミニンでロマンチックな印象。
特別な日を彩る優雅な雰囲気。"""
    },
    {
        "id": 7,
        "name": "肌寒い朝の、軽やかカーディガン",
        "category": "カーディガン",
        "focus": "トップス",
        "filename": "theme7_morning_bg",
        "prompt": """早朝の穏やかな雰囲気を表現した背景画像。
朝もやの中の風景、柔らかい朝日。
ミルクティーベージュ、グレージュ、オフホワイトの優しい色調。
温かみのあるニットの質感を連想させる。
落ち着いた、ナチュラルで心地よい印象。"""
    },
    {
        "id": 8,
        "name": "ディナーに映える、上品セットアップ",
        "category": "セットアップ",
        "focus": "全身",
        "filename": "theme8_dinner_bg",
        "prompt": """高級レストランの雰囲気を表現した背景画像。
キャンドルの柔らかい光、シャンデリア、ワイングラス。
ボルドー、ゴールド、ダークネイビーのエレガントな色調。
大人の洗練された空間、特別な夜の雰囲気。
上品でラグジュアリーな印象。"""
    },
    {
        "id": 9,
        "name": "公園散歩の、柔らかコットンニット",
        "category": "ニット",
        "focus": "トップス",
        "filename": "theme9_park_bg",
        "prompt": """春の公園の穏やかな雰囲気を表現した背景画像。
新緑の木々、芝生、木漏れ日。
ライトグリーン、クリーム、スカイブルーの自然な色調。
ピクニックを連想させる、リラックスした雰囲気。
心地よい春の陽気と自然の優しさ。"""
    }
]

def generate_all_theme_images():
    """全テーマの背景画像を生成"""
    print("=" * 50)
    print("テーマ別背景画像生成開始")
    print("=" * 50)
    
    # 画像サイズ（テーマヘッダーの右側4分の1に配置）
    width_inch = 4.0
    height_inch = 2.5
    
    for theme in THEMES:
        print(f"\n[{theme['id']}/9] {theme['name']}")
        print(f"  カテゴリ: {theme['category']} / {theme['focus']}")
        
        result = generate_partial_image(
            prompt=theme["prompt"],
            width_inch=width_inch,
            height_inch=height_inch,
            output_dir=str(OUTPUT_DIR),
            filename=theme["filename"]
        )
        
        if result:
            print(f"  ✅ 生成完了: {result}")
        else:
            print(f"  ❌ 生成失敗")
    
    print("\n" + "=" * 50)
    print("全テーマの画像生成完了")
    print("=" * 50)

if __name__ == "__main__":
    generate_all_theme_images()
