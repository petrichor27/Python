
import sqlite3

connection = sqlite3.connect('dance-school.db')
cursor = connection.cursor()

table_course = '''CREATE TABLE course (
                            id_cor INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price REAL NOT NULL);'''
    
table_client = '''CREATE TABLE client (
                            id_cl INTEGER PRIMARY KEY,
                            lastname TEXT NOT NULL,
                            firstname TEXT NOT NULL,
                            middlename TEXT NOT NULL);'''

table_teacher = '''CREATE TABLE teacher (
                            id_t INTEGER PRIMARY KEY,
                            lastname TEXT NOT NULL,
                            firstname TEXT NOT NULL,
                            middlename TEXT NOT NULL);'''

table_group = '''CREATE TABLE dgroup (
                            id_g INTEGER PRIMARY KEY,
                            id_cl INTEGER,
                            id_cor INTEGER,
                            id_t INTEGER,
                            FOREIGN KEY(id_cl) REFERENCES client(id_cl),
                            FOREIGN KEY(id_cor) REFERENCES course(id_cor),
                            FOREIGN KEY(id_t) REFERENCES teacher(id_t));'''

#cursor.execute(table_course)
#cursor.execute(table_client)
#cursor.execute(table_teacher)
#cursor.execute(table_group)
#connection.commit()

#cursor.execute('''INSERT INTO course VALUES (1, 'Танго', 1500), (2, 'Самбо', 1500), (3, 'Вальс', 2000), (4, 'Народные танцы', 1000);''')
#cursor.execute('''INSERT INTO client VALUES (1, 'Иванов','Иван', 'Иванович'), (2, 'Петров', 'Петр', 'Петрович'), (3, 'Иващенко', 'Мария', 'Васильевна'), (4, 'Чернова', 'Людмила', 'Николаевна');''')
#cursor.execute('''INSERT INTO teacher VALUES (1, 'Иванова','Анна', 'Ивановна'), (2, 'Петрова', 'Дарья', 'Викторовна'), (3, 'Сороченко', 'Михаил', 'Васильевич'), (4, 'Капустин', 'Евгений', 'Евгеньевич');''')
#cursor.execute('''INSERT INTO dgroup VALUES (1, 1, 1, 1), (2, 2, 3, 2), (3, 3, 4, 3), (4, 4, 2, 4);''')
#connection.commit()
    
cursor.execute('SELECT * FROM course')
templist=list(cursor.fetchall())
print(templist)

cursor.execute('SELECT * FROM client')
templist=list(cursor.fetchall())
print(templist)

cursor.execute('SELECT * FROM teacher')
templist=list(cursor.fetchall())
print(templist)

cursor.execute('SELECT * FROM dgroup')
templist=list(cursor.fetchall())
print(templist)

#connection.commit()

cursor.close()
connection.close()