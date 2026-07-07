import streamlit as st
from datetime import datetime


def dashboard(
    total_toko,
    total_produk,
    total_baru,
    total_naik,
    total_turun,
    status="🟢 Scan selesai",
):

    last_scan = datetime.now().strftime("%d %b %Y %H:%M:%S")

    with st.container(border=True):

        st.subheader("Hot Wheels Tracker")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Status**")
            st.success(status)

        with col2:
            st.write("**Last Scan**")
            st.info(last_scan)

        st.divider()

        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric("🏪 Toko", total_toko)
        c2.metric("🚗 Produk", total_produk)
        c3.metric("🆕 Baru", total_baru)
        c4.metric("🟢 Naik", total_naik)
        c5.metric("🔴 Turun", total_turun)
