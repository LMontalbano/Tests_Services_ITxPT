from http.server import HTTPServer, BaseHTTPRequestHandler
import xml.etree.ElementTree as ET
import logging
import sys

cancel = False
tous = False


# Création de l'objet Server
class Server(BaseHTTPRequestHandler):

    # Setup du headers
    def _set_headers(self):

        """ Fonction qui permet de setup le headers
            Nom fonction : _set_headers
            Paramètre : self
            Return : rien"""

        # Répondre avec le code 200 OK pour signaler la réussite de la requête
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()

    # Fonction do_POST
    def do_POST(self):

        """ Fonction qui permet de récupérer les stream xml envoyer en POST et de les traiter
            Nom fonction : do_POST
            Paramètre : self
            Return : rien mais peut print la data après avoir été traiter dans les différentes fonctions 
                     (driver_id, destination_name, line_name, last_stop_point_ref et time_next_stop)"""

        # Récupération de la taille des données
        content_length = int(self.headers['Content-Length'])

        # Récupération des données
        post_data = self.rfile.read(content_length)

        # Création du tree et récupération de la root
        tree = ET.ElementTree(ET.fromstring(post_data))
        root = tree.getroot()

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

        # Parcours le plus haut node
        for tag in root.findall("."):
            # Vérification si il s'agit d'un packet provenant du module "PlannedPattern"
            if tag.tag == "PlannedPatternDelivery":
                print("DriverID : ")
                # Execution de la fonction driver_id sur la data récupéré
                logger.info(driver_id(post_data))
                logger.removeHandler(handler)
                print("\n")

                print("Destination : ")
                # Execution de la fonction destination_name sur la data récupéré
                logger.info(destination_name(post_data))
                logger.removeHandler(handler)
                print("\n")

                print("Nom de ligne : ")
                # Execution de la fonction line_name sur la data récupéré
                logger.info(line_name(post_data))
                logger.removeHandler(handler)
                print("\n")

            # Vérification si il s'agit d'un packet provenant du module "VehicleMonitoring"
            if tag.tag == "VehicleMonitoringDelivery":
                print("Dernier Arrêt : ")
                # Execution de la fonction last_stop_point_ref sur la data récupéré
                logger.info(last_stop_point_ref(post_data))
                logger.removeHandler(handler)
                print("\n")

            # Vérification si il s'agit d'un packet provenant du module "JourneyMonitoring"
            if tag.tag == "JourneyMonitoringDelivery":
                # Execution de la fonction time_next_stop sur la data récupéré
                res = time_next_stop(post_data)
                # Si la longueur de res est supérieur à deux cela veut dire que time_next_stop retourne un message d'erreur
                if len(res) > 2:
                    print("Heure d'arrivée : ")
                    logger.info(res)
                    logger.removeHandler(handler)
                else:
                    print("Heure d'arrivée prévue : ")
                    # Affichage sur la console de l'heure d'arrivée prévue
                    logger.info(res[0])
                    logger.removeHandler(handler)
                    print("Heure d'arrivée éstimé : ")
                    # Affichage sur la console de l'heure d'arrivée éstimé
                    logger.info(res[1])
                    logger.removeHandler(handler)
                    print("\n")





def driver_id(data):
    """ Fonction qui permet de récupérer l'identifiant du conducteur en fonction de data passé en paramètre
        Nom fonction : driver_id
        Paramètre : data, un flux xml
        Return : un string qui a comme valeur le DriverID"""

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()

    for tag in root.findall("."):

        if tag.tag == "PlannedPatternDelivery":

            if tag.find("PlannedPattern") is None:
                return "Error, 'PlannedPattern' tag not exists"

            else:
                if tag.find("PlannedPattern/DriverID") is None:
                    return "Error, 'DriverID' tag not exists"

                else:
                    for elem in root.findall("./PlannedPattern/DriverID"):

                        if elem.text is None:
                            return "Error, 'DriverID' tag is empty"
                        else:
                            return elem.text


def destination_name(data):
    """ Fonction qui permet de récupérer le nom du terminus en fonction de data passé en paramètre
        Nom fonction : destination_name
        Paramètre : data, un flux xml
        Return : un string qui a comme valeur le libellé de la destination final"""

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()

    for tag in root.findall("."):

        if tag.tag == "PlannedPatternDelivery":

            if tag.find("PlannedPattern") is None:
                return "Error, 'PlannedPattern' tag not exists"

            else:
                if tag.find("PlannedPattern/DestinationName") is None:
                    return "Error, 'DestinationName' tag not exists"

                else:
                    for elem in root.findall("./PlannedPattern/DestinationName"):

                        if elem.text is None:
                            return "Error, 'DestinationName' tag is empty"
                        else:
                            return elem.text


def line_name(data):
    """ Fonction qui permet de récupérer le nom de la ligne en fonction de data passé en paramètre
        Nom fonction : line_name
        Paramètre : data, un flux xml
        Return : un string qui a comme valeur le mnémonique commercial de ligne"""

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()

    for tag in root.findall("."):

        if tag.tag == "PlannedPatternDelivery":

            if tag.find("PlannedPattern") is None:
                return "Error, 'PlannedPattern' tag not exists"

            else:
                if tag.find("PlannedPattern/ExternalLineRef") is None:
                    return "Error, 'ExternalLineRef' tag not exists"

                else:
                    for elem in root.findall("./PlannedPattern/ExternalLineRef"):

                        if elem.text is None:
                            return "Error, 'ExternalLineRef' tag is empty"
                        else:
                            return elem.text


def last_stop_point_ref(data):
    """ Fonction qui permet de récupérer le nom du dernier arrêt auquel le bus s'est arrêté
        Nom fonction : last_stop_point_ref
        Paramètre : data, un flux xml
        Return : un string qui a comme valeur le numéro du point (NLP de l'objet arrêt du fichier neutre des points)"""

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()

    for tag in root.findall("."):

        if tag.tag == "VehicleMonitoringDelivery":

            if tag.find("VehicleActivity") is None:
                return "Error, 'VehicleActivity' tag not exists"

            else:
                if tag.find("VehicleActivity/ProgressBetweenStops") is None:
                    return "Error, 'ProgressBetweenStops' tag not exists"

                else:
                    if tag.find("VehicleActivity/ProgressBetweenStops/PreviousCallRef") is None:
                        return "Error, 'PreviousCallRef' tag not exists"

                    else:
                        if tag.find("VehicleActivity/ProgressBetweenStops/PreviousCallRef/StopPointRef") is None:
                            return "Error, 'StopPointRef' tag not exists"

                        else:
                            for elem in root.findall(
                                    "./VehicleActivity/ProgressBetweenStops/PreviousCallRef/StopPointRef"):

                                if elem.text is None:
                                    return "Error, 'StopPointRef' tag is empty"
                                else:
                                    return elem.text


def time_next_stop(data):
    """ Fonction qui permet de récupérer à la fois, l'heure d'arrivée prévue et celle éstimé, du prochain arrêt, en fonction de data passé en paramètre
        Nom fonction : time_next_stop
        Paramètre : data, un flux xml
        Return : un tuple qui a comme valeur en indice 0, l'heure théorique d’arrivée au prochaine arrêt (YYYY-MMDDThh:mm:ss+hh:mm)
                 et en indice 1, l'heure applicable d’arrivée au prochaine arrêt (YYYY-MMDDThh:mm:ss+hh:mm) (théorique +avance/retard)"""

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()

    for tag in root.findall("."):

        if tag.tag == "JourneyMonitoringDelivery":

            if tag.find("MonitoredJourney") is None:
                return "Error, 'MonitoredJourney' tag not exists"

            else:
                if tag.find("MonitoredJourney/MonitoredCall") is None:
                    return "Error, 'MonitoredCall' tag not exists"

                else:
                    if tag.find("MonitoredJourney/MonitoredCall/Order") is None:
                        return "Error, 'Order' tag not exists"

                    else:
                        # Récupération du numéro Order du MonitoredCall
                        for orders in root.findall("./MonitoredJourney/MonitoredCall/Order"):

                            if orders.text is None:
                                return "Error, 'Order' tag is empty"
                            else:
                                order = orders.text

                            if tag.find("MonitoredJourney/OnwardCalls") is None:
                                return "Error, 'OnwardCalls' tag not exists"

                            else:
                                if tag.find("MonitoredJourney/OnwardCalls/OnwardCall") is None:
                                    return "Error, 'OnwardCall' not exists"

                                else:
                                    # Recherche du numéro Order +1 (qui correspond donc au prochain arrêt)
                                    for elem in root.findall("./MonitoredJourney/OnwardCalls/OnwardCall"):

                                        if elem[1].text is None:
                                            return "Error, 'Order' tag is empty"
                                        else:
                                            if int(elem[1].text) == int(order) + 1:

                                                if tag.find(
                                                        "MonitoredJourney/OnwardCalls/OnwardCall/PlannedArrivalTime") is None:
                                                    return "Error, 'PlannedArrivalTime' not exists"

                                                else:
                                                    if tag.find(
                                                            "MonitoredJourney/OnwardCalls/OnwardCall/ExpectedArrivalTime") is None:
                                                        return "Error, 'ExpectedArrivalTime' tag not exists"

                                                    else:
                                                        # elem[2].text correspond au contenue de la balise PlannedArrivalTime
                                                        if elem[2].text is None:
                                                            return "Error, 'PlannedArrivalTime' tag is empty"

                                                        else:
                                                            # elem[3].text correspond au contenue de la balise ExpectedArrivalTime
                                                            if elem[3].text is None:
                                                                return "Error, 'ExpectedArrivalTime' tag is empty"
                                                            else:
                                                                return elem[2].text, elem[3].text


def run(server_class=HTTPServer, handler_class=Server, addr="localhost", port=8000):
    """ Fonction qui permet de run le serveur
        Paramètres: server_class: , handler_class: la class Server par défaut, addr: localhost par défaut, port: 8000 par défaut
        Return: Ne retourne rien, permet de faire tourner le serveur"""

    # Initialisation du server_address via les paramètre addr et port de la fonction    
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")

    x = 0
    while not cancel and x < 5:
        if not tous:
            x = 0
        else:
            x += 1
        httpd.handle_request()


def main_serv_avms(serv):
    run(addr=str(serv), port=8000)
