from http.server import HTTPServer, BaseHTTPRequestHandler
import xml.etree.ElementTree as ET


# Création 
class Server(BaseHTTPRequestHandler):
    
    # Setup du headers
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()

    # Setup du do_POST
    def do_POST(self):
        # Récupération de la taille des données
        content_length = int(self.headers['Content-Length'])
        
        # Récupération des données
        post_data = self.rfile.read(content_length)
        
        # Affichage des données sur la console
        #print(post_data)
        #print("\n")
        #self._set_headers()
        
        print("DriverID : " + driver_id(post_data))
        
        print("Destination : " + destination_name(post_data))

        print("Nom de ligne : " + line_name(post_data))

        print("Dernier Arrêt : " + last_stop_point_ref(post_data))

        print("Heure d'arrivée prévue : " + time_next_stop(post_data)[0] + "\n" + "Heure d'arrivée éstimé : " + time_next_stop(post_data)[1])
        
        
        
        
def driver_id(data):
    
    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()
    
    for tag in root.findall("."):
        if tag.tag == "PlannedPatternDelivery":
            
            if tag.find("PlannedPattern/DriverID") is None:
                return "Error, 'DriverID' tag not exists"
            else:
                for elem in root.findall("./PlannedPattern/DriverID"):
                    if elem.text is None:
                        return "Error, 'DriverID' tag is empty"
                    else:
                        return elem.text
                    

def destination_name(data):
    
    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()
    
    for tag in root.findall("."):
        if tag.tag == "PlannedPatternDelivery":
            
            if tag.find("PlannedPattern/DestinationName") is None:
                return "Error, 'DestinationName' tag not exists"
            else:
                for elem in root.findall("./PlannedPattern/DestinationName"):
                    if elem.text is None:
                        return "Error, 'DestinationName' tag is empty"
                    else:
                        return elem.text


def line_name(data):

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()

    for tag in root.findall("."):
        if tag.tag == "PlannedPatternDelivery":

            if tag.find("PlannedPattern/ExternalLineRef") is None:
                return "Error, 'ExternalLineRef' tag not exists"
            else:
                for elem in root.findall("./PlannedPattern/ExternalLineRef"):
                    if elem.text is None:
                        return "Error, 'ExternalLineRef' tag is empty"
                    else:
                        return elem.text



def last_stop_point_ref(data):

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()

    for tag in root.findall("."):
        if tag.tag == "VehicleMonitoringDelivery":

            if tag.find("VehicleMonitoring/PreviousCallRef") is None:
                return "Error, 'PreviousCallRef' tag not exists"
            else:
                if tag.find("VehicleMonitoring/PreviousCallRef/StopPointRef") is None:
                    return "Error, 'StopPointRef' tag not exists"
                else:
                    for elem in root.findall("./VehicleMonitoring/PreviousCallRef/StopPointRef"):
                        if elem.text is None:
                            return "Error, 'StopPointRef' tag is empty"
                        else:
                            return elem.text


def time_next_stop(data): ########## A revoir car là je me base sur l'heure d'arrivé du dernier arrêt et pas du prochain #########

    lspr = last_stop_point_ref(data)

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()
    
    for tag in root.findall("."):
        if tag.tag == "JourneyMonitoringDelivery":
            
            for elem in root.findall("./MonitoredJourney/OnwardCalls/OnwardCall"):
                if elem["StopPointRef"].text == lspr:
                    return (elem["PlannedArrivalTime"], elem["ExpectedArrivalTime"])




def run(server_class=HTTPServer, handler_class=Server, addr="localhost", port=8000):
    """ Fonction qui permet de run le serveur
        Paramètres: server_class: , handler_class: la class Server par défaut, addr: localhost par défaut, port: 8000 par défaut
        Return: Ne retourne rien, permet de faire tourné le serveur"""
    
    # Initialisation du server_address via les paramètre addr et port de la fonction    
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    
    run(addr='127.0.0.1', port=8000)
