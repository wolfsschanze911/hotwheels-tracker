import streamlit as st
import pandas as pd
from urllib.parse import quote

from config import DAFTAR_TOKO
from history import load_history, save_history
from scanner import scan_store
from compare import compare_stock
from ui import dashboard

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="WOLFSSCHANZE HW PROJECT",
    layout="wide"
)

st.title("WOLFSSCHANZE HW PROJECT")

# ==========================================
# SESSION STATE
# ==========================================

from datetime import datetime

if "dashboard" not in st.session_state:

    st.session_state.dashboard = {
        "status": "⚪ Belum Scan",
        "last_scan": "-",
        "scanned": 0,
        "produk": 0,
        "baru": 0,
        "naik": 0,
        "turun": 0,
        "progress": 0,
    }

# ==========================================
# DASHBOARD
# ==========================================

dashboard(
    total_toko=len(DAFTAR_TOKO),
    total_produk=st.session_state.dashboard["total_produk"],
    total_baru=st.session_state.dashboard["baru"],
    total_naik=st.session_state.dashboard["naik"],
    total_turun=st.session_state.dashboard["turun"],
    status=st.session_state.dashboard["status"],
)

st.divider()

# ==========================================
# BUTTON
# ==========================================

if st.button("🚀 SCAN SEMUA TOKO", use_container_width=True):

    history = load_history()

    total_produk = 0
    total_baru = 0
    total_naik = 0
    total_turun = 0

    progress = st.progress(0)

    for i, toko in enumerate(DAFTAR_TOKO):

        try:

            products = scan_store(toko)

            stok_tersedia = [
                p for p in products
                if p.get("stock", 0) > 0
            ]

            col1, col2 = st.columns([4,1])

            with col1:
                st.subheader(f"📍 {toko['nama']}")

            with col2:
                maps = (
                    "https://www.google.com/maps/search/?api=1&query="
                    + quote("Alfamart " + toko["nama"])
                )

                st.link_button("📍 Maps", maps)

            with st.expander(f"{len(stok_tersedia)} produk tersedia"):

                if not stok_tersedia:
                    st.info("Tidak ada stok.")
                    continue

                rows = []

                for p in stok_tersedia:

                    nama_toko = " ".join(
                        toko["nama"].split()
                    ).upper()

                    nama_produk = " ".join(
                        p.get("productName", "").split()
                    ).upper()

                    current_stock = p.get("stock", 0)

                    key = f"{nama_toko}_{nama_produk}"

                    status, prev_stock, diff = compare_stock(
                        history,
                        key,
                        current_stock,
                    )

                    # Statistik Dashboard
                    total_produk += 1

                    if status == "🆕 Baru":
                        total_baru += 1

                    elif status.startswith("🟢"):
                        total_naik += 1

                    elif status.startswith("🔴"):
                        total_turun += 1

                    rows.append({
                        "Produk": nama_produk,
                        "Stok": current_stock,
                        "Status": status,
                        "Harga": f"Rp {p.get('finalPrice',0):,.0f}"
                    })

                    history[key] = current_stock

                st.dataframe(
                    pd.DataFrame(rows),
                    use_container_width=True,
                    hide_index=True,
                )

        except Exception as e:
            st.error(f"{toko['nama']} : {e}")

        progress.progress((i + 1) / len(DAFTAR_TOKO))

    save_history(history)

    # =====================================
    # UPDATE DASHBOARD
    # =====================================

    st.session_state.dashboard = {
        "status": "🟢 Scan selesai",
        "total_produk": total_produk,
        "baru": total_baru,
        "naik": total_naik,
        "turun": total_turun,
    }

    st.success("✅ Scan selesai")

    st.session_state.dashboard = {...}

    st.session_state.scan_result = [...]
