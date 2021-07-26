# on commence toujours par importer le module tkinter
# ici on lui donne le surnom (alias) de tk

from tkinter import *
import os
import sys

from ClientNTP import run_ntp, get_network_time

# il suffit alors de déclarer l'objet Tk() qui deviendra la fenêtre principale

fenetre = Tk(className='Test_services_ITxPT')
fenetre.geometry("750x375")


# on crée ensuite un objet Label() rattaché à fenetre pour afficher du texte non éditable
# on profite du constructeur de l'objet pour définir un texte "Hello World" dans la foulée (on peut faire autrement)


def close():
    fenetre.destroy()


def ntp():
    run_ntppp()


def change_text_button_ntp():
    NTP_button['text'] = 'Test NTP en cours...'


def run_ntppp():
    change_text_button_ntp()

    ############### Faire Apparaitre une fenêtre test en cours ###############




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
            fenetre.after(1000, run_ntp(server='10.15.2.13'))

        fenetre.mainloop()


def gnss():
    os.system('py C:/Users/lmontalbano/Documents/Codes/Clients_Service_ITxPT/GNSS/ClientGNSS.py')


def avms():
    os.system('py C:/Users/lmontalbano/Documents/Codes/Clients_Service_ITxPT/AVMS/ServerAVMS.py')
    os.system('py C:/Users/lmontalbano/Documents/Codes/Clients_Service_ITxPT/AVMS/ClientAVMS.py')


def apc():
    pass


NTP_button = Button(fenetre, text="Test NTP", command=ntp)
NTP_button.pack()

GNSS_button = Button(fenetre, text="Test GNSS", command=gnss)
GNSS_button.pack()

AVMS_button = Button(fenetre, text="Test AVMS", command=avms)
AVMS_button.pack()

APC_button = Button(fenetre, text="Test APC", command=apc)
APC_button.pack()

label = Label(fenetre)
label.pack()

Close_button = Button(fenetre, text="Fermer", command=close, width=50, bg='red')
Close_button.pack()

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=change_text_button_ntp)
menu1.add_command(label="Editer", command=change_text_button_ntp)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=change_text_button_ntp)
menu2.add_command(label="Copier", command=change_text_button_ntp)
menu2.add_command(label="Coller", command=change_text_button_ntp)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=change_text_button_ntp)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

# pour finir, on lance la boucle programme
fenetre.mainloop()
