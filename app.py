import time
import streamlit as st

from dashboard import render_dashboard
from scan_button import render_scan_button
from search_ui import render_search
from updates_ui import render_updates

from state import (
    scan_results,
    scan_state
)


# ==================================
# Page Config
# ==================================

st.set_page_config(
    page_title="Hot Wheels Tracker",
    page_icon="🚗",
    layout="centered"
)



# ==================================
# Header
# ==================================

st.markdown(
    """
# 🚗 Hot Wheels Tracker

Monitor stok Hot Wheels secara realtime.
"""
)



# ==================================
# Dashboard
# ==================================

render_dashboard()



st.divider()



# ==================================
# Scan Button
# ==================================

render_scan_button()



st.divider()



# ==================================
# Search
# ==================================

render_search()



st.divider()



# ==================================
# Latest Updates
# ==================================

render_updates(
    scan_results
)



# ==================================
# LIVE REFRESH
# ==================================

if scan_state.get(
    "running",
    False
):

    time.sleep(1)

    st.rerun()
