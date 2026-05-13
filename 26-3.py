import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="16톤 상세 퍼스널 컬러 큐레이터", page_icon="💄", layout="wide")

# 2. 스타일 설정
st.markdown("""
    <style>
    .report-container {
        background-color: #f8f9fa;
        border-radius: 20px;
        padding: 30px;
        margin-top: 20px;
    }
    .category-header {
        font-size: 16px;
        font-weight: 800;
        color: #ff4b4b;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    .product-card {
        background-color: white;
        border-radius: 15px;
        padding: 25px;
        border: 1px solid #dee2e6;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.05);
        height: 100%;
    }
    .product-title {
        font-size: 18px;
        font-weight: 700;
        color: #111;
        margin-bottom: 8px;
        line-height: 1.4;
    }
    .product-detail {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
    }
    .highlight {
        color: #ff4b4b;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 16개 세부 톤 구조 정의
tone_structure = {
    "봄 (Spring)": ["봄 페일 (Pale)", "봄 라이트 (Light)", "봄 브라이트 (Bright)", "봄 비비드 (Vivid)"],
    "여름 (Summer)": ["여름 페일 (Pale)", "여름 라이트 (Light)", "여름 뮤트 (Mute)", "여름 그레이시 (Grayish)"],
    "가을 (Autumn)": ["가을 소프트 (Soft)", "가을 뮤트 (Mute)", "가을 딥 (Deep)", "가을 다크 (Dark)"],
    "겨울 (Winter)": ["겨울 브라이트 (Bright)", "겨울 비비드 (Vivid)", "겨울 딥 (Deep)", "겨울 다크 (Dark)"]
}

# 4. 상세 제품 데이터베이스 (호수까지 정확하게 기술)
# 예시로 몇 가지 톤에 데이터를 3개씩 넣었습니다. (더 추가할수록 랜덤성이 강력해집니다)
cosmetics_db = {
    "여름 라이트 (Light)": {
        "palette": [
            {"name": "클리오 - 프로 아이 팔레트 에어", "info": "02호 로즈 커넥션 (맑은 핑크 로즈 구성)"},
            {"name": "웨이크메이크 - 소프트 블러링 아이 팔레트", "info": "02호 생기 블러링 (청순한 라이트 핑크)"},
            {"name": "데이지크 - 섀도우 팔레트", "info": "18호 베리 스무디 (쿨한 베리 핑크 톤)"}
        ],
        "blusher": [
            {"name": "롬앤 - 베러 댄 치크", "info": "W01 오디 밀크 (우유 한 방울 섞인 라벤더)"},
            {"name": "피(fwee) - 블러셔 멜로우", "info": "01호 세븐틴 (맑은 베이비 핑크)"},
            {"name": "디올 - 백스테이지 로지 글로우", "info": "001 핑크 (피부 온도로 올라오는 맑은 핑크)"}
        ],
        "tint": [
            {"name": "입생로랑 - 캔디 글레이즈", "info": "11호 핑크 새티스팩션 (투명한 쿨 핑크)"},
            {"name": "페리페라 - 잉크 무드 글로이 틴트", "info": "05호 어쩔체리 (생기 가득한 체리 핑크)"},
            {"name": "라카 - 프루티 글램 틴트", "info": "111호 멜로우 (부드러운 데일리 핑크)"}
        ]
    },
    "가을 딥 (Deep)": {
        "palette": [
            {"name": "에스쁘아 - 리얼 아이 팔레트", "info": "05호 뎁스 (그윽한 딥 브라운 음영)"},
            {"name": "3CE - 멀티 아이 컬러 팔레트", "info": "#SHOT AGAIN (붉은기 섞인 딥 오렌지 브라운)"},
            {"name": "데이지크 - 섀도우 팔레트", "info": "11호 초콜릿 퍼지 (진한 초콜릿 브라운)"}
        ],
        "blusher": [
            {"name": "나스 - 블러쉬", "info": "타오스 (금펄이 박힌 딥 브릭 레드)"},
            {"name": "맥 - 글로우 플레이 블러쉬", "info": "댓츠 피치 (차분한 웜 코랄 브라운)"},
            {"name": "무지개맨션 - 피팅 블러쉬", "info": "05호 파인 (고급스러운 샌드 베이지)"}
        ],
        "tint": [
            {"name": "맥 - 파우더 키스 리퀴드", "info": "디보티드 투 칠리 (가을 딥의 정석 칠리 레드)"},
            {"name": "헤라 - 센슈얼 파우더 매트 리퀴드", "info": "187호 섹슈얼 초콜릿 (딥한 모브 초코)"},
            {"name": "롬앤 - 쥬시 래스팅 틴트", "info": "20호 다크 코코넛 (분위기 있는 브라운 레드)"}
        ]
    }
}

# 기본값 처리 (데이터가 없는 톤을 위해)
default_pool = {
    "palette": [{"name": "브랜드 정보 준비 중", "info": "세부 데이터 업데이트 예정입니다."}],
    "blusher": [{"name": "브랜드 정보 준비 중", "info": "세부 데이터 업데이트 예정입니다."}],
    "tint": [{"name": "브랜드 정보 준비 중", "info": "세부 데이터 업데이트 예정입니다."}]
}

# 5. 세션 상태 초기화 (랜덤성 보장)
if 'refresh_seed' not in st.session_state:
    st.session_state.refresh_seed = 0

# 6. 사이드바 제어
st.sidebar.title("🎨 16-Tone Diagnostic")
selected_season = st.sidebar.selectbox("1. 계절 선택", list(tone_structure.keys()))
selected_detail = st.sidebar.radio("2. 세부 톤 선택", tone_structure[selected_season])

if st.sidebar.button("다른 조합 보기 (새로고침) 🔄"):
    st.session_state.refresh_seed += 1

# 랜덤 시드 고정 (버튼 클릭시에만 변경되도록 제어)
random.seed(st.session_state.refresh_seed + sum(ord(c) for c in selected_detail))

# 7. 메인 화면
st.title(f"✨ {selected_detail}를 위한 상세 추천")
st.write(f"현재 선택된 타입: **{selected_detail}** | 오늘 당신에게 가장 잘 어울리는 제품 조합입니다.")

# 데이터 매칭
pool = cosmetics_db.get(selected_detail, default_pool)

p = random.choice(pool["palette"])
b = random.choice(pool["blusher"])
t = random.choice(pool["tint"])

# 결과 출력 레이아웃
st.markdown('<div class="report-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<p class="category-header">👁️ Eye Palette</p>', unsafe_allow_html=True)
    st.markdown(f"""<div class="product-card">
        <div class="product-title">{p['name']}</div>
        <div class="product-detail">{p['info']}</div>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown('<p class="category-header">😊 Blusher</p>', unsafe_allow_html=True)
    st.markdown(f"""<div class="product-card">
        <div class="product-title">{b['name']}</div>
        <div class="product-detail">{b['info']}</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown('<p class="category-header">💄 Tint / Lip</p>', unsafe_allow_html=True)
    st.markdown(f"""<div class="product-card">
        <div class="product-title">{t['name']}</div>
        <div class="product-detail">{t['info']}</div>
    </div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.markdown(f"💡 **스타일링 팁:** {selected_detail} 타입은 전체적인 색감의 통일성이 중요합니다. 위 조합은 전문가가 추천하는 가장 안정적인 매칭입니다.")
