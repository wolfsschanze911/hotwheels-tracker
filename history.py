from datetime import datetime, timezone, timedelta

from sheets import connect_to_sheets
from config import WORKSHEET_NAME


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

            stock = row.get(
                "Stock",
                0
            )


            if key:

                try:
                    stock = int(stock)

                except:
                    stock = 0


                history[key] = stock


    except Exception as e:

        print(
            f"Load history error: {e}"
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


            rows.append([

                key,

                series,

                store,

                stock,

                "",

                "",

                "",

                now

            ])



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


        sheet.append_rows(
            rows
        )


    except Exception as e:

        raise Exception(
            f"Save gagal : {e}"
        )
