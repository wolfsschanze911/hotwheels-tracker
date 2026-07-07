scan_state = {

    "running": False,
    "status": "⚪ Idle",
    "last_scan": "-",
    "stores_done": 0,
    "stores_total": 15,
    "cars_found": 0,
    "new_items": 0,
    "price_down": 0,
    "price_up": 0,
    "progress": 0
}


def reset_state():

    scan_state.update({
        "status": "🟡 Preparing scan...",
        "last_scan": "-",
        "stores_done": 0,
        "stores_total": 0,
        "cars_found": 0,
        "new_items": 0,
        "price_down": 0,
        "price_up": 0,
        "progress": 0
    })



def update_state(**kwargs):

    scan_state.update(kwargs)
