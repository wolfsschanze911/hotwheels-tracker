from collections import defaultdict

from state import scan_results


def search(keyword):
    """
    Mencari produk berdasarkan keyword.

    Returns:
        list[dict]
    """

    keyword = keyword.strip().lower()

    if not keyword:
        return []

    grouped_results = defaultdict(list)

    for item in scan_results:

        product_name = item["produk"]

        if keyword not in product_name.lower():
            continue

        grouped_results[product_name].append(item)

    results = []

    for product_name, stores in grouped_results.items():

        stores.sort(
            key=lambda item: item["stok"],
            reverse=True
        )

        results.append({
            "produk": product_name,
            "jumlah_toko": len(stores),
            "toko": stores
        })

    results.sort(
        key=lambda item: item["jumlah_toko"],
        reverse=True
    )

    return results
