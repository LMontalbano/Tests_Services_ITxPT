import socket
import time
import xml.etree.ElementTree as ET
import logging
import sys


def parseXML(xml_string):
    # print(xml_string)

    tree = ET.ElementTree(ET.fromstring(xml_string))
    # print (tree)
    root = tree.getroot()
    # print(root)

    # permet de faire un print du fichier xml
    # ET.dump(tree)

    # Création de notre dico
    dico = {"Latitude": ["", ""], "Longitude": ["", ""], "Altitude": "", "SpeedOverGround": "", "Time": "", "Date": ""}

    for tag in root.findall("./GNSSLocation"):

        ######### Récupération de la latitude #########
        # Degree
        if tag.find("Latitude") is None:
            # print(tags.find("Latitude"))
            return "Error, 'Latitude' tag not exists"
        else:
            if tag.find("Latitude/Degree") is None:
                # print(tags.find("Latitude/Degree"))
                return "Error, 'Degree' tag not exists"
            else:
                for elem in root.findall("./GNSSLocation/Latitude/Degree"):
                    dico["Latitude"][0] = elem.text

        # Direction
        if tag.find("Latitude") is None:
            # print(tags.find("Latitude"))
            return "Error, 'Latitude' tag not exists"
        else:
            if tag.find("Latitude/Direction") is None:
                # print(tags.find("Latitude/Direction"))
                return "Error, 'Direction' tag not exists"
            else:
                for elem in root.findall("./GNSSLocation/Latitude/Direction"):
                    dico["Latitude"][1] = elem.text

        ######### Récupération de la longitude #########
        # Degree
        if tag.find("Longitude") is None:
            # print(tags.find("Longitude"))
            return "Error, 'Longitude' tag not exists"
        else:
            if tag.find("Longitude/Degree") is None:
                # print(tags.find("Longitude/Degree"))
                return "Error, 'Degree' tag not exists"
            else:
                for elem in root.findall("./GNSSLocation/Longitude/Degree"):
                    dico["Longitude"][0] = elem.text

        # Direction
        if tag.find("Longitude") is None:
            # print(tags.find("Longitude"))
            return "Error, 'Longitude' tag not exists"
        else:
            if tag.find("Longitude/Direction") is None:
                # print(tags.find("Longitude/Direction"))
                return "Error, 'Direction' tag not exists"
            else:
                for elem in root.findall("./GNSSLocation/Longitude/Direction"):
                    dico["Longitude"][1] = elem.text

        ######### Récupération de l'altitude #########
        if tag.find("Altitude") is None:
            return "Error, 'Altitude' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Altitude"):
                dico["Altitude"] = elem.text

        ######### Récupération de la speed #########
        if tag.find("SpeedOverGround") is None:
            return "Error, 'SpeedOverGround' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/SpeedOverGround"):
                dico["SpeedOverGround"] = elem.text

        ######### Récupération du time #########
        if tag.find("Time") is None:
            return "Error, 'Time' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Time"):
                dico["Time"] = elem.text

        ######### Récupération de la date #########
        if tag.find("Date") is None:
            return "Error, 'Date' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Date"):
                dico["Date"] = elem.text

    return dico


IP_CLI = '127.0.0.1'
PORT_CLI = 5004
client_address = (IP_CLI, PORT_CLI)

t = 1

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(client_address)

while True:
    logging.basicConfig(filename="std.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    s.settimeout(t)
    try:
        data, address = s.recvfrom(4096)
    # print(data)
    # print(parseXML(data.decode()))
    except socket.timeout as e:
        err = e.args[0]
        if err == 'timed out':
            time.sleep(1)
            logging.basicConfig(filename="std.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')
            logger.error("recvfrom() timed out Error")
            logger.removeHandler(handler)
            continue

        else:
            print(err)
            logging.basicConfig(filename="std.log",
                                format='%(asctime)s %(message)s',
                                filemode='w')
            logger.error(err)
            logger.removeHandler(handler)
            continue

    logger.info(parseXML(data.decode()))

    time.sleep(1)
    logger.removeHandler(handler)
