

import socket
import os
import datetime

HOST1 = '127.0.0.1' #'172.20.10.2'

PORT1 = 50100
PORT2 = 50105

data_server = {'number': "Hello World"}

def log(user,text):
    log = open("log.txt", "a")
    log.write(user+"["+datetime.datetime.isoformat(datetime.datetime.now())+"]"+text+"\n")
    log.close()

"""def verif_path(path, folder = False):
    if folder:
        path+=os.sep+"creating_file"
    if not os.path.exists(path):
        original_path = os.getcwd()
        path_to_create = ""
        for x in path.split(os.sep)[:len(path.split(os.sep))-1]:
            path_to_create += x+os.sep
            try:
                os.mkdir(path_to_create)
            except Exception as error:
                pass
        if not folder:
            a = open(path, "w")
            a.close()

    else:
        pass"""

"""def find_key_in_dict(data_server, phrase):
    for cle, val in data_server.items():
        if val == phrase:
            return cle

    return None"""


def receive():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:

        s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s1.bind((HOST1, PORT1))

        s1.listen(10)

        connexion1, address = s1.accept()

        print('\nCLIENT  ' + address[0] + ':' + str(address[1]))

        with connexion1:

            while True:

                byte_data = connexion1.recv(1024)

                if not byte_data:
                    break

                request1 = byte_data.decode()

                print('Request: ', request1)

                response1 = process_request(request1)

                print('Responce: ', response1)

                byte_data = response1.encode()

                connexion1.sendall(byte_data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:

        s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s2.bind((HOST, PORT2))

        s2.listen(11)

        connexion2, address = s2.accept()

        print('\nCLIENT  ' + address[0] + ':' + str(address[1]))

        with connexion2:

            while True:

                byte_data = connexion2.recv(1024)

                if not byte_data:
                    break

                request2 = byte_data.decode()

                print('Request: ', request2)

                response2 = process_request(request2)

                print('Responce: ', response2)

                byte_data = response2.encode()

                connexion2.sendall(byte_data)


def process_request(request1,request2):

    response2 = request1
    log('Client1',response2)
    response1 = request2
    log('Client1',response1)



    return response1

def run():

    print('SERVER  ' + HOST1 + ':' + str(PORT1) + ' / ' + '\n') #+ str(PORT2)

    while True:
        receive()

run()