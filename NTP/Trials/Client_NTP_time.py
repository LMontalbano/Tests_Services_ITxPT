import socket
import struct
import time


# addr une adresse d'un serveur NTP
def RequestTimefromNtp(addr='pool.ntp.org'):                    
    
    # Correspond au 1er janvier 2040 00:00:00 UTC+0
    REF_TIME = 2208988800
    
    #REF_TIME_PLUS_5_MIN = 2208989100 Correspond au 1er janvier 2040 00:05:00 UTC+0
    
    
    # AF_INET parce qu'on est en IPV4 si on passe sur du IPV6 se serra AF_INET6
    # SOCK_DGRAM parce que le NTP est en UDP si on était en TCP se serrait SOCK_STREAM
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #print(mySocket)
    #print("------------------------------------------------------------------------------------------------------------------------------------------")
    
    
    # le b'\x23' correspond à 0X23, il s'agit du premier octet spécifiant LI, VN et MODE
    # ici j'ai 0X23 pour avoir le VN = 4 qui est une version plus récente que le VN=3 (0X1B) (b'\x1b' + 47 * b'\0')
    # le + 47 * b'\0' correspond à 47 fois 00 00 00 00 (47 octets de 0).
    # cela fait donc 48 octets
    data = b'\x23' + 47 * b'\0'
    #print(data)
                                                                                                
    #print(data.decode())                                        
    #print("------------------------------------------------------------------------------------------------------------------------------------------")
    
    
    # le sendto() permet d'envoyé des données à une adresse donnée
    # socket.sendto(message.encode(), (serverName, serverPort)) 
    # ici 123 car il s'agit du Network Time Protocol NTP, used for time synchronization
    # addr c'est ce qu'on a en paramètre de la fonction ici le serveur est : pool.ntp.org
    # et notre "message" c'est notre data qui est déjà encodé donc pas besoin de encode()
    mySocket.sendto(data, (addr, 123))
    
    # reçoit les données et l'adresse de l'envoyeur sous forme de tuple (données, addresse)
    # En paramètre on lui indique le nombre d'octets à lire (bufsize) à partir du socket UDP
    # ici je mets 50 comme nous n'avons que 48 octets pour notre date
    (data, addr) = mySocket.recvfrom(50)
    #print((data, addr))
    #print("------------------------------------------------------------------------------------------------------------------------------------------")
    
    
    if data:
        # le unpack prend en paramètre un format et une data unpack(format, data)
        # on va décomposer le '!12I'
        # le '!' ont le met car le service NTP est gros-boutiste
        # le I c'est parce que nos data sont des INTEGER et que la taille standard est de 4 octets
        # et donc le 12 permet de faire 4*12= 48 le nombre d'octets de notre data
        # ici au lieu de 12I nous pourrions très bien mettre ('!IIIIIIIIIIII', data)
        
        #t0 = struct.unpack('!12I', data)
        #print(t0)
        
        # ici le [10] correspond à l'indice auquel il faut ce référé dans le tuple
        # le tuple de t ressemble à ça : (604111848, 1388, 465, 3646630929, 3832838620, 1970307624, 0, 0, 3832838889, 2680661994, 3832838889, 2681604820)
        # on a donc 12 octets (8bits) qui vont de l'indice 0 à l'indice 11
        t = struct.unpack('!12I', data)[10]
        #print(t)
        #print("------------------------------------------------------------------------------------------------------------------------------------------")
        
        t -= REF_TIME
        
    # time.ctime convertie une date/heure exprimée en sec depuis epoch (1er janvier 1970 00:00:00 UTC +0) en date sous la forme:
    # 'Jour Mois NumJour Heure:Min:Sec Annee en UTC +0'
    return time.ctime(t)

if __name__ == "__main__":
    
    # t en second car on l'utilise pour le time.sleep()
    t = 2
    # boucle à True pour faire une boucle infinie
    boucle = True
    
    while boucle:
        print(RequestTimefromNtp())
        # time.sleep(t) permet de freeze le programme pendant une période t sec
        time.sleep(t)
    