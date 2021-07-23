import tkinter as tk
import sys


class PrintLogger:  # create file like object
    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text)  # write text to textbox
        # could also scroll to end of textbox here to make sure always visible

    def flush(self):  # needed for file like object
        pass


if __name__ == '__main__':
    import ntplib
    import time
    import sys
    import logging
    import socket


    def get_network_time(ntp_server='pool.ntp.org'):
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


    def run_ntp(server):

        logger = logging.getLogger()

        try:
            print(get_network_time(server))

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



    root = tk.Tk()
    t = tk.Text()
    t.pack()

    # create instance of file like object
    pl = PrintLogger(t)
    # replace sys.stdout with our object
    sys.stdout = pl

    i = 0
    x = 3
    while i < x:
        i += 1
        root.after(1000, run_ntp(server='10.15.2.13'))

    root.mainloop()


