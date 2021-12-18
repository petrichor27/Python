#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi, cgitb
import html
import sqlite3

connection = sqlite3.connect("dance-school.db")
cursor = connection.cursor()
form = cgi.FieldStorage()

table = form.getvalue('Таблицы')
button = form.getvalue('Button')
query = form.getvalue('Queries')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<meta charset=""utf-8"">")
print ("<title>Школа танцев</title>")
print ("</head>")
print ("<h1 align = 'center'>Школа танцев</h1>")

print('''<form action = "/cgi-bin/to_web.py" method = "post">
Таблица: <select name = "Таблицы">
<option value = "course">Курсы</option>
<option value = "client">Клиенты</option>
<option value = "teacher">Преподаватели</option>
<option value = "dgroup">Группы</option>
</select><br><br>
<input type = "submit" name = "Button" value = "Вывод">
<input type = "submit" name = "Button" value = "Добавить">
<input type = "submit" name = "Button" value = "Удалить"><br><br>
</form>''')

print('''<form action = "/cgi-bin/to_web.py" method = "post">
Запросы: <select name = "Queries">
<option value = "valseTeachers">Преподаватели, которые ведут вальс</option>
<option value = "tangoPrice">Цена занятий танго</option>
</select><br><br>
<input type = "submit" value = "Запросить">
</form><br><br>''')

if button == 'Вывод':
    if table == 'course':
        cursor.execute('SELECT * FROM course')
        course = cursor.fetchall()
        print("<table cellspacing = '10'>"
              "<caption><h2>Курсы</h2></caption>"
              "<tr>"
              "<th>Номер</th>"
              "<th>Название</th>"
              "<th>Цена</th>"
              "</tr>")
        for row in course:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
                  "</td><td align = 'center'>", row[2], "</td></tr>")
        print("</table>")

    elif table == 'client':
        cursor.execute("""SELECT * FROM client""")
        client = cursor.fetchall()
        print("<table cellspacing = '10'>"
              "<caption><h2>Клиенты</h2></caption>"
              "<tr>"
              "<th>Id</th>"
              "<th>Фамилия</th>"
              "<th>Имя</th>"
              "<th>Отчество</th>"
              "</tr>")
        for row in client:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
                  "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3], "</td></tr>")
        print("</table>")

    elif table == 'teacher':
        cursor.execute("""SELECT * FROM teacher""")
        teacher = cursor.fetchall()
        print("<table cellspacing = '10'>"
              "<caption><h2>Преподаватели</h2></caption>"
              "<tr>"
              "<th>Id</th>"
              "<th>Фамилия</th>"
              "<th>Имя</th>"
              "<th>Отчество</th>"
              "</tr>")
        for row in teacher:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
                  "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3], "</td></tr>")
        print("</table>")

    elif table == 'dgroup':
        cursor.execute('SELECT id_g, client.lastname, client.firstname, client.middlename, name, teacher.lastname, teacher.firstname, teacher.middlename FROM ((dgroup join client on dgroup.id_cl=client.id_cl) join course on dgroup.id_cor=course.id_cor) join teacher on dgroup.id_t=teacher.id_t')
        group = cursor.fetchall()
        print("<table cellspacing = '10'>"
              "<caption><h2>Ученики</h2></caption>"
              "<tr>"
              "<th>Номер группы</th>"
              "<th>Фамилия ученика</th>"
              "<th>Имя ученика</th>"
              "<th>Отчество ученика</th>"
              "<th>Курс</th>"
              "<th>Фамилия преп.</th>"
              "<th>Имя преп.</th>"
              "<th>Отчество преп.</th>"
              "</tr>")
        for row in group:
            print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
                  "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3], 
                  "</td><td align = 'center'>", row[4], "</td><td align = 'center'>", row[5], 
                  "</td><td align = 'center'>", row[6], "</td><td align = 'center'>", row[7], "</td></tr>")
        print("</table>")

if button == 'Добавить':
    if table == 'course':
        print("""<form action = "/cgi-bin/to_web.py" method="post">
        <caption><h2>Курсы</h2></caption>
        <p>Номер:</p><input type = "text" name = "id_cor"><br>
        <p>Название:</p><input type = "text" name = "name"><br>
        <p>Цена:</p><input type = "text" name = "price"><br><br>
        <input type = 'submit' value = 'Добавить запись'>
        </form>""")

id_cor = form.getvalue('id_cor')
name = form.getvalue('name')
price = form.getvalue('price')
if id_cor:
    cursor.execute('INSERT INTO course VALUES (?, ?, ?)', (id_cor, name, price))
    connection.commit()

if button == 'Удалить':
    if table == 'course':
        print("""<form action = "/cgi-bin/to_web.py" method = "post">
        <caption><h2>Курсы</h2></caption>
        id: <input type = "text" name = "del" /><br><br>
        <input type = 'submit' value = 'Удалить'>
        </form>""")
        col = 'id_cor'

    #elif table == 'client':
    #    print("""<form action = "/cgi-bin/to_web.py" method = "post">
    #    <caption><h2>Клиенты</h2></caption>
    #    id: <input type = "text" name = "del" /><br><br>
    #    <input type = 'submit' value = 'Удалить'>
    #    </form>""")
    #    col = 'id_cl'

    #elif table == 'teacher':
    #    print("""<form action = "/cgi-bin/to_web.py" method = "post">
    #    <caption><h2>Преподаватели</h2></caption>
    #     id: <input type = "text" name = "del" /><br><br>
    #    <input type = 'submit' value = 'Удалить'>
    #    </form>""")
    #    col = 'id_t'

    #elif table == 'dgroup':
    #    print("""<form action = "/cgi-bin/to_web.py" method = "post">
    #    <caption><h2>Ученики</h2></caption>
    #    id: <input type = "text" name = "del" /><br><br>
    #    <input type = 'submit' value = 'Удалить'>
    #    </form>""")
    #    col = 'id_g'

val = form.getvalue('del')

if val:
    cursor.execute('DELETE FROM {:} WHERE {:} = {:}'.format('course','id_cor',val))
    connection.commit()

    
if query == 'valseTeachers':
    cursor.execute('SELECT teacher.id_t,lastname,firstname,middlename FROM teacher JOIN dgroup ON teacher.id_t = dgroup.id_t WHERE id_cor = 3')
    teacher = cursor.fetchall()
    print("<table cellspacing = '10'>"
          "<h2>Преподаватели, которые ведут вальс</h2>"
          "<tr>"
          "<th>Id</th>"
          "<th>Фамилия</th>"
          "<th>Имя</th>"
          "<th>Отчество</th>"
          "</tr>")
    for row in teacher:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1],
              "</td><td align = 'center'>", row[2], "</td><td align = 'center'>", row[3], "</td></tr>")
    print("</table>")

if query == 'tangoPrice':
    cursor.execute('SELECT name, price FROM course WHERE name = "Танго"')
    course = cursor.fetchall()
    print("<table cellspacing = '10'>"
          "<h2>Цена занятий танго</h2>"
          "<tr>"
          "<th>Курс</th>"
          "<th>Цена</th>"
          "</tr>")
    for row in course:
        print("<tr><td align = 'center'>", row[0], "</td><td align = 'center'>", row[1], "</td></tr>")
    print("</table>")

print ("</body>")
print ("</html>")
connection.close()