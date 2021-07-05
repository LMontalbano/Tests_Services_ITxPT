import requests


###################Client##################
ADDRESS = "http://127.0.0.1"
PORT = 8000

with open('xml_RunMonitoring_Unsub.xml', "rb") as file:
    rxml = file.read(4096)


print('\n' + '##### rxml #####')
print(rxml.decode())

headers = {
        "Content-Length": "",
        "Accept-Encoding": "identity",
        "Host": "127.0.0.1:8000",
        "Content-Type": "text/xml"
    }

r = requests.post(ADDRESS + ':' + PORT + "/avms/runmonitoring", data= rxml, headers= headers)


print('###############################################################################')
print(r.request.headers)
print('###############################################################################')

print(r.status_code) # doit répondre 200
print(r.status_code == requests.codes.ok) # doit répondre True

print('##### reponse #####')
print(r.text)




