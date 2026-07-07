import streamlit as st

from state import scan_state


def render_dashboard():

    st.markdown("## 📊 Dashboard")


    # ==========================
    # Status Scan
    # ==========================

    status = scan_state.get(
        "status",
        "⚪ Menunggu scan..."
    )

    st.info(status)



    # ==========================
    # Progress
    # ==========================

    progress = scan_state.get(
        "progress",
        0
    )

    st.progress(
        progress / 100
    )

    st.caption(
        f"Progress scan : {progress}%"
    )



    # ==========================
    # Statistik
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🏪 Toko",
            f'{scan_state.get("stores_done",0)} / {scan_state.get("stores_total",0)}'
        )


    with col2:

        st.metric(
            "🚗 Produk",
            scan_state.get(
                "cars_found",
                0
            )
        )


    with col3:

        st.metric(
            "🆕 Baru",
            scan_state.get(
                "new_items",
                0
            )
        )



    col4, col5 = st.columns(2)


    with col4:

        st.metric(
            "🟢 Stok Naik",
            scan_state.get(
                "price_down",
                0
            )
        )


    with col5:

        st.metric(
            "🔴 Stok Turun",
            scan_state.get(
                "price_up",
                0
            )
        )



    # ==========================
    # Last Scan
    # ==========================

    last_scan = scan_state.get(
        "last_scan",
        "-"
    )


    st.caption(
        f"🕒 Last scan : {last_scan}"
    )
