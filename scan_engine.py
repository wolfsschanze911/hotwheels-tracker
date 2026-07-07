import time
from datetime import datetime

from config import DAFTAR_TOKO
from scanner import scan_store
from compare import compare_stock
from history import load_history, save_history

from state import (
    reset_state,
    update_state
)


def start_scan():

    reset_state()

    history = load_history()

    total_produk = 0
    total_baru = 0
    total_naik = 0
    total_turun = 0

    total_toko = len(DAFTAR_TOKO)


    update_state(
        status="🟡 Preparing scan...",
        stores_total=total_toko
    )


    for i, toko in enumerate(DAFTAR_TOKO):

        try:
            nama_toko = toko["nama"]
            update_state(
                status=f"🟡 Scanning {nama_toko}..."
            )
            products = scan_store(toko)
            stok_tersedia = [
                p for p in products
                if p.get("stock", 0) > 0
            ]


            for p in stok_tersedia:

                nama_produk = " ".join(
                    p.get("productName", "").split()
                ).upper()

                nama_toko_clean = " ".join(
                    nama_toko.split()
                ).upper()

                current_stock = p.get(
                    "stock",
                    0
                )
                
                key = (
                    f"{nama_toko_clean}_"
                    f"{nama_produk}"
                )

                status, prev_stock, diff = compare_stock(
                    history,
                    key,
                    current_stock
                )

                total_produk += 1
                if status == "🆕 Baru":
                    total_baru += 1
                elif status.startswith("🟢"):
                    total_naik += 1
                elif status.startswith("🔴"):
                    total_turun += 1
                history[key] = current_stock



            update_state(
                stores_done=i + 1,
                cars_found=total_produk,
                new_items=total_baru,
                price_down=total_naik,
                price_up=total_turun,
                progress=int(
                    ((i + 1) / total_toko) * 100
                )
            )


        except Exception as e:
            update_state(
                status=f"⚠️ Error {nama_toko}"
            )
        time.sleep(0.5)


    save_history(history)

    update_state(

        status="🟢 Scan selesai",
        last_scan=datetime.now(
            timezone(timedelta(hours=7))
        )
        .strftime("%d %b %Y %H:%M WIB"),
    )

    return True
