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
# SCAN THREAD
# ==========================================

def run_scan():

    start_scan()

    st.session_state.scan_running = False



# ==========================================
# BUTTON
# ==========================================

if st.session_state.scan_running:

    button_text = "⏳ SCANNING..."

else:

    button_text = "🚀 SCAN SEMUA TOKO"



clicked = st.button(
    button_text,
    use_container_width=True,
    disabled=st.session_state.scan_running
)



if clicked:

    st.session_state.scan_running = True


    thread = threading.Thread(
        target=run_scan,
        daemon=True
    )

    thread.start()


    time.sleep(0.1)

    st.rerun()



# ==========================================
# DASHBOARD REFRESH
# ==========================================

placeholder = st.empty()


if st.session_state.scan_running:

    while st.session_state.scan_running:

        with placeholder.container():

            render_dashboard()

        time.sleep(1)


else:

    with placeholder.container():

        render_dashboard()
