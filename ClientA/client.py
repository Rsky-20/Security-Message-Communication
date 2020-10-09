
import socket

id_network1 = input("Donnez l'id du reseaux (exemple : 127) : ")
id_network2 = input("Donnez l'id du reseaux (exemple : 0) : ")
id_network3 = input("Donnez l'id de l'hote (exemple : 0) : ")
id_network4 = input("Donnez le numero de l'hote (exemple : 1) : ")
print()

HOST = str(id_network1 + "." + id_network2 + "." + id_network3 + "." + id_network4)

print(HOST)

PORT = 50100


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
