

import socket

HOST = '127.0.0.1'

PORT = 50100

data_server = {'number': int(input("Donner un nombre qui servirara de reference au jeu : "))}


def receive():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((HOST, PORT))

        s.listen(10)

        connexion, address = s.accept()

        print('\nCLIENT  ' + address[0] + ':' + str(address[1]))

        with connexion:

            while True:

                byte_data = connexion.recv(1024)

                if not byte_data:
                    break

                request = byte_data.decode()

                print('Request: ', request)

                response = process_request(request)

                print('Responce: ', response)

                byte_data = response.encode()

                connexion.sendall(byte_data)


def process_request(data):

    number_client = int(data)

    if number_client > data_server['number']:
        response = "Le chiffre {} ne correspond pas a celui du server, il est trop grand !".format(number_client)

    elif number_client < data_server['number']:
        response = "Le chiffre {} ne correspond pas a celui du server, il est trop petit !".format(number_client)

    else:
        response = "Le chiffre {} correspond a celui du server !".format(number_client)

    return response


def run():


    print('SERVER  ' + HOST + ':' + str(PORT) + '\n')

    while True:
        receive()

run()