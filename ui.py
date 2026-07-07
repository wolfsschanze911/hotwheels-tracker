import streamlit as st
from datetime import datetime


def dashboard_card(
    total_toko,
    total_produk,
    total_baru,
    total_naik,
    total_turun,
    status="🟢 Scan selesai",
):
    last_scan = datetime.now().strftime("%d %b %Y • %H:%M:%S")

    st.markdown(
        f"""
        <div style="
            border:1px solid #E5E7EB;
            border-radius:16px;
            padding:18px;
            margin-bottom:20px;
            background:#FFFFFF;
            box-shadow:0 2px 8px rgba(0,0,0,.05);
        ">

            <div style="
                font-size:22px;
                font-weight:700;
                margin-bottom:12px;
            ">
                🚗 Hot Wheels Tracker
            </div>

            <div style="font-size:14px; margin-bottom:4px;">
                <b>Status :</b> {status}
            </div>

            <div style="
                font-size:13px;
                color:#666666;
                margin-bottom:12px;
            ">
                🕒 Last Scan : {last_scan}
            </div>

            <hr style="border:none;border-top:1px solid #EEEEEE;">

            <div style="
                display:flex;
                justify-content:space-between;
                flex-wrap:wrap;
                gap:10px;
                margin-top:12px;
            ">

                <div style="text-align:center;min-width:70px;">
                    <div style="font-size:22px;font-weight:bold;">🏪</div>
                    <div style="font-size:20px;font-weight:bold;">{total_toko}</div>
                    <div style="font-size:12px;color:#666;">Toko</div>
                </div>

                <div style="text-align:center;min-width:70px;">
                    <div style="font-size:22px;font-weight:bold;">🚗</div>
                    <div style="font-size:20px;font-weight:bold;">{total_produk}</div>
                    <div style="font-size:12px;color:#666;">Produk</div>
                </div>

                <div style="text-align:center;min-width:70px;">
                    <div style="font-size:22px;font-weight:bold;">🆕</div>
                    <div style="font-size:20px;font-weight:bold;">{total_baru}</div>
                    <div style="font-size:12px;color:#666;">Baru</div>
                </div>

                <div style="text-align:center;min-width:70px;">
                    <div style="font-size:22px;font-weight:bold;">🟢</div>
                    <div style="font-size:20px;font-weight:bold;">{total_naik}</div>
                    <div style="font-size:12px;color:#666;">Naik</div>
                </div>

                <div style="text-align:center;min-width:70px;">
                    <div style="font-size:22px;font-weight:bold;">🔴</div>
                    <div style="font-size:20px;font-weight:bold;">{total_turun}</div>
                    <div style="font-size:12px;color:#666;">Turun</div>
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
