import streamlit as st

from search_engine import search


def render_search():

    st.markdown(
        "## 🔎 Cari Hot Wheels"
    )


    keyword = st.text_input(
        "",
        placeholder="Cari nama mobil..."
    )


    if not keyword:

        return


    results = search(keyword)


    if not results:

        st.info(
            "Tidak ada hasil ditemukan."
        )

        return


    st.caption(
        f"Ditemukan {len(results)} produk"
    )


    for product in results:


        nama_produk = product.get(
            "produk",
            "-"
        )

        jumlah_toko = product.get(
            "jumlah_toko",
            0
        )


        st.markdown(
            f"""
🚗 **{nama_produk}**

🏪 Tersedia di {jumlah_toko} toko
"""
        )


        for store in product.get(
            "toko",
            []
        ):

            harga = store.get(
                "harga",
                0
            )

            try:
                harga = int(harga)

            except (TypeError, ValueError):
                harga = 0


            st.markdown(
                f"""
&nbsp;&nbsp;🏬 {store.get("toko","-")}

&nbsp;&nbsp;📦 {store.get("stok",0)}
&nbsp;&nbsp;💰 Rp {harga:,.0f}
&nbsp;&nbsp;{store.get("status","")}
"""
            )


        st.divider()
