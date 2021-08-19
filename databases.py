import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')
conn.commit()

cur.execute('DELETE FROM Ages;')
cur.execute("INSERT INTO Ages (name, age) VALUES ('Kelsiee', 27);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Trinity', 26);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Ewa', 30);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Siannon', 24);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Ronin', 34);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Hollee', 20);")
conn.commit()



cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
    print(row)
conn.commit()

conn.close()