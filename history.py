import gspread
import streamlit as st

from google.oauth2.service_account import Credentials
from config import SPREADSHEET_NAME, WORKSHEET_NAME



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


            if key:

                stock = int(
                    row.get("Stock", 0)
                )


                history[key] = stock


        return history


    except Exception as e:

        st.error(
            f"load_history gagal : {e}"
        )

        return history



def save_history(history):

    sheet = connect_to_sheets()


    if sheet is None:

        return


    try:

        # ambil data lama dulu
        old_history = load_history()


        # gabungkan data lama + baru
        old_history.update(history)


        rows = [
            [
                "Key",
                "Stock"
            ]
        ]


        for key, stock in old_history.items():

            rows.append(
                [
                    key,
                    stock
                ]
            )


        # backup data lama tetap aman
        sheet.clear()


        sheet.update(
            "A1",
            rows
        )


        st.success(
            "History berhasil disimpan."
        )


    except Exception as e:

        st.error(
            f"Save gagal : {e}"
        )
