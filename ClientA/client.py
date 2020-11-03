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




def process_response(data,data2):
    str_l = data

    client_data = str_l.split('|')

    del client_data[0]

    msg = str2dict(str(client_data[0]))

    if msg[0] != data2:
        print('Response: ' + msg[1])
    else:
        print('')




def connexion_server(HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT))
    #s.listen(10)

    print("Connexion établie avec le serveur sur le port {}".format(PORT))
    client_info = '[' + 'CLIENT ' + s.getsockname()[0] + ':' + '' + str(s.getsockname()[1]) + "]"
    print('\033[31m' + 'CLIENT  ' + '\033[36m' + s.getsockname()[0] + ':' + '\033[33m' + str(s.getsockname()[1]))
    print('\033[31m' + 'SERVER  ' + '\033[36m' + HOST + ':' + '\033[33m' + str(PORT))


    send_msg = b""
    while send_msg != b"/disconnection":
        send_msg = input("> ")
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
    connexion_server(HOST, PORT)


run()
