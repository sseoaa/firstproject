import streamlit as st
import random
from datetime import date

# 🌈 Streamlit 페이지 설정
st.set_page_config(page_title="오늘의 별자리 운세", page_icon="🔮", layout="centered")

# ✨ 제목 & 설명
st.markdown("# 🔮 오늘의 별자리 운세")
st.markdown("## 당신의 운명을 알아보세요... ⭐")
st.markdown("💫 하루의 시작을 마법처럼! 오늘의 별자리를 선택하고 운세를 확인해보세요 ✨")
st.markdown("---")

# 🌟 별자리 리스트
zodiacs = {
    "양자리 ♈": "Aries",
    "황소자리 ♉": "Taurus",
    "쌍둥이자리 ♊": "Gemini",
    "게자리 ♋": "Cancer",
    "사자자리 ♌": "Leo",
    "처녀자리 ♍": "Virgo",
    "천칭자리 ♎": "Libra",
    "전갈자리 ♏": "Scorpio",
    "사수자리 ♐": "Sagittarius",
    "염소자리 ♑": "Capricorn",
    "물병자리 ♒": "Aquarius",
    "물고기자리 ♓": "Pisces"
}

# 🔮 운세 예시 모음
fortunes = [
    "✨ 오늘은 뜻밖의 행운이 찾아올 거예요. 기회를 꼭 잡으세요! 🍀",
    "💼 열심히 한 만큼 결과가 따라올 거예요. 꾸준함이 빛나는 날입니다!",
    "💖 사랑의 기운이 강해요. 새로운 인연을 기대해보세요 💌",
    "😌 작은 실수는 지나가니 너무 걱정 마세요. 당신은 충분히 잘하고 있어요!",
    "🎁 누군가로부터 깜짝 선물을 받을지도 몰라요! 기대해보세요 🎉",
    "🧘‍♀️ 휴식이 필요한 날이에요. 스스로를 돌보는 데 집중하세요 💆‍♂️",
    "📚 오늘은 배우기에 좋은 날! 새로운 정보를 받아들이기 좋아요 📖",
    "🌈 마음을 열면 좋은 일이 따라올 거예요. 긍정의 힘을 믿으세요 ☀️",
    "🔥 강력한 에너지가 느껴져요. 중요한 일을 시작하기 좋은 타이밍입니다!",
    "🍽️ 맛있는 음식과 함께 좋은 사람과의 시간이 기다리고 있어요 😊"
]

# 🧑‍🚀 사용자 별자리 선택
selected_zodiac = st.selectbox("🌟 당신의 별자리를 선택하세요:", list(zodiacs.keys()))

# 🧠 운세 보기 버튼
if st.button("💫 오늘의 운세 보기"):
    today = date.today().strftime("%Y년 %m월 %d일")
    chosen_fortune = random.choice(fortunes)

    st.markdown("### 🗓️ " + today)
    st.markdown(f"### ⭐ {selected_zodiac} ({zodiacs[selected_zodiac]})의 운세는...")
    st.markdown("---")
    st.markdown(f"## {chosen_fortune}")
    st.markdown("---")
    st.balloons()

# 🌌 하단 장식
st.markdown("###### 📍 이 운세는 재미로만 봐주세요. 오늘도 좋은 하루 되세요! 😊")
st.markdown("###### Made with ❤️ using Streamlit & Python")
