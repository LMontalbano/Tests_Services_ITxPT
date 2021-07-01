from AVMS.ClientAVMS import ADDRESS
import socket
import time
import xml.etree.ElementTree as ET
import logging
import sys
import struct


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
                    if elem.text is not None:
                        dico["Latitude"][0] = elem.text
                    else:
                        return "Error, 'Degree' tag is empty"

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
                    if elem.text is not None:
                        dico["Latitude"][1] = elem.text
                    else:
                        return "Error, 'Direction' tag is empty"
                    

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
                    if elem.text is not None:
                        dico["Longitude"][0] = elem.text
                    else:
                        return "Error, 'Degree' tag is empty"

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
                    if elem.text is not None:
                        dico["Longitude"][1] = elem.text
                    else:
                        return "Error, 'Direction' tag is empty"

        ######### Récupération de l'altitude #########
        if tag.find("Altitude") is None:
            return "Error, 'Altitude' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Altitude"):
                if elem.text is not None:
                    dico["Altitude"] = elem.text
                else:
                    return "Error, 'Altitude' tag is empty"

        ######### Récupération de la speed #########
        if tag.find("SpeedOverGround") is None:
            return "Error, 'SpeedOverGround' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/SpeedOverGround"):
                if elem.text is not None:
                    dico["SpeedOverGround"] = elem.text
                else:
                    return "Error, 'SpeedOverGround' tag is empty"
    

        ######### Récupération du time #########
        if tag.find("Time") is None:
            return "Error, 'Time' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Time"):
                if elem.text is not None:
                    dico["Time"] = elem.text
                else:
                    return "Error, 'Time' tag is empty"

        ######### Récupération de la date #########
        if tag.find("Date") is None:
            return "Error, 'Date' tag not exists"
        else:
            for elem in root.findall("./GNSSLocation/Date"):
                if elem.text is not None:
                    dico["Date"] = elem.text
                else:
                    return "Error, 'Date' tag is empty"

    return dico


t = 1

GRP_MULTI = '127.0.0.1'
PORT = 5004
ADDRESS_SERV = '127.0.0.1'
server_address = (ADDRESS_SERV, PORT)

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(server_address)

group = socket.inet_aton(GRP_MULTI)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


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
