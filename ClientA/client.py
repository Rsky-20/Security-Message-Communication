import socket

HOST ="127.0.0.1"

print(HOST)

PORT = 50100

'------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
# fonction de chiffrement affine
def chiffrementAffine(a,b,L):
        data=['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n','A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W','X', 'C', 'V', 'B', 'N','1', '2', '3', '4', '5', '6', '7', '8', '9', '0','-','_'," ",'?', '.', '/', '§', ':', '!', '%', '$', '£', '€', '*', '=', '"', "'", '|', '`', '\ ', "^", "@", '&', '~','#','(', '{', '[', '<', '>', "]", "}", ')','ù', 'é', 'è', 'ç', 'à']
        x=data.index(L)
        y=(a*x+b)%97
        return data[y]
# Calcul de l'inverse d'un nombre modulo 26
def inverse(a):
        x=0
        while (a*x%97!=1):
                x=x+1
        return x
# Fonction de déchiffrement
def dechiffrementAffine(a,b,L):
    data=['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n','A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'W','X', 'C', 'V', 'B', 'N','1', '2', '3', '4', '5', '6', '7', '8', '9', '0','-','_'," ",'?', '.', '/', '§', ':', '!', '%', '$', '£', '€', '*', '=', '"', "'", '|', '`', '\ ', "^", "@", '&', '~','#','(', '{', '[', '<', '>', "]", "}", ')','ù', 'é', 'è', 'ç', 'à']
    x=data.index(L)
    y=(inverse(a)*(x-b))%97
    return data[y]
def crypt(M,a,b):
    if (pgcd(a,97)==1):
        mot = []
        for i in range(0,len(M)):
                mot.append(chiffrementAffine(a,b,M[i]))
        return "".join(mot)
    else:
        return "Chiffrement impossible. Veuillez choisir un nombre ( a ) premier avec 26."
# Affichage du mot déchiffré
def decrypt(M,a,b):
    if (pgcd(a,97)==1):
        mot = []
        for i in range(0,len(M)):
                mot.append(dechiffrementAffine(a,b,M[i]))
        return "".join(mot)
    else:
        return "Déchiffrement impossible. Le nombre a n'est pas premier avec 26"

'_________________________________________________________________________________________________________________________________________________________________________'

def send(request):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))

        print('CLIENT : ' + s.getsockname()[0] + ':' + str(s.getsockname()[1]))

        print('SERVER : ' + HOST + ':' + str(PORT))

        byte_data = request.encode()

        s.sendall(byte_data)

        byte_data = s.recv(1024)

        if byte_data:
            response = byte_data.decode()
            process_response(response,request)


def process_response(response, request):

    print('Response: ' + response)
    data_exit = "Le chiffre {} correspond a celui du server !".format(request)
    if response == data_exit:
        exit()


def run():

    while True:

        request = input('\nRequest: ')

        if request == '':
            break

        send(request)

run()
