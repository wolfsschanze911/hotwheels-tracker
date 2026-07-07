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

st.title("🚗 Hot Wheels Tracker")

# ==========================================
# SESSION STATE
# ==========================================

if "scan_running" not in st.session_state:
    st.session_state.scan_running = False

if "scan_finished" not in st.session_state:
    st.session_state.scan_finished = False


# ==========================================
# HANDLE SCAN FINISH
# ==========================================

if st.session_state.scan_finished:
    st.session_state.scan_running = False
    st.session_state.scan_finished = False


# ==========================================
# BUTTON
# ==========================================

if st.session_state.scan_running:
    button_text = "⏳ SCANNING..."
else:
    button_text = "🚀 SCAN SEMUA TOKO"

if st.button(
    button_text,
    use_container_width=True,
    disabled=st.session_state.scan_running
):
    st.session_state.scan_running = True


    def run_scan():
        start_scan()
        st.session_state.scan_finished = True

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
