import socket
import datetime
from time import strftime
import zipfile
import glob
import os

HOST = "127.0.0.1"

PORT = 50100

fid_client = '#jhd62j2hkzp' #input("Give your Friend Id_client (like => #jhd62j2hkzp: ")
id_client = '#8hd27dh1js2'

def str2dict(data):
    str_msg = data.split(',')
    return str_msg


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# fonction de chiffrement affine
def chiffrementAffine(a, b, L):
    data = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w',
            'x', 'c', 'v', 'b', 'n', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H',
            'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-',
            '_', " ", '?', '.', '/', '§', ':', '!', '%', '$', '£', '€', '*', '=', '"', "'", '|', '`', '\ ', "^", "@",
            '&', '~', '#', '(', '{', '[', '<', '>', "]", "}", ')', 'ù', 'é', 'è', 'ç', 'à']
    x = data.index(L)
    y = (a * x + b) % 97
    return data[y]


# Calcul de l'inverse d'un nombre modulo 97
def inverse(a):
    x = 0
    while a * x % 97 != 1:
        x = x + 1
    return x


# Fonction de déchiffrement
def dechiffrementAffine(a, b, L):
    data = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w',
            'x', 'c', 'v', 'b', 'n', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H',
            'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-',
            '_', " ", '?', '.', '/', '§', ':', '!', '%', '$', '£', '€', '*', '=', '"', "'", '|', '`', '\ ', "^", "@",
            '&', '~', '#', '(', '{', '[', '<', '>', "]", "}", ')', 'ù', 'é', 'è', 'ç', 'à']
    x = data.index(L)
    y = (inverse(a) * (x - b)) % 97
    return data[y]


def crypt(M, a, b):
    if pgcd(a, 97) == 1:
        mot = []
        for i in range(0, len(M)):
            mot.append(chiffrementAffine(a, b, M[i]))
        return "".join(mot)
    else:
        return "Chiffrement impossible. Veuillez choisir un nombre ( a ) premier avec 97."


# Affichage du mot déchiffré
def decrypt(M, a, b):
    if pgcd(a, 97) == 1:
        mot = []
        for i in range(0, len(M)):
            mot.append(dechiffrementAffine(a, b, M[i]))
        return "".join(mot)
    else:
        return "Déchiffrement impossible. Le nombre a n'est pas premier avec 97"


def process_response(data,data2):
    str_l = data

    client_data = str_l.split('|')

    del client_data[0]

    msg = str2dict(str(client_data[0]))

    if msg[0] != data2:
        print('Response: ' + decrypt(msg[1], 35, 19))
    else:
        print('')


def connection_client(HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT))
    #s.listen(10)

    print("connection établie avec le serveur sur le port {}".format(PORT))
    client_info = '[' + 'CLIENT ' + s.getsockname()[0] + ':' + '' + str(s.getsockname()[1]) + "]"
    print('\033[31m' + 'CLIENT  ' + '\033[36m' + s.getsockname()[0] + ':' + '\033[33m' + str(s.getsockname()[1]))
    print('\033[31m' + 'SERVER  ' + '\033[36m' + HOST + ':' + '\033[33m' + str(PORT))


    send_msg = b""
    while send_msg != b"/stop":
        send_msg = crypt(input("> "), 35,19)
        send_msg = datetime.datetime.isoformat(datetime.datetime.now()) + '|'+ client_info + "@" + send_msg

        sending_msg = send_msg.encode()
        s.sendall(sending_msg)

        msg_recv = s.recv(1024)

        response = msg_recv.decode()
        #print(response)

        #######################################################################

        process_response(response, client_info)

        #######################################################################

    print("Close all connection")
    s.close()


def run():
    connection_client(HOST, PORT)


run()
