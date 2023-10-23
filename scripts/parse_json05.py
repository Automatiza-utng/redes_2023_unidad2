'''
    Descripcion:    Invocando REST API MapQuest
    Autor:          Max Cervantes López
    Fecha:          23 octubre 2023
'''
import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    # Agregar condicion para dest
    # Un mensaje hasta luego

    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "RrtauqSEGAZkLVZqIVrzwgrYtaPQuGcz"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()

    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("=============================================")
        # Add RouteType, Longitud y Latitud







