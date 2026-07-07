import streamlit as st


# ==========================================
# INIT SESSION STATE
# ==========================================

def init_state():

    if "scan_state" not in st.session_state:

        st.session_state.scan_state = {

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
        }


    if "scan_results" not in st.session_state:

        st.session_state.scan_results = []


    if "update_feed" not in st.session_state:

        st.session_state.update_feed = []


# ==========================================
# RESET
# ==========================================

def reset_state():

    init_state()

    st.session_state.scan_state.update({

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

    st.session_state.scan_results.clear()

    st.session_state.update_feed.clear()


# ==========================================
# START SCAN
# ==========================================

def start_scan_state(total_store=0):

    init_state()

    st.session_state.scan_state.update({

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

    st.session_state.scan_results.clear()

    st.session_state.update_feed.clear()


# ==========================================
# FINISH SCAN
# ==========================================

def finish_scan_state(last_scan):

    init_state()

    st.session_state.scan_state.update({

        "running": False,

        "status": "🟢 Scan selesai",

        "last_scan": last_scan,

        "progress": 100

    })


# ==========================================
# UPDATE STATE
# ==========================================

def update_state(**kwargs):

    init_state()

    for key, value in kwargs.items():

        if key in st.session_state.scan_state:

            st.session_state.scan_state[key] = value


# ==========================================
# RESULT
# ==========================================

def add_scan_result(result):

    init_state()

    st.session_state.scan_results.append(result)


# ==========================================
# UPDATE FEED
# ==========================================

def add_update(item):

    init_state()

    st.session_state.update_feed.insert(
        0,
        item
    )

    if len(st.session_state.update_feed) > 50:

        st.session_state.update_feed.pop()


# ==========================================
# GETTER
# ==========================================

def get_scan_state():

    init_state()

    return st.session_state.scan_state


def get_scan_results():

    init_state()

    return st.session_state.scan_results


def get_update_feed():

    init_state()

    return st.session_state.update_feed
