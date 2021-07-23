import ast
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

        def parse_sub_unsub(data):
            """ Fonction pour parse un stream xml
                Nom fonction: parse_sub_unsub
                Paramètre: data, un flux xml
                Return: un string avec le Client-IP-Address, le ReplyPort et le ReplyPath"""

            print(data.decode())
            ip_address = ''
            reply_port = ''
            reply_path = ''

            tree = ET.ElementTree(ET.fromstring(data))
            root = tree.getroot()

            # Parcours le plus haut node
            for tag in root.findall("."):
                print('for')
                if tag.tag == "SubscribeRequest":
                    print('if tag.tag')
                    if tag.find("Client-IP-Address") is None:
                        print("Error, 'Client-IP-Address' tag not exists")
                    else:
                        if tag.find("Client-IP-Address").text is None:
                            print("Error, 'Client-IP-Address' tag is empty")
                        else:
                            ip_address = tag.find("Client-IP-Address").text
                        print(ip_address)

                    if tag.find("ReplyPort") is None:
                        print("Error, 'ReplyPort' tag not exists")
                    else:
                        if tag.find("ReplyPort").text is None:
                            print("Error, 'ReplyPort' tag is empty")
                        else:
                            reply_port = tag.find("ReplyPort").text
                    if tag.find("ReplyPath") is None:
                        print("Error, 'ReplyPath' tag not exists")
                    else:
                        if tag.find("ReplyPath").text is None:
                            print("Error, 'ReplyPath' tag is empty")
                        else:
                            reply_path = tag.find("ReplyPath").text

                    print(ip_address + ', ' + reply_port + ', ' + reply_path)
                    sub = ip_address, reply_port, reply_path

                    with open('Sub_Unsub/Dict_Sub_Unsub.txt', "r") as file:
                        readfile = file.readlines()
                    if str(sub) not in readfile:
                        with open('Sub_Unsub/Dict_Sub_Unsub.txt', "w") as sub_file:
                            sub_file.write(str(sub))
                            sub_file.write("\n")

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
                        lines = file.readlines()
                        for elem in lines:
                            # Convert String to Tuple
                            elem = ast.literal_eval(elem)

                            print('Elem : ')
                            print(elem)
                            headers["Host"] = elem[0] + ':' + elem[1]
                            r0 = requests.post(elem[0] + ':' + elem[1] + elem[2], data=xml_to_send0, headers=headers)
                            r1 = requests.post(elem[0] + ':' + elem[1] + elem[2], data=xml_to_send1, headers=headers)
                            print(r0)
                            print(r1)

                else:
                    if tag.tag == "UnsubscribeRequest":
                        print('if tag.tag')
                        if tag.find("Client-IP-Address") is None:
                            print("Error, 'Client-IP-Address' tag not exists")
                        else:
                            if tag.find("Client-IP-Address").text is None:
                                print("Error, 'Client-IP-Address' tag is empty")
                            else:
                                ip_address = tag.find("Client-IP-Address").text
                            print(ip_address)

                        if tag.find("ReplyPort") is None:
                            print("Error, 'ReplyPort' tag not exists")
                        else:
                            if tag.find("ReplyPort").text is None:
                                print("Error, 'ReplyPort' tag is empty")
                            else:
                                reply_port = tag.find("ReplyPort").text
                        if tag.find("ReplyPath") is None:
                            print("Error, 'ReplyPath' tag not exists")
                        else:
                            if tag.find("ReplyPath").text is None:
                                print("Error, 'ReplyPath' tag is empty")
                            else:
                                reply_path = tag.find("ReplyPath").text

                        print(ip_address + ', ' + reply_port + ', ' + reply_path)
                        unsub = ip_address, reply_port, reply_path

                        # Récupération des lignes du Dict_Sub_Unsub
                        with open("Sub_Unsub/Dict_Sub_Unsub.txt", "r") as file:
                            lines = file.readlines()
                        with open("Sub_Unsub/Dict_Sub_Unsub.txt", "w") as file:
                            for line in lines:
                                # Si la ligne n'est pas égale à l'élement que l'on veut supprimer on la réécrit
                                # (ce qui permet de réécrire toute les lignes sauf celle que l'on veut supprimer
                                if line.strip("\n") != unsub:
                                    file.write(line)

                        with open('Reponse_XML/reponse_Unsub.xml', 'r') as file:
                            xml_unsub = file.read(4096)

                        # unsub = ast.literal_eval(unsub)

                        headers = {
                            "Content-Length": "",
                            "Accept-Encoding": "identity",
                            "Host": unsub[0] + ':' + unsub[1],
                            "Content-Type": "text/xml"
                        }

                        r = requests.post(unsub[0] + ':' + unsub[1] + unsub[2], data=xml_unsub, headers=headers)

                        print(r)

        # Récupération de la taille des données
        content_length = int(self.headers['Content-Length'])

        # Récupération des données
        post_data = self.rfile.read(content_length)

        parse_sub_unsub(post_data)


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
