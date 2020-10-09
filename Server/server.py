"""

Serveur

Objectif du serveur :
Ce serveur a pour fonction de comparer un chiffre referant avec un chiffre donnee par un client. La valeur de reference
est demandee à l'admin (ou utilisateur cote serveur) puis place dans une dictionnaire servant de base de donnee.
C'est donc un serveur qui propose de trouver un nombre mystere.

"""

import socket

# Entree manuelle de l'adresse ip du serveur. On peut fixer l'ip mais il est plus pratique de la saisie que
# modifier le script (serveur ou client). On peut alors passer le script (serveur et client) sans avoir a le modifier
# avant utilisation.

# L'ip est decomposee en 4 parties puis reassemblee en une chaine de caractere
id_network1 = input("Donnez l'id du reseaux (exemple : 127) : ")
id_network2 = input("Donnez l'id du reseaux (exemple : 0) : ")
id_network3 = input("Donnez l'id de l'hote (exemple : 0) : ")
id_network4 = input("Donnez le numero de l'hote (exemple : 1) : ")
print()
# Rassemble les donnees renseignees sur l'ip afin de le retranscrire dans le socket
HOST = str(id_network1 + "." + id_network2 + "." + id_network3 + "." + id_network4)

# Le port utilisé ( entre 1024 et 65535 )
# On peut demander le port d'ecoute à l'utilisateur (on rentre obligatoirement un int)
# PORT = input(int("Renseigner la valeur du port d'ecoute (exemple : 1111) : "))
PORT = 50100

# On demande a l'utilisateur de definir un chiffre mystere.
# La seul rentree utilisateur est la valeur (value). La cle (key) etant fixee
data_server = {'number': int(input("Donner un nombre qui servirara de reference au jeu : "))}


def receive():
    """
    Crée une connexion , attend de recevoir des données, les traite avec la
    fonction process_request. Si la réponse est vide la connexion est fermée
    et une nouvelle connexion est créée.

    AF_INET représente la famille d'adresse IPv4.
    SOCK_STREAM représente le protocole TCP.

    """

    # Création d'un connecteur (socket en anglais),
    # en créant un objet socket nommé s.
    # with permet de fermer le connecteur après utilisation et en cas d'erreur.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Permet de réutiliser la même addresse.
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # s.bind(address) associe une adresse et un port a la socket s.
        # Le paramètre address est un tuple constitué de l'adresse IP du
        # serveur et d'un numéro de port.
        s.bind((HOST, PORT))

        # s.listen() rend le serveur prêt à accepter des connections.
        s.listen(10)

        # Accepte une connexion.
        # Retourne un tuple constitué d'un objet socket nommé connection et de
        # l'adresse IP du client.
        connexion, address = s.accept()

        print('\nCLIENT  ' + address[0] + ':' + str(address[1]))

        # with permet de fermer la connexion en sortant de la boucle et en cas
        # d'erreur.
        with connexion:

            while True:

                # Récupération des données du connecteur.
                # 1024 octets au maximum.
                # recv retourne un bytearray
                byte_data = connexion.recv(1024)

                # Si la requête est vide on sort du while.
                if not byte_data:
                    break

                # decode convertis un bytearray en str.
                request = byte_data.decode()

                print('Request: ', request)

                # Le traitement de la requête.
                response = process_request(request)

                print('Responce: ', response)

                # encode convertis un str en bytearray.
                byte_data = response.encode()

                # Envoie les donnée sur la socket.
                connexion.sendall(byte_data)

                """    
                Si le serveur dialogue avec un seul client alors on peut mettre cette condition qui va fermer le serveur
                apres avoir retourner la reponse au client.
                
                Si on voulait couper le serveur quant il n'y a plus aucun client, il aurait fallu faire un objet avec 
                thread pour dire au serveur de se couper quand plus de connexion en cours           

                #Condition qui coupe le serveur (mais il faudrait utiliser s.close() pour couper le serveur proprement
                if response == "Le chiffre {} correspond a celui du server !".format(request):
                    exit()
                """

def process_request(data):
    """
    Traite les données reçues du client et retourne une réponse de type str.

        Arguments:
            data: Les données de type str

        Retourne:
            Une réponse de type str.

        Condition du jeu :
            Si le nombre est inferieur / superieur par rapport à celui enregiste dans le dictionnaire du serveur:
                alors on affiche que le chiffre est trop petit ou trop grand puis on continue
            Sinon:
                la reponse trouvee est la bonne
    """
    number_client = int(data)

    if number_client > data_server['number']:
        response = "Le chiffre {} ne correspond pas a celui du server, il est trop grand !".format(number_client)

    elif number_client < data_server['number']:
        response = "Le chiffre {} ne correspond pas a celui du server, il est trop petit !".format(number_client)

    else:
        response = "Le chiffre {} correspond a celui du server !".format(number_client)

    return response


def run():
    """
    Démarre le serveur.
    Redémarre après qu'une connexion soit terminée.
    """

    print('SERVER  ' + HOST + ':' + str(PORT) + '\n')

    while True:
        receive()

# Execution de la fonction qui demarre le serveur
run()
