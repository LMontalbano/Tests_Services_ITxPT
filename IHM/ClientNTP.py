import ntplib
import time
import sys
import logging
import socket


def get_network_time(ntp_server):
    """ Fonction pour récupérer l'heure à partir d'un server NTP
        Nom fonction: get_network_time()
        Paramètre: server, un server NTP, par défaut 'pool.ntp.org'
        Return: une date sous la forme : 'Jour Mois NumJour Heure:Min:Sec Année en UTC +0' """

    # Création d'un client via la librairie ntplib
    c = ntplib.NTPClient()

    # Requête au server ntp
    response = c.request(ntp_server)

    # Récupération de la réponse
    ts = response.tx_time

    # time.ctime convertie une date/heure exprimée en sec depuis epoch (1er janvier 1970 00:00:00 UTC +0) en date
    return time.ctime(ts)


def main_ntp(server):

    # Configuration du logging
    logging.basicConfig(filename="std.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Création et configuration d'un handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    try:
        logger.info(get_network_time(server))
        logger.removeHandler(handler)

    # Si la fonction retourne une NTPException
    except ntplib.NTPException:
        logging.basicConfig(filename="std.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        logger.error("Error NTPException")
        logger.removeHandler(handler)

    # Si la fonction retourne une socket.gaierror
    except socket.gaierror:
        # Indique sur la console que la connexion au server NTP à fail et de rentrée une address NTP valide

        # Enregistrement de l'erreur dans le fichier std.log
        logging.basicConfig(filename="std.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        logger.warning("Failed address lookup")
        logger.removeHandler(handler)

    logger.removeHandler(handler)
