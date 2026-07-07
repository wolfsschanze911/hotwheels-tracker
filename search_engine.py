from collections import defaultdict
from state import scan_results


def search_product(keyword):

    keyword = keyword.strip().lower()

    if keyword == "":
        return []

    grouped = defaultdict(list)

    for item in scan_results:

        nama = item["produk"].lower()

        if keyword in nama:

            grouped[item["produk"]].append(item)

    results = []

    for produk, toko_list in grouped.items():

        toko_list.sort(
            key=lambda x: x["stok"],
            reverse=True
        )

        results.append({

            "produk": produk,

            "toko": toko_list

        })

    results.sort(
        key=lambda x: len(x["toko"]),
        reverse=True
    )

    return results
