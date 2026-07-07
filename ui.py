import streamlit as st


def dashboard(
    total_toko,
    scanned_toko,
    total_produk,
    total_baru,
    total_naik,
    total_turun,
    progress,
    status,
    last_scan,
):

    with st.container(border=True):

        st.markdown("### 🚗 Hot Wheels Tracker")

        st.write(status)

        st.caption(f"🕒 {last_scan}")

        st.write("")

        st.markdown(
            f"""
            **🏪 {scanned_toko}/{total_toko}**
            &nbsp;&nbsp;&nbsp;
            **🚗 {total_produk}**
            &nbsp;&nbsp;&nbsp;
            **🆕 {total_baru}**
            &nbsp;&nbsp;&nbsp;
            **🟢 {total_naik}**
            &nbsp;&nbsp;&nbsp;
            **🔴 {total_turun}**
            """,
            unsafe_allow_html=True,
        )

        st.progress(progress)
