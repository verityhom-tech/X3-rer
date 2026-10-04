import sqlite3
from datetime import datetime
import requests

response = requests.get("https://wttr.in/Kyiv?format=%t")

if response.status_code == 200:
    temp = response.text.strip()

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conection = sqlite3.connect("HW100.sl3", 5)
    cur = conection.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS weather (date_time TEXT, temperature TEXT);"
    )
    cur.execute(
        "INSERT INTO weather (date_time, temperature) VALUES (?, ?);",
        (date_time, temp),
    )

    conection.commit()
    conection.close()

