import time

from datetime import datetime, timezone, timedelta

from config import DAFTAR_TOKO

from scanner import scan_store

from compare import compare_stock

from history import (
    load_history,
    save_history
)

from state import (
    start_scan_state,
    finish_scan_state,
    update_state,
    scan_results,
    add_update
)



# ==========================================
# Process Product
# ==========================================

def process_products(
    products,
    store_name,
    history,
    counters
):

    available_products = [

        p for p in products

        if p.get(
            "stock",
            0
        ) > 0

    ]


    store_key = " ".join(
        store_name.split()
    ).upper()



    for product in available_products:


        product_name = " ".join(

            product.get(
                "productName",
                ""
            ).split()

        ).upper()



        stock = product.get(
            "stock",
            0
        )



        key = (
            f"{store_key}_{product_name}"
        )



        status, prev, diff = compare_stock(

            history,

            key,

            stock

        )



        history[key] = stock



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

            "harga": product.get(
                "finalPrice",
                0
            ),

            "status": status

        })
# ==============================
# Live Update Feed
# ==============================

        if status != "➖ Tetap":

            add_update({

                "produk": product_name,

                "toko": store_name,

                "stok": stock,

                "harga": product.get(
                    "finalPrice",
                    0
                ),

                "status": status

            })



# ==========================================
# MAIN SCAN
# ==========================================

def start_scan():


    total_store = len(
        DAFTAR_TOKO
    )


    start_scan_state(
        total_store
    )



    history = load_history()



    counters = {

        "products": 0,

        "new": 0,

        "up": 0,

        "down": 0

    }



    try:


        for index, store in enumerate(
            DAFTAR_TOKO,
            start=1
        ):


            store_name = store["nama"]



            update_state(

                status=f"🟡 Scanning {store_name}",

                stores_done=index - 1,

                progress=int(

                    ((index - 1)
                     /
                     total_store)
                    *
                    100

                )

            )



            products = scan_store(
                store
            )



            process_products(

                products,

                store_name,

                history,

                counters

            )



            update_state(

                stores_done=index,

                cars_found=counters["products"],

                new_items=counters["new"],

                price_down=counters["up"],

                price_up=counters["down"],

                progress=int(

                    (index / total_store)
                    *
                    100

                )

            )



            time.sleep(
                0.2
            )



        save_history(
            history
        )



        finish_scan_state(

            datetime.now(

                timezone(

                    timedelta(hours=7)

                )

            ).strftime(
                "%d %b %Y %H:%M WIB"
            )

        )



    except Exception as e:


        update_state(

            status=f"❌ Scan gagal: {e}"

        )



        raise


