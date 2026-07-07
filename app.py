import streamlit as st
import threading

from dashboard import render_dashboard
from scan_engine import start_scan
from state import scan_state


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Hot Wheels Tracker",
    layout="centered"
)


# ==========================================
# TITLE
# ==========================================

st.title("WOLFSSCHANZE HW PROJECT")


# ==========================================
# BUTTON
# ==========================================

if scan_state["running"]:
    button_text = "⏳ SCANNING..."
else:
    button_text = "🚀 SCAN SEMUA TOKO"
if st.button(
    button_text,
    use_container_width=True,
    disabled=scan_state["running"]
):
    thread = threading.Thread(
        target=start_scan,
        daemon=True
    )
    
    thread.start()

# ==========================================
# DASHBOARD
# ==========================================

render_dashboard()
