import socket
import time

command = 'test.xml'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 54239))

s.send(command)

time.sleep(2)
resp = s.recv(3000)

print(resp)