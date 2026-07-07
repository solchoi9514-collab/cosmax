import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="쿠션 인사이트",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit 기본 패딩 제거
st.markdown("""
<style>
.block-container { padding: 0 !important; max-width: 100% !important; }
header[data-testid="stHeader"] { display: none; }
.stApp > header { display: none; }
iframe { border: none; }
</style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1200, scrolling=True)
