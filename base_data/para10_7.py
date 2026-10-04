import sqlite3

cones = sqlite3.connect("para10_DB.sl3", 5)
cur = cones.cursor()

cur.execute("DELETE FROM first_table WHERE rowid = 6;")
cones.commit()

cones.close()