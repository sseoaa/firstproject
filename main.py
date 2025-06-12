import streamlit as st
import random

# 🎨 페이지 꾸미기
st.set_page_config(page_title="가위✌️바위✊보🖐️ 게임", page_icon="🎮", layout="centered")

st.markdown("# 🎮 가위✌️바위✊보🖐️ 챌린지!")
st.markdown("### 🤖 컴퓨터와 맞붙는 스릴 넘치는 한 판!")
st.markdown("---")

# 🎨 이모지 딕셔너리
emoji_map = {
    "가위": "✌️",
    "바위": "✊",
    "보": "🖐️"
}

# 🧍‍♂️ 사용자 선택
user_choice = st.radio("👉 당신의 선택은?", ("가위", "바위", "보"), horizontal=True)

# 🧠 컴퓨터 선택
computer_choice = random.choice(["가위", "바위", "보"])

# 🥊 승부 로직
def get_result(user, computer):
    if user == computer:
        return "😲 비겼습니다!"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "🎉 당신이 이겼어요! 대단해요! 💪"
    else:
        return "😭 아쉽게도 졌네요... 다시 도전!"

# 🎮 게임 실행 버튼
if st.button("🔥 한 판 승부!"):
    st.markdown(f"### 🧍‍♂️ 당신: {emoji_map[user_choice]} **{user_choice}**")
    st.markdown(f"### 🖥️ 컴퓨터: {emoji_map[computer_choice]} **{computer_choice}**")
    st.markdown("---")
    result = get_result(user_choice, computer_choice)
    st.markdown(f"## {result}")

# 📌 하단 노트
st.markdown("---")
st.markdown("🔁 언제든 다시 도전해보세요!")
st.markdown("📱 모바일에서도 완벽하게 작동합니다. 즐거운 게임 되세요! ✨")
