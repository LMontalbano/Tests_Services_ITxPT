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


# Création de la fenêtre principale
fenetre = Tk(className='test_services_ITxPT')
fenetre.geometry("910x650")

f0 = LabelFrame(fenetre)
f0.grid(row=0, column=1, padx=50, pady=10)

f1 = LabelFrame(fenetre)
f1.grid(row=0, column=1, padx=50, pady=10)

f11 = LabelFrame(f1)
f11.grid(row=0, column=1, padx=50, pady=10)

f12 = LabelFrame(f1)
f12.grid(row=0, column=2, padx=50, pady=10)


f2 = LabelFrame(fenetre)
f2.grid(row=1, column=1, padx=50, pady=10)

f3 = LabelFrame(fenetre)
f3.grid(row=2, column=1, padx=50, pady=10)

f4 = LabelFrame(fenetre)
f4.grid(row=3, column=1, padx=100, pady=10)

img = ImageTk.PhotoImage(file="ressources/logo_Keolis_metropole_orleans.png")
p1 = Label(f12, image=img)
p1.config(width=190, height=50)
p1.grid(column=3, row=1)

address_label_SAE = Label(f11, text="SAE Address : ")
address_label_SAE.grid(column=1, row=2)

server = tk.StringVar(value='127.0.0.1')

address_input_SAE = Entry(f11, textvariable=server)
address_input_SAE.grid(column=2, row=2, padx=5, pady=5)


address_label_LOCAL = Label(f11, text="Local Address : ")
address_label_LOCAL.grid(column=1, row=1)

local = tk.StringVar(value='127.0.0.1')

address_input_LOCAL = Entry(f11, textvariable=local)
address_input_LOCAL.grid(column=2, row=1, padx=5, pady=5)


def callback(url):
    webbrowser.open_new(url)

link1 = Label(fenetre, text="https://github.com/LMontalbano/Clients_Service_ITxPT", fg="blue", cursor="hand2")
link1.grid(row=5, column=1)
link1.bind("<Button-1>", lambda e: callback("https://github.com/LMontalbano/Clients_Service_ITxPT"))

###################################### Function utiles ###############################################
def run_ntp(temps, tous):
    sec = 0
    num_lines = 0
    thread_time = temps
    test_ok = 0
    nb_test = 0
    if tous:
        change_text_button_ntp()
        if t.compare("end-1c", "!=", "1.0"):
            print("\n")
        print("############### All Tests Started... ###############")
        time.sleep(1)

    if t.compare("end-1c", "!=", "1.0"):
        print("\n")
    print("########## Test NTP ##########")
    # Affichage du server NTP sur lequel le programme va récupérer l'heure
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
    thread_time = temps
    sec = 0
    nb_test = nb_test
    test_ok = test_ok
    if tous:
        change_text_button_gnss()

    if t.compare("end-1c", "!=", "1.0"):
        print("\n")
    print("########## Test GNSS ##########")
    # Affichage du server NTP sur lequel le programme va récupérer l'heure
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



def run_avms(temps, tous, nb_test, test_ok):
    ServerAVMS.cancel = False
    thread_time = temps
    sec = 0
    nb_test = nb_test
    test_ok = test_ok
    if tous:
        change_text_button_avms()
        ServerAVMS.tous = True

    if t.compare("end-1c", "!=", "1.0"):
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
    return nb_test, test_ok


def run_apc():
    print("\n")
    print("########## Test APC ##########")
    print("Not Yet Implemented")
    setup_end_apc()



######################################### Class utiles ###############################################
class PrintLogger:  # create file like object
    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text)  # write text to textbox
        self.textbox.see("end")
        # could also scroll to end of textbox here to make sure always visible

    def flush(self):  # needed for file like object
        pass


class ThreadNTP(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        run_ntp(temps=self.thread_time, tous=False)


class ThreadGNSS(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        run_gnss(temps=self.thread_time, tous=False, nb_test=None, test_ok=None)


class ThreadAVMSServer(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        run_avms(temps=self.thread_time, tous=False, nb_test=None, test_ok=None)


class ThreadAVMSClient(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        client_avms()


class ThreadAVMSCancel(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        ServerAVMS.cancel = True


class ThreadAPC(threading.Thread):
    def __init__(self, thread_time):
        threading.Thread.__init__(self)
        self.thread_time = thread_time

    def run(self):
        run_apc()


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
        res_avms = run_avms(temps=self.thread_time, tous=True, nb_test=res_gnss[0], test_ok=res_gnss[1])


########################################### NTP ##############################################

def ntp():
    change_text_button_ntp()
    main_ntp()


def setup_start_ntp():
    address_input_LOCAL.config(state=DISABLED)
    address_input_SAE.config(state=DISABLED)
    t.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    GNSS_button.config(state=DISABLED)
    AVMS_button.config(state=DISABLED)
    APC_button.config(state=DISABLED)
    GLOBAL_button.config(state=DISABLED)
    Cancel_AVMS_button.config(state=DISABLED)


def setup_end_ntp():
    change_back_button_ntp()
    address_input_LOCAL.config(state=NORMAL)
    address_input_SAE.config(state=NORMAL)
    t.config(state=DISABLED)
    NTP_button.config(state=NORMAL)
    GNSS_button.config(state=NORMAL)
    AVMS_button.config(state=NORMAL)
    APC_button.config(state=NORMAL)
    GLOBAL_button.config(state=NORMAL)
    Cancel_AVMS_button.config(state=DISABLED)


def main_ntp():
    setup_start_ntp()
    # create instance of file like object
    p1 = PrintLogger(t)
    # replace sys.stdout with our object
    sys.stdout = p1

    test_time = 5
    thread1 = ThreadNTP(test_time)
    thread1.start()


def change_text_button_ntp():
    NTP_button['text'] = 'Test NTP in progress...'


def change_back_button_ntp():
    NTP_button['text'] = 'Test NTP'


NTP_button = Button(f2, text="Test NTP", command=ntp)
NTP_button.grid(column=2, row=3, ipadx=15, ipady=10, padx=5, pady=5)


##################################### GNSS ################################################

def gnss():
    change_text_button_gnss()
    main_gnss()


def setup_start_gnss():
    address_input_LOCAL.config(state=DISABLED)
    address_input_SAE.config(state=DISABLED)
    t.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    GNSS_button.config(state=DISABLED)
    AVMS_button.config(state=DISABLED)
    APC_button.config(state=DISABLED)
    GLOBAL_button.config(state=DISABLED)
    Cancel_AVMS_button.config(state=DISABLED)


def setup_end_gnss():
    change_back_button_gnss()
    address_input_LOCAL.config(state=NORMAL)
    address_input_SAE.config(state=NORMAL)
    t.config(state=DISABLED)
    NTP_button.config(state=NORMAL)
    GNSS_button.config(state=NORMAL)
    AVMS_button.config(state=NORMAL)
    APC_button.config(state=NORMAL)
    GLOBAL_button.config(state=NORMAL)
    Cancel_AVMS_button.config(state=DISABLED)


def main_gnss():
    setup_start_gnss()
    # create instance of file like object
    p2 = PrintLogger(t)
    # replace sys.stdout with our object
    sys.stdout = p2

    test_time = 5
    thread2 = ThreadGNSS(test_time)
    thread2.start()


def change_text_button_gnss():
    GNSS_button['text'] = 'Test GNSS in progress...'


def change_back_button_gnss():
    GNSS_button['text'] = 'Test GNSS'


GNSS_button = Button(f2, text="Test GNSS", command=gnss)
GNSS_button.grid(column=3, row=3, ipadx=15, ipady=10, padx=5, pady=5)


###################################### AVMS #################################################

def avms():
    change_text_button_avms()
    main_avms()


def setup_start_avms():
    address_input_LOCAL.config(state=DISABLED)
    address_input_SAE.config(state=DISABLED)
    t.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    GNSS_button.config(state=DISABLED)
    AVMS_button.config(state=DISABLED)
    APC_button.config(state=DISABLED)
    GLOBAL_button.config(state=DISABLED)
    Cancel_AVMS_button.config(state=NORMAL)

def setup_end_avms():
    change_back_button_avms()
    address_input_LOCAL.config(state=NORMAL)
    address_input_SAE.config(state=NORMAL)
    t.config(state=DISABLED)
    NTP_button.config(state=NORMAL)
    GNSS_button.config(state=NORMAL)
    AVMS_button.config(state=NORMAL)
    APC_button.config(state=NORMAL)
    GLOBAL_button.config(state=NORMAL)
    Cancel_AVMS_button.config(state=DISABLED)


def main_avms():
    setup_start_avms()
    server_avms()


def server_avms():
    # create instance of file like object
    p3 = PrintLogger(t)
    # replace sys.stdout with our object
    sys.stdout = p3

    test_time = 5
    thread3 = ThreadAVMSServer(test_time)
    thread3.start()

    # os.system("start python Trials/ClientAVMS.py")

    thread10 = ThreadAVMSClient(test_time)
    thread10.start()


def client_avms():
    time.sleep(1)
    ClientAVMS.main_cli_avms(server.get(), local.get())


def cancel_avms():
    test_time = 5
    thread4 = ThreadAVMSCancel(test_time)
    thread4.start()


def change_text_button_avms():
    AVMS_button['text'] = 'Test AVMS in progress...'


def change_back_button_avms():
    AVMS_button['text'] = 'Test AVMS'


AVMS_button = Button(f2, text="Test AVMS", command=avms)
AVMS_button.grid(column=4, row=3, ipadx=15, ipady=10, padx=5, pady=5)

Cancel_AVMS_button = Button(f2, text="Cancel Test AVMS", command=cancel_avms)
Cancel_AVMS_button.grid(column=4, row=5, ipadx=15, ipady=10, padx=5, pady=5)
Cancel_AVMS_button.config(state=DISABLED)


####################################### APC ##################################################

def apc():
    main_apc()


def main_apc():
    setup_start_apc()
    p4 = PrintLogger(t)
    sys.stdout = p4
    test_time = 5
    thread5 = ThreadAPC(test_time)
    thread5.start()

def setup_start_apc():
    t.config(state=NORMAL)

def setup_end_apc():
    t.config(state=DISABLED)


APC_button = Button(f2, text="Test APC", command=apc)
APC_button.grid(column=5, row=3, ipadx=15, ipady=10, padx=5, pady=5)


#################################### Tous les Tests #########################################

def all_tests():
    main_all_tests()


def setup_start_global():
    address_input_LOCAL.config(state=DISABLED)
    address_input_SAE.config(state=DISABLED)
    t.config(state=NORMAL)
    NTP_button.config(state=DISABLED)
    GNSS_button.config(state=DISABLED)
    AVMS_button.config(state=DISABLED)
    APC_button.config(state=DISABLED)
    GLOBAL_button.config(state=DISABLED)
    Cancel_AVMS_button.config(state=DISABLED)


def main_all_tests():
    setup_start_global()

    # create instance of file like object
    p_global = PrintLogger(t)
    # replace sys.stdout with our object
    sys.stdout = p_global

    test_time = 5
    thread_global = ThreadGlobal(test_time)
    thread_global.start()


def change_text_button_global():
    GLOBAL_button['text'] = 'Tests in progress...'


def change_back_button_global():
    GLOBAL_button['text'] = 'All Tests'


GLOBAL_button = Button(f2, text="All Tests", command=all_tests)
GLOBAL_button.grid(column=6, row=3, ipadx=15, ipady=10, padx=5, pady=5)

###################################### Fenêtre principale ####################################


t = tk.Text(f3, width=100, height=21, state=DISABLED)
t.grid(column=1, row=4)


# fonction pour close la fenêtre
def close():
    fenetre.destroy()


# Bouton 'Fermer'
# Close_button = Button(f4, text="Fermer", command=close, width=50, bg='red')
# Close_button.grid(column=1, row=8)

# Pour finir, on lance la boucle programme
fenetre.mainloop()
