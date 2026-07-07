import streamlit as st
import time

from dashboard import render_dashboard
from scan_engine import start_scan


st.set_page_config(
    page_title="Hot Wheels Tracker",
    layout="centered"
)


st.title("WOLFSSCHANZE HW PROJECT")


dashboard_placeholder = st.empty()



def refresh_dashboard():

    with dashboard_placeholder.container():

        render_dashboard()



# tampil awal
refresh_dashboard()



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

