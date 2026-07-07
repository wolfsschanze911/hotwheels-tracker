import gspread
import streamlit as st

from google.oauth2.service_account import Credentials
from config import SPREADSHEET_NAME, WORKSHEET_NAME


# ==========================================
# GOOGLE SHEETS
# ==========================================

def connect_to_sheets():

    try:

        creds_dict = dict(
            st.secrets["gcp_service_account"]
        )

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=scopes
        )

        client = gspread.authorize(creds)

        return client.open(
            SPREADSHEET_NAME
        ).worksheet(
            WORKSHEET_NAME
        )

    except Exception as e:

        st.error(
            f"Gagal koneksi Google Sheets : {e}"
        )

        return None


# ==========================================
# HISTORY UNTUK COMPARE
# Return:
# {
#     key: stock
# }
# ==========================================

def load_history():

    history = {}

    sheet = connect_to_sheets()

    if sheet is None:
        return history

    try:

        rows = sheet.get_all_records()

        for row in rows:

            key = str(
                row.get("Key", "")
            ).strip()

            if not key:
                continue

            try:
                stock = int(
                    row.get("Stock", 0)
                )
            except:
                stock = 0

            history[key] = stock

        return history

    except Exception as e:

        st.error(
            f"load_history gagal : {e}"
        )

        return history


# ==========================================
# LOAD DATABASE
# Return seluruh isi sheet
# ==========================================

def load_database():

    sheet = connect_to_sheets()

    if sheet is None:
        return []

    try:

        return sheet.get_all_records()

    except Exception as e:

        st.error(
            f"load_database gagal : {e}"
        )

        return []


# ==========================================
# SAVE DATABASE
# Menerima list of dict
# ==========================================

def save_history(records):

    sheet = connect_to_sheets()

    if sheet is None:
        return

    try:

        rows = [[
            "Key",
            "Series",
            "Store",
            "Stock",
            "Price",
            "Status",
            "Change",
            "Last Scan"
        ]]

        for item in records:

            rows.append([

                item.get("Key", ""),

                item.get("Series", ""),

                item.get("Store", ""),

                item.get("Stock", 0),

                item.get("Price", 0),

                item.get("Status", ""),

                item.get("Change", 0),

                item.get("Last Scan", "")

            ])

        sheet.update(
            "A1:H{}".format(len(rows)),
            rows
        )

    except Exception as e:

        st.error(
            f"Save gagal : {e}"
        )
