# on commence toujours par importer le module tkinter
# ici on lui donne le surnom (alias) de tk

from tkinter import *
import os
import subprocess as sub

# il suffit alors de déclarer l'objet Tk() qui deviendra la fenêtre principale

fenetre = Tk(className='Test_services_ITxPT')
fenetre.geometry("750x375")


# on crée ensuite un objet Label() rattaché à fenetre pour afficher du texte non éditable
# on profite du constructeur de l'objet pour définir un texte "Hello World" dans la foulée (on peut faire autrement)


# pour finir, on lance la boucle programme

def close():
    fenetre.destroy()


def ntp_window():
    window = Toplevel(fenetre)
    window.title("test_services_ITxPT - Test NTP")
    window.geometry('376x188')
    Label(window, text="Test NTP...").pack
    start_button = Button(window, text="Démarer le test", command=run_ntp)
    start_button.pack()


def ntp():
    ntp_window()
    change_text_button_ntp()


def change_text_button_ntp():
    NTP_button['text'] = 'Test NTP en cours...'


def run_ntp():
    os.system('py C:/Users/lmontalbano/Documents/Codes/Clients_Service_ITxPT/NTP/ClientNTP.py')


def close_ntp():
    os.system(close)


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
