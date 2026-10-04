import sqlite3

cones = sqlite3.connect("para10_DB.sl3", 5)
cur = cones.cursor()

cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
cones.commit()

cones.close()