from datetime import datetime, timezone, timedelta

from config import SPREADSHEET_NAME, WORKSHEET_NAME

from google.oauth2.service_account import Credentials


SHEET_HEADER = [
    "Key",
    "Series",
    "Store",
    "Stock",
    "Price",
    "Status",
    "Change",
    "Last Scan"
]


def load_history():

    history = {}

    try:

        sheet = connect_to_sheets()

        records = sheet.get_all_records()


        for row in records:

            key = row.get(
                "Key"
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

            split_key = key.split(
                "_",
                1
            )


            store = split_key[0]

            series = (
                split_key[1]
                if len(split_key) > 1
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
            SHEET_HEADER
        )


        if rows:

            sheet.append_rows(
                rows
            )


    except Exception as e:

        raise Exception(
            f"Save gagal : {e}"
        )
