import streamlit as st
import pandas as pd
from urllib.parse import quote

# 1. 페이지 설정
st.set_page_config(page_title="Personal Color Shop", page_icon="🛍️", layout="wide")

# 2. 제품 데이터 (12톤 체계 반영)
# 이미지 URL은 실제 제품과 유사한 샘플 이미지들입니다.
cosmetics_data = {
    "봄 (Spring)": {
        "봄 라이트": [
            {"brand": "데이지크", "name": "피치 블렌딩 치크", "desc": "복숭아 빛 화사한 생기", "img": "https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?w=400"},
            {"brand": "롬앤", "name": "쥬시 래스팅 틴트 베어 애플", "desc": "맑은 사과 코랄", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"}
        ],
        "봄 브라이트": [
            {"brand": "페리페라", "name": "잉크 무드 글로이 틴트 갓기천사", "desc": "쨍한 핑크 코랄", "img": "https://images.unsplash.com/photo-1625093765735-3058863f350c?w=400"}
        ]
    },
    "여름 (Summer)": {
        "여름 라이트": [
            {"brand": "클리오", "name": "프로 아이 팔레트 에어 복사꽃 필 무렵", "desc": "시원하고 깨끗한 핑크", "img": "https://images.unsplash.com/photo-1522338221030-42404c1833d1?w=400"}
        ],
        "여름 뮤트": [
            {"brand": "롬앤", "name": "베러 댄 팔레트 피오니 누드 가든", "desc": "차분한 모브 라벤더", "img": "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=400"}
        ]
    },
    "가을 (Autumn)": {
        "가을 뮤트": [
            {"brand": "헤라", "name": "센슈얼 파우더 매트 팜파스", "desc": "부드러운 살구 브라운", "img": "https://images.unsplash.com/photo-1583241475880-083f84372725?w=400"}
        ],
        "가을 딥": [
            {"brand": "맥(MAC)", "name": "매트 립스틱 칠리", "desc": "깊이 있는 고추장 레드", "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"}
        ]
    },
    "겨울 (Winter)": {
        "겨울 브라이트": [
            {"brand": "롬앤", "name": "블러 퍼지 틴트 푸시아 바이브", "desc": "쨍한 쿨 핑크 레드", "img": "https://images.unsplash.com/photo-1625093765735-3058863f350c?w=400"}
        ],
        "겨울 딥": [
            {"brand": "디올", "name": "어딕트 립 글로우 베리", "desc": "신비로운 퍼플 버건디", "img": "https://images.unsplash.com/photo-1591360236631-4506ba5281a8?w=400"}
        ]
    }
}

# 3. UI 구성
st.title("🎨 퍼스널 컬러별 맞춤 쇼핑 추천")
st.write("선택하신 톤에 맞는 제품을 클릭하면 최저가 쇼핑 페이지로 이동합니다.")

# 선택 박스
col_s1, col_s2 = st.columns(2)
with col_s1:
    season = st.selectbox("큰 계절 선택", list(cosmetics_data.keys()))
with col_s2:
    detail = st.selectbox("세부 톤 선택", list(cosmetics_data[season].keys()))

st.divider()

#
