import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="Personal Color Text Curator", page_icon="📝", layout="wide")

# 2. 스타일 설정 (이미지 제외, 텍스트 가독성 중심)
st.markdown("""
    <style>
    .category-title {
        font-size: 18px;
        font-weight: 800;
        color: #ff4b4b;
        margin-bottom: 10px;
        border-bottom: 2px solid #ff4b4b;
        display: inline-block;
    }
    .product-box {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 30px 20px;
        border: 2px solid #f0f2f6;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .product-name {
        font-size: 20px;
        font-weight: bold;
        color: #222;
        margin-bottom: 10px;
    }
    .product-tag {
        font-size: 14px;
        color: #666;
        background-color: #f8f9fa;
        padding: 5px 12px;
        border-radius: 20px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 16톤 세부 구조
tone_structure = {
    "봄 (Spring)": ["봄 페일", "봄 라이트", "봄 브라이트", "봄 비비드"],
    "여름 (Summer)": ["여름 페일", "여름 라이트", "여름 뮤트", "여름 그레이시"],
    "가을 (Autumn)": ["가을 소프트", "가을 뮤트", "가을 딥", "가을 다크"],
    "겨울 (Winter)": ["겨울 브라이트", "겨울 비비드", "겨울 딥", "겨울 다크"]
}

# 4. 텍스트 기반 제품 데이터 풀 (사진 링크 제거)
cosmetics_pool = {
    "기본": {
        "palette": [{"name": "에스쁘아 - 리얼 아이 팔레트", "tag": "데일리 음영의 정석"}],
        "blusher": [{"name": "롬앤 - 베러 댄 치크", "tag": "뽀얀 수채화 발색"}],
        "tint": [{"name": "페리페라 - 잉크 무드 글로이 틴트", "tag": "탱글한 유리알 광택"}]
    },
    "여름 라이트": {
        "palette": [
            {"name": "클리오 - 에어 섀도우 [라벤더 가든]", "tag": "맑은 보랏빛 음영"},
            {"name": "데이지크 - 쿨 블렌딩", "tag": "시원한 쿨톤 베이스"}
        ],
        "blusher": [
            {"name": "디올 - 로지 글로우 001", "tag": "화사한 쿨 핑크 치크"},
            {"name": "롬앤 - 오디 밀크", "tag": "피부톤 보정 라벤더"}
        ],
        "tint": [
            {"name": "입생로랑 - 캔디 글레이즈 11호", "tag": "청순한 루비 핑크"},
            {"name": "롬앤 - 베어 베리 스무디", "tag": "생기 넘치는 베리 컬러"}
        ]
    },
    "가을 딥": {
        "palette": [
            {"name": "에스쁘아 - 뎁스", "tag": "그윽한 딥 브라운"},
            {"name": "3CE - 로우 누드", "tag": "분위기 있는 누드톤"}
        ],
        "blusher": [
            {"name": "나스 - 타오스", "tag": "건강한 브릭 레드 치크"},
            {"name": "맥 - 웜 소울", "tag": "은은한 골드 펄 베이지"}
        ],
        "tint": [
            {"name": "맥 - 디보티드 투 칠리", "tag": "분위기 여신 브릭 레드"},
            {"name": "헤라 - 팜파스", "tag": "부드러운 벨벳 오렌지"}
        ]
    }
}

# 5. 사이드바 제어
st.sidebar.title("🔍 퍼스널 컬러 설정")
selected_season = st.sidebar.selectbox("계절 선택", list(tone_structure.keys()))
selected_detail = st.sidebar.radio("세부 타입 선택", tone_structure[selected_season])

if st.sidebar.button("다른 추천 보기 🔄"):
    st.rerun()

# 6. 결과 화면
st.title(f"✨ {selected_detail}를 위한 추천 리스트")
st.write("이미지 없이 텍스트로 깔끔하게 제품 정보만 확인하세요.")
st.divider()

# 데이터 랜덤 추출 로직
pool = cosmetics_pool.get(selected_detail, cosmetics_pool["기본"])
p = random.choice(pool["palette"])
b = random.choice(pool["blusher"])
t = random.choice(pool["tint"])

# 레이아웃 구성
col1, col2, col3 = st.columns(3)

items = [
    ("👁️ EYE PALETTE", p, col1),
    ("😊 BLUSHER", b, col2),
    ("💄 TINT / LIP", t, col3)
]

for title, item, col in items:
    with col:
        st.markdown(f'<div class="category-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="product-box">
                <div class="product-name">{item['name']}</div>
                <div><span class="product-tag">#{item['tag']}</span></div>
            </div>
        """, unsafe_allow_html=True)

st.info(f"💡 {selected_detail} 타입은 위 제품들의 색감을 참고하여 쇼핑해 보세요!")
