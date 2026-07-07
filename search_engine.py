from state import scan_results

def search_product(keyword):
  
    results = []
    keyword = keyword.lower().strip()
    if not keyword:
       
      return results

    for item in scan_results:

        produk = item.get(
            "produk",
            ""
        ).lower()

        toko = item.get(
            "toko",
            ""
        ).lower()


        if (
            keyword in produk
            or keyword in toko
        ):

            results.append(item)


    return results
