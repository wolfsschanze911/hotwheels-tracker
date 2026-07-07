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
    "stores_total": 15,
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
# Dipakai Update Terbaru
# ==========================================

update_feed = []


# ==========================================
# RESET DASHBOARD
# ==========================================

def reset_state():

    scan_state.update({

        "running": False,

        "status": "🟡 Preparing scan...",
        "last_scan": "-",

        "stores_done": 0,
        "stores_total": 15,

        "progress": 0,

        "cars_found": 0,
        "new_items": 0,
        "price_down": 0,
        "price_up": 0
    })

    scan_results.clear()
    update_feed.clear()


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

    scan_results.append(result)


# ==========================================
# TAMBAH UPDATE TERBARU
# ==========================================

def add_update(item):

    update_feed.insert(0, item)

    # Simpan maksimal 50 update
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
