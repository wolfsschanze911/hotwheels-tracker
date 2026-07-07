import streamlit as st

from scan_engine import start_scan
from state import scan_state



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

        st.session_state["start_scan"] = True

        st.rerun()



    if st.session_state.get(
        "start_scan",
        False
    ):

        st.session_state["start_scan"] = False

        start_scan()
