import ntplib
import time
import argparse

    
def get_network_time(x):
    #start = time.time()
    c = ntplib.NTPClient()
    response = c.request(x)
    ts = response.tx_time
    return time.ctime(ts)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pool.ntp.org")
    args = parser.parse_args()

    if args.pool.ntp.org:
        x = "pool.ntp.org"
        
        
    parser = argparse.ArgumentParser()
    parser.add_argument("ntp.midway.ovh")
    args = parser.parse_args()

    if args.pool.ntp.org:
        x = "ntp.midway.ovh"
        
        
    parser = argparse.ArgumentParser()
    parser.add_argument("ntp.unice.fr")
    args = parser.parse_args()

    if args.pool.ntp.org:
        x = "ntp.unice.fr"


    # t en second car on l'utilise pour le time.sleep()
    t = 2
    # boucle à True pour faire une boucle infinie
    boucle = True

    while boucle:
        print(get_network_time(x))
        # time.sleep(t) permet de freeze le programme pendant une période t sec
        time.sleep(t)