import streamlit as st

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
# BUTTON
# ==========================================

if st.button(
    "🚀 SCAN SEMUA TOKO",
    use_container_width=True
):

    start_scan()

    st.success(
        "✅ Scan selesai"
    )


# ==========================================
# DASHBOARD
# ==========================================

render_dashboard()
