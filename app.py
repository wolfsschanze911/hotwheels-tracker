import streamlit as st

from dashboard import render_dashboard
from scan_button import render_scan_button

# nanti
# from search_ui import render_search
# from updates_ui import render_updates

st.set_page_config(
    page_title="Hot Wheels Tracker",
    layout="centered"
)

st.title("WOLFSSCHANZE HW PROJECT")

# Dashboard
render_dashboard()

# Tombol Scan
render_scan_button()

st.divider()

# Placeholder Search
st.subheader("🔎 Search Hot Wheels")

st.text_input(
    "",
    placeholder="Cari seri Hot Wheels...",
    label_visibility="collapsed"
)

st.divider()

# Placeholder Update
st.subheader("📢 Update Terbaru")

st.info("Belum ada update.")
