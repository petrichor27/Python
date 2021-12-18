#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi, cgitb
import html
import sqlite3
from lxml import etree, objectify

def create_struct(data): 
    value = objectify.Element("course")
    value.id_cor = data["id_cor"]
    value.name = data["name"]
    value.price = data["price"]
    return value

def bdOut(file):# Экспорт в файл
    xml = '''<?xml version="1.0"?>
    <course_table>
    </course_table>'''
    root = objectify.fromstring(xml)
    cursor.execute("SELECT * FROM course")
    c = cursor.fetchall()
    for row in c:
        value = create_struct({"id_cor": row[0], "name":  row[1], "price":  row[2]})
        root.append(value)
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
    obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True)
    f = open(file, "wb")
    f.write(obj_xml)
    
def parse_xml(file):
    f = open(file)
    xml = f.read()
    tree = etree.parse(file)
    root = tree.getroot()    
    values = []
    for i in root.getchildren():
        val = []
        for j in i.getchildren():
            if not j.text:
                val.append("null")
            else:
                val.append(j.text)
        values.append(val)
    return [tuple(i) for i in values]

def dbin(file):# Импорт из файла
    tree = parse_xml(file)
    print(tree)

connection = sqlite3.connect("dance-school.db")
cursor = connection.cursor()
bdOut('dbOut.xml')
dbin('dbOut.xml')
connection.close()