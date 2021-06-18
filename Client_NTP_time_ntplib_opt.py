import ntplib
import time
import sys
import getopt


def get_network_time(x='pool.ntp.org'):
    #start = time.time()
    c = ntplib.NTPClient()
    response = c.request(x)
    ts = response.tx_time
    return time.ctime(ts)


if __name__ == "__main__":
    
    x = sys.argv[1:][0]
    print('récupération de: ')
    print(x)
    
    # t en second car on l'utilise pour le time.sleep()
    t = 2
    # boucle à True pour faire une boucle infinie
    boucle = True

    while boucle:
        print(get_network_time(x))
        # time.sleep(t) permet de freeze le programme pendant une période t sec
        time.sleep(t)