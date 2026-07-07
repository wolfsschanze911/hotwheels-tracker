

SPREADSHEET_NAME = "HotWheelsDB"
WORKSHEET_NAME = "Sheet1"

URL_PENCARIAN = "https://webcommerce-gw.alfagift.id/v2/products/searches?keyword=hot-wheels&start=0&limit=60"

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

DAFTAR_TOKO = [
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
