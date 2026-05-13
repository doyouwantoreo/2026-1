import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="데일리 퍼스널 컬러 AI", page_icon="🎨", layout="wide")

# 2. 스타일 설정
st.markdown("""
    <style>
    .category-label {
        font-size: 16px;
        font-weight: 800;
        color: #333;
        margin-bottom: 10px;
        text-align: center;
        background-color: #f0f2f6;
        padding: 5px;
        border-radius: 8px;
    }
    .product-card {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 20px;
        border: 1px solid #f0f2f6;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    .product-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 15px;
        margin-bottom: 15px;
    }
    .product-title {
        font-size: 16px;
        font-weight: bold;
        color: #222;
        min-height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 16톤 구조 정의
tone_structure = {
    "봄 (Spring)": ["봄 페일", "봄 라이트", "봄 브라이트", "봄 비비드"],
    "여름 (Summer)": ["여름 페일", "여름 라이트", "여름 뮤트", "여름 그레이시"],
    "가을 (Autumn)": ["가을 소프트", "가을 뮤트", "가을 딥", "가을 다크"],
    "겨울 (Winter)": ["겨울 브라이트", "겨울 비비드", "겨울 딥", "겨울 다크"]
}

# 4. 무작위 추천을 위한 데이터베이스 (각 톤별로 여러 제품을 리스트로 저장)
# 여기에 제품을 추가할수록 더 다양한 조합이 나옵니다.
cosmetics_pool = {
    "기본": { # 데이터가 부족한 톤을 위한 기본값
        "palette": [
            {"name": "에스쁘아 리얼 아이 팔레트", "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"},
            {"name": "데이지크 섀도우 팔레트", "img": "https://images.unsplash.com/photo-1522338221030-42404c1833d1?w=400"}
        ],
        "blusher": [
            {"name": "롬앤 베러 댄 치크", "img": "https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?w=400"},
            {"name": "클리니크 치크 팝", "img": "https://images.unsplash.com/photo-1620464389199-bf06742f6d2e?w=400"}
        ],
        "tint": [
            {"name": "페리페라 잉크 무드 틴트", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"},
            {"name": "롬앤 쥬시 래스팅 틴트", "img": "https://images.unsplash.com/photo-1591360236631-4506ba5281a8?w=400"}
        ]
    },
    "봄 라이트": {
        "palette": [
            {"name": "데이지크 - 피치 블렌딩", "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"},
            {"name": "페리페라 - 봄바람아 너는 계획이 다 있구나", "img": "https://images.unsplash.com/photo-1522338221030-42404c1833d1?w=400"}
        ],
        "blusher": [
            {"name": "롬앤 - 애프리콧 밀크", "img": "https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?w=400"},
            {"name": "피플씨 - 살구 피치", "img": "https://images.unsplash.com/photo-1620464389199-bf06742f6d2e?w=400"}
        ],
        "tint": [
            {"name": "코랄듀 틴트", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"},
            {"name": "베네피트 - 차차틴트", "img": "https://images.unsplash.com/photo-1591360236631-4506ba5281a8?w=400"}
        ]
    },
    # 다른 톤들도 위와 같은 방식으로 리스트 안에 여러 제품을 넣으면 됩니다.
}

# 5. 사이드바 구성
st.sidebar.title("🔍 세부 톤 선택")
selected_season = st.sidebar.selectbox("계절", list(tone_structure.keys()))
selected_detail = st.sidebar.radio("세부 타입", tone_structure[selected_season])

# 새로고침 버튼 (무작위 셔플을 유도)
if st.sidebar.button("다른 조합 보기 🔄"):
    st.rerun()

# 6. 메인 화면 - 랜덤 로직 적용
st.title(f"✨ {selected_detail}를 위한 오늘의 추천")
st.write("매번 새로운 조합으로 당신의 매력을 찾아드려요.")

# 해당 톤의 데이터가 있으면 가져오고, 없으면 기본값에서 랜덤 추출
pool = cosmetics_pool.get(selected_detail, cosmetics_pool["기본"])

# random.choice를 사용하여 리스트 중 하나를 무작위로 선택
random_palette = random.choice(pool["palette"])
random_blusher = random.choice(pool["blusher"])
random_tint = random.choice(pool["tint"])

# 레이아웃 출력
col1, col2, col3 = st.columns(3)

display_items = [
    ("👁️ EYE PALETTE", random_palette, col1),
    ("😊 BLUSHER", random_blusher, col2),
    ("💄 TINT / LIP", random_tint, col3)
]

for label, item, col in display_items:
    with col:
        st.markdown(f'<div class="category-label">{label}</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="product-card">
                <img src="{item['img']}" class="product-img">
                <div class="product-title">{item['name']}</div>
            </div>
        """, unsafe_allow_html=True)

st.divider()
st.info("💡 Tip: 왼쪽 사이드바의 '다른 조합 보기' 버튼을 누르면 새로운 화장품이 나타납니다!")
