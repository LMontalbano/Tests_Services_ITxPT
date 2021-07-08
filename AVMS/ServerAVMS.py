from http.server import HTTPServer, BaseHTTPRequestHandler
import xml.etree.ElementTree as ET

lspr = ''

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

        tree = ET.ElementTree(ET.fromstring(post_data))
        root = tree.getroot()


        for tag in root.findall("."):
            if tag.tag == "PlannedPatternDelivery":
                print("DriverID : ")
                print(driver_id(post_data))
                print("\n")
        
                print("Destination : ")
                print(destination_name(post_data))
                print("\n")

                print("Nom de ligne : ")
                print(line_name(post_data))
                print("\n")

            
            if tag.tag == "VehicleMonitoringDelivery":
                print("Dernier Arrêt : ")
                lspr = last_stop_point_ref(post_data)
                print(lspr)
                print("\n")

            if tag.tag == "JourneyMonitoringDelivery" and lspr != '':

                #print(post_data)
                res = time_next_stop(post_data, lspr)
                print("Heure d'arrivée prévue : ")
                print(res[0])
                print("Heure d'arrivée éstimé : ")
                print(res[1])
        
            print("############################################################################################################")
        
        
        
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
            if tag.findall("VehicleActivity/ProgressBetweenStops") is None:
                return "Error, 'ProgressBetweenStops' tag not exists"
            else:
                if tag.find("VehicleActivity/ProgressBetweenStops/PreviousCallRef") is None:
                    return "Error, 'PreviousCallRef' tag not exists"
                else:
                    if tag.find("VehicleActivity/ProgressBetweenStops/PreviousCallRef/StopPointRef") is None:
                        return "Error, 'StopPointRef' tag not exists"
                    else:
                        for elem in root.findall("./VehicleActivity/ProgressBetweenStops/PreviousCallRef/StopPointRef"):
                            if elem.text is None:
                                return "Error, 'StopPointRef' tag is empty"
                            else:
                                return elem.text


def time_next_stop(data, lspr):

    #lspr = last_stop_point_ref(data)
    #print(lspr)

    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()
    
    for tag in root.findall("."):
        if tag.tag == "JourneyMonitoringDelivery":

            position = 0
            for elem in root.findall("./MonitoredJourney/OnwardCalls/OnwardCall"):
                print("passage ici")
                print(elem[0].text)
                # elem[0] correspond à la balise StopPointRef
                if elem[0].text != lspr:
                    print(position)
                    position +=1
                    print(position)
                else:
                    if elem[0].text == lspr:
                        print("passage là")
                        for elem in root.findall("./MonitoredJourney/OnwardCalls"):
                            print("passage là aussi")
                            # elem[2] correspond à la balise PlannedArrivalTime et elem[3] correspond à la balise ExpectedArrivalTime
                            return (elem[position +1][2], elem[position +1][3])
                    else:
                        return "Error, lspr n'existe pas"

                    


                    


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
