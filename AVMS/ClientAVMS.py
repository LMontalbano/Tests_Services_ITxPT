import socket
import requests
import http.client



###################Client##################
TCP_IP = "127.0.0.1"
TCP_PORT = 8000

with open('xml_RunMonitoring_Sub.xml', "rb") as file:
        rxml = file.read(4096)

connection = http.client.HTTPConnection('127.0.0.1', 8000)
print(connection)

#r = requests.post("192.168.0.10", data = rxml)
