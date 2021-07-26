import threading
from tkinter import *
import tkinter as tk
import sys
# from NTP import ClientNTP
from Trials import ClientNTP
# from GNSS import ClientGNSS
from Trials import ClientGNSS
# from AVMS import ClientAVMS, ServerAVMS
from Trials import ClientAVMS, ServerAVMS

# from Trials import ServerAPC
# from APC import ServerAPC


# Création de la fenêtre principale
fenetre = Tk(className='Test_services_ITxPT')
fenetre.geometry("750x375")

address_label = Label(fenetre, text="Adresse IP : ")
address_label.pack()

server = tk.StringVar(value='pool.ntp.org')

address_input = Entry(textvariable=server)
address_input.pack()


######################################### Class utiles ###############################################
class PrintLogger:  # create file like object
    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text)  # write text to textbox
        # could also scroll to end of textbox here to make sure always visible

    def flush(self):  # needed for file like object
        pass


class ThreadNTP(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        sec = 0
        num_lines = 0
        if t.compare("end-1c", "!=", "1.0"):
            print("\n")
        print("########## Test NTP ##########")
        # Affichage du server NTP sur lequel le programme va récupérer l'heure
        if server.get() == "":
            print("Please enter a NTP server")
        else:
            print('Server: ' + server.get())
            while sec < self.thread_time:
                fenetre.after(1000, ClientNTP.main_ntp(server.get()))
                num_lines = sum(1 for _ in open("std.log"))
                n = 0
                fail = False
                with open("std.log") as f:
                    if num_lines <= 1:
                        if 'Failed' in f.readline():
                            sec = self.thread_time
                            print('Please enter a valide NTP server')
                            fail = True
                    else:
                        for line in f:
                            if n == num_lines - 1:
                                if 'Failed' in line:
                                    sec = self.thread_time
                                    print('Please enter a valide NTP server')
                                    fail = True
                            n += 1

                    sec += 1

            err = 0
            with open("std.log") as f:
                if 'Failed' not in f.readlines()[num_lines - 1]:
                    x = num_lines
                    num_lines -= 1
                    while num_lines >= x - 5:
                        f.seek(0)
                        if 'Error' in f.readlines()[num_lines] and fail is False:
                            err += 1
                        num_lines -= 1

                    if err < 1:
                        print("Test OK" + " " + u'\u2713')
                    else:
                        print("Test Fail !!!")

        change_back_button_ntp()
        t.config(state=DISABLED)
        NTP_button.config(state=NORMAL)


########################################### NTP ##############################################

def ntp():
    change_text_button_ntp()
    main_ntp()


def main_ntp():
    t.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    # create instance of file like object
    pl = PrintLogger(t)
    # replace sys.stdout with our object
    sys.stdout = pl

    test_time = 5
    thread1 = ThreadNTP(test_time)
    thread1.start()


def change_text_button_ntp():
    NTP_button['text'] = 'Test NTP en cours...'


def change_back_button_ntp():
    NTP_button['text'] = 'Test NTP'


NTP_button = Button(fenetre, text="Test NTP", command=ntp)
NTP_button.pack()


##################################### GNSS ################################################

def gnss():
    change_text_button_gnss()
    main_gnss()


def main_gnss():
    ClientGNSS.main_gnss()


def change_text_button_gnss():
    GNSS_button['text'] = 'Test GNSS en cours...'


def change_back_button_gnss():
    GNSS_button['text'] = 'Test GNSS'


GNSS_button = Button(fenetre, text="Test GNSS", command=gnss)
GNSS_button.pack()


###################################### AVMS #################################################

def avms():
    change_text_button_avms()
    main_avms()


def main_avms():
    # Faire un Thread ici pour pouvoir lancer en parallèle le Server et le Client
    ServerAVMS.main_serv_avms()
    ClientAVMS.main_cli_avms()


def change_text_button_avms():
    AVMS_button['text'] = 'Test GNSS en cours...'


def change_back_button_avms():
    AVMS_button['text'] = 'Test GNSS'


AVMS_button = Button(fenetre, text="Test AVMS", command=avms)
AVMS_button.pack()


####################################### APC ##################################################

def apc():
    pass


def main_apc():
    pass





APC_button = Button(fenetre, text="Test APC", command=apc)
APC_button.pack()

###################################### Fenêtre principale ####################################
t = tk.Text(state=DISABLED)
t.pack()


# fonction pour close la fenêtre
def close():
    fenetre.destroy()


# Bouton 'Fermer'
Close_button = Button(fenetre, text="Fermer", command=close, width=50, bg='red')
Close_button.pack()

# Pour finir, on lance la boucle programme
fenetre.mainloop()
