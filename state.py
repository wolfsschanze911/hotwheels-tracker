# ==========================================
# GLOBAL SCAN STATE
# ==========================================

scan_state = {

    # Scan status
    "running": False,
    "status": "⚪ Idle",
    "last_scan": "-",

    # Progress
    "stores_done": 0,
    "stores_total": 0,
    "progress": 0,

    # Statistics
    "cars_found": 0,
    "new_items": 0,
    "price_down": 0,
    "price_up": 0
}



# ==========================================
# HASIL SCAN TERBARU
# Dipakai Search & Save History
# ==========================================

scan_results = []



# ==========================================
# LIVE UPDATE FEED
# Dipakai Latest Updates
# ==========================================

update_feed = []



# ==========================================
# RESET SEMUA DATA SCAN
# ==========================================

def reset_state():

    scan_state.update({

        "running": False,

        "status": "⚪ Idle",

        "last_scan": "-",

        "stores_done": 0,

        "stores_total": 0,

        "progress": 0,

        "cars_found": 0,

        "new_items": 0,

        "price_down": 0,

        "price_up": 0
    })


    scan_results.clear()

    update_feed.clear()



# ==========================================
# MULAI SCAN
# ==========================================

def start_scan_state(total_store=0):

    scan_state.update({

        "running": True,

        "status": "🟡 Preparing scan...",

        "last_scan": "-",

        "stores_done": 0,

        "stores_total": total_store,

        "progress": 0,

        "cars_found": 0,

        "new_items": 0,

        "price_down": 0,

        "price_up": 0
    })


    scan_results.clear()

    update_feed.clear()



# ==========================================
# SELESAI SCAN
# ==========================================

def finish_scan_state(last_scan):

    scan_state.update({

        "running": False,

        "status": "🟢 Scan selesai",

        "last_scan": last_scan,

        "progress": 100
    })



# ==========================================
# UPDATE DASHBOARD
# ==========================================

def update_state(**kwargs):

    for key, value in kwargs.items():

        if key in scan_state:

            scan_state[key] = value



# ==========================================
# TAMBAH HASIL SCAN
# ==========================================

def add_scan_result(result):

    scan_results.append(
        result
    )



# ==========================================
# TAMBAH UPDATE TERBARU
# ==========================================

def add_update(item):

    update_feed.insert(
        0,
        item
    )


    if len(update_feed) > 50:

        update_feed.pop()



# ==========================================
# GETTER
# ==========================================

def get_scan_results():

    return scan_results



def get_update_feed():

    return update_feed



def get_scan_state():

    return scan_state
