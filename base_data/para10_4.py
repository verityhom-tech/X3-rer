import sqlite3

cones = sqlite3.connect("para10_DB.sl3", 5)
cur = cones.cursor()

cur.execute("INSERT INTO first_table (name) VALUES ('Vasyl');")
cur.execute("INSERT INTO first_table (name) VALUES ('Nikita');")
cur.execute("INSERT INTO first_table (name) VALUES ('Franys');")
cur.execute("SELECT rowid name FROM first_table;")

cones.commit()
res = cur.fetchall()
print(res)
cones.close()