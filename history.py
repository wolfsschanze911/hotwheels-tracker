from datetime import datetime, timezone, timedelta

import streamlit as st

from google.oauth2.service_account import Credentials

from config import (
    SPREADSHEET_NAME,
    WORKSHEET_NAME
)


# ==================================
# Google Sheet Connection
# ==================================

def connect_to_sheets():

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(
        dict(
            st.secrets["gcp_service_account"]
        ),
        scopes=scopes
    )

    client = gspread.authorize(
        creds
    )

    spreadsheet = client.open(
        SPREADSHEET_NAME
    )

    worksheet = spreadsheet.worksheet(
        WORKSHEET_NAME
    )

    return worksheet



# ==================================
# Load History
# ==================================

def load_history():

    history = {}

    try:

        sheet = connect_to_sheets()

        records = sheet.get_all_records()


        for row in records:

            key = row.get(
                "Key",
                ""
            )


            if not key:
                continue


            stock = row.get(
                "Stock",
                0
            )


            try:

                stock = int(stock)

            except:

                stock = 0


            history[key] = stock


    except Exception as e:

        print(
            f"Load history gagal: {e}"
        )


    return history



# ==================================
# Save History
# ==================================

def save_history(history):

    try:

        sheet = connect_to_sheets()


        now = datetime.now(
            timezone(
                timedelta(hours=7)
            )
        ).strftime(
            "%d %b %Y %H:%M WIB"
        )


        rows = []


        for key, stock in history.items():

            parts = key.split(
                "_",
                1
            )


            store = parts[0]

            series = (
                parts[1]
                if len(parts) > 1
                else "-"
            )


            rows.append(
                [
                    key,
                    series,
                    store,
                    stock,
                    "",
                    "",
                    "",
                    now
                ]
            )


        sheet.clear()


        sheet.append_row(
            [
                "Key",
                "Series",
                "Store",
                "Stock",
                "Price",
                "Status",
                "Change",
                "Last Scan"
            ]
        )


        if rows:

            sheet.append_rows(
                rows
            )


    except Exception as e:

        print(
            "DETAIL SAVE ERROR:",
            repr(e)
        )

        raise Exception(
            f"Save gagal : {e}"
        )
