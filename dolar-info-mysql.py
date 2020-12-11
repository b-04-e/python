import json
import urllib.request
import pymysql
from datetime import datetime

now = datetime.now()
fecha_dt = now.strftime("%d-%m-%Y %H:%M:%S")



url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
req = urllib.request.Request(url)


r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0

conexion = pymysql.connect(host='127.0.0.1', user='root', password='clave', db='datos')

consulta="insert into datos(moneda,fecha, compra, venta) VALUES(%s,%s,%s,%s)"
cursor=conexion.cursor()

for item in cont[0]['casa']:
    counter += 1
    nombre1 = cont[counter]['casa']['nombre']
    compra1 = cont[counter]['casa']['compra']
    venta1 = cont[counter]['casa']['venta']
    oficial = "Dolar"
    solidario = "Dolar turista"
    dolarbolsa = "Dolar bolsa"
    dolarccl = "Dolar Contado con Liqui"
    dolarno = "Dolar Soja"
    dolarblue = "Dolar blue"
    if (nombre1 == oficial):
        now = datetime.now()
        fecha_dt = now.strftime("%d-%m-%Y %H:%M:%S")
        cursor.execute(consulta, (oficial, fecha_dt, compra1, venta1))
    if (nombre1 == solidario):
        now = datetime.now()
        fecha_dt = now.strftime("%d-%m-%Y %H:%M:%S")
        cursor.execute(consulta, (solidario, fecha_dt, "NULL", venta1))
    if (nombre1 == dolarbolsa):
        now = datetime.now()
        fecha_dt = now.strftime("%d-%m-%Y %H:%M:%S")
        cursor.execute(con+sulta, (bolsa, fecha_dt, compra1, venta1))
    if (nombre1 == dolarccl):
        now = datetime.now()
        fecha_dt = now.strftime("%d-%m-%Y %H:%M:%S")
        cursor.execute(consulta, (dolarccl, fecha_dt, compra1, venta1))

btc = 'https://blockchain.info/ticker'
reqs = urllib.request.Request(btc)


rbtc = urllib.request.urlopen(reqs).read()
contenido = json.loads(rbtc.decode('utf-8'))

bitcoin = contenido['USD']['last']
now = datetime.now()
fecha_dt = now.strftime("%d-%m-%Y %H:%M:%S")
cursor.execute(consulta, ("Bitcoin", fecha_dt, bitcoin, bitcoin))
conexion.commit()
