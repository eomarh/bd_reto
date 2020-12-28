from mysql.connector import errorcode
import xml.etree.ElementTree as ET
import mysql.connector
import dicttoxml

#conexion-datos
try:
    cnx = mysql.connector.connect(host="127.0.0.1", user="root", passwd="12345", db="bd_reto")
except mysql.connector.Error as er:
    if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuario o contraseña incorrecto.")
        print('')
    elif er.errno == errorcode.ER_BAD_DB_ERROR:
        print("No existe la Base de Datos indicada.")
        print('')
    else:
        print(er)
else:
    exe = cnx.cursor(dictionary=True)

    #codigos
    query = "SELECT * FROM oc"
    exe.execute(query)
    filas = exe.fetchall()

    cnx.close()

    #Archivo XML
    ruta = "E:/C disk/Local C/Documentos/Universidad/5° Semestre/Repos 5°/Bases de datos/proyecto/Reto"

    xml = dicttoxml.dicttoxml(filas, custom_root='productos', attr_type=False)
    print(xml)
    tree = ET.ElementTree(ET.fromstring(xml))

    tree.write("output.xml", xml_declaration=True)