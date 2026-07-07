import streamlit as st


def render_updates(results):
    """
    Menampilkan daftar perubahan stok terbaru.
    """

    st.markdown("## 📈 Stock Updates")

    if not results:
        st.info("Belum ada hasil scan.")
        return

    updates = [
        item
        for item in results
        if item["status"] != "➖ Tetap"
    ]

    if not updates:
        st.success("Tidak ada perubahan stok.")
        return

    updates.sort(
        key=lambda item: item["stok"],
        reverse=True
    )

    st.caption(f"{len(updates)} perubahan ditemukan")

    for item in updates:

        try:
            price = int(item.get("harga", 0))
        except (TypeError, ValueError):
            price = 0

        with st.container(border=True):

            st.markdown(
                f"""
### 🚗 {item["produk"]}

🏪 **{item["toko"]}**

📦 Stok : **{item["stok"]}**

💰 Rp {price:,.0f}

{item["status"]}
"""
            )
