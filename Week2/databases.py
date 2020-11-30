import sqlite3
import re

# If it does not exists, creates it

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email Text, count INTEGER)
''')

fhandler = open("mbox-short.txt")

for line in fhandler:
    email = re.findall('^From: (\S+@\S+)', line)

    if 1 != len(email): continue

    cur.execute("SELECT count FROM Counts WHERE email = ?", (email[0],))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (email, count) VALUES (?,1)",(email[0],))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?",(email[0],))

    conn.commit()

sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"
for row in cur.execute(sqlstr):
    print(row[0],row[1])

