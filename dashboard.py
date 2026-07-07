import streamlit as st

from state import scan_state


def render_dashboard():

    status = scan_state.get(
        "status",
        "⚪ Menunggu scan..."
    )

    last_scan = scan_state.get(
        "last_scan",
        "-"
    )

    stores_done = scan_state.get(
        "stores_done",
        0
    )

    stores_total = scan_state.get(
        "stores_total",
        0
    )

    products = scan_state.get(
        "cars_found",
        0
    )

    new_items = scan_state.get(
        "new_items",
        0
    )

    stock_up = scan_state.get(
        "price_down",
        0
    )

    stock_down = scan_state.get(
        "price_up",
        0
    )

    progress = scan_state.get(
        "progress",
        0
    )


    # ==========================
    # Compact Dashboard
    # ==========================

    with st.container(border=True):

        st.markdown(
            """
            ### 🚗 Hot Wheels Tracker
            """
        )


        st.markdown(
            f"""
            {status}

            🕒 {last_scan}
            """
        )


        st.markdown(
            f"""
            🏪 {stores_done}/{stores_total}
            &nbsp;&nbsp;
            🚗 {products}
            &nbsp;&nbsp;
            🆕 {new_items}
            &nbsp;&nbsp;
            🟢 {stock_up}
            &nbsp;&nbsp;
            🔴 {stock_down}
            """,
            unsafe_allow_html=True
        )


        st.progress(
            progress / 100
        )


        st.caption(
            f"{progress}%"
        )
