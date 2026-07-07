import streamlit as st
from scan_engine import start_scan
from state import scan_state


def render_scan_button(refresh=None):

    if scan_state["running"]:
        text = "⏳ SCANNING..."
        disabled = True
    else:
        text = "🚀 SCAN SEMUA TOKO"
        disabled = False

    if st.button(
        text,
        use_container_width=True,
        disabled=disabled
    ):
        start_scan(refresh=refresh)
