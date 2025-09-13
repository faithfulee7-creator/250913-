import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(
    page_title="우리 몸의 구조와 기능",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto"
)

# 스타일 적용
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stSelectbox label {
        font-size: 18px;
        font-weight: bold;
        color: #333;
    }
    .stMarkdown h1 {
        color: #2e8b57;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align: center;'>🧬 우리 몸의 구조와 기능</h1>", unsafe_allow_html=True)
st.write("아래에서 기관을 선택하면 해당 기관의 역할을 확인할 수 있어요.")

# 기관 정보
organs_info = {
    "뇌 🧠": "뇌는 우리 몸의 중심 제어 장치로, 생각하고 기억하며 몸의 움직임을 조절합니다.",
    "심장 ❤️": "심장은 혈액을 온몸으로 보내는 펌프 역할을 합니다.",
    "폐 🫁": "폐는 공기 중의 산소를 받아들이고 이산화탄소를 내보내는 기관입니다.",
    "위 🥣": "위는 음식물을 저장하고 소화시키는 역할을 합니다.",
    "소장 🧵": "소장은 음식물에서 영양분을 흡수하는 기관입니다.",
    "대장 🧻": "대장은 남은 음식물에서 수분을 흡수하고 배설물로 만듭니다.",
    "간 🧪": "간은 해로운 물질을 해독하고 영양소를 저장합니다.",
    "신장 💧": "신장은 혈액을 걸러 노폐물을 소변으로 배출합니다.",
    "근육 💪": "근육은 몸을 움직이게 하고 자세를 유지하게 합니다.",
    "뼈 🦴": "뼈는 몸을 지탱하고 내부 기관을 보호합니다."
}

# 드롭다운 메뉴
selected_organ = st.selectbox("기관을 선택하세요", list(organs_info.keys()))

# 카드 스타일로 설명 출력
st.markdown(f"""
    <div class="card">
        <h2>{selected_organ}</h2>
        <p>{organs_info[selected_organ]}</p>
    </div>
""", unsafe_allow_html=True)
