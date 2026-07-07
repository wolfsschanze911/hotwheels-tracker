import streamlit as st

from search_engine import search_product



def render_search():

    st.markdown("## 🔎 Search Hot Wheels")


    keyword = st.text_input(
        "",
        placeholder="Cari nama mobil atau toko..."
    )


    if keyword:

        results = search_product(keyword)


        if not results:

            st.info(
                "Tidak ada hasil ditemukan."
            )

            return



        st.caption(
            f"Ditemukan {len(results)} item"
        )


        for item in results:


            harga = item.get(
                "harga",
                0
            )


            try:

                harga = int(harga)

            except:

                harga = 0



            with st.container(border=True):

                st.markdown(

                    f"""
                    🚗 **{item.get("produk","-")}**

                    🏪 {item.get("toko","-")}

                    📦 Stok : **{item.get("stok",0)}**

                    💰 Harga : **Rp {harga:,.0f}**

                    {item.get("status","")}
                    """

                )
