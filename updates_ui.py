import streamlit as st


def render_updates(results):

    st.markdown(
        "## 🔥 Latest Updates"
    )


    if not results:

        st.caption(
            "Belum ada update stok."
        )

        return


    updates = [
        item
        for item in results
        if item.get("status") != "➖ Tetap"
    ]


    if not updates:

        st.success(
            "Tidak ada perubahan stok."
        )

        return


    # tampilkan update terbaru di atas
    updates = updates[::-1]


    for item in updates[:20]:

        product = item.get(
            "produk",
            "-"
        )

        store = item.get(
            "toko",
            "-"
        )

        stock = item.get(
            "stok",
            0
        )

        status = item.get(
            "status",
            ""
        )


        st.markdown(
            f"""
🚗 **{product}**

🏪 {store}
📦 Stok : **{stock}** {status}

---
"""
        )
