import mysql.connector
import xml2dict

#DB
cnx = mysql.connector.connect(host="127.0.0.1", user="root", passwd="12345", db="bd_reto")
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
    query = ("INSERT INTO oc_2(id_oc, proveedor, producto, descproducto, cantidad, fechaentrega, precio) VALUES(%(id_oc)s, %(proveedor)s, %(producto)s, %(descproducto)s, %(cantidad)s, %(fechaentrega)s, %(precio)s)")
    exe.execute(query, data)
    cnx.commit()

cnx.close()