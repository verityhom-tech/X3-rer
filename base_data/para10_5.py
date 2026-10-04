import sqlite3

cones = sqlite3.connect("para10_DB.sl3", 5)
cur = cones.cursor()

cur.execute("SELECT rowid name FROM first_table WHERE rowid = 3;")
cones.commit()

res = cur.fetchall()
print(res)

cones.close()