import streamlit as st
from state import scan_state

def render_dashboard():
    with st.container(border=True):

        st.markdown(
            """
            <style>
            .hw-title {
                font-size: 20px;
                font-weight: 700;
                margin-bottom: 2px;
            }

            .hw-status {
                font-size: 15px;
                margin: 0;
            }

            .hw-info {
                font-size: 13px;
                margin-top: 2px;
            }

            .hw-stat {
                font-size: 14px;
                margin-top: 6px;
            }

            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="hw-title">
            🚗 Hot Wheels Tracker
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="hw-status">
            {scan_state["status"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="hw-info">
            🕒 {scan_state["last_scan"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="hw-stat">
            🏪 {scan_state["stores_done"]}/{scan_state["stores_total"]}
            &nbsp;&nbsp;
            🚗 {scan_state["cars_found"]}
            &nbsp;&nbsp;
            🆕 {scan_state["new_items"]}
            &nbsp;&nbsp;
            🟢 {scan_state["price_down"]}
            &nbsp;&nbsp;
            🔴 {scan_state["price_up"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(
            scan_state["progress"] / 100
        )
