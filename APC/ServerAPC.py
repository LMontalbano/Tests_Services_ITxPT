from http.server import HTTPServer, BaseHTTPRequestHandler
import xml.etree.ElementTree as ET
import requests


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
            Return : """

        def parse_sub_unsub():
            """ Fonction pour parse un stream xml
                Nom fonction: parse_sub_unsub
                Paramètre: data, un flux xml
                Return: un string avec le Client-IP-Address, le ReplyPort et le ReplyPath"""

            ipaddress = ''
            replyport = ''
            replypath = ''

            if tag.find("Client-IP-Address") is None:
                return "Error, 'Client-IP-Address' tag not exists"
            else:
                for ip in root.findall("./SubscribeRequest/Client-IP-Address"):
                    if ip.text is None:
                        return "Error, 'Client-IP-Address' tag is empty"
                    else:
                        ipaddress = ip.text
            if tag.find("ReplyPort") is None:
                return "Error, 'ReplyPort' tag not exists"
            else:
                for port in root.findall("./SubscribeRequest/ReplyPort"):
                    if port.text is None:
                        return "Error, 'ReplyPort' tag is empty"
                    else:
                        replyport = port.text
            if tag.find("ReplyPath") is None:
                return "Error, 'ReplyPath' tag not exists"
            else:
                for path in root.findall("./SubscribeRequest/ReplyPath"):
                    if path.text is None:
                        return "Error, 'ReplyPath' tag is empty"
                    else:
                        replypath = path.text

            return ipaddress + ', ' + replyport + ', ' + replypath

        # Récupération de la taille des données
        content_length = int(self.headers['Content-Length'])

        # Récupération des données
        post_data = self.rfile.read(content_length)

        # Création du tree et récupération de la root
        tree = ET.ElementTree(ET.fromstring(post_data))
        root = tree.getroot()

        # Parcours le plus haut node
        for tag in root.findall("."):

            if tag.tag == "SubscribeRequest":
                sub = parse_sub_unsub()

                with open('Sub_Unsub/Dict_Sub_Unsub.txt', "r") as file:
                    readfile = file.readlines()
                if sub not in readfile:
                    with open('Sub_Unsub/Dict_Sub_Unsub.txt', "w") as sub_file:
                        sub_file.write(sub + "\n")

                with open('Reponse_XML/reponse200OK.xml', "r") as a_file:
                    xml_to_send0 = a_file.read(4096)
                with open('ExempleXML/PassengerVehicleCountDelivery.xml', "r") as d_file:
                    xml_to_send1 = d_file.read(4096)

                headers = {
                    "Content-Length": "",
                    "Accept-Encoding": "identity",
                    "Host": "",
                    "Content-Type": "text/xml"
                }

                with open('Sub_Unsub/Dict_Sub_Unsub.txt', "r") as file:
                    for elem in file:
                        # Convert String to Tuple
                        elem = eval(elem)
                        headers["Host"] = elem[0] + ':' + elem[1]
                        r0 = requests.post(elem[0] + ':' + elem[1] + elem[2], data=xml_to_send0, headers=headers)
                        r1 = requests.post(elem[0] + ':' + elem[1] + elem[2], data=xml_to_send1, headers=headers)

                        print(r0)
                        print(r1)
            else:
                sub = parse_sub_unsub()

                # Récupération des lignes du Dict_Sub_Unsub
                with open("Sub_Unsub/Dict_Sub_Usunb", "r") as file:
                    lines = file.readlines()
                with open("Sub_Unsub/Dict_Sub_Unsub.txt", "w") as file:
                    for line in lines:
                        # Si la ligne n'est pas égale à l'élement que l'on veut supprimmer on la réécrie
                        # (ce qui permet de réécrire toute les lignes sauf celle que l'on veut supprimmer
                        if line.strip("\n") != sub:
                            file.write(line)

                with open('Reponse_XML/reponse_Unsub.xml', 'r') as file:
                    xml_unsub = file.read(4096)

                xml_unsub = eval(xml_unsub)

                headers = {
                    "Content-Length": "",
                    "Accept-Encoding": "identity",
                    "Host": elem[0] + ':' + elem[1],
                    "Content-Type": "text/xml"
                }

                r = requests.post(elem[0] + ':' + elem[1] + elem[2], data=xml_unsub, headers=headers)

                print(r)


def run(server_class=HTTPServer, handler_class=Server, addr='localhost', port=9000):
    """ Fonction qui permet de run le serveur
        Paramètres: server_class: , handler_class: la class Server par défaut, addr: localhost, port: 8000
        Return: Ne retourne rien, permet de faire tourner le serveur"""

    # Initialisation du server_address via les paramètre addr et port de la fonction
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    ADDRESS = "http://127.0.0.1"
    PORT = 9000

    # Lancement du server
    run(addr=ADDRESS, port=PORT)
