from collections import defaultdict

from state import scan_results


def search(keyword):

    keyword = keyword.strip().lower()

    if keyword == "":
        return []

    hasil = defaultdict(list)

    for item in scan_results:

        nama = item["produk"].lower()

        if keyword in nama:

            hasil[item["produk"]].append(item)

    response = []

    for produk, toko in hasil.items():

        toko.sort(
            key=lambda x: x["stok"],
            reverse=True
        )

        response.append({

            "produk": produk,

            "jumlah_toko": len(toko),

            "toko": toko

        })

    response.sort(

        key=lambda x: x["jumlah_toko"],

        reverse=True

    )

    return response
