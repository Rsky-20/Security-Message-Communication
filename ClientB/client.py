import socket
import zipfile
import glob
import os

HOST = "127.0.0.1"

PORT = 50100

fid_client = input("Give your Friend Id_client (like => #jhd62j2hkzp: ")
id_client = '#8hdjajcur5d'


def zipdirectory(filezip, pathzip):
    # Cette fonction cree une archive Zip. Elle est utlisee pour faire des sauvegardes lors de la deconnexion.
    lenpathparent = len(pathzip) + 1  # utile si on veut stocker les chemins relatifs

    def _zipdirectory(zfile, path):
        for i in glob.glob(path + '/*'):
            if os.path.isdir(i):
                _zipdirectory(zfile, i)
            else:
                zfile.write(i, i[lenpathparent:])  # zfile.write(i) pour stocker les chemins complets

    zfile = zipfile.ZipFile(filezip, 'w', compression=zipfile.ZIP_DEFLATED)
    _zipdirectory(zfile, pathzip)
    zfile.close()


def dezip(filezip, pathdst=''):
    if pathdst == '':
        pathdst = os.getcwd()  # on dezippe dans le repertoire locale
    zfile = zipfile.ZipFile(filezip, 'r')
    for i in zfile.namelist():  # On parcourt l'ensemble des fichiers de l'archive
        if os.path.isdir(i):  # S'il s'agit d'un repertoire, on se contente de creer le dossier
            try:
                os.makedirs(pathdst + os.sep + i)
            except:
                pass
        else:
            try:
                os.makedirs(pathdst + os.sep + os.path.dirname(i))
            except:
                pass
            data = zfile.read(i)  # lecture du fichier compresse
            fp = open(pathdst + os.sep + i, "wb")  # creation en local du nouveau fichier
            fp.write(data)  # ajout des donnees du fichier compresse dans le fichier local
            fp.close()
    zfile.close()


def process_response(response):
    print('Response: ' + response)

    return response


def connexion_server(HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT))
    # s.listen(10)

    print("Connexion établie avec le serveur sur le port {}".format(PORT))
    print('\033[31m' + 'CLIENT  ' + '\033[36m' + s.getsockname()[0] + ':' + '\033[33m' + str(s.getsockname()[1]))
    print('\033[31m' + 'SERVER  ' + '\033[36m' + HOST + ':' + '\033[33m' + str(PORT))

    send_msg = b""
    while send_msg != b"/disconnection":
        send_msg = input("> ")
        send_msg = fid_client + "@" + send_msg

        sending_msg = send_msg.encode()
        s.sendall(sending_msg)

        msg_recv = s.recv(1024)

        response = msg_recv.decode()
        print("> {}".format(response))

        process_response(response)

    print("Close all connection")
    s.close()


def run():
    connexion_server(HOST, PORT)


run()
