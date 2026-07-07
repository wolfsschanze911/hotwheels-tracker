from collections import defaultdict

from state import scan_results



def clean_product_name(name):

    name = name.upper()


    remove_words = [
        "HOT WHEELS",
        "MAINAN MOBIL ANAK",
        "MAINAN MOBIL",
        "MAINAN",
        "MOBIL",
        "ANAK",
        "ASSORTED",
    ]


    for word in remove_words:

        name = name.replace(
            word,
            ""
        )


    name = " ".join(
        name.split()
    )


    return name.strip()



def search(keyword):

    keyword = keyword.strip().lower()


    if not keyword:

        return []



    grouped_results = defaultdict(list)



    for item in scan_results:


        original_name = item.get(
            "produk",
            "-"
        )


        clean_name = clean_product_name(
            original_name
        )


        if keyword not in clean_name.lower():

            continue



        item_copy = item.copy()


        item_copy["produk"] = clean_name



        grouped_results[clean_name].append(
            item_copy
        )



    results = []



    for product_name, stores in grouped_results.items():


        stores.sort(
            key=lambda item: item.get(
                "stok",
                0
            ),
            reverse=True
        )


        results.append(

            {

                "produk": product_name,

                "jumlah_toko": len(stores),

                "toko": stores

            }

        )



    results.sort(

        key=lambda item: item["jumlah_toko"],

        reverse=True

    )


    return results
