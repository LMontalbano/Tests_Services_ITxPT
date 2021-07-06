import requests

###################Client##################
ADDRESS = "http://127.0.0.1"
PORT = 8000

with open('Sub_Unsub/RunMonitoring_Sub.xml', "rb") as file:
    rxml0 = file.read(4096)

with open('Sub_Unsub/PlannedPattern_Sub.xml', "rb") as file:
    rxml1 = file.read(4096)

with open('Sub_Unsub/VehicleMonitoring_Sub.xml', "rb") as file:
    rxml2 = file.read(4096)

with open('Sub_Unsub/JourneyMonitoring_Sub.xml', "rb") as file:
    rxml3 = file.read(4096)

with open('Sub_Unsub/GeneralMessage_Sub.xml', "rb") as file:
    rxml4 = file.read(4096)

with open('Sub_Unsub/PatternMonitoring_Sub.xml', "rb") as file:
    rxml5 = file.read(4096)


print('\n' + '##### rxml #####')
print(rxml0.decode())

headers = {
        "Content-Length": "",
        "Accept-Encoding": "identity",
        "Host": "192.168.0.10:8000",
        "Content-Type": "text/xml"
    }

r0 = requests.post(ADDRESS + ':' + PORT + "/avms/runmonitoring", data= rxml0, headers= headers)
r1 = requests.post(ADDRESS + ':' + PORT + "/avms/plannedpattern", data= rxml1, headers= headers)
r2 = requests.post(ADDRESS + ':' + PORT + "/avms/vehiclemonitoring", data= rxml2, headers= headers)
r3 = requests.post(ADDRESS + ':' + PORT + "/avms/journeymonitoring", data= rxml3, headers= headers)
r4 = requests.post(ADDRESS + ':' + PORT + "/avms/generalmessage", data= rxml4, headers= headers)
r5 = requests.post(ADDRESS + ':' + PORT + "/avms/patternmonitoring", data= rxml5, headers= headers)

print('###############################################################################')
#print(r0.request.headers)
print('###############################################################################')

#print(r0.status_code) # doit répondre 200
#print(r0.status_code == requests.codes.ok) # doit répondre True

#print('##### reponse #####')
#print(r0.text)
#print(r1.text)
#print(r2.text)
#print(r3.text)
#print(r4.text)
#print(r5.text)




