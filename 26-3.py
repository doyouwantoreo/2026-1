import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="AI 퍼스널 컬러 큐레이터", page_icon="✨", layout="wide")

# 2. 스타일 설정 (CSS 업그레이드)
st.markdown("""
    <style>
    .product-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #f0f0f0;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        height: 400px; /* 카드 높이 통일 */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .product-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
    }
    .product-title {
        font-size: 16px;
        font-weight: 700;
        color: #222;
        margin: 10px 0 5px 0;
    }
    .product-desc {
        font-size: 13px;
        color: #888;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 (기존 데이터 유지)
# ... (작성하신 cosmetics_data 그대로 사용) ...

# 4. 앱 화면 구성
st.title("🎨 12-Tone 퍼스널 컬러 화장품 추천")
st.write("나에게 딱 맞는 '인생템'을 확인해보세요.")

# 사이드바
st.sidebar.header("🔍 상세 톤 선택")
selected_season = st.sidebar.selectbox("계절을 선택하세요", list(cosmetics_data.keys()))
selected_detail = st.sidebar.selectbox("세부 톤을 선택하세요", list(cosmetics_data[selected_season].keys()))

# 5. 결과 표시
st.divider()
st.subheader(f"✨ {selected_detail}를 위한 추천 아이템")

items = cosmetics_data[selected_season][selected_detail]

if items:
    # 한 줄에 최대 3개씩 배치하도록 개선
    for i in range(0, len(items), 3):
        cols = st.columns(3)
        for j, item in enumerate(items[i:i+3]):
            with cols[j]:
                st.markdown(f"""
                    <div class="product-card">
                        <img src="{item['img']}" class="product-img">
                        <div>
                            <div class="product-title">{item['name']}</div>
                            <div class="product-desc">{item['desc']}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"🔍 '{item['name']}' 최저가", f"https://search.shopping.naver.com/search/all?query={item['name']}", use_container_width=True)
else:
    st.info("해당 톤에 대한 추천 아이템을 준비 중입니다.")

# 6. 하단 팁 (Expander로 깔끔하게 정리)
with st.expander(f"💡 {selected_detail} 활용 팁 보기"):
    if "라이트" in selected_detail:
        st.write("고명도의 파스텔 톤이 베스트! 메이크업은 투명하고 맑게 하는 것이 핵심입니다.")
    elif "브라이트" in selected_detail:
        st.write("선명한 원색이 이목구비를 살려줍니다. 입술에 포인트를 주는 메이크업을 추천해요.")
    elif "뮤트" in selected_detail:
        st.write("회색기가 섞인 차분한 컬러가 우아함을 더해줍니다. 매트한 질감의 섀도우가 잘 어울려요.")
    elif "딥" in selected_detail:
        st.write("깊이감 있는 컬러로 분위기를 연출하세요. 음영 메이크업이 가장 잘 어울리는 타입입니다.")
