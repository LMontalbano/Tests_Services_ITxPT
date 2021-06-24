import socket
import time

IP_SERV = '127.0.0.1'
PORT_SERV = 5005
server_address = (IP_SERV, PORT_SERV)

IP_CLI = '127.0.0.1'
PORT_CLI = 5004
client_adress = (IP_CLI, PORT_CLI)

t = 1

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(server_address)

print("Server is running...")
while True:
    with open('test.xml', "rb") as file:
        data = file.read(1024)
    s.sendto(data, client_adress)
    print(data)
    
    time.sleep(t)