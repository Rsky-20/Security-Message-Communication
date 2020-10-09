

import socket

# Rassemble les donnees renseignees sur l'ip afin de le retranscrire dans le socket
HOST = '127.0.0.1' #'172.20.10.2'

print(HOST)


PORT = 50100


def send(request):

    # Création d'un objet socket nommé s.
    # with permet de fermer le connecteur après utilisation et en cas d'erreur.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:

        # Connexion à la socket distante d'adresse ip HOST sur le port PORT
        s2.connect((HOST, PORT))

        # getsockname retourne un tuple constitué de l'adresse ip et le port
        # utlisé par le client.
        print('CLIENT : ' + s2.getsockname()[0] + ':' + str(s2.getsockname()[1]))

        print('SERVER : ' + HOST + ':' + str(PORT))

        # encode convertis un str en bytearray.
        byte_data = request.encode()

        # Envoie les donnée sur la socket.
        s2.sendall(byte_data)

        # Récupération des données du connecteur.
        # 1024 octets au maximum.
        # recv retourne un bytearray
        byte_data = s2.recv(1024)

        # Si la réponse n'est pas vide on la traite
        if byte_data:
            # decode convertis un bytearray en str.
            response = byte_data.decode()
            process_response(response,request)


def process_response(response, request):


    print('Response: ' + response)
    data_exit = "Le chiffre {} correspond a celui du server !".format(request)
    if response == data_exit:
        exit()

    return response


def run():


    while True:

        request = input('\nRequest: ')

        if request == '':
            break

        send(request)

# Execution de la fonction qui demarre le client
run()
