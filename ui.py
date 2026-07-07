import streamlit as st
from datetime import datetime


def dashboard(
    total_toko,
    total_produk,
    total_baru,
    total_naik,
    total_turun,
    status="⚪ Belum Scan",
):

    now = datetime.now().strftime("%d %b %Y • %H:%M")

    with st.container(border=True):

        st.markdown("### 🚗 Hot Wheels Tracker")

        st.caption(status)
        st.caption(f"🕒 {now}")

        st.markdown(
            f"""
            <div style="
                font-size:18px;
                font-weight:600;
                text-align:center;
                padding-top:8px;
            ">
                🏪 {total_toko}
                &nbsp;&nbsp;&nbsp;
                🚗 {total_produk}
                &nbsp;&nbsp;&nbsp;
                🆕 {total_baru}
                &nbsp;&nbsp;&nbsp;
                🟢 {total_naik}
                &nbsp;&nbsp;&nbsp;
                🔴 {total_turun}
            </div>
            """,
            unsafe_allow_html=True,
        )
