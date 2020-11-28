from mysql.connector import errorcode
import mysql.connector
import xml2dict

#DB
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

    #XML to dict
    xml=open('output.xml')
    xmldict = xml2dict.parse(xml.read())

    print('--Valores a insertar--')
    for item in xmldict["productos"]["item"]:
        print(item["id_oc"],item["proveedor"],item["producto"],item["descproducto"],item["cantidad"], item["fechaentrega"], item["precio"])
        #Asignacion a variables
        data = {
            'id_oc': int(item["id_oc"]),
            'proveedor': item["proveedor"],
            'producto': item["producto"],
            'descproducto': item["descproducto"],
            'cantidad': int(item["cantidad"]),
            'fechaentrega': item["fechaentrega"],
            'precio': float(item["precio"])
        }
        #Ejecucion de QUERIES
        query = ("INSERT INTO oc_2(id_oc, proveedor, producto, descproducto, cantidad, fechaentrega, precio) VALUES(%(id_oc)s, %(proveedor)s, %(producto)s, %(descproducto)s, %(cantidad)s, %(fechaentrega)s, %(precio)s)")
        exe.execute(query, data)
        cnx.commit()

    cnx.close()