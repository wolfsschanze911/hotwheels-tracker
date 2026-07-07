def compare_stock(history, key, current_stock):

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
