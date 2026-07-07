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


    if sheet is
