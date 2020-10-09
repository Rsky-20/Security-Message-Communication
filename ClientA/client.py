"""

Client

Objectif:
Le client dialogue avec le serveur. Il permet a l'utilisateur de communiquer avec le serveur a distance.
Le client evoi des informations au serveur qui renvoi ensuite une reponse.
Ici le client permet de jouer au chiffre mystere avec le serveur.


"""

import socket


# Saisie adresse IP du serveur.
id_network1 = input("Donnez l'id du reseaux (exemple : 127) : ")
id_network2 = input("Donnez l'id du reseaux (exemple : 0) : ")
id_network3 = input("Donnez l'id de l'hote (exemple : 0) : ")
id_network4 = input("Donnez le numero de l'hote (exemple : 1) : ")
print()
# Rassemble les donnees renseignees sur l'ip afin de le retranscrire dans le socket
HOST = str(id_network1 + "." + id_network2 + "." + id_network3 + "." + id_network4)

print(HOST)

# Le port utilisé par le serveur.
#On peut demander le port de dialogue avec le serveur à l'utilisateur (on rentre obligatoirement un int)
#PORT = input(int("Renseigner la valeur du port d'ecoute (exemple : 1111) : "))
#input(int("renseigner le port sur lequel le serveur ecoute"))
PORT = 50100


def send(request):
    """
     Crée un connecteur (socket) et lui envoie des données

     AF_INET représente la famille d'adresse IPv4.
     SOCK_STREAM représente le protocole TCP.

     Arguments:
       request: Une chaîne de carcatères représentant des données.
    """

    # Création d'un objet socket nommé s.
    # with permet de fermer le connecteur après utilisation et en cas d'erreur.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Connexion à la socket distante d'adresse ip HOST sur le port PORT
        s.connect((HOST, PORT))

        # getsockname retourne un tuple constitué de l'adresse ip et le port
        # utlisé par le client.
        print('CLIENT : ' + s.getsockname()[0] + ':' + str(s.getsockname()[1]))

        print('SERVER : ' + HOST + ':' + str(PORT))

        # encode convertis un str en bytearray.
        byte_data = request.encode()

        # Envoie les donnée sur la socket.
        s.sendall(byte_data)

        # Récupération des données du connecteur.
        # 1024 octets au maximum.
        # recv retourne un bytearray
        byte_data = s.recv(1024)

        # Si la réponse n'est pas vide on la traite
        if byte_data:
            # decode convertis un bytearray en str.
            response = byte_data.decode()
            process_response(response,request)


def process_response(response, request):
    """
    Traite les données reçues du serveur.

        Arguments:
            response: Les données de type str
    """

    print('Response: ' + response)
    data_exit = "Le chiffre {} correspond a celui du server !".format(request)
    if response == data_exit:
        exit()


def run():
    """
    Démarre le client.
    Eteint le client si reponse vide
    """

    while True:

        request = input('\nRequest: ')

        if request == '':
            break

        send(request)

# Execution de la fonction qui demarre le client
run()
