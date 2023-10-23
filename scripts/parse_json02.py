'''
    Descripcion:    Invocando REST API MapQuest
    Autor:          Max Cervantes López
    Fecha:          23 octubre 2023
'''
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Ocote"
dest = "San Miguel de allende"
key = "RrtauqSEGAZkLVZqIVrzwgrYtaPQuGcz"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()

print("URL: " + (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
# Codificar para manejar el error distinto a Cero






