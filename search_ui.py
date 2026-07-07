import streamlit as st

from search_engine import search


def render_search():

    st.markdown("## 🔎 Search Hot Wheels")

    keyword = st.text_input(
        "",
        placeholder="Cari nama Hot Wheels..."
    )

    if not keyword:
        return

    results = search(keyword)

    if not results:
        st.info("Tidak ada hasil ditemukan.")
        return

    st.caption(f"Ditemukan {len(results)} produk")

    for product in results:

        with st.container(border=True):

            st.markdown(
                f"""
### 🚗 {product["produk"]}

📍 **Tersedia di {product["jumlah_toko"]} toko**
"""
            )

            for store in product["toko"]:

                try:
                    price = int(store.get("harga", 0))
                except (TypeError, ValueError):
                    price = 0

                st.markdown(
                    f"""
🏪 **{store["toko"]}**

📦 Stok : **{store["stok"]}**

💰 Rp {price:,.0f}

{store["status"]}

---
"""
                )
