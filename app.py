import streamlit as st
import threading
import time

from dashboard import render_dashboard
from scan_engine import start_scan

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
# SESSION STATE
# ==========================================

if "scan_running" not in st.session_state:
    st.session_state.scan_running = False

# ==========================================
# HANDLE SCAN FINISH
# ==========================================

if st.session_state.scan_finished:
    st.session_state.scan_running = False
    st.session_state.scan_finished = False


# ==========================================
# BUTTON
# ==========================================

from state import scan_state

if scan_state["status"].startswith("🟡"):
    button_text = "⏳ TUNGGU...."
else:
    button_text = "🚀 SCAN SEMUA TOKO"

if st.button(
    button_text,
    use_container_width=True,
    disabled=scan_state["status"].startswith("🟡")
):

    def run_scan():
        start_scan()

    thread = threading.Thread(
        target=run_scan,
        daemon=True
    )

    thread.start()
    st.rerun()

# ==========================================
# DASHBOARD LIVE
# ==========================================

dashboard_placeholder = st.empty()
while True:
    with dashboard_placeholder.container():
        render_dashboard()
    time.sleep(1)
    st.rerun()
