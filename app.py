import streamlit as st
import threading
import time

from dashboard import render_dashboard
from scan_engine import start_scan
from state import scan_state


st.set_page_config(
    page_title="Hot Wheels Tracker",
    layout="centered"
)


st.title("WOLFSSCHANZE HW PROJECT")



# ==============================
# BUTTON
# ==============================

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



# ==============================
# DASHBOARD LOOP
# ==============================

placeholder = st.empty()


while scan_state["running"]:

    with placeholder.container():

        render_dashboard()

    time.sleep(1)


with placeholder.container():

    render_dashboard()
