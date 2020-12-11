import json
import urllib.request
from datetime import datetime

now = datetime.now()
fecha_dt = now.strftime("%d-%m-%Y %H:%M:%S")



url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
req = urllib.request.Request(url)


r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0
now = datetime.now()
fecha_dt = now.strftime("%d-%m-%Y %H:%M:%S")
print("Ultima cotizacion: ", fecha_dt)
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
        print("\nDolar Oficial: \n Compra:", compra1, "\n Venta:", venta1 )
    if (nombre1 == solidario):
        print("\nDolar Solidario:", venta1)

    if (nombre1 == dolarbolsa):
        print("\nDolar Bolsa: \n Compra:", compra1, "\n Venta:", venta1 )


    if (nombre1 == dolarccl):

        print("\nDolar Contado con Liqui: \n Compra:", compra1, "\n Venta:", venta1 )


btc = 'https://blockchain.info/ticker'
reqs = urllib.request.Request(btc)


rbtc = urllib.request.urlopen(reqs).read()
contenido = json.loads(rbtc.decode('utf-8'))

bitcoin = contenido['USD']['last']
print ("\nBitcoin: ", bitcoin)
