import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="퍼스널 컬러 큐레이터", page_icon="💄", layout="wide")

# 2. 스타일 설정 (CSS) - 깔끔한 카드 디자인
st.markdown("""
    <style>
    .product-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #eeeeee;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 10px;
    }
    .product-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .product-title {
        font-size: 16px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 5px;
    }
    .product-desc {
        font-size: 13px;
        color: #777777;
        margin-bottom: 15px;
        height: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 구성 (12톤 체계)
cosmetics_data = {
    "봄 (Spring)": {
        "봄 라이트 (Light)": [
            {"name": "데이지크 - 피치 블렌딩", "desc": "맑은 피치빛 블러셔", "img": "https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?w=400"},
            {"name": "롬앤 - 듀이풀 워터 틴트 [코랄 듀]", "desc": "촉촉한 코랄 립", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"}
        ],
        "봄 브라이트 (Bright)": [
            {"name": "페리페라 - 틴메추해", "desc": "생기 넘치는 코랄 레드", "img": "https://images.unsplash.com/photo-1625093765735-3058863f350c?w=400"},
            {"name": "베네피트 - 러브틴트", "desc": "선명한 파워 레드", "img": "https://images.unsplash.com/photo-1591360236631-4506ba5281a8?w=400"}
        ]
    },
    "여름 (Summer)": {
        "여름 라이트 (Light)": [
            {"name": "입생로랑 - 핑크 새티스팩션", "desc": "청순한 쿨 핑크", "img": "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=400"},
            {"name": "클리오 - 에어 2호", "desc": "맑은 라벤더 음영", "img": "https://images.unsplash.com/photo-1522338221030-42404c1833d1?w=400"}
        ],
        "여름 뮤트 (Mute)": [
            {"name": "롬앤 - 피오니 누드 가든", "desc": "차분한 모브 핑크", "img": "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=400"}
        ]
    },
    "가을 (Autumn)": {
        "가을 뮤트 (Mute)": [
            {"name": "헤라 - 팜파스", "desc": "부드러운 오렌지 브라운", "img": "https://images.unsplash.com/photo-1583241475880-083f84372725?w=400"}
        ],
        "가을 딥 (Deep)": [
            {"name": "맥 - 칠리", "desc": "깊이 있는 브릭 레드", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"}
        ]
    },
    "겨울 (Winter)": {
        "겨울 브라이트 (Bright)": [
            {"name": "롬앤 - 푸시아 바이브", "desc": "쨍한 비비드 핑크", "img": "https://images.unsplash.com/photo-1625093765735-3058863f350c?w=400"}
        ],
        "겨울 딥 (Deep)": [
            {"name": "디올 - 베리", "desc": "신비로운 플럼 버건디", "img": "https://images.unsplash.com/photo-1591360236631-4506ba5281a8?w=400"}
        ]
    }
}

# 4. 앱 화면 레이아웃
st.title("💄 퍼스널 컬러 AI 추천 서비스")
st.write("나의 세부 톤에 맞는 인생 화장품을 찾아보세요.")

# 사이드바 필터
st.sidebar.header("톤 선택")
season_list = list(cosmetics_data.keys())
selected_season = st.sidebar.selectbox("계절 선택", season_list)

detail_list = list(cosmetics_data[selected_season].keys())
selected_detail = st.sidebar.selectbox("상세 톤 선택", detail_list)

# 5. 제품 출력 섹션
st.subheader(f"✨ {selected_detail} 타입을 위한 추천")

items = cosmetics_data[selected_season][selected_detail]

# 컬럼 레이아웃 처리
if items:
    cols = st.columns(len(items))
    for i, item in enumerate(items):
        with cols[i]:
            # HTML 카드 렌더링
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['img']}" class="product-img">
                    <div class="product-title">{item['name']}</div>
                    <div class="product-desc">{item['desc']}</div>
                </div>
            """, unsafe_allow_html=True)
            # 쇼핑 버튼 (Streamlit 기본 버튼 사용)
            st.link_button("최저가 확인", f"https://search.shopping.naver.com/search/all?query={item['name']}", use_container_width=True)
else:
    st.info("데이터를 준비 중입니다.")

# 6. 하단 팁
st.divider()
with st.expander("전문가 한 줄 팁"):
    if "라이트" in selected_detail:
        st.write("밝고 투명한 메이크업이 베스트입니다. 두꺼운 화장은 피해주세요!")
    elif "브라이트" in selected_detail:
        st.write("립에 확실한 포인트 컬러를 주면 안색이 확 살아납니다.")
    elif "뮤트" in selected_detail:
        st.write("채도가 낮은 '말린 장미' 계열의 컬러를 활용해 보세요.")
    elif "딥" in selected_detail:
        st.write("깊이 있는 음영 메이크업과 진한 컬러가 이목구비를 뚜렷하게 해줍니다.")
