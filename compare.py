def compare_stock(history, key, current_stock):
    """
    Membandingkan stok sekarang dengan histori.

    Returns:
        status (str)
        previous_stock (int)
        diff (int)
    """

    previous_stock = history.get(key)

    if previous_stock is None:
        return "🆕 Baru", 0, current_stock

    diff = current_stock - previous_stock

    if diff == 0:
        status = "➖ Tetap"
    elif diff > 0:
        status = f"🟢 +{diff}"
    else:
        status = f"🔴 {abs(diff)}"

    return status, previous_stock, diff
