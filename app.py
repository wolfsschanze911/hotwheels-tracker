import streamlit as st
import threading

from dashboard import render_dashboard
from scan_engine import start_scan
from state import scan_state


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
# BUTTON STATUS
# ==========================================

status = scan_state["status"]
if status.startswith("🟡"):
    button_text = "⏳ SCANNING..."
else:
    button_text = "🚀 SCAN SEMUA TOKO"

# ==========================================
# BUTTON
# ==========================================

if st.button(
    button_text,
    use_container_width=True,
    disabled=status.startswith("🟡")
):

    thread = threading.Thread(
        target=start_scan,
        daemon=True
    )

    thread.start()
    st.rerun()

# ==========================================
# DASHBOARD
# ==========================================

render_dashboard()
