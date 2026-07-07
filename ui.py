mport streamlit as st
from datetime import datetime


def dashboard(
    total_toko,
    total_produk,
    total_baru,
    total_naik,
    total_turun,
    status="⚪ Belum Scan",
):

    tanggal = datetime.now().strftime("%d %b %Y")
    jam = datetime.now().strftime("%H:%M")

    with st.container(border=True):

        st.markdown("#### 🚗 Hot Wheels Tracker")

        st.write(status)

        st.caption(f"{tanggal}")
        st.caption(f"{jam}")

        st.divider()

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.markdown(
            f"""
            <div style="text-align:center">
            🏪<br><b>{total_toko}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col2.markdown(
            f"""
            <div style="text-align:center">
            🚗<br><b>{total_produk}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col3.markdown(
            f"""
            <div style="text-align:center">
            🆕<br><b>{total_baru}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col4.markdown(
            f"""
            <div style="text-align:center">
            🟢<br><b>{total_naik}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col5.markdown(
            f"""
            <div style="text-align:center">
            🔴<br><b>{total_turun}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )
