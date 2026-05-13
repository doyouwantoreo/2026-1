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
        min-height: 450px;
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
        margin-bottom: 15px;
    }
    .product-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 세팅 (12톤 체계)
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
            {"name": "입생로랑 - 캔디 글레이즈 [핑크 새티스팩션]", "desc": "청순한 쿨 핑크", "img": "
