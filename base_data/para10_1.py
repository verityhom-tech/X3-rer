import sqlite3

cones = sqlite3.connect("para10_DB.sl3", 5)
cur = cones.cursor()

cur.execute("CREATE TABLE first_table (NAME TEXT);")
cones.commit()

cones.close()