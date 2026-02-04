// タグ種類
const tagPool = [
  { label: "人気", className: "tag-popular" },
  { label: "限定", className: "tag-limited" },
  { label: "残りわずか", className: "tag-fewleft" }
];

// 9つのテーマデータ
const allThemes = [
  {
    id: 1,
    title: "休日のカフェで過ごす、とろみブラウス",
    concept: "柔らかな陽射しの中、街へ出かけたくなる一枚",
    bgImage: "./images/theme1_cafe_bg.png",
    items: [
      { brand: "Sola & Leaf", name: "とろみサテンブラウス アイボリー", price: "¥5,900" },
      { brand: "Lune Atelier", name: "フリルブラウス ミルクティー", price: "¥6,500" },
      { brand: "Riverline", name: "シアーブラウス ペールピンク", price: "¥5,900" },
      { brand: "Mellow Days", name: "ボウタイブラウス オフホワイト", price: "¥7,200" },
      { brand: "Noir & Tide", name: "バックリボンブラウス ベージュ", price: "¥9,800" }
    ]
  },
  {
    id: 2,
    title: "信頼感を纏う、春のオフィスジャケット",
    concept: "凛とした佇まいで、新しい季節を迎える",
    bgImage: "./images/theme2_office_bg.png",
    items: [
      { brand: "Northline", name: "テーラードジャケット ネイビー", price: "¥18,900" },
      { brand: "Pure Frame", name: "ノーカラージャケット グレージュ", price: "¥12,800" },
      { brand: "Aster Studio", name: "リネンジャケット オフホワイト", price: "¥24,800" },
      { brand: "Urban Vale", name: "ダブルジャケット ブラック", price: "¥28,600" },
      { brand: "Roche Line", name: "ツイードジャケット ピンクベージュ", price: "¥19,800" }
    ]
  },
  {
    id: 3,
    title: "街歩きが楽しくなる、こなれデニム",
    concept: "カジュアルなのに洗練された、大人のデニムスタイル",
    bgImage: "./images/theme3_street_bg.png",
    items: [
      { brand: "Bluecraft", name: "ストレートデニム インディゴ", price: "¥14,800" },
      { brand: "Drift & Co.", name: "ワイドデニム ライトブルー", price: "¥12,800" },
      { brand: "AZURA", name: "スキニーデニム ダークネイビー", price: "¥8,900" },
      { brand: "Journal Lane", name: "フレアデニム ヴィンテージ", price: "¥16,500" },
      { brand: "Beamstone", name: "テーパードデニム ミディアムブルー", price: "¥15,800" }
    ]
  },
  {
    id: 4,
    title: "風に揺れる、春のプリーツスカート",
    concept: "歩くたびに美しく揺れる、フェミニンな一枚",
    bgImage: "./images/theme4_breeze_bg.png",
    items: [
      { brand: "Frayline", name: "シアープリーツスカート ラベンダー", price: "¥16,500" },
      { brand: "Mint Sol", name: "サテンプリーツスカート ミント", price: "¥14,800" },
      { brand: "Celfordia", name: "フラワープリーツスカート ピンク", price: "¥18,900" },
      { brand: "Jill Atelier", name: "ロングプリーツスカート アイボリー", price: "¥22,000" },
      { brand: "Mila Row", name: "ニットプリーツスカート ベージュ", price: "¥12,800" }
    ]
  },
  {
    id: 5,
    title: "旅先で映える、リラックスワイドパンツ",
    concept: "快適さと美しさを両立した、旅のパートナー",
    bgImage: "./images/theme5_travel_bg.png",
    items: [
      { brand: "Gala Lane", name: "リネンワイドパンツ ホワイト", price: "¥15,800" },
      { brand: "Tomorrowly", name: "イージーワイドパンツ カーキ", price: "¥18,900" },
      { brand: "Deuxime", name: "リラックスパンツ ネイビー", price: "¥24,800" },
      { brand: "IENNE", name: "コットンワイドパンツ ベージュ", price: "¥14,800" },
      { brand: "Plageur", name: "サマーワイドパンツ ブルー", price: "¥19,800" }
    ]
  },
  {
    id: 6,
    title: "一枚で決まる、春のワンピース",
    concept: "華やかに、でも気負わずに。春を纏う",
    bgImage: "./images/theme6_garden_bg.png",
    items: [
      { brand: "Apuwea", name: "フラワーワンピース ピンク", price: "¥19,800" },
      { brand: "Proportion", name: "シャツワンピース ストライプ", price: "¥14,800" },
      { brand: "Grace & Coast", name: "レースワンピース ホワイト", price: "¥32,000" },
      { brand: "Rirand", name: "ティアードワンピース ラベンダー", price: "¥16,500" },
      { brand: "Anayie", name: "ベルテッドワンピース ネイビー", price: "¥28,600" }
    ]
  },
  {
    id: 7,
    title: "肌寒い朝の、軽やかカーディガン",
    concept: "さっと羽織れる、春の頼れるパートナー",
    bgImage: "./images/theme7_morning_bg.png",
    items: [
      { brand: "Apron Lane", name: "シアーカーディガン ラベンダー", price: "¥4,900" },
      { brand: "Natural Basic", name: "ロングカーディガン ベージュ", price: "¥6,800" },
      { brand: "Ienne", name: "コットンカーディガン ミント", price: "¥8,900" },
      { brand: "Spica Span", name: "ショートカーディガン アイボリー", price: "¥7,500" },
      { brand: "Mila Reve", name: "透かし編みカーディガン ピンク", price: "¥9,200" }
    ]
  },
  {
    id: 8,
    title: "ディナーに映える、上品セットアップ",
    concept: "特別な夜を彩る、洗練された装い",
    bgImage: "./images/theme8_dinner_bg.png",
    items: [
      { brand: "Epoce", name: "ジャケットセットアップ ブラック", price: "¥48,000" },
      { brand: "Theory Luxe", name: "パンツセットアップ ネイビー", price: "¥52,000" },
      { brand: "Maxmarae", name: "スカートセットアップ ベージュ", price: "¥68,000" },
      { brand: "Adoreva", name: "ワイドパンツセットアップ グレー", price: "¥42,000" },
      { brand: "Enfolde", name: "モダンセットアップ カーキ", price: "¥56,000" }
    ]
  },
  {
    id: 9,
    title: "公園散歩の、柔らかコットンニット",
    concept: "心地よい春の陽気に包まれて",
    bgImage: "./images/theme9_park_bg.png",
    items: [
      { brand: "Sola & Leaf", name: "コットンニット セージグリーン", price: "¥5,900" },
      { brand: "Lune Atelier", name: "ワッフルニット クリームホワイト", price: "¥6,500" },
      { brand: "Riverline", name: "リブニット ブルーグレー", price: "¥5,900" },
      { brand: "Mellow Days", name: "ケーブルニット ナチュラルベージュ", price: "¥7,200" },
      { brand: "Noir & Tide", name: "カシミヤ混ニット ラベンダーグレー", price: "¥9,800" }
    ]
  }
];

// リロードカウンター管理（0, 1, 2でループ）
function getThemeSet() {
  let counter = parseInt(sessionStorage.getItem('themeCounter') || '0');
  const set = counter % 3;
  sessionStorage.setItem('themeCounter', ((counter + 1) % 3).toString());
  return set;
}

// テーマセクションを生成
function renderThemes() {
  const container = document.getElementById('theme-sections');
  if (!container) return;

  const themeSet = getThemeSet();
  const startIndex = themeSet * 3;
  const themes = allThemes.slice(startIndex, startIndex + 3);

  container.innerHTML = '';

  let itemIndex = 0;
  themes.forEach((theme, index) => {
    const themeHtml = `
      <div class="theme-container" data-delay="${index}">
        <div class="theme-header" style="--bg-image: url('${theme.bgImage}');">
          <h3 class="theme-title">${theme.title}</h3>
          <p class="theme-concept">${theme.concept}</p>
        </div>
        <div class="recommend-grid">
          ${theme.items.map((item, i) => `
            <article class="recommend-card">
              <div class="recommend-image">
                <span class="recommend-rank">${i + 1}</span>
                <img src="./fashion_images/theme${theme.id}_0${i + 1}.png" alt="${item.name}" loading="lazy">
              </div>
              <div class="recommend-info">
                <p class="recommend-brand">${item.brand}</p>
                <p class="recommend-name">${item.name}</p>
                <p class="recommend-price">${item.price} <span class="tax">税込</span></p>
                <div class="recommend-tags">
                  ${(() => {
                    const firstTag = tagPool[(itemIndex * 2) % tagPool.length];
                    const secondTag = tagPool[(itemIndex * 2 + 1) % tagPool.length];
                    itemIndex += 1;
                    return `
                      <span class="tag ${firstTag.className}">${firstTag.label}</span>
                      <span class="tag ${secondTag.className}">${secondTag.label}</span>
                    `;
                  })()}
                </div>
              </div>
            </article>
          `).join('')}
        </div>
      </div>
    `;
    container.innerHTML += themeHtml;
  });
}

// ページ読み込み時に実行
document.addEventListener('DOMContentLoaded', () => {
  renderThemes();
  
  // リロード後にスクロール（ウェルカムセクションが見える位置から）
  if (sessionStorage.getItem('scrollToTheme') === 'true') {
    sessionStorage.removeItem('scrollToTheme');
    const welcomeSection = document.querySelector('.welcome');
    if (welcomeSection) {
      setTimeout(() => {
        const rect = welcomeSection.getBoundingClientRect();
        const scrollTop = window.pageYOffset + rect.top - 20; // ウェルカムの上端から少し上
        window.scrollTo({ top: scrollTop, behavior: 'smooth' });
      }, 100);
    }
  }
  
  // もっと教えて（吹き出し＋店員）のイベント
  const staffWrapper = document.getElementById('staff-bubble-wrapper');
  const speechBubble = document.getElementById('speech-bubble');
  const loadingOverlay = document.getElementById('loading-overlay');
  
  if (staffWrapper && loadingOverlay && speechBubble) {
    staffWrapper.addEventListener('click', () => {
      // びっくり画像に切り替え
      staffWrapper.classList.add('clicked');
      speechBubble.classList.add('clicked');
      
      // 少し待ってからローディング表示
      setTimeout(() => {
        loadingOverlay.classList.add('active');
        
        // スクロールフラグをセット
        sessionStorage.setItem('scrollToTheme', 'true');
        
        // 1.5秒後にリロード
        setTimeout(() => {
          location.reload();
        }, 1500);
      }, 600);
    });
  }
});
