import streamlit as st

from state import scan_state


def render_dashboard():

    progress = scan_state["progress"]

    filled = int(progress / 5)

    bar = (
        "█" * filled
        +
        "░" * (20 - filled)
    )


    st.markdown(
        f"""
        <div style="
            background:#111;
            padding:20px;
            border-radius:15px;
            width:360px;
            color:white;
            font-family:Arial;
        ">

        <div style="
            font-size:22px;
            font-weight:bold;
        ">
        🚗 Hot Wheels Tracker
        </div>


        <br>

         {scan_state["status"]}

        <br>

        🕒 {scan_state["last_scan"]}


        <br><br>


        🏪 {scan_state["stores_done"]}/{scan_state["stores_total"]}
        &nbsp;&nbsp;

        🚗 {scan_state["cars_found"]}
        &nbsp;&nbsp;

        🆕 {scan_state["new_items"]}
        &nbsp;&nbsp;

        🟢 {scan_state["price_down"]}
        &nbsp;&nbsp;

        🔴 {scan_state["price_up"]}


        <br><br>


        <span style="font-size:18px">
        {bar} {progress}%
        </span>


        </div>
        """,

        unsafe_allow_html=True
    )
