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
    xml=open('extra/downOutput.xml')
    xmldict = xml2dict.parse(xml.read())

    print('--Valores a insertar--')
    for item in xmldict["xml"]["item"]:
        print(item["id_ocM"],item["proveedorM"],item["productoM"],item["descproductoM"],item["cantidadM"], item["fechaentregaM"], item["precioM"])
        #Asignacion a variables
        data = {
            'id_oc': int(item["id_ocM"]),
            'proveedor': item["proveedorM"],
            'producto': item["productoM"],
            'descproducto': item["descproductoM"],
            'cantidad': int(item["cantidadM"]),
            'fechaentrega': item["fechaentregaM"],
            'precio': float(item["precioM"])
        }
        #Ejecucion de QUERIES
        try:
            query = ("INSERT INTO oc_2(id_oc, proveedor, producto, descproducto, cantidad, fechaentrega, precio) VALUES(%(id_oc)s, %(proveedor)s, %(producto)s, %(descproducto)s, %(cantidad)s, %(fechaentrega)s, %(precio)s)")
            exe.execute(query, data)
        except mysql.connector.IntegrityError:
            print("Error: Valor duplicado en PrimaryKey.")
        except mysql.connector.DataError:
            print("Error en los datos introducidos")
        except mysql.connector.ProgrammingError:
            print("Error de sintaxis.")
        cnx.commit()

    cnx.close()