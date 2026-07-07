import streamlit as st
import pandas as pd

from urllib.parse import quote

from config import DAFTAR_TOKO
from history import load_history, save_history
from scanner import scan_store
from compare import compare_stock
from ui import dashboard

st.set_page_config(
    page_title="Hot Wheels Tracker",
    layout="wide"
)

st.title("🚗 Alfagift Hotwheels Live Tracker")

with st.container(border=True):
    st.subheader("🚗 Hot Wheels Tracker")

    col1, col2 = st.columns(2)
    col1.write("🟢 Status")
    col1.success("Scan selesai")

    col2.write("🕒 Last Scan")
    col2.info(last_scan)

    st.divider()

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("🏪 Toko", total_toko)
    c2.metric("🚗 Produk", total_produk)
    c3.metric("🆕 Baru", baru)
    c4.metric("🟢 Naik", naik)
    c5.metric("🔴 Turun", turun)

if st.button("SCAN SEMUA TOKO"):

    history = load_history()

    progress_bar = st.progress(0)

    for i, toko in enumerate(DAFTAR_TOKO):

        try:

            products = scan_store(toko)

            stok_tersedia = [
                p for p in products
                if p.get("stock", 0) > 0
            ]

            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader(f"📍 {toko['nama']}")

            with col2:

                url_maps = (
                    "https://www.google.com/maps/search/?api=1&query="
                    + quote("Alfamart " + toko["nama"])
                )

                st.link_button(
                    "📍 Maps",
                    url=url_maps,
                )

            with st.expander(
                f"Lihat stok ({len(stok_tersedia)} item ditemukan)"
            ):

                if stok_tersedia:

                    list_data = []

                    for p in stok_tersedia:

                        nama_produk = p.get("productName", "N/A")
                        current_stock = p.get("stock", 0)

                        nama_toko = " ".join(toko["nama"].split()).upper()
                        nama_produk = " ".join(
                            p.get("productName", "N/A").split()
                        ).upper()

                        key = f"{nama_toko}_{nama_produk}"

                        status, prev_stock, diff = compare_stock(
                            history,
                            key,
                            current_stock,
                        )

                        list_data.append(
                            {
                                "Produk": nama_produk,
                                "Stok": current_stock,
                                "Status": status,
                                "Harga": f"Rp {p.get('finalPrice', 0):,.0f}",
                            }
                        )

                        history[key] = current_stock

                    st.table(pd.DataFrame(list_data))

                else:
                    st.write("Stok kosong.")

        except Exception as e:

            st.error(f"Error di {toko['nama']}: {e}")

        progress_bar.progress((i + 1) / len(DAFTAR_TOKO))

    save_history(history)
    dashboard_card(
        total_toko=len(DAFTAR_TOKO),
        total_produk=total_produk,
        total_baru=total_baru,
        total_naik=total_naik,
        total_turun=total_turun,
        status="🟢 Scan selesai",
    )

    st.success("✅ Scan selesai! Data stok terbaru telah disimpan.")
