import time
from datetime import datetime, timezone, timedelta

from config import DAFTAR_TOKO
from scanner import scan_store
from compare import compare_stock
from history import load_history, save_history

from state import (
    reset_state,
    update_state,
    scan_state,
    scan_results,
)


# ==========================================
# Helper
# ==========================================

def process_products(products, store_name, history, counters):
    """
    Memproses seluruh produk dari satu toko.
    """

    available_products = [
        p for p in products
        if p.get("stock", 0) > 0
    ]

    store_key = " ".join(store_name.split()).upper()

    for product in available_products:

        product_name = " ".join(
            product.get("productName", "").split()
        ).upper()

        stock = product.get("stock", 0)

        history_key = f"{store_key}_{product_name}"

        status, previous_stock, diff = compare_stock(
            history,
            history_key,
            stock
        )

        history[history_key] = stock

        counters["products"] += 1

        if status == "🆕 Baru":
            counters["new"] += 1

        elif status.startswith("🟢"):
            counters["up"] += 1

        elif status.startswith("🔴"):
            counters["down"] += 1

        scan_results.append({
            "produk": product_name,
            "toko": store_name,
            "stok": stock,
            "harga": product.get("finalPrice", 0),
            "status": status
        })


def refresh_dashboard(refresh):
    if refresh:
        refresh()


# ==========================================
# Main Scan
# ==========================================

def start_scan(refresh=None):

    scan_state["running"] = True

    reset_state()
    scan_results.clear()

    history = load_history()

    total_store = len(DAFTAR_TOKO)

    counters = {
        "products": 0,
        "new": 0,
        "up": 0,
        "down": 0,
    }

    update_state(
        status="🟡 Preparing scan...",
        stores_total=total_store,
        progress=0
    )

    refresh_dashboard(refresh)

    try:

        for index, store in enumerate(DAFTAR_TOKO, start=1):

            store_name = store["nama"]

            update_state(
                status=f"🟡 Scanning {store_name}..."
            )

            refresh_dashboard(refresh)

            try:

                products = scan_store(store)

                process_products(
                    products,
                    store_name,
                    history,
                    counters
                )

            except Exception as e:

                update_state(
                    status=f"⚠️ {store_name} gagal : {e}"
                )

                refresh_dashboard(refresh)

                continue

            progress = int(
                (index / total_store) * 100
            )

            update_state(
                stores_done=index,
                cars_found=counters["products"],
                new_items=counters["new"],
                price_down=counters["up"],
                price_up=counters["down"],
                progress=progress,
            )

            refresh_dashboard(refresh)

            time.sleep(0.2)

        save_history(history)

        update_state(
            status="🟢 Scan selesai",
            progress=100,
            last_scan=datetime.now(
                timezone(
                    timedelta(hours=7)
                )
            ).strftime("%d %b %Y %H:%M WIB")
        )

        refresh_dashboard(refresh)

    finally:

        scan_state["running"] = False
