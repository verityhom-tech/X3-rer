import sqlite3

cones = sqlite3.connect("para10_DB.sl3", 5)
cur = cones.cursor()

cur.execute("INSERT INTO pet (name) VALUES ('Cat');")
cur.execute("INSERT INTO pet (name) VALUES ('Dog');")
cones.commit()

res = cur.fetchall()
print(res)

cones.close()