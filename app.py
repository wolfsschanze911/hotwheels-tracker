import streamlit as st
import threading

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
# CALLBACK SCAN
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



if st.button(
    button_text,
    use_container_width=True,
    disabled=st.session_state.scan_running
):

    st.session_state.scan_running = True


    thread = threading.Thread(
        target=run_scan,
        daemon=True
    )

    thread.start()


    st.rerun()



# ==========================================
# DASHBOARD
# ==========================================

render_dashboard()
