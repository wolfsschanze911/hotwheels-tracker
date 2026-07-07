def compare_stock(history, key, current_stock):
    """
    Membandingkan stok saat ini dengan history.

    Return:
        status      -> teks status
        prev_stock  -> stok sebelumnya
        diff        -> selisih stok
    """

    if key not in history:
        return "🆕 Baru", 0, current_stock

    prev_stock = history[key]
    diff = current_stock - prev_stock

    if diff > 0:
        status = f"🟢 +{diff}"

    elif diff < 0:
        status = f"🔴 {abs(diff)}"

    else:
        status = "➖ Tetap"

    return status, prev_stock, diff
    return {
    "status": "🟢 +2",
    "type": "increase",
    "previous": 3,
    "current": 5,
    "diff": 2,
}
