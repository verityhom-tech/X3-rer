import sqlite3

cones = sqlite3.connect("para10_DB.sl3", 5)
cur = cones.cursor()

cur.execute("UPDATE first_table SET name='Lisa' WHERE rowid = 2;")
cur.execute("UPDATE first_table SET name='Clif' WHERE rowid = 3;")
cones.commit()

cones.close()