import streamlit as st
import os

# MBTI별 추천 공부 방법 데이터
study_tips = {
    "INTJ": "계획을 세우고 목표 중심으로 공부하세요. 장기적인 전략이 효과적입니다.",
    "INFP": "자기 동기 부여가 중요합니다. 감정과 연결된 주제를 중심으로 공부하세요.",
    "ENTP": "토론과 아이디어 교환을 통해 학습하세요. 창의적인 접근이 효과적입니다.",
    "ISFJ": "체계적인 노트 정리와 반복 학습이 잘 맞습니다.",
    "ESTJ": "목표 설정과 시간 관리가 중요합니다. 실용적인 예제를 활용하세요.",
    "ENFP": "다양한 방식으로 학습하세요. 시각적 자료와 이야기 중심 학습이 효과적입니다.",
    "ISTP": "실습과 문제 해결 중심 학습이 좋습니다. 직접 해보는 것이 중요합니다.",
    "INFJ": "깊이 있는 이해와 의미 중심 학습이 효과적입니다. 조용한 환경에서 집중하세요.",
    "ESFP": "재미있고 활동적인 방식으로 학습하세요. 그룹 스터디도 잘 맞습니다.",
    "ESTP": "즉각적인 피드백과 실전 중심 학습이 효과적입니다.",
    "ISFP": "감각적이고 예술적인 접근이 잘 맞습니다. 시각적 자료를 활용하세요.",
    "ENTJ": "목표 설정과 리더십을 활용한 학습이 효과적입니다. 전략적으로 접근하세요.",
    "INTP": "논리적이고 분석적인 학습이 잘 맞습니다. 개념을 깊이 있게 탐구하세요.",
    "ESFJ": "협력적인 환경에서 학습하세요. 정리된 자료와 루틴이 도움이 됩니다.",
    "ISTJ": "규칙적인 학습 습관과 체크리스트가 효과적입니다.",
    "ENFJ": "다른 사람과 함께 학습하며 동기를 얻으세요. 감정적 연결도 중요합니다."
}

# 이미지 경로 설정
def get_image_path(mbti_type):
    path = f"images/{mbti_type}.png"
    return path if os.path.exists(path) else None

# 앱 제목
st.title("MBTI 유형별 공부 방법 추천")

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(study_tips.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"{selected_mbti} 유형에 맞는 공부 방법:")
    st.write(study_tips[selected_mbti])

    # 이미지 출력
    image_path = get_image_path(selected_mbti)
    if image_path:
        st.image(image_path, caption=f"{selected_mbti} 이미지", use_container_width=True)
    else:
        st.warning("해당 MBTI 이미지가 아직 준비되지 않았습니다.")
