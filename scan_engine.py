import time
from datetime import datetime

from state import (
    scan_state,
    reset_state,
    update_state
)


def start_scan():

    reset_state()

    total_store = scan_state["stores_total"]


    for store in range(1, total_store + 1):

        update_state(
            status=f"Scanning store {store}/{total_store}"
        )


        time.sleep(1)


        update_state(

            stores_done=store,

            cars_found=scan_state["cars_found"] + 10,

            new_items=scan_state["new_items"] + 1,

            price_down=scan_state["price_down"] + 2,

            price_up=scan_state["price_up"] + 1,


            progress=int(
                (store / total_store) * 100
            )
        )


    update_state(

        status="Completed",

        last_scan=datetime.now()
        .strftime("%d %b %Y %H:%M"),

        progress=100
    )
