import gspread
import streamlit as st

from datetime import datetime, timezone, timedelta

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


    return spreadsheet.worksheet(
        WORKSHEET_NAME
    )



# ==================================
# Series Cleaner
# ==================================

def clean_series_name(name):

    name = name.upper()


    remove_words = [
        "HOT WHEELS",
        "MAINAN MOBIL ANAK",
        "MAINAN MOBIL",
        "MAINAN",
        "MOBIL",
        "ANAK",
        "ASSORTED",
    ]


    for word in remove_words:

        name = name.replace(
            word,
            ""
        )


    name = " ".join(
        name.split()
    )


    return name.strip()



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


            try:

                history[key] = int(
                    row.get(
                        "Stock",
                        0
                    )
                )


            except:

                history[key] = 0



    except Exception as e:

        print(
            f"Load history gagal: {e}"
        )


    return history



# ==================================
# Save History
# ==================================

def save_history(history):

    sheet = connect_to_sheets()


    now = datetime.now(
        timezone(
            timedelta(hours=7)
        )
    ).strftime(
        "%d %b %Y %H:%M WIB"
    )


    rows = [

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

    ]



    for key, stock in history.items():


        parts = key.split(
            "_",
            1
        )


        store = parts[0]


        raw_series = (

            parts[1]

            if len(parts) > 1

            else "-"

        )


        series = clean_series_name(
            raw_series
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


    sheet.update(
        "A1",
        rows
    )
