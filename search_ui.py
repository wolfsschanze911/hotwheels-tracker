import streamlit as st

from search_engine import search


def render_search():

    st.markdown("## 🔎 Search Hot Wheels")


    keyword = st.text_input(
        "",
        placeholder="Cari series Hot Wheels..."
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
        f"Ditemukan {len(results)} series"
    )


    for item in results:

        total_stock = sum(
            toko["stok"]
            for toko in item["toko"]
        )


        with st.container(border=True):

            st.markdown(
                f"""
### 🚗 {item['produk']}

<small>
🏪 {item['jumlah_toko']} toko ditemukan &nbsp;&nbsp;|&nbsp;&nbsp;
📦 Total stok <b>{total_stock}</b>
</small>
""",
                unsafe_allow_html=True
            )

            st.divider()


            for toko in item["toko"]:

                harga = toko.get(
                    "harga",
                    0
                )

                try:

                    harga = int(harga)

                except:

                    harga = 0


                st.markdown(f"**🏪 {toko['toko']}**")

                c1, c2, c3 = st.columns([1,2,1])

                c1.caption(f"📦 {toko['stok']}")
                c2.caption(f"💰 Rp {harga:,.0f}")
                c3.caption(toko["status"])
