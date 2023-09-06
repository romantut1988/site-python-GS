import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS stories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)""")

cur.execute("""
    INSERT INTO stories (title, content)
    VALUES ('Анекдот про SQL №1''', 'Текст какой-то истории1. Тут должна быть история.')""")
conn.commit()

cur.execute("""
    INSERT INTO stories (title, content)
    VALUES ('Анекдот про SQL №2''', 'Текст какой-то истории1. Тут должна быть история.')""")
conn.commit()

cur.execute("""
    INSERT INTO stories (title, content)
    VALUES ('Анекдот про SQL №3''', 'Текст какой-то истории1. Тут должна быть история.')""")
conn.commit()

cur.execute("""SELECT * FROM stories""")
stories = cur.fetchall()
for story in stories:
    print(story)

conn.close()
