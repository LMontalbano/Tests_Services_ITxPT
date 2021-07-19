import ntplib
import time
import sys
import logging
import socket


def get_network_time(server='pool.ntp.org'):
    
    """ Fonction pour récupérer l'heure à partir d'un server NTP
        Nom fonction: get_network_time()
        Paramètre: server, un server NTP, par défaut 'pool.ntp.org'
        Return: une date sous la forme : 'Jour Mois NumJour Heure:Min:Sec Annee en UTC +0' """
    
    # Création d'un client via la librairie ntplib
    c = ntplib.NTPClient()
    
    # Requette au server ntp
    response = c.request(server)
    
    # Récupération de la réponse
    ts = response.tx_time
    
    # time.ctime convertie une date/heure exprimée en sec depuis epoch (1er janvier 1970 00:00:00 UTC +0) en date
    return time.ctime(ts)




if __name__ == "__main__":

    # Récupération du server NTP passer en argument
    if len(sys.argv[1:]) == 1:
        server = sys.argv[1:][0]
                
    else:
    # Création d'un input demandant à l'utilisateur de rentrer un server NTP    
        print('Please enter an NTP server: ')
        server = input()
        
    # Temps d'attente en second avant de reprendre le programme (utilisée avec le time.sleep())
    t = 1
    
    # Affichage du server NTP sur lequel le programme va récupérer l'heure
    print('Server: ' + server)
    
    
    # Boucle infinie 
    while True:
        logger = logging.getLogger()
        
        try:
            print(get_network_time(server))
            
            # time.sleep(t) permet de freeze le programme pendant une période t sec
            time.sleep(t)
            
        # Si la fonction retourne une NTPException    
        except ntplib.NTPException:
            print("Error NTPException")
            # Enregistrement de l'erreur dans le fichier std.log
            logging.basicConfig(filename="std.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')
            logger.error("Error NTPException")
        
        # Si la fonction retourne une socket.gaierror    
        except socket.gaierror:
            # Indique sur la console que la connexion au server NTP à fail et de rentrée une address NTP valide
            print("Failed address lookup")
            print('Please enter an NTP server: ')
            server = input()
            
            # Enregistrement de l'erreur dans le fichier std.log
            logging.basicConfig(filename="std.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')
            logger.warning("Failed address lookup")