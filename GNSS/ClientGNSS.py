import socket
import time
import xml.etree.ElementTree as ET
import logging
import sys


def parseXML(xml_string):
    
    """ Fonction pour parse un stream xml
        Nom fonction: parseXML
        Paramètre: xml_string, un flux xml
        Return: un dico avec la les données du stream xml passer en paramètre"""

    # Création du tree et récupération de la root
    tree = ET.ElementTree(ET.fromstring(xml_string))
    root = tree.getroot()
    

    # Création de notre dico
    dico = {"Latitude": ["", ""], "Longitude": ["", ""], "Altitude": "", "SpeedOverGround": "", "Time": "", "Date": ""}


    for tag in root.findall("./GNSSLocation"):

        ######### Récupération de la latitude #########
        
        ## Degree ##
        # Vérification si les balises "Latitude" et "Degree" exists et si elles ne sont pas vident
        # Si il n'y a pas d'erreurs, ajout de la donnée dans le dico
        if tag.find("Latitude") is None:
            return "Error, 'Latitude' tag not exists"
        else:
            if tag.find("Latitude/Degree") is None:
                
                return "Error, 'Degree' tag not exists"
            else:
                for elem in root.findall("./GNSSLocation/Latitude/Degree"):
                    if elem.text is not None:
                        dico["Latitude"][0] = elem.text
                    else:
                        return "Error, 'Degree' tag is empty"

        ## Direction ##
        # Vérification de l'existance des balises "Latitude" et "Direction" et si elles ne sont pas vident
        # Si il n'y a pas d'erreurs, ajout de la donnée dans le dico
        if tag.find("Latitude") is None:
            return "Error, 'Latitude' tag not exists"
        else:
            if tag.find("Latitude/Direction") is None:
                
                return "Error, 'Direction' tag not exists"
            else:
                for elem in root.findall("./GNSSLocation/Latitude/Direction"):
                    if elem.text is not None:
                        dico["Latitude"][1] = elem.text
                    else:
                        return "Error, 'Direction' tag is empty"
                    

        ######### Récupération de la longitude #########
        
        ## Degree ##
        # Vérification de l'existance des balises "Longitude" et "Direction" et si elles ne sont pas vident
        # Si il n'y a pas d'erreurs, ajout de la donnée dans le dico
        if tag.find("Longitude") is None:
            return "Error, 'Longitude' tag not exists"
        else:
            if tag.find("Longitude/Degree") is None:
                
                return "Error, 'Degree' tag not exists"
            else:
                for elem in root.findall("./GNSSLocation/Longitude/Degree"):
                    if elem.text is not None:
                        dico["Longitude"][0] = elem.text
                    else:
                        return "Error, 'Degree' tag is empty"

        ## Direction ##
        # Vérification de l'existance des balises "Longitude" et "Direction" et si elles ne sont pas vident
        # Si il n'y a pas d'erreurs, ajout de la donnée dans le dico
        if tag.find("Longitude") is None:
            return "Error, 'Longitude' tag not exists"
        else:
            if tag.find("Longitude/Direction") is None:
                
                return "Error, 'Direction' tag not exists"
            else:
                for elem in root.findall("./GNSSLocation/Longitude/Direction"):
                    if elem.text is not None:
                        dico["Longitude"][1] = elem.text
                    else:
                        return "Error, 'Direction' tag is empty"


        ######### Récupération de l'altitude #########
        
        # Vérification de l'existance de la balise "Altitude" et si elle n'est pas vide
        # Si il n'y a pas d'erreurs, ajout de la donnée dans le dico
        if tag.find("Altitude") is None:
            return "Error, 'Altitude' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Altitude"):
                if elem.text is not None:
                    dico["Altitude"] = elem.text
                else:
                    return "Error, 'Altitude' tag is empty"


        ######### Récupération de la speed #########
        
        # Vérification de l'existance de la balise "SpeedOverGround" et si elle n'est pas vide
        # Si il n'y a pas d'erreurs, ajout de la donnée dans le dico
        if tag.find("SpeedOverGround") is None:
            return "Error, 'SpeedOverGround' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/SpeedOverGround"):
                if elem.text is not None:
                    dico["SpeedOverGround"] = elem.text
                else:
                    return "Error, 'SpeedOverGround' tag is empty"
    


        ######### Récupération du time #########

        # Vérification de l'existance de la balise "Time" et si elle n'est pas vide
        # Si il n'y a pas d'erreurs, ajout de la donnée dans le dico
        if tag.find("Time") is None:
            return "Error, 'Time' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Time"):
                if elem.text is not None:
                    dico["Time"] = elem.text
                else:
                    return "Error, 'Time' tag is empty"


        ######### Récupération de la date #########
        
        # Vérification de l'existance de la balise "Date" et si elle n'est pas vide
        # Si il n'y a pas d'erreurs, ajout de la donnée dans le dico
        if tag.find("Date") is None:
            return "Error, 'Date' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Date"):
                if elem.text is not None:
                    dico["Date"] = elem.text
                else:
                    return "Error, 'Date' tag is empty"

    return dico

# temps d'attente en second avant de reprendre le programme (utilisée avec le time.sleep())
t = 1

# Initialisation des différentes address et port
GRP_MULTI = '127.0.0.1'
PORT = 5004
IP_INTERFACE = '127.0.0.1'
IP_INTERFACE_PORT = (IP_INTERFACE, PORT)

# Création du socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Autoriser d'autres sockets à lier ce port aussi
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Rejoindre le groupe multicast sur l'interface spécifiée
s.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,
             socket.inet_aton(GRP_MULTI) + socket.inet_aton(IP_INTERFACE))

# Lier le socket pour récupérer les données
s.bind(IP_INTERFACE_PORT)


while True:
    
    # Configuration du logging
    logging.basicConfig(filename="std.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Création et configuration d'un handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Setup d'un timeout
    s.settimeout(t)
    
    try:
        # Récupération des données
        data, address = s.recvfrom(4096)
    
    # Si on ne récupère pas de data au bout de t second
    except socket.timeout as e:
        err = e.args[0]
        if err == 'timed out':
            # Enregistrement de l'erreur dans le fichier std.log
            logging.basicConfig(filename="std.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')
            logger.error("recvfrom() timed out Error")
            logger.removeHandler(handler)
            
            # Tempo de 1 sec avant de réessayer
            time.sleep(t)
            continue

        else:
            # Affichage de l'erreur et enregistrement de l'erreur dans le fichier std.log
            print(err)
            logging.basicConfig(filename="std.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')
            logger.error(err)
            logger.removeHandler(handler)
            continue

    # Affichage de mes données triées et analysés
    logger.info(parseXML(data.decode()))

    # Tempo de t second avant de recommencer
    time.sleep(t)
    logger.removeHandler(handler)
