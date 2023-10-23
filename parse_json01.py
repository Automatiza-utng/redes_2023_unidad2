'''
    Descripcion:    Invocando REST API MapQuest
    Autor:          Max Cervantes López
    Fecha:          23 octubre 2023
'''
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San Miguel de allende"
key = "RrtauqSEGAZkLVZqIVrzwgrYtaPQuGcz"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()
print(json_data['route']['sessionId'])

# Extrae la distancia y el tiempo


# Extrae del primer elemento Legs el campo formattedTime




