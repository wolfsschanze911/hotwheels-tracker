import streamlit as st
def render_dashboard():
    from state import scan_state
    with st.container(border=True):

        st.markdown(
            """
            <div style="
                padding:0px;
                margin:0px;
                line-height:1.1;
            ">
            <h3 style="margin:0;">
            🚗 Hot Wheels Tracker
            </h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                margin-top:4px;
                font-size:16px;
            ">
            {scan_state["status"]}
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div style="
                font-size:13px;
                margin-top:2px;
            ">
            🕒 {scan_state["last_scan"]}
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div style="
                margin-top:8px;
                font-size:15px;
            ">
            🏪 {scan_state.get("stores_done",0)}/
            {scan_state.get("stores_total",0)}
            &nbsp;&nbsp;
            🚗 {scan_state.get("cars_found",0)}
            &nbsp;&nbsp;
            🆕 {scan_state.get("new_items",0)}
            &nbsp;&nbsp;
            🟢 {scan_state.get("price_down",0)}
            &nbsp;&nbsp;
            🔴 {scan_state.get("price_up",0)}
            </div>
            """,
            unsafe_allow_html=True
        )


        st.progress(
            scan_state.get("progress",0) / 100
        )
