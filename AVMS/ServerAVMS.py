import http.server

PORT = 8000
SERV_ADDRESS = ("", PORT)


server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

print("Serveur actif sur le port : {}".format(PORT))

httpd = server(SERV_ADDRESS, handler)
httpd.serve_forever()



    