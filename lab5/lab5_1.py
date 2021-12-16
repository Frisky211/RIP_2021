import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='dbuser',
    passwd='123',
    db='first_db'
)

c = db.cursor()
c.execute("INSERT INTO books (name, dicription) VALUES (%s, %s);", ('Книга', 'Описание'))
db.commit()
c.execute("SELECT * FROM books")
records = c.fetchall()
for row in records:
    print(row)
c.execute("DELETE FROM BOOKS")
db.commit()
c.close()
db.close()
