import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="퍼스널 컬러 AI 큐레이터", page_icon="💄", layout="wide")

# 2. 스타일 설정 (CSS)
st.markdown("""
    <style>
    .product-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #eee;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    .product-title {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-top: 10px;
    }
    .product-desc {
        font-size: 14px;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 세부 톤 및 실제 화장품 데이터 (12톤 체계)
cosmetics_data = {
    "봄 (Spring)": {
        "봄 라이트 (Light)": [
            {"name": "데이지크 - 피치 블렌딩", "desc": "맑은 피치빛 블러셔", "img": "https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?w=400"},
            {"name": "롬앤 - 듀이풀 워터 틴트 [코랄 듀]", "desc": "촉촉한 코랄 립", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"}
        ],
        "봄 브라이트 (Bright)": [
            {"name": "페리페라 - 잉크 무드 글로이 [틴메추해]", "desc": "생기 넘치는 코랄 레드", "img": "https://images.unsplash.com/photo-1625093765735-3058863f350c?w=400"},
            {"name": "베네피트 - 러브틴트", "desc": "선명한 파워 레드", "img": "https://images.unsplash.com/photo-1591360236631-4506ba5281a8?w=400"}
        ],
        "봄 트루 (True/Warm)": [
            {"name": "에스쁘아 - 리얼 아이 팔레트 [오트밀 레더]", "desc": "따뜻한 브라운 음영", "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"}
        ]
    },
    "여름 (Summer)": {
        "여름 라이트 (Light)": [
            {"name": "입생로랑 - 캔디 글레이즈 [핑크 새티스팩션]", "desc": "청순한 쿨 핑크", "img": "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=400"},
            {"name": "클리오 - 프로 아이 팔레트 [에어 2호]", "desc": "맑은 라벤더 음영", "img": "https://images.unsplash.com/photo-1522338221030-42404c1833d1?w=400"}
        ],
        "여름 뮤트 (Mute)": [
            {"name": "롬앤 - 베러 댄 팔레트 [피오니 누드 가든]", "desc": "차분한 모브 핑크", "img": "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=400"},
            {"name": "힌스 - 무드인핸서 매트 [얼루어]", "desc": "오묘한 로즈 모브 컬러", "img": "https://images.unsplash.com/photo-1503236123135-083567c91670?w=400"}
        ],
        "여름 트루 (True/Cool)": [
            {"name": "디올 - 백스테이지 로지 글로우 [001 핑크]", "desc": "시원한 쿨 핑크 치크", "img": "https://images.unsplash.com/photo-1620464389199-bf06742f6d2e?w=400"}
        ]
    },
    "가을 (Autumn)": {
        "가을 뮤트 (Mute)": [
            {"name": "헤라 - 센슈얼 파우더 매트 [팜파스]", "desc": "부드러운 오렌지 브라운", "img": "https://images.unsplash.com/photo-1583241475880-083f84372725?w=400"}
        ],
        "가을 딥 (Deep)": [
            {"name": "맥 - 매트 립스틱 [칠리]", "desc": "깊이 있는 브릭 레드", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"}
        ],
        "가을 트루 (True/Warm)": [
            {"name": "3CE - 멀티 아이 컬러 팔레트 [버터 크림]", "desc": "포근한 옐로우 브라운", "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"}
        ]
    },
    "겨울 (Winter)": {
        "겨울 브라이트 (Bright)": [
            {"name": "롬앤 - 블러 퍼지 틴트 [푸시아 바이브]", "desc": "쨍한 비비드 핑크", "img": "https://images.unsplash.com/photo-1625093765735-3058863f350c?w=400"}
        ],
        "겨울 딥 (Deep)": [
            {"name": "디올 - 어딕트 립 글로우 [베리]", "desc": "신비로운 플럼 버건디", "img": "https://images.unsplash.com/photo-1591360236631-4506ba5281a8?w=400"}
        ],
        "겨울 트루 (True/Cool)": [
            {"name": "바비브라운 - 럭스 아이섀도우 [문스톤]", "desc": "화려한 실버 펄 글리터", "img": "https://images.unsplash.com/photo-1522338221030-42404c1833d1?w=400"}
        ]
    }
}

# 4. 앱 화면 구성
st.title("🎨 12-Tone 퍼스널 컬러 화장품 추천")
st.write("당신의 세부 톤을 선택하면 실제 인생템을 보여드려요!")

# 사이드바에서 선택
st.sidebar.header("Filter")
selected_season = st.sidebar.selectbox("계절을 선택하세요", list(cosmetics_data.keys()))
selected_detail = st.sidebar.selectbox("세부 톤을 선택하세요", list(cosmetics_data[selected_season].keys()))

# 5. 결과 표시
st.subheader(f"✨ {selected_detail}를 위한 추천 아이템")

items = cosmetics_data[selected_season][selected_detail]

# 2열 또는 3열로 이미지와 텍스트 배치
cols = st.columns(len(items) if len(items) > 0 else 1)

for idx, item in enumerate(items):
    with cols[idx]:
        st.markdown(f"""
            <div class="product-card">
                <img src="{item['img']}" style="width:100%; border-radius:10px;">
                <div class="product-title">{item['name']}</div>
                <div class="product-desc">{item['desc']}</div>
            </div>
        """, unsafe_allow_html=True)
        # 실제 쇼핑 링크 버튼
        st.link_button("쇼핑 정보 확인", f"https://search.shopping.naver.com/search/all?query={item['name']}")

# 6. 하단 정보
st.info(f"💡 {selected_detail} 타입은 주로 어떤 컬러가 베스트인가요?")
if "라이트" in selected_detail:
    st.write("밝고 투명한 고명도 컬러가 얼굴의 혈색을 화사하게 살려줍니다.")
elif "브라이트" in selected_detail:
    st.write("채도가 높은 선명한 컬러가 인상을 또렷하고 생기 있게 만듭니다.")
elif "뮤트" in selected_detail:
    st.write("부드러운 회색기가 섞인 중채도 컬러가 오묘하고 고급스러운 분위기를 연출합니다.")
elif "딥" in selected_detail:
    st.write("깊이감 있는 저명도 컬러가 안정감 있고 분위기 있는 무드를 만들어줍니다.")
