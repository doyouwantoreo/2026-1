import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="16톤 랜덤 큐레이터", page_icon="🎲", layout="wide")

# 2. 스타일 설정
st.markdown("""
    <style>
    .category-title {
        font-size: 18px;
        font-weight: 800;
        color: #ff4b4b;
        margin-bottom: 10px;
        text-align: center;
    }
    .product-box {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 30px 20px;
        border: 2px solid #f0f2f6;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        min-height: 150px;
    }
    .product-name {
        font-size: 19px;
        font-weight: bold;
        color: #222;
        margin-bottom: 8px;
    }
    .product-tag {
        color: #ff4b4b;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터베이스 (데이터를 많이 넣을수록 랜덤성이 커집니다)
# 톤 구분을 '기본'으로 통합해서 테스트해볼 수 있게 양을 늘렸습니다.
db = {
    "palette": [
        "클리오 프로 아이 팔레트 에어", "데이지크 섀도우 팔레트", "웨이크메이크 소프트 블러링", 
        "3CE 멀티 아이 컬러", "에스쁘아 리얼 아이 팔레트", "페리페라 올테이크 무드",
        "롬앤 베러 댄 팔레트", "딘토 단테 원바이원", "힌스 뉴 뎁스", "피버 누드 팔레트"
    ],
    "blusher": [
        "롬앤 베러 댄 치크", "크리니크 치크 팝", "피 블러셔 멜로우", 
        "나스 블러쉬", "무지개맨션 피팅 블러쉬", "데이지크 블렌딩 무드",
        "릴리바이레드 러브빔", "어뮤즈 소프트 크림 치크", "글린트 하이라이터", "라카 러브 실크"
    ],
    "tint": [
        "페리페라 잉크 무드 글로이", "롬앤 쥬시 래스팅", "입생로랑 캔디 글레이즈", 
        "아워글래스 팬텀 볼륨", "무지개맨션 오브제 리퀴드", "헤라 센슈얼 파우더 매트",
        "클리오 크리스탈 글램", "에스쁘아 꾸뛰르 립틴트", "데이지크 쥬시 듀이", "힌스 무드인핸서"
    ]
}

# 4. 사이드바 및 상태 관리
st.sidebar.title("🔍 톤 설정")
season = st.sidebar.selectbox("계절", ["봄", "여름", "가을", "겨울"])

# 버튼을 누를 때마다 세션 상태에 랜덤 시드를 부여
if st.sidebar.button("다른 조합 보기 🔄") or 'seed' not in st.session_state:
    st.session_state.seed = random.randint(1, 1000)

# 고정된 랜덤 시드를 사용해 해당 세션 동안은 유지되다가 버튼 누르면 변경
random.seed(st.session_state.seed)

# 5. 메인 화면
st.title(f"✨ {season} 타입을 위한 무작위 추천")
st.write("이미지 없이 텍스트로만 구성된 실시간 랜덤 리스트입니다.")

# 데이터 추출 (중복 없이 셔플)
p_pick = random.choice(db["palette"])
b_pick = random.choice(db["blusher"])
t_pick = random.choice(db["tint"])

# 레이아웃 구성
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="category-title">👁️ PALETTE</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="product-box"><div class="product-name">{p_pick}</div><div class="product-tag">#추천템1</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="category-title">😊 BLUSHER</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="product-box"><div class="product-name">{b_pick}</div><div class="product-tag">#추천템2</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="category-title">💄 TINT</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="product-box"><div class="product-name">{t_pick}</div><div class="product-tag">#추천템3</div></div>', unsafe_allow_html=True)

st.divider()
st.caption(f"현재 조합 번호: {st.session_state.seed} (버튼을 누를 때마다 이 번호가 바뀌며 제품도 바뀝니다.)")
