print("UI.PY LOADED")
import streamlit as st
from datetime import datetime


def dashboard(total_toko, total_produk, baru, naik, turun):

    html = f"""
    <div style="
        background:#1d1f24;
        padding:18px;
        border-radius:12px;
        border:1px solid #333;
        margin-bottom:20px;
    ">

        <div style="font-size:22px;font-weight:bold;">
            🚗 Hot Wheels Tracker
        </div>

        <div style="margin-top:8px;">
            🟢 <b>Status :</b> Scan selesai
        </div>

        <div style="font-size:13px;color:#999;">
            🕒 Terakhir scan<br>
            {datetime.now().strftime("%d %b %Y • %H:%M:%S")}
        </div>

        <hr>

        <div style="
            display:flex;
            justify-content:space-between;
            flex-wrap:wrap;
            gap:8px;
        ">
            <div>🏪 <b>{total_toko}</b> Toko</div>
            <div>🚗 <b>{total_produk}</b> Produk</div>
            <div>🆕 <b>{baru}</b> Baru</div>
            <div>🟢 <b>{naik}</b> Naik</div>
            <div>🔴 <b>{turun}</b> Turun</div>
        </div>

    </div>
    """

    st.markdown(html, unsafe_allow_html=True)
