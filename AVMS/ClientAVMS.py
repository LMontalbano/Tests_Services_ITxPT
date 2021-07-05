import requests


###################Client##################
ADDRESS = "http://127.0.0.1"
PORT = 8000

with open('xml_RunMonitoring_Sub.xml', "rb") as file:
    rxml = file.read(4096)


print('\n' + '##### rxml #####')
print(rxml.decode())

headers = {
        "Content-Length": "",
        "Accept-Encoding": "identity",
        "Host": "127.0.0.1:8000",
        "Content-Type": "text/xml"
    }

r0 = requests.post(ADDRESS + ':' + PORT + "/avms/runmonitoring", data= rxml, headers= headers)
#r1 = requests.post(ADDRESS + ':' + PORT + "/avms/plannedpattern", data= rxml, headers= headers)
#r2 = requests.post(ADDRESS + ':' + PORT + "/avms/patternmonitoring", data= rxml, headers= headers)
#r3 = requests.post(ADDRESS + ':' + PORT + "/avms/vehiclemonitoring", data= rxml, headers= headers)
#r4 = requests.post(ADDRESS + ':' + PORT + "/avms/journeymonitoring", data= rxml, headers= headers)
#r5 = requests.post(ADDRESS + ':' + PORT + "/avms/generalmessage", data= rxml, headers= headers)
#r6 = requests.post(ADDRESS + ':' + PORT + "/avms/connectionmonitoring", data= rxml, headers= headers)

print('###############################################################################')
print(r0.request.headers)
print('###############################################################################')

print(r0.status_code) # doit répondre 200
print(r0.status_code == requests.codes.ok) # doit répondre True

print('##### reponse #####')
print(r0.text)
#print(r1.text)
#print(r2.text)
#print(r3.text)
#print(r4.text)
#print(r5.text)
#print(r6.text)




