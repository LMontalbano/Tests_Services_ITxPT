import ntplib
import time
import sys
import getopt
import requests
import datetime
import logging
import socket


def get_network_time(server='pool.ntp.org'):
    #start = time.time()
    c = ntplib.NTPClient()
    response = c.request(server)
    ts = response.tx_time
    return time.ctime(ts)


if __name__ == "__main__":

    if len(sys.argv[1:]) == 1:
        server = sys.argv[1:][0]
                
    else:
        print('Please enter an NTP server: ')
        server = input()
        
    # t en second car on l'utilise pour le time.sleep()
    t = 1
    # boucle à True pour faire une boucle infinie
    boucle = True
    
    print('Server: ' + server)
    
    
    
    
    while boucle:
        logger = logging.getLogger()
        try:
            print(get_network_time(server))
            # time.sleep(t) permet de freeze le programme pendant une période t sec
            time.sleep(t)
            
        except ntplib.NTPException:
            print("Error NTPException")
            
            logging.basicConfig(filename="std.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')
            logger.error("Error NTPException")
            
        except socket.gaierror:
            print("Failed address lookup")
            print('Please enter an NTP server: ')
            server = input()
            
            logging.basicConfig(filename="std.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')
            logger.warning("Failed address lookup")
            
               
            
            
            
            