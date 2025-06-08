import random
import streamlit as st

# --- Affirmations ---
affirmations = [
    "You are doing amazing! 💖",
    "You are enough, just as you are. 🌸",
    "You're a little star in this big universe ✨",
    "You make the world brighter just by being in it 🌞",
    "You’re brave, strong, and so loved 💪🌈",
    "Breathe. You’ve got this. 🌿",
    "You're allowed to rest. You've earned it 💤",
    "Your smile is magic 🧚‍♀️",
    "It's okay to take things one step at a time 🐢",
    "You are a masterpiece in progress 🎨",
]

# --- Cute Styling ---
st.set_page_config(page_title="Cute Affirmation App", page_icon="💌", layout="centered")

cute_css = """
<style>
body {
    background-color: #fff5f9;
    color: #222;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
h1 {
    color: #ff69b4;
    text-align: center;
}
.stButton button {
    background-color: #ffccdd;
    color: black;
    border-radius: 12px;
    font-size: 20px;
    padding: 10px 20px;
    transition: 0.3s;
}
.stButton button:hover {
    background-color: #ffaecb;
    transform: scale(1.05);
}
</style>
"""

st.markdown(cute_css, unsafe_allow_html=True)

# --- App Layout ---
st.markdown("<h1>💌 Daily Affirmation 💌</h1>", unsafe_allow_html=True)
st.markdown("### Click below for a cozy little boost ☕✨")

if st.button("Give me an affirmation! 💖"):
    affirmation = random.choice(affirmations)
    st.success(affirmation)
    st.balloons()
else:
    st.image("https://i.imgur.com/JnPmEZg.png", width=250, caption="(Click the button!)")
