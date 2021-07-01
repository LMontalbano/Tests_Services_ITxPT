import requests
import http.client



###################Client##################
ADDRESS = "http://127.0.0.1"
PORT = 8000

with open('xml_RunMonitoring_Sub.xml', "rb") as file:
    rxml = file.read(4096)

connection = http.client.HTTPConnection(ADDRESS, PORT)
print('##### connection #####')
print(connection)

print('\n' + '##### rxml #####')
print(rxml.decode())

r = requests.post(ADDRESS + "/avms/runmonitoring", data= rxml)

print('##### reponse #####')
print(r.text)




