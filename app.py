def load_history():
    try:
        sheet = connect_to_sheets()
        # Mengambil semua nilai sebagai list of lists (baris per baris)
        # Cara ini TIDAK bergantung pada struktur dictionary yang sering error
        all_rows = sheet.get_all_values() 
        
        history = {}
        # Jika sheet kosong atau cuma ada header, kembalikan {}
        if len(all_rows) <= 1:
            return {}
        
        # Mulai dari baris index 1 (melewati header di index 0)
        for row in all_rows[1:]:
            if len(row) >= 2: # Pastikan ada kolom Key dan Stock
                key = row[0]
                stock = row[1]
                try:
                    history[key] = int(stock)
                except ValueError:
                    continue # Lewati jika angka stok tidak valid
        return history
    except Exception as e:
        st.error(f"Error saat load: {e}")
        return {}

# 3. Fungsi Save History yang LEBIH STABIL
def save_history(history):
    try:
        sheet = connect_to_sheets()
        sheet.clear()
        
        # Siapkan data lengkap dengan Header
        data_to_write = [["Key", "Stock"]]
        for key, val in history.items():
            data_to_write.append([key, val])
        
        # Tulis semua sekaligus (lebih cepat dan aman)
        sheet.append_rows(data_to_write)
        st.write("Data berhasil disimpan ke Sheets.")
    except Exception as e:
        st.error(f"Gagal menyimpan history: {e}")
