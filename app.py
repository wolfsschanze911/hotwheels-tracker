import streamlit as st
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
# DASHBOARD PLACEHOLDER
# ==========================================

dashboard_placeholder = st.empty()



def refresh_dashboard():

    with dashboard_placeholder.container():

        render_dashboard()



# ==========================================
# INITIAL DASHBOARD
# ==========================================

refresh_dashboard()



# ==========================================
# SCAN BUTTON
# ==========================================

if st.button(
    "🚀 SCAN SEMUA TOKO",
    use_container_width=True
):


    def refresh():

        refresh_dashboard()

        time.sleep(0.1)



    start_scan(
        refresh=refresh
    )


    refresh_dashboard()
