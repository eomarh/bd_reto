import mysql.connector
import xml.etree.ElementTree as ET
import xml2dict, dicttoxml

#conexion-datos
cnx = mysql.connector.connect(host="127.0.0.1", user="root", passwd="12345", db="bd_reto")
exe = cnx.cursor(dictionary=True)

#codigos
query = "SELECT * FROM oc"
exe.execute(query)
filas = exe.fetchall()

cnx.close()

#Archivo XML
ruta = "E:/C disk/Local C/Documentos/Universidad/5° Semestre/Repos 5°/Bases de datos/proyecto/Reto"

xml = dicttoxml.dicttoxml(filas, custom_root='productos', attr_type=False)
tree = ET.ElementTree(ET.fromstring(xml))

tree.write(ruta+'/ejemplo.xml')