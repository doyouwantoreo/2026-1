import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="12톤 퍼스널 컬러 큐레이터", page_icon="🎨", layout="wide")

# 2. 스타일 설정 (CSS)
st.markdown("""
    <style>
    .category-label {
        font-size: 14px;
        font-weight: bold;
        color: #ff4b4b;
        margin-bottom: 5px;
    }
    .product-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #f0f2f6;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 10px;
        transition: transform 0.3s;
    }
    .product-card:hover {
        transform: translateY(-5px);
    }
    .product-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .product-title {
        font-size: 16px;
        font-weight: bold;
        color: #333;
        min-height: 45px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 12톤 상세 데이터 (아이템 3종 세트)
cosmetics_db = {
    "봄 라이트 (Spring Light)": {
        "palette": {"name": "데이지크 - 피치 블렌딩", "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"},
        "blusher": {"name": "롬앤 - 베러 댄 치크 [애프리콧 밀크]", "img": "https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?w=400"},
        "tint": {"name": "페리페라 - 잉크 무드 글로이 [갓성비템]", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"}
    },
    "여름 뮤트 (Summer Mute)": {
        "palette": {"name": "클리오 - 프로 아이 팔레트 [한남동 아뜰리에]", "img": "https://images.unsplash.com/photo-1522338221030-42404c1833d1?w=400"},
        "blusher": {"name": "힌스 - 트루 디멘션 [베어 레플렉션]", "img": "https://images.unsplash.com/photo-1503236123135-083567c91670?w=400"},
        "tint": {"name": "롬앤 - 쥬시 래스팅 [베어 그레이프]", "img": "https://images.unsplash.com/photo-1625093765735-3058863f350c?w=400"}
    },
    "가을 딥 (Autumn Deep)": {
        "palette": {"name": "에스쁘아 - 리얼 아이 팔레트 [뎁스]", "img": "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=400"},
        "blusher": {"name": "나스 - 블러쉬 [타오스]", "img": "https://images.unsplash.com/photo-1620464389199-bf06742f6d2e?w=400"},
        "tint": {"name": "맥 - 칠리", "img": "https://images.unsplash.com/photo-1591360236631-4506ba5281a8?w=400"}
    },
    "겨울 브라이트 (Winter Bright)": {
        "palette": {"name": "웨이크메이크 - 소프트 블러링 [퓨어 라벤더]", "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"},
        "blusher": {"name": "크리니크 - 치크 팝 [팬지 팝]", "img": "https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?w=400"},
        "tint": {"name": "입생로랑 - 캔디 글레이즈 [11호]", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"}
    }
    # 나머지 8개 톤도 위와 같은 형식으로 추가 가능합니다.
}

# 4. 앱 레이아웃
st.title("✨ 퍼스널 컬러 풀세트 추천")
st.write("선택하신 톤에 가장 잘 어울리는 **팔레트, 블러셔, 틴트** 조합입니다.")

# 사이드바 선택
all_tones = list(cosmetics_db.keys())
selected_tone = st.sidebar.selectbox("당신의 세부 톤을 선택하세요", all_tones)

# 5. 추천 결과 출력
if selected_tone in cosmetics_db:
    data = cosmetics_db[selected_tone]
    
    # 카테고리별 컬럼 생성
    col1, col2, col3 = st.columns(3)
    
    categories = [
        ("👁️ EYE PALETTE", data['palette'], col1),
        ("😊 BLUSHER", data['blusher'], col2),
        ("💄 TINT / LIP", data['tint'], col3)
    ]
    
    for label, item, col in categories:
        with col:
            st.markdown(f'<div class="category-label">{label}</div>', unsafe_allow_html=True)
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['img']}" class="product-img">
                    <div class="product-title">{item['name']}</div>
                </div>
            """, unsafe_allow_html=True)
            # 네이버 쇼핑 검색 링크 자동 생성
            st.link_button("최저가 구매하기", f"https://search.shopping.naver.com/search/all?query={item['name']}", use_container_width=True)

# 6. 추가 팁
st.divider()
st.caption(f"💡 {selected_tone} 타입은 이 세 가지 조합만으로도 완벽한 메이크업 룩을 완성할 수 있습니다.")
