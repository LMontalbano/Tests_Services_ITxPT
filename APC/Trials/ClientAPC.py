import requests

# Initialisation de l'address et du port
ADDRESS = "http://127.0.0.1"
PORT = '9000'

# Récupération du contenue du fichier PassengerDoorCount_Sub.xml
with open('Sub_Unsub/PassengerDoorCount_Sub.xml', "rb") as file:
    rxml0 = file.read(4096)

# Récupération du contenue du fichier PassengerVehicleCount_Sub.xml
with open('Sub_Unsub/PassengerVehicleCount_Sub.xml', "rb") as file:
    rxml1 = file.read(4096)

# Création d'un headers personnalisé
headers = {
    "Content-Length": "",
    "Accept-Encoding": "identity",
    "Host": "127.0.0.1:9000",
    "Content-Type": "text/xml"
}

### POST Requests ###

# Request pour le module passengerdoorcount
#r0 = requests.post(ADDRESS + ':' + PORT + "/apc/passengerdoorcount", data=rxml0, headers=headers)

# Request pour le module passengervehiclecount
r1 = requests.post(ADDRESS + ':' + PORT + "/apc/passengervehiclecount", data=rxml1, headers=headers)

