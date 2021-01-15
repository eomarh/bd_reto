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

#Descarga del archivo FTP
try:
    ftp.cwd("public_html/salida/")
    ftp.retrbinary('RETR outputData.xml',open('extra/downOutput.xml','wb').write)
    print("Archivo descargado.")
    ftp.delete("outputData.xml")
    print("Y eliminado.")
except Exception as e:
    print("Algo salio mal: "+e)