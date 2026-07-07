import streamlit as st
import threading

from scan_engine import start_scan
from state import scan_state


def run_scan():

    start_scan()



def render_scan_button():

    running = scan_state.get(
        "running",
        False
    )


    if running:

        st.button(
            "🟡 Scan berjalan...",
            disabled=True,
            use_container_width=True
        )

        return



    if st.button(
        "🚗 Mulai Scan",
        use_container_width=True
    ):


        thread = threading.Thread(
            target=run_scan,
            daemon=True
        )


        thread.start()


        st.rerun()
