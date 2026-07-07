import requests

from config import (
    URL_PENCARIAN,
    HEADERS,
)


def scan_store(toko):
    """
    Mengambil data produk Hot Wheels dari satu toko.
    Return: list products
    """

    headers = HEADERS.copy()

    headers.update({
        "storecode": toko["storecode"],
        "fccode": toko["fccode"],
    })

    response = requests.get(
        URL_PENCARIAN,
        headers=headers,
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    products = (
        data.get("products", [])
        or data.get("data", {}).get("products", [])
    )

    return products
