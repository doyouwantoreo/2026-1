import streamlit as st

# 페이지 기본 설정 (타이틀, 아이콘)
st.set_page_config(
    page_title="텍스트 요약 및 대본 변환기",
    page_icon="📝",
    layout="centered"
)

# 앱 타이틀 및 설명
st.title("📝 가독성 극대화 텍스트 요약 & 대본 변환기")
st.markdown("긴 텍스트나 유튜브 스크립트를 넣으면 핵심 요약과 발표용 대본 형태로 가공해 줍니다.")
st.markdown("---")

# 1. 원본 텍스트 입력 영역
st.subheader("1. 원본 텍스트 입력")
input_text = st.text_area(
    "여기에 변환할 원본 텍스트를 복사해서 붙여넣으세요.", 
    height=250, 
    placeholder="여기에 긴 전공 서적 내용, 뉴스 기사, 유튜브 대본 등을 입력하세요..."
)

# 2. 옵션 설정 영역
st.subheader("2. 변환 옵션 설정")
summary_count = st.slider("핵심 요약 줄 수 선택", min_value=1, max_value=5, value=3)
line_spacing = st.selectbox("대본 줄바꿈 간격 설정", ["1줄 공백", "2줄 공백", "줄바꿈만"])

# 3. 변환 실행 버튼 및 로직
if st.button("✨ 가독성 극대화 변환하기", type="primary"):
    if not input_text.strip():
        st.warning("텍스트를 입력해 주세요!")
    else:
        # 문장 단위 분리 알고리즘 (온점 기준 구문 파싱)
        sentences = [s.strip() for s in input_text.replace('\n', ' ').split('.') if s.strip()]
        total_sentences = len(sentences)
        
        # 규칙 기반 핵심 문장 추출 로직
        step = max(1, total_sentences // summary_count)
        summarized_sentences = [sentences[i] for i in range(0, min(total_sentences, step * summary_count), step)]
        summarized_sentences = summarized_sentences[:summary_count]
        
        st.markdown("---")
        
        # 결과 화면 레이아웃 (좌우 2단 분할)
        col1, col2 = st.columns(2)
        
        # 왼쪽: 요약 결과 출력
        with col1:
            st.success(f"📌 핵심 {summary_count}줄 요약")
            summary_result = ""
            for i, sentence in enumerate(summarized_sentences, 1):
                summary_result += f"{i}. {sentence}.\n"
            st.text_area("요약 결과 박스", value=summary_result, height=250, label_visibility="collapsed")
            
        # 오른쪽: 대본 결과 출력
        with col2:
            st.info("🗣️ 발표/가독성용 대본 변환")
            if line_spacing == "1줄 공백":
                script_result = "\n\n".join(sentences)
            elif line_spacing == "2줄 공백":
                script_result = "\n\n\n".join(sentences)
            else:
                script_result = "\n".join(sentences)
            st.text_area("대본 결과 박스", value=script_result, height=250, label_visibility="collapsed")
            
        # 성공 효과 연출
        st.balloons()
