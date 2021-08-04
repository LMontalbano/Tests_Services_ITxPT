import threading
import time
from tkinter import *
import tkinter as tk
from PIL import ImageTk
import webbrowser
import sys
import ClientNTP
import ClientGNSS
import ClientAVMS
import ServerAVMS

######################### Création de la fenêtre principale #########################
fenetre = Tk(className='test_services_ITxPT')
fenetre.geometry("910x635")
fenetre.iconbitmap("ressources/ITxPT_logo.ico")


### Création des Labels ###
label_principale = LabelFrame(fenetre)
label_principale.grid(row=0, column=1, padx=50, pady=10)

label_input = LabelFrame(label_principale)
label_input.grid(row=0, column=1, padx=50, pady=10)

label_logo = LabelFrame(label_principale)
label_logo.grid(row=0, column=2, padx=50, pady=10)

label_button = LabelFrame(fenetre)
label_button.grid(row=1, column=1, padx=50, pady=10)

label_console = LabelFrame(fenetre)
label_console.grid(row=2, column=1, padx=50, pady=10)


### Création des input ###
# Address Local
address_label_LOCAL = Label(label_input, text="Local Address : ")
address_label_LOCAL.grid(column=1, row=1)

local = tk.StringVar(value='127.0.0.1')

address_input_LOCAL = Entry(label_input, textvariable=local)
address_input_LOCAL.grid(column=2, row=1, padx=5, pady=5)

# Address SAE
address_label_SAE = Label(label_input, text="SAE Address : ")
address_label_SAE.grid(column=1, row=2)

server = tk.StringVar(value='127.0.0.1')

address_input_SAE = Entry(label_input, textvariable=server)
address_input_SAE.grid(column=2, row=2, padx=5, pady=5)


### Logo Keolis ###
img = ImageTk.PhotoImage(file="ressources/logo_Keolis_metropole_orleans.png")
p1 = Label(label_logo, image=img)
p1.config(width=190, height=50)
p1.grid(column=3, row=1)


### Création du lien vers le github ###
def callback(url):
    """ Fonction qui permet d'ouvrir un url sur un navigateur
        Paramètre : url, un string
        Return : Rien
    """
    webbrowser.open_new(url)


link = Label(fenetre, text="https://github.com/LMontalbano/Clients_Service_ITxPT", fg="blue", cursor="hand2")
link.grid(row=5, column=1)
link.bind("<Button-1>", lambda e: callback("https://github.com/LMontalbano/Clients_Service_ITxPT"))


######################### Fonctions run #########################
def run_ntp(temps, tous):
    """ Fonction qui permet de lancer le test NTP
        Paramètres : temps, un int et tous un boolean
        Return : un tuple de int, (nb_test, test_ok)
    """
    # Initialisation des variables
    sec = 0
    num_lines = 0
    thread_time = temps
    test_ok = 0
    nb_test = 0

    if tous:
        change_text_button_ntp()
        if text_console.compare("end-1c", "!=", "1.0"):
            print("\n")
        print("############### All Tests Started... ###############")
        time.sleep(1)

    if text_console.compare("end-1c", "!=", "1.0"):
        print("\n")
    print("########## Test NTP ##########")

    if server.get() == "":
        print("Please enter a NTP server")
    else:
        print('Server: ' + server.get())
        while sec < thread_time:
            fenetre.after(1000, ClientNTP.main_ntp(server.get()))
            num_lines = sum(1 for _ in open("std.log"))
            n = 0
            fail = False
            with open("std.log") as f:
                if num_lines <= 1:
                    if 'Failed' in f.readline():
                        sec = thread_time
                        print('Please enter a valide NTP server')
                        fail = True
                else:
                    for line in f:
                        if n == num_lines - 1:
                            if 'Failed' in line:
                                sec = thread_time
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
                    print("Test NTP OK" + " " + u'\u2713')
                    if tous:
                        test_ok += 1

                else:
                    print("Test NTP Failed !!!")
    if tous:
        nb_test += 1

    res = nb_test, test_ok
    setup_end_ntp()

    return res


def run_gnss(temps, tous, nb_test, test_ok):
    """ Fonction qui permet de lancer le test GNSS
        Paramètres : 'temps' un int, 'tous' un boolean, 'nb_test' un int et 'test_ok' un int
        Return : un tuple de int, (nb_test, test_ok)
    """
    # Initialisation des variables
    thread_time = temps
    sec = 0
    nb_test = nb_test
    test_ok = test_ok

    if tous:
        change_text_button_gnss()

    if text_console.compare("end-1c", "!=", "1.0"):
        print("\n")
    print("########## Test GNSS ##########")

    if server.get() == "":
        print("Please enter a GNSS server")
    else:
        print('Server: ' + server.get())
        while sec < thread_time:
            fenetre.after(1000, ClientGNSS.main_gnss(local.get()))
            sec += 1

        err = 0
        num_lines = sum(1 for _ in open("std.log"))
        x = num_lines
        num_lines -= 1
        with open("std.log") as f:
            while num_lines >= x - 5:
                f.seek(0)
                if 'Error' in f.readlines()[num_lines]:
                    err += 1
                num_lines -= 1

        if err < 1:
            print("Test GNSS OK" + " " + u'\u2713')
            if tous:
                test_ok += 1
        else:
            print("Test GNSS Failed !!!")

    setup_end_gnss()

    if tous:
        nb_test += 1

    res = nb_test, test_ok

    return res


def run_avms(tous, nb_test, test_ok):
    """ Fonction qui permet de lancer le test AVMS
        Paramètres : 'tous' un boolean, 'nb_test' un int et 'test_ok' un int
        Return : un tuple de int, (nb_test, test_ok)
    """
    # Initialisation des variables
    ServerAVMS.cancel = False
    nb_test = nb_test
    test_ok = test_ok

    if tous:
        change_text_button_avms()
        ServerAVMS.tous = True

    if text_console.compare("end-1c", "!=", "1.0"):
        print("\n")
    print("########## Test AVMS ##########")
    print('Server: ' + server.get())
    fenetre.after(1000, ServerAVMS.main_serv_avms(local.get()))

    err = 0
    num_lines = sum(1 for _ in open("std.log"))
    x = num_lines
    num_lines -= 1

    with open("std.log") as f:
        while num_lines >= x - 5:
            f.seek(0)
            if 'Error' in f.readlines()[num_lines]:
                err += 1
            num_lines -= 1

    if err < 1:
        print("Test AVMS OK" + " " + u'\u2713')
        if tous:
            test_ok += 1
    else:
        print("Test AVMS Failed !!!")

    if tous:
        nb_test += 1

        time.sleep(1)
        print("\n")
        print("############### All Tests Done ###############")
        print("Passed Tests : " + str(test_ok) + "/" + str(nb_test))

    ServerAVMS.tous = False
    setup_end_avms()

    if tous:
        change_back_button_global()

    res = nb_test, test_ok

    return res


def run_apc():
    """ Fonction qui permet de lancer le test APC
        Paramètres :
        Return :
    """
    print("\n")
    print("########## Test APC ##########")
    print("Not Yet Implemented")
    setup_end_apc()


######################### Class PrintLogger et Class Threads #########################
# Class pour print sur la console Tkinter
class PrintLogger:
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert(tk.END, text)
        self.textbox.see("end")

    def flush(self):
        pass


# Class du Thread du test NTP
class ThreadNTP(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        run_ntp(temps=self.thread_time, tous=False)


# Class du Thread du test GNSS
class ThreadGNSS(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        run_gnss(temps=self.thread_time, tous=False, nb_test=None, test_ok=None)


# Class du Thread Server du test AVMS
class ThreadAVMSServer(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        run_avms(tous=False, nb_test=None, test_ok=None)


# Class du Thread Client du test AVMS
class ThreadAVMSClient(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        client_avms()


# Class du Thread pour cancel le test AVMS
class ThreadAVMSCancel(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        ServerAVMS.cancel = True
        setup_end_avms()


# Class du Thread du test APC
class ThreadAPC(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        run_apc()


# Class du Thread du test global
class ThreadGlobal(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        res_ntp = run_ntp(temps=self.thread_time, tous=True)
        setup_start_gnss()
        res_gnss = run_gnss(temps=self.thread_time, tous=True, nb_test=res_ntp[0], test_ok=res_ntp[1])
        setup_start_avms()

        thread10 = ThreadAVMSClient(self.thread_time)
        thread10.start()
        run_avms(tous=True, nb_test=res_gnss[0], test_ok=res_gnss[1])


######################### NTP #########################

def ntp():
    """ Fonction qui permet de lancer le test NTP
        Paramètres : aucun
        Return : rien
    """
    change_text_button_ntp()
    main_ntp()


def setup_start_ntp():
    """ Fonction qui permet de setup l'état des différents élément du logiciel au start du test ntp
        Paramètres : aucun
        Return : rien
    """
    address_input_LOCAL.config(state=DISABLED)
    address_input_SAE.config(state=DISABLED)
    text_console.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    GNSS_button.config(state=DISABLED)
    AVMS_button.config(state=DISABLED)
    APC_button.config(state=DISABLED)
    GLOBAL_button.config(state=DISABLED)
    Cancel_AVMS_button.config(state=DISABLED)


def setup_end_ntp():
    """ Fonction qui permet de setup l'état des différents élément du logiciel a la fin du test ntp
        Paramètres : aucun
        Return : rien
    """
    change_back_button_ntp()
    address_input_LOCAL.config(state=NORMAL)
    address_input_SAE.config(state=NORMAL)
    text_console.config(state=DISABLED)
    NTP_button.config(state=NORMAL)
    GNSS_button.config(state=NORMAL)
    AVMS_button.config(state=NORMAL)
    APC_button.config(state=NORMAL)
    GLOBAL_button.config(state=NORMAL)
    Cancel_AVMS_button.config(state=DISABLED)


def main_ntp():
    """ Fonction qui va lancer le setup_start_ntp ainsi que le Thread du test
        Paramètres : aucun
        Return : rien
    """
    setup_start_ntp()

    console_tkinter = PrintLogger(text_console)
    sys.stdout = console_tkinter

    thread_time = 5
    thread_ntp = ThreadNTP(thread_time)
    thread_ntp.start()


def change_text_button_ntp():
    """ Fonction qui permet de changer le texte du bouton 'Test NTP'
        Paramètres : aucun
        Return : rien
    """
    NTP_button['text'] = 'Test NTP in progress...'


def change_back_button_ntp():
    """ Fonction qui permet de réinisiatiler le texte du bouton 'Test NTP'
        Paramètres : aucun
        Return : rien
    """
    NTP_button['text'] = 'Test NTP'


#### Création du bouton NTP ####
NTP_button = Button(label_button, text="Test NTP", command=ntp)
NTP_button.grid(column=2, row=3, ipadx=15, ipady=10, padx=5, pady=5)


######################### GNSS #########################

def gnss():
    """ Fonction qui permet de lancer le test gnss
        Paramètres : aucun
        Return : rien
    """
    change_text_button_gnss()
    main_gnss()


def setup_start_gnss():
    """ Fonction qui permet de setup l'état des différents élément du logiciel au start du test gnss
        Paramètres : aucun
        Return : rien
    """
    address_input_LOCAL.config(state=DISABLED)
    address_input_SAE.config(state=DISABLED)
    text_console.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    GNSS_button.config(state=DISABLED)
    AVMS_button.config(state=DISABLED)
    APC_button.config(state=DISABLED)
    GLOBAL_button.config(state=DISABLED)
    Cancel_AVMS_button.config(state=DISABLED)


def setup_end_gnss():
    """ Fonction qui permet de setup l'état des différents élément du logiciel a la fin du test gnss
        Paramètres : aucun
        Return : rien
    """
    change_back_button_gnss()
    address_input_LOCAL.config(state=NORMAL)
    address_input_SAE.config(state=NORMAL)
    text_console.config(state=DISABLED)
    NTP_button.config(state=NORMAL)
    GNSS_button.config(state=NORMAL)
    AVMS_button.config(state=NORMAL)
    APC_button.config(state=NORMAL)
    GLOBAL_button.config(state=NORMAL)
    Cancel_AVMS_button.config(state=DISABLED)


def main_gnss():
    """ Fonction qui va lancer le setup_start_gnss ainsi que le Thread du test
        Paramètres : aucun
        Return : rien
    """
    setup_start_gnss()

    console_tkinter = PrintLogger(text_console)
    sys.stdout = console_tkinter

    thread_time = 5
    thread_gnss = ThreadGNSS(thread_time)
    thread_gnss.start()


def change_text_button_gnss():
    """ Fonction qui permet de changer le texte du bouton 'Test GNSS'
        Paramètres : aucun
        Return : rien
    """
    GNSS_button['text'] = 'Test GNSS in progress...'


def change_back_button_gnss():
    """ Fonction qui permet de réinisiatiler le texte du bouton 'Test GNSS'
        Paramètres : aucun
        Return : rien
    """
    GNSS_button['text'] = 'Test GNSS'


#### Création du bouton GNSS ####
GNSS_button = Button(label_button, text="Test GNSS", command=gnss)
GNSS_button.grid(column=3, row=3, ipadx=15, ipady=10, padx=5, pady=5)


######################### AVMS #########################

def avms():
    """ Fonction qui permet de lancer le test avms
        Paramètres : aucun
        Return : rien
    """
    change_text_button_avms()
    main_avms()


def setup_start_avms():
    """ Fonction qui permet de setup l'état des différents élément du logiciel au start du test avms
        Paramètres : aucun
        Return : rien
    """
    address_input_LOCAL.config(state=DISABLED)
    address_input_SAE.config(state=DISABLED)
    text_console.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    GNSS_button.config(state=DISABLED)
    AVMS_button.config(state=DISABLED)
    APC_button.config(state=DISABLED)
    GLOBAL_button.config(state=DISABLED)


def setup_end_avms():
    """ Fonction qui permet de setup l'état des différents élément du logiciel a la fin du test avms
        Paramètres : aucun
        Return : rien
    """
    change_back_button_avms()
    address_input_LOCAL.config(state=NORMAL)
    address_input_SAE.config(state=NORMAL)
    text_console.config(state=DISABLED)
    NTP_button.config(state=NORMAL)
    GNSS_button.config(state=NORMAL)
    AVMS_button.config(state=NORMAL)
    APC_button.config(state=NORMAL)
    GLOBAL_button.config(state=NORMAL)
    Cancel_AVMS_button.config(state=DISABLED)


def main_avms():
    """ Fonction qui va lancer le setup_start_avms ainsi que le server_avms
        Paramètres : aucun
        Return : rien
    """
    setup_start_avms()
    server_avms()


def server_avms():
    """ Fonction qui va lancer le setup_start_ntp ainsi que le Thread du test
        Paramètres : aucun
        Return : rien
    """
    console_tkinter = PrintLogger(text_console)
    sys.stdout = console_tkinter

    thread_time = 5
    thread_server_avms = ThreadAVMSServer(thread_time)
    thread_server_avms.start()

    thread_client_avms = ThreadAVMSClient(thread_time)
    thread_client_avms.start()


def client_avms():
    """ Fonction qui permet de lancer le client_avms
        Paramètres : aucun
        Return : rien
    """
    time.sleep(1)
    ClientAVMS.main_cli_avms(server.get(), local.get())
    Cancel_AVMS_button.config(state=NORMAL)


def cancel_avms():
    """ Fonction qui permet de cancel le test avms
        Paramètres : aucun
        Return : rien
    """
    thread_time = 5
    thread_cancel_avms = ThreadAVMSCancel(thread_time)
    thread_cancel_avms.start()


def change_text_button_avms():
    """ Fonction qui permet de changer le texte du bouton 'Test AVMS'
        Paramètres : aucun
        Return : rien
    """
    AVMS_button['text'] = 'Test AVMS in progress...'


def change_back_button_avms():
    """ Fonction qui permet de réinisiatiler le texte du bouton 'Test AVMS'
        Paramètres : aucun
        Return : rien
    """
    AVMS_button['text'] = 'Test AVMS'


#### Création des boutons AVMS ####
# Bouton avms
AVMS_button = Button(label_button, text="Test AVMS", command=avms)
AVMS_button.grid(column=4, row=3, ipadx=15, ipady=10, padx=5, pady=5)

# Bouton cancel avms
Cancel_AVMS_button = Button(label_button, text="Cancel Test AVMS", command=cancel_avms)
Cancel_AVMS_button.grid(column=4, row=5, ipadx=15, ipady=10, padx=5, pady=5)
Cancel_AVMS_button.config(state=DISABLED)


######################### APC #########################

def apc():
    """ Fonction qui permet de lancer le test apc
        Paramètres : aucun
        Return : rien
    """
    main_apc()


def main_apc():
    """ Fonction qui permet de lancer le setup_start_apc et le Thread du test apc
        Paramètres : aucun
        Return : rien
    """
    setup_start_apc()

    console_tkinter = PrintLogger(text_console)
    sys.stdout = console_tkinter

    thread_time = 5
    thread_apc = ThreadAPC(thread_time)
    thread_apc.start()


def setup_start_apc():
    """ Fonction qui permet de setup l'état des différents élément du logiciel au start du test apc
        Paramètres : aucun
        Return : rien
    """
    text_console.config(state=NORMAL)


def setup_end_apc():
    """ Fonction qui permet de setup l'état des différents élément du logiciel a la fin du test apc
        Paramètres : aucun
        Return : rien
    """
    text_console.config(state=DISABLED)


#### Création du bouton APC ####
APC_button = Button(label_button, text="Test APC", command=apc)
APC_button.grid(column=5, row=3, ipadx=15, ipady=10, padx=5, pady=5)


######################### All Tests #########################

def all_tests():
    """ Fonction qui permet de lancer l'ensemble des tests
        Paramètres : aucun
        Return : rien
    """
    main_all_tests()


def setup_start_global():
    """ Fonction qui permet de setup l'état des différents élément du logiciel au start du all test
        Paramètres : aucun
        Return : rien
    """
    address_input_LOCAL.config(state=DISABLED)
    address_input_SAE.config(state=DISABLED)
    text_console.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    GNSS_button.config(state=DISABLED)
    AVMS_button.config(state=DISABLED)
    APC_button.config(state=DISABLED)
    GLOBAL_button.config(state=DISABLED)
    Cancel_AVMS_button.config(state=DISABLED)


def main_all_tests():
    """ Fonction qui permet de lancer le setup_start_global et le Thread du all test
        Paramètres : aucun
        Return : rien
    """
    setup_start_global()

    console_tkinter = PrintLogger(text_console)
    sys.stdout = console_tkinter

    thread_time = 5
    thread_global = ThreadGlobal(thread_time)
    thread_global.start()


def change_text_button_global():
    """ Fonction qui permet de changer le texte du bouton 'All Test'
        Paramètres : aucun
        Return : rien
    """
    GLOBAL_button['text'] = 'Tests in progress...'


def change_back_button_global():
    """ Fonction qui permet de réinisiatiler le texte du bouton 'All Test'
        Paramètres : aucun
        Return : rien
    """
    GLOBAL_button['text'] = 'All Tests'


#### Création du bouton All Test ####
GLOBAL_button = Button(label_button, text="All Tests", command=all_tests)
GLOBAL_button.grid(column=6, row=3, ipadx=15, ipady=10, padx=5, pady=5)


######################### Zone de texte #########################

text_console = tk.Text(label_console, width=100, height=21, state=DISABLED)
text_console.grid(column=1, row=4)


# Pour finir, on lance la boucle programme
fenetre.mainloop()
