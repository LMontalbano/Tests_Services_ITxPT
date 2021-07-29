import requests


def main_cli_avms():
    # Initialisation de l'adresse et du port
    ADDRESS = "http://127.0.0.1"
    PORT = '8000'

    ### RunMonitoring ###
    # Récupération du contenue du fichier RunMonitoring_Sub.xml
    with open('../Trials/Sub_Unsub/RunMonitoring_Sub.xml', "rb") as file:
        rxml_0 = file.read(4096)

    ### PlannedPattern ###
    # Récupération du contenue du fichier PlannedPattern_Sub.xml
    with open('../Trials/Sub_Unsub/PlannedPattern_Sub.xml', "rb") as file:
        rxml_1 = file.read(4096)

    ### VehicleMonitoring ###
    # Récupération du contenue du fichier VehicleMonitoring.xml
    with open('../Trials/Sub_Unsub/VehicleMonitoring_Sub.xml', "rb") as file:
        rxml_2 = file.read(4096)

    ### JourneyMonitoring ###
    # Récupération du contenue du fichier JourneyMonitoring_Sub.xml
    with open('../Trials/Sub_Unsub/JourneyMonitoring_Sub.xml', "rb") as file:
        rxml_3 = file.read(4096)

    ### GeneralMessage ###
    # Récupération du contenue du fichier GeneralMessage_Sub.xml
    with open('../Trials/Sub_Unsub/GeneralMessage_Sub.xml', "rb") as file:
        rxml_4 = file.read(4096)

    ### PatternMonitoring ###
    # Récupération du contenue du fichier PatternMonitoring_Sub.xml
    with open('../Trials/Sub_Unsub/PatternMonitoring_Sub.xml', "rb") as file:
        rxml_5 = file.read(4096)

    # Création d'un headers personnalisé
    headers = {
        "Content-Length": "",
        "Accept-Encoding": "identity",
        "Host": "http://127.0.0.1:8000",
        "Content-Type": "text/xml"
    }

    ### POST Requests ###

    # Request pour le module runmonitoring
    r0 = requests.post(ADDRESS + ':' + PORT + "/avms/runmonitoring", data=rxml_0, headers=headers)

    # Request pour le module plannedpattern
    r1 = requests.post(ADDRESS + ':' + PORT + "/avms/plannedpattern", data=rxml_1, headers=headers)

    # Request pour le module vehiclemonitoring
    r2 = requests.post(ADDRESS + ':' + PORT + "/avms/vehiclemonitoring", data=rxml_2, headers=headers)

    # Request pour le module journeymonitoring
    r3 = requests.post(ADDRESS + ':' + PORT + "/avms/journeymonitoring", data=rxml_3, headers=headers)

    # Request pour le module generalmessage
    r4 = requests.post(ADDRESS + ':' + PORT + "/avms/generalmessage", data=rxml_4, headers=headers)

    # Request pour le module patternmonitoring
    r5 = requests.post(ADDRESS + ':' + PORT + "/avms/patternmonitoring", data=rxml_5, headers=headers)
