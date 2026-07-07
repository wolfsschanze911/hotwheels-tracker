import streamlit as st

from scan_engine import start_scan
from state import scan_state


def render_scan_button():

    st.markdown("## 🔍 Scanner")


    is_running = scan_state.get(
        "running",
        False
    )


    if is_running:

        st.warning(
            "🟡 Scan sedang berjalan..."
        )

        return



    if st.button(
        "🚗 Mulai Scan",
        use_container_width=True
    ):

        start_scan(
            refresh=st.rerun
        )
