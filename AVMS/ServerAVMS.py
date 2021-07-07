from http.server import HTTPServer, BaseHTTPRequestHandler

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
        print(post_data)
        print("\n")
        #self._set_headers()


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
