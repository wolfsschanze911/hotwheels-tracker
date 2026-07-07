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



# ==========================================
# DASHBOARD AREA
# ==========================================

dashboard_placeholder = st.empty()



# ==========================================
# BUTTON
# ==========================================

if st.button(
    "🚀 SCAN SEMUA TOKO",
    use_container_width=True
):

    if not st.session_state.scan_running:


        st.session_state.scan_running = True


        thread = threading.Thread(
            target=start_scan
        )

        thread.start()



# ==========================================
# LIVE UPDATE
# ==========================================

while True:


    with dashboard_placeholder.container():

        render_dashboard()


    time.sleep(1)
