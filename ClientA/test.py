import socket

hote = "localhost"
port = 50100

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connexion_avec_serveur.close()

    def _zipdirectory(zfile, path):
        for i in glob.glob(path + '/*'):
            if os.path.isdir(i):
                _zipdirectory(zfile, i)
            else:
                zfile.write(i, i[lenpathparent:])  ## zfile.write(i) pour stocker les chemins complets

    zfile = zipfile.ZipFile(filezip, 'w', compression=zipfile.ZIP_DEFLATED)
    _zipdirectory(zfile, pathzip)
    zfile.close()


def dezip(filezip, pathdst=''):
    if pathdst == '': pathdst = os.getcwd()  ## on dezippe dans le repertoire locale
    zfile = zipfile.ZipFile(filezip, 'r')
    for i in zfile.namelist():  ## On parcourt l'ensemble des fichiers de l'archive
        if os.path.isdir(i):  ## S'il s'agit d'un repertoire, on se contente de creer le dossier
            try:
                os.makedirs(pathdst + os.sep + i)
            except:
                pass
        else:
            try:
                os.makedirs(pathdst + os.sep + os.path.dirname(i))
            except:
                pass
            data = zfile.read(i)  ## lecture du fichier compresse
            fp = open(pathdst + os.sep + i, "wb")  ## creation en local du nouveau fichier
            fp.write(data)  ## ajout des donnees du fichier compresse dans le fichier local
            fp.close()
    zfile.close()
