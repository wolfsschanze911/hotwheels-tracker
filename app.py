import json
import gspread
import request
import streamlit as st
from google.oauth2.service_account import Credentials

def connect_to_sheets(): 
    st.write(type(st.secrets["gcp_service_account"]))
    try:
        creds_dict = dict(st.secrets["gcp_service_account"])

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=scopes
        )

        client = gspread.authorize(creds)

        return client.open("HotWheelsDB").worksheet("Sheet1")

    except Exception as e:
        st.error(f"Gagal koneksi Google Sheets: {e}")
        return None
        
# 2. LOAD - Menggunakan list murni, ANTI ERROR
def load_history():

    history = {}

    sheet = connect_to_sheets()

    if sheet is None:
        return history

    try:

        rows = sheet.get_all_records()

        for row in rows:

            key = str(row.get("Key", "")).strip()

            stock = int(row.get("Stock", 0))

            history[key] = stock

        return history

    except Exception as e:

        st.error(f"load_history gagal : {e}")

        return history

# 3. SAVE - Menulis ulang sheet secara bersih
def save_history(history):

    sheet = connect_to_sheets()

    if sheet is None:
        return

    try:

        rows = [["Key", "Stock"]]

        for key, stock in history.items():

            rows.append([key, stock])

        sheet.clear()

        sheet.update("A1", rows)

        st.success("History berhasil disimpan.")

    except Exception as e:

        st.error(f"Save gagal : {e}")

# --- KONFIGURASI TOKO & HEADERS ---
# Data dari skrip kerja Anda
daftar_toko_depok = [
    {"nama": "MARGASATWA RAYA", "storecode": "eyJzdG9yZV9jb2RlIjoiMU1UOCIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjE2MzUuNiwibWF4RGlzdGFuY2UiOjIwMDAsImZsYWdSb3V0ZSI6IjFNMUciLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "FATMAWATI PDK LABU", "storecode": "eyJzdG9yZV9jb2RlIjoiMU1OOSIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjIzOTEuNiwibWF4RGlzdGFuY2UiOjIwMDAsImZsYWdSb3V0ZSI6IjFNMUciLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "CILANDAK KKO 5", "storecode": "eyJzdG9yZV9jb2RlIjoiMU0xRyIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjQ4ODEuMiwibWF4RGlzdGFuY2UiOjMwMDAsImZsYWdSb3V0ZSI6IjFNNlUiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "DS BUKIT RAYA", "storecode": "eyJzdG9yZV9jb2RlIjoiMU03VCIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjUzMTIuMSwibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IjFNMUciLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "DS ANDARA JAGAKARSA", "storecode": "eyJzdG9yZV9jb2RlIjoiMU04USIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjU1NTcuMCwibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IjIwMjYtMDYtMTBUMjE6MzE6MzguMjc0KzA3MDAiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "JL MPR III", "storecode": "eyJzdG9yZV9jb2RlIjoiMU01TyIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjYxNzUuNywibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IjIwMjYtMDYtMTZUMjI6MjA6NTguMDgzKzA3MDAiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "KEBAGUSAN 2", "storecode": "eyJzdG9yZV9jb2RlIjoiS0I1OSIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjYyMzMuMCwibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IjFNMUciLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "DS PONDOK INDAH", "storecode": "eyJzdG9yZV9jb2RlIjoiMU03QSIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjMwNTAuOCwibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IktGODQiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "DS MERUYUNG", "storecode": "eyJzdG9yZV9jb2RlIjoiMU04TSIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjU3MDYuNCwibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IjIwMjYtMDYtMTBUMjE6MzE6MzguMjc0KzA3MDAiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "PONDOK PINANG", "storecode": "eyJzdG9yZV9jb2RlIjoiQUI1MiIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjc4MjcuOCwibWF4RGlzdGFuY2UiOjMwMDAsImZsYWdSb3V0ZSI6IjFNTTMiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "H. NAWI", "storecode": "eyJzdG9yZV9jb2RlIjoiSzcyMSIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjMzMzEuNCwibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IktGODQiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "DAMAI V", "storecode": "eyJzdG9yZV9jb2RlIjoiSzk1NiIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjQwNzkuNCwibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IktGODQiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "DS KEMANG", "storecode": "eyJzdG9yZV9jb2RlIjoiMU02VSIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjc1NjYuNiwibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IjFNMUciLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "RAYA OTISTA", "storecode": "eyJzdG9yZV9jb2RlIjoiQTA5OCIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjc0NzkuNywibWF4RGlzdGFuY2UiOjgwMDAsImZsYWdSb3V0ZSI6IjIwMjYtMDYtMjFUMjM6Mjk6MDIuMTU3KzA3MDAiLCJkZXBvX2lkIjoiS1kxMiJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IktaMDEifQ"},
    {"nama": "RIDWAN RAIS 4 F", "storecode": "eyJzdG9yZV9jb2RlIjoiWEIyMSIsImRlbGl2ZXJ5Ijp0cnVlLCJzYXBhIjp0cnVlLCJzdG9yZV9tZXRob2QiOjEsImJsYWNrbGlzdF90YWdzIjpbXSwiZGlzdGFuY2UiOjc1MzAuMywibWF4RGlzdGFuY2UiOm51bGwsImZsYWdSb3V0ZSI6IjIwMjYtMDYtMTBUMjE6MzE6MzguMjc0KzA3MDAiLCJkZXBvX2lkIjoiSlkwMSJ9", "fccode": "eyJzZWxsZXJfaWQiOiIxIiwiZmNfY29kZSI6IkpaMDEifQ"}
]

HEADERS = {
    'accept': 'application/json',
    'accept-language': 'id',
    'devicemodel': 'chrome',
    'devicetype': 'Web',
    'fingerprint': 'FDmEBG3ie1PuHLynHv2KiLJwdsBrq2aZSM3LLxWB1FpPdZJxmJB3BKF8qBOrKo4E',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2YTM1NzVmMTg2NWVkYmY2ZWYyN2UwZTciLCJzdWIiOiJvY3RvcHV4M0BnbWFpbC5jb20iLCJpc3MiOiJ3ZWJjb21tZXJjZXxzZXNzaW9ufFdFQiIsImV4cCI6MTc4NTc2ODU5MSwiaWF0IjoxNzgzMTc2NTkxfQ.dQ7x50decbATh9uiktH5Ib1x5SGseNPx47OoHxRAIwc',
    'trxid': '8983712366',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0'
}

url_pencarian = "https://webcommerce-gw.alfagift.id/v2/products/searches?keyword=hot-wheels&start=0&limit=60"

st.set_page_config(page_title="Hot Wheels Tracker", layout="wide")
st.title("🚗 Alfagift Hotwheels Live Tracker")


if st.button("SCAN SEMUA TOKO"):
    history = load_history()
    progress_bar = st.progress(0)

    for i, toko in enumerate(daftar_toko_depok):
        try:
            # 1. Setup headers
            headers_toko = HEADERS.copy()
            headers_toko.update({'storecode': toko['storecode'], 'fccode': toko['fccode']})
            
            # 2. AMBIL DATA DULU (Penting!)
            response = requests.get(url_pencarian, headers=headers_toko, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                # 3. Definisikan stok_tersedia DI SINI
                products = data.get("products", []) or data.get("data", {}).get("products", [])
                stok_tersedia = [p for p in products if p.get("stock", 0) > 0]
            else:
                stok_tersedia = [] # Kalau gagal, kosongkan saja supaya tidak error

            # 4. Baru tampilkan UI (Tombol Maps & Expander)
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(f"📍 {toko['nama']}")
            with col2:
                url_maps = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote('Alfamart ' + toko['nama'])}"
                st.link_button("📍 Maps", url=url_maps)

            # Sekarang stok_tersedia sudah ada, jadi expander tidak akan error lagi
            with st.expander(f"Lihat stok ({len(stok_tersedia)} item ditemukan)"):
                if stok_tersedia:
                    list_data = []
                    for p in stok_tersedia:
                        nama_produk = p.get("productName", "N/A")
                        current_stock = p.get("stock", 0)
                        key = f"{toko['nama']}_{nama_produk}"

                        prev_stock = history.get(key, 0)
                        diff = current_stock - prev_stock
                            
                        # Logika Status
                        if prev_stock == 0: status = "🆕 Baru"
                        elif diff > 0: status = f"🟢 +{diff}"
                        elif diff < 0: status = f"🔴 {diff}"
                        else: status = "➖ Tetap"
                            
                        history[key] = current_stock
                        
                        list_data.append({
                            "Produk": nama_produk,
                            "Stok": current_stock,
                            "Status": status,
                            "Harga": f"Rp {p.get('finalPrice', 0):,.0f}"
                        })
                    st.table(pd.DataFrame(list_data))
                else:
                    st.write("Stok kosong.")
        
        except Exception as e:
            st.error(f"Error di {toko['nama']}: {e}")
            
        progress_bar.progress((i + 1) / len(daftar_toko_depok))
            
    # Save history (Berada di luar for loop)
    save_history(history)
    st.success("Scan selesai! Data stok terbaru telah disimpan.")
