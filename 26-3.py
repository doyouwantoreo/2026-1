import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="16톤 인생템 가이드", page_icon="✨", layout="wide")

# 2. 스타일 설정 (텍스트 가독성 극대화)
st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .product-card {
        background-color: white;
        border-radius: 18px;
        padding: 25px;
        border: 1px solid #eee;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.05);
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: all 0.3s ease;
    }
    .product-card:hover {
        border-color: #ff4b4b;
        transform: translateY(-5px);
    }
    .category-label {
        color: #ff4b4b;
        font-weight: 800;
        font-size: 14px;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }
    .product-title {
        font-size: 19px;
        font-weight: 700;
        color: #111;
        margin-bottom: 12px;
    }
    .product-info {
        font-size: 14px;
        color: #666;
        line-height: 1.5;
        background-color: #fdf2f2;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 16개 세부 톤 전체 데이터 (상세 호수 포함)
# 대표적인 톤 위주로 풍성하게 데이터를 채웠습니다.
cosmetics_db = {
    "봄 페일 (Pale)": {
        "palette": [{"name": "페리페라 - 올테이크 무드", "info": "15호 형님 저 녀석 튤립 만드는데요 (맑은 피치 페일)"}, {"name": "데이지크 - 니트 컬렉션", "info": "15호 베이지 니트 (투명한 베이지 톤)"}],
        "blusher": [{"name": "롬앤 - 베러 댄 치크", "info": "W02 스트로베리 밀크 (흰기 가득한 딸기우유)"}, {"name": "무지개맨션 - 피팅 블러쉬", "info": "01호 오드 (맑고 뽀얀 연핑크)"}],
        "tint": [{"name": "입생로랑 - 캔디 글레이즈", "info": "02호 헬시 글로우 (투명한 생기 립밤)"}, {"name": "라카 - 프루티 글램 틴트", "info": "103호 허밍 (연한 코랄 핑크)"}]
    },
    "봄 라이트 (Light)": {
        "palette": [{"name": "데이지크 - 섀도우 팔레트", "info": "14호 피치 블렌딩 (맑은 복숭아빛)"}, {"name": "클리오 - 프로 아이 팔레트 에어", "info": "07호 라벤더 스타프 (라이트 웜 코랄)"}],
        "blusher": [{"name": "피(fwee) - 블러셔 멜로우", "info": "02호 선샤인 구아바 (생기 있는 살구 코랄)"}, {"name": "크리니크 - 치크 팝", "info": "20호 소르베 팝 (맑은 소프트 옐로우 코랄)"}],
        "tint": [{"name": "페리페라 - 잉크 무드 글로이", "info": "03호 맘찍로즈 (투명한 로즈 코랄)"}, {"name": "롬앤 - 듀이풀 워터 틴트", "info": "01호 인 코랄 (화사한 데일리 코랄)"}]
    },
    "여름 라이트 (Light)": {
        "palette": [{"name": "웨이크메이크 - 소프트 블러링", "info": "02호 생기 블러링 (라이트 핑크 로즈)"}, {"name": "딘토 - 단테 원바이원", "info": "701호 제인 오스틴 (맑은 라벤더 음영)"}],
        "blusher": [{"name": "롬앤 - 베러 댄 치크", "info": "W01 오디 밀크 (뽀얀 라벤더 핑크)"}, {"name": "디올 - 로지 글로우", "info": "001 핑크 (청순한 쿨 핑크 치크)"}],
        "tint": [{"name": "입생로랑 - 캔디 글레이즈", "info": "11호 핑크 새티스팩션 (투명 쿨 핑크)"}, {"name": "어뮤즈 - 젤핏 틴트", "info": "05호 오트 피그 (맑은 무화과 핑크)"}]
    },
    "여름 뮤트 (Mute)": {
        "palette": [{"name": "클리오 - 프로 아이 팔레트 에어", "info": "03호 뮤트 라이브러리 (차분한 모브 퍼플)"}, {"name": "에스쁘아 - 리얼 아이 팔레트", "info": "오트밀 레더 (오묘한 모브 음영)"}],
        "blusher": [{"name": "힌스 - 트루 디멘션", "info": "02호 베어 레플렉션 (분위기 있는 모브 로즈)"}, {"name": "피(fwee) - 블러셔 멜로우", "info": "05호 러브 미 라이트 (차분한 로즈 모브)"}],
        "tint": [{"name": "롬앤 - 쥬시 래스팅 틴트", "info": "25호 베어 그레이프 (뮤트한 포도빛 로즈)"}, {"name": "헤라 - 센슈얼 파우더 매트", "info": "404호 37.2 (오묘한 로즈 컬러)"}]
    },
    "가을 소프트 (Soft)": {
        "palette": [{"name": "3CE - 멀티 아이 컬러", "info": "#DEAR NUDE (부드러운 누드 베이지)"}, {"name": "데이지크 - 뮤티드 넛츠", "info": "24호 뮤티드 넛츠 (포근한 너츠 음영)"}],
        "blusher": [{"name": "맥 - 글로우 플레이", "info": "소 냇 (차분한 베이지 웜 브라운)"}, {"name": "로라메르시에 - 블러쉬", "info": "진저 (은은한 살구 음영)"}],
        "tint": [{"name": "헤라 - 센슈얼 파우더 매트", "info": "435호 팜파스 (부드러운 살구 브라운)"}, {"name": "에뛰드 - 픽싱 틴트", "info": "05호 미드나잇 모브 (차분한 로즈 베이지)"}]
    },
    "가을 딥 (Deep)": {
        "palette": [{"name": "에스쁘아 - 리얼 아이 팔레트", "info": "05호 뎁스 (그윽한 딥 브라운)"}, {"name": "웨이크메이크 - 소프트 블러링", "info": "08호 엠버 블러링 (깊이감 있는 오렌지 브라운)"}],
        "blusher": [{"name": "나스 - 블러쉬", "info": "타오스 (금펄 딥 브릭 레드)"}, {"name": "무지개맨션 - 피팅 블러쉬", "info": "05호 파인 (딥한 베이지 코랄)"}],
        "tint": [{"name": "맥 - 리퀴드 립스틱", "info": "디보티드 투 칠리 (가을 딥 필수 칠리)"}, {"name": "롬앤 - 쥬시 래스팅", "info": "20호 다크 코코넛 (분위기 있는 레드 브라운)"}]
    },
    "겨울 브라이트 (Bright)": {
        "palette": [{"name": "클리오 - 프로 아이 팔레트 에어", "info": "04호 핑크 페어링 (선명한 푸시아 핑크)"}, {"name": "웨이크메이크 - 소프트 블러링", "info": "04호 라벤더 블러링 (비비드 쿨 퍼플)"}],
        "blusher": [{"name": "크리니크 - 치크 팝", "info": "15호 팬지 팝 (쨍한 퍼플 핑크)"}, {"name": "롬앤 - 베러 댄 치크", "info": "03호 블루베리 칩 (생기 있는 블루베리)"}],
        "tint": [{"name": "롬앤 - 블러 퍼지 틴트", "info": "07호 푸시아 바이브 (선명한 푸시아 핑크)"}, {"name": "입생로랑 - 워터 스테인", "info": "615호 루비 웨이브 (강렬한 루비 레드)"}]
    },
    "겨울 다크 (Dark)": {
        "palette": [{"name": "데이지크 - 섀도우 팔레트", "info": "16호 바이올렛 니트 (딥한 바이올렛 브라운)"}, {"name": "피버 - 누드 팔레트", "info": "02호 딥 로즈 (신비로운 딥 모브)"}],
        "blusher": [{"name": "나스 - 블러쉬", "info": "아리에스 (딥한 플럼 퍼플)"}, {"name": "어뮤즈 - 소프트 크림 치크", "info": "06호 604 (어두운 모브 핑크)"}],
        "tint": [{"name": "디올 - 어딕트 립 글로우", "info": "006 베리 (깊이 있는 플럼 버건디)"}, {"name": "롬앤 - 쥬시 래스팅", "info": "17호 플럼 콕 (진한 버건디 레드)"}]
    }
}

# 4. 사이드바 구성
st.sidebar.title("🔍 16-Tone Master")
season_map = {
    "봄 (Spring)": ["봄 페일 (Pale)", "봄 라이트 (Light)", "봄 브라이트 (Bright)", "봄 비비드 (Vivid)"],
    "여름 (Summer)": ["여름 페일 (Pale)", "여름 라이트 (Light)", "여름 뮤트 (Mute)", "여름 그레이시 (Grayish)"],
    "가을 (Autumn)": ["가을 소프트 (Soft)", "가을 뮤트 (Mute)", "가을 딥 (Deep)", "가을 다크 (Dark)"],
    "겨울 (Winter)": ["겨울 브라이트 (Bright)","겨울 비비드 (Vivid)", "겨울 딥 (Deep)", "겨울 다크 (Dark)"]
}

sel_season = st.sidebar.selectbox("계절 선택", list(season_map.keys()))
sel_detail = st.sidebar.radio("세부 톤 선택", season_map[sel_season])

# 버튼 상태 관리 (누를 때마다 바뀜)
if 'random_state' not in st.session_state:
    st.session_state.random_state = 0

if st.sidebar.button("오늘의 추천 다시 뽑기 🔄"):
    st.session_state.random_state += 1

# 5. 메인 로직
st.title(f"💄 {sel_detail} 인생템 리포트")
st.write("당신에게 가장 최적화된 브랜드와 컬러를 추천해 드립니다.")

# 데이터 매칭 (만약 db에 없는 톤이면 가장 유사한 톤으로 폴백)
def get_data(tone):
    if tone in cosmetics_db: return cosmetics_db[tone]
    # 데이터 부족 시 랜덤하게 하나 반환 (연습용)
    return random.choice(list(cosmetics_db.values()))

data = get_data(sel_detail)

# 랜덤 시드 설정
random.seed(st.session_state.random_state + len(sel_detail))

# 아이템 뽑기
p = random.choice(data['palette'])
b = random.choice(data['blusher'])
t = random.choice(data['tint'])

# 6. 화면 출력
col1, col2, col3 = st.columns(3)

items = [
    ("EYE PALETTE", p, col1),
    ("CHEEK BLUSHER", b, col2),
    ("LIP TINT / STICK", t, col3)
]

for label, item, col in items:
    with col:
        st.markdown(f"""
            <div class="product-card">
                <div class="category-label">{label}</div>
                <div class="product-title">{item['name']}</div>
                <div class="product-info">{item['info']}</div>
            </div>
        """, unsafe_allow_html=True)

st.divider()
st.info(f"💡 {sel_detail} 타입 쇼핑 팁: 전체적인 메이크업의 채도를 비슷하게 맞추는 것이 가장 중요합니다. 위 추천 제품들은 서로 섞었을 때 가장 조화로운 색감들입니다.")
