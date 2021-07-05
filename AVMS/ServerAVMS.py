import http.server
#import socketserver

PORT = 8000
SERV_ADDRESS = ("", PORT)


server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

print("Serveur actif sur le port : {}".format(PORT))

httpd = server(SERV_ADDRESS, handler)
httpd.serve_forever()






















#SERVER WEB AVEC SOCKET
#Handler = socketserver.StreamRequestHandler

#with socketserver.TCPServer(('', PORT), Handler) as tcp_server:
    #print(tcp_server)
    #tcp_server.serve_forever()
    #print("Recieved one request from {Handler.client_address[0]}")
    #res = Handler.rfile.readline().strip()
    #print("Data Recieved from client is: {res}")
    #print(res)
    
#SERVER WEB AVEC SOCKET 
#class RequestHandler(socketserver.StreamRequestHandler):
    #def handle(self):
        #print("Receive one request from {}".format(self.client_address[0]))
        #msg = self.rfile.readline().strip()
        #print("Data Recieved from client is:".format(msg))

#server = socketserver.TCPServer(("127.0.0.1", 8000), RequestHandler)

#server.serve_forever()



    