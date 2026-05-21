import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

st.set_page_config(
    page_title="Nikk's AI",
    page_icon="✨",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    box-sizing: border-box;
}

.stApp {
    background: #080c14;
    color: #dce6f5;
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding-top: 2.2rem !important;
    padding-bottom: 5rem !important;
    max-width: 800px !important;
}

.app-header {
    text-align: center;
    margin-bottom: 2rem;
}

.app-title {
    font-size: 2.6rem;
    font-weight: 600;
    letter-spacing: -0.5px;
    color: #dce6f5;
    margin: 0 0 6px;
}

.app-title .accent {
    background: linear-gradient(90deg, #4f9eff, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.app-subtitle {
    color: #5a6a85;
    font-size: 0.88rem;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #1e2d47, transparent);
    margin: 0 0 1.8rem;
}

[data-testid="stChatMessage"] {
    padding: 14px 18px;
    border-radius: 14px;
    margin-bottom: 10px;
    transition: box-shadow 0.2s;
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background: #0e1e36;
    border: 1px solid #1e3a5f;
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background: #0b1120;
    border: 1px solid #131f33;
}

[data-testid="stChatMessage"]:hover {
    box-shadow: 0 2px 16px rgba(79, 158, 255, 0.07);
}

[data-testid="stMarkdownContainer"] p {
    color: #c9d9f0 !important;
    font-size: 15px;
    line-height: 1.7;
}

[data-testid="stMarkdownContainer"] li {
    color: #c9d9f0 !important;
    font-size: 15px;
    line-height: 1.7;
}

[data-testid="stMarkdownContainer"] strong {
    color: #dce6f5 !important;
    font-weight: 500;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: #7fb3ff !important;
    font-weight: 500;
}

[data-testid="stMarkdownContainer"] code {
    background: #0e1e36 !important;
    color: #7fb3ff !important;
    border-radius: 5px;
    padding: 1px 5px;
    font-size: 13px;
}

.stChatInputContainer {
    background: #080c14 !important;
    border-top: 1px solid #131f33 !important;
    padding: 12px 0 !important;
}

div[data-testid="stChatInput"] {
    background: #080c14 !important;
}

textarea {
    background: #0e1b2e !important;
    color: #dce6f5 !important;
    border: 1px solid #1e3355 !important;
    border-radius: 12px !important;
    font-size: 15px !important;
    padding: 13px 16px !important;
    caret-color: #4f9eff;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}

textarea::placeholder {
    color: #3d536e !important;
}

textarea:focus {
    border-color: #2d5fa6 !important;
    box-shadow: 0 0 0 3px rgba(79, 158, 255, 0.12) !important;
    outline: none !important;
}

button[kind="primary"] {
    background: linear-gradient(135deg, #1a4f9c, #3b3bb8) !important;
    border: none !important;
    border-radius: 10px !important;
    color: white !important;
    transition: opacity 0.2s, transform 0.1s !important;
}

button[kind="primary"]:hover {
    opacity: 0.88 !important;
    transform: scale(1.04) !important;
}

[data-testid="stSidebar"] {
    background: #060a10 !important;
    border-right: 1px solid #111d2e !important;
}

[data-testid="stSidebar"] > div {
    padding: 1.6rem 1.2rem !important;
}

.sidebar-logo {
    font-size: 1.1rem;
    font-weight: 600;
    color: #7fb3ff;
    margin-bottom: 1.6rem;
    display: flex;
    align-items: center;
    gap: 8px;
}

.sidebar-section-label {
    font-size: 0.7rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #3d536e;
    margin: 1.4rem 0 0.5rem;
}

.sidebar-value {
    font-size: 0.9rem;
    color: #8ab4e0;
    font-weight: 400;
}

.sidebar-badge {
    display: inline-block;
    background: #0e1e36;
    border: 1px solid #1e3a5f;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.8rem;
    color: #4f9eff;
    margin-top: 4px;
}

.sidebar-divider {
    height: 1px;
    background: #111d2e;
    margin: 1.4rem 0;
}

.sidebar-stat {
    font-size: 0.82rem;
    color: #3d536e;
    margin-top: 0.5rem;
}

.sidebar-stat span {
    color: #5a7fa8;
    font-weight: 500;
}

.stButton > button {
    width: 100%;
    background: #0e1b2e !important;
    color: #8ab4e0 !important;
    border: 1px solid #1e3355 !important;
    border-radius: 10px !important;
    padding: 0.55rem 1rem !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.3px;
    transition: all 0.2s !important;
}

.stButton > button:hover {
    background: #142236 !important;
    border-color: #2d5fa6 !important;
    color: #7fb3ff !important;
}

/* Style the selectbox to match theme */
[data-testid="stSelectbox"] > div > div {
    background: #0e1b2e !important;
    border: 1px solid #1e3355 !important;
    border-radius: 10px !important;
    color: #dce6f5 !important;
}

[data-testid="stSelectbox"] label {
    color: #3d536e !important;
    font-size: 0.7rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1.2px !important;
}

[data-testid="stSpinner"] > div {
    border-color: #4f9eff transparent transparent transparent !important;
}

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: #1a2d47;
    border-radius: 6px;
}
::-webkit-scrollbar-thumb:hover { background: #274060; }
</style>
""", unsafe_allow_html=True)


# ── Mood → System Prompt mapping ──────────────────────────────────────────── #
def get_system_prompt(mood):
    if mood == "😊 Happy":
        return (
            "You are a cheerful, enthusiastic, and upbeat assistant. "
            "You respond with warmth, positivity, and encouragement. "
            "Use friendly language, celebrate the user's questions, and always end on a bright note."
        )
    elif mood == "😢 Sad":
        return (
            "You are a melancholic, soft-spoken assistant. "
            "You respond in a gentle, somber, and reflective tone. "
            "You tend to be empathetic but a little heavy-hearted in your replies."
        )
    elif mood == "😠 Angry":
        return (
            "You are a blunt, irritable, and impatient assistant. "
            "You respond with short, direct, and slightly frustrated answers. "
            "You still provide accurate information, but your tone is harsh and no-nonsense."
        )
    elif mood == "😂 Funny":
        return (
            "You are a witty, humorous, and sarcastic assistant. "
            "You crack jokes, use puns, and keep things light-hearted while still being helpful. "
            "Sprinkle in humor naturally throughout your responses."
        )
    elif mood == "🧊 Cold & Formal":
        return (
            "You are an extremely professional, formal, and emotionless assistant. "
            "You respond with precision, use formal language, avoid small talk, "
            "and stick strictly to facts with zero personality."
        )
    else:
        return "You are a helpful assistant that helps answer questions and solve problems."


# ── Session state init ────────────────────────────────────────────────────── #
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = "😊 Happy"

# ── Sidebar ───────────────────────────────────────────────────────────────── #
with st.sidebar:
    st.markdown('<div class="sidebar-logo">✨ Nikk\'s AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-label">Model</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-value">Mistral Small 2506</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-label">Temperature</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-badge">0.9 — Creative</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # ── Mood selector ── #
    mood_options = ["😊 Happy", "😢 Sad", "😠 Angry", "😂 Funny", "🧊 Cold & Formal"]

    selected_mood = st.selectbox(
        "AI Personality Mood",
        options=mood_options,
        index=mood_options.index(st.session_state.selected_mood)
    )

    # If mood changed, reset the conversation with new system prompt
    if selected_mood != st.session_state.selected_mood:
        st.session_state.selected_mood = selected_mood
        st.session_state.messages = []
        st.rerun()

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-label">Context</div>', unsafe_allow_html=True)
    msg_count = len([m for m in st.session_state.messages if isinstance(m, (HumanMessage, AIMessage))])
    st.markdown(
        f'<div class="sidebar-stat"><span>{msg_count}</span> message(s) in session</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    if st.button("🗑  Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# ── Build system prompt from current mood ─────────────────────────────────── #
system_prompt = SystemMessage(content=get_system_prompt(st.session_state.selected_mood))

# ── Header ────────────────────────────────────────────────────────────────── #
st.markdown("""
<div class="app-header">
    <div class="app-title">Nikk's <span class="accent">AI</span> ✨</div>
    <div class="app-subtitle">Powered by Mistral · Intelligent · Conversational</div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ── Model ─────────────────────────────────────────────────────────────────── #
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

# ── Render chat history ───────────────────────────────────────────────────── #
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# ── Input ─────────────────────────────────────────────────────────────────── #
prompt = st.chat_input("Ask me anything...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Build full message list: system prompt + conversation history
    full_messages = [system_prompt] + st.session_state.messages

    with st.chat_message("assistant"):
        with st.spinner(""):
            response = model.invoke(full_messages)
        st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))
    