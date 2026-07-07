import streamlit as st

from dashboard import render_dashboard
from scan_button import render_scan_button
from search_ui import render_search
from updates_ui import render_updates

from state import scan_results


# =====================================
# Page Config
# =====================================

st.set_page_config(
    page_title="Hot Wheels Scanner",
    page_icon="🚗",
    layout="wide"
)



# =====================================
# Header
# =====================================

st.title("🚗 Hot Wheels Stock Scanner")

st.caption(
    "Monitoring stok dan perubahan Hot Wheels secara realtime"
)



# =====================================
# Scan Control
# =====================================

render_scan_button()



st.divider()



# =====================================
# Dashboard
# =====================================

render_dashboard()



st.divider()



# =====================================
# Search
# =====================================

render_search()



st.divider()



# =====================================
# Updates
# =====================================

render_updates(
    scan_results
)
