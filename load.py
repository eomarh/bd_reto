from ftplib import FTP
import os

host = "files.000webhost.com"
username = "home-pruebas"
passwd = "hpoe8541"

try:
    ftp = FTP(host, username, passwd)
    print("Conexion establecida.")
except Exception as e:
    print("Algo salio mal: "+e)

#Envío de archivo a FTP
archivo = open('./extra/output.xml', 'rb')
try:
    ftp.storbinary('STOR public_html/entrada/inputData.xml', archivo)
    print("Archivo subido.")
except Exception as e:
    print("Algo salio mal: "+e)