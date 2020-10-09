import datetime
import select
import socket

HOST = '127.0.0.1'

PORT = 50100


def documentation():
    print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
    print('#                   Welcome in SMC server                      #')
    print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
    print('Reste de la doc à venir °°°')


def log(response):
    with open("log.txt", "a") as log:
        log.write("\n" + "\t[" + datetime.datetime.isoformat(datetime.datetime.now())
                  + "]\n" + "{\n" + response + "\n}\n" + "#________________________________________________#\n")
        log.close()


def log_connexion(clients_connected):
    with open("log_connexion.txt", "a") as log:
        log.write(datetime.datetime.isoformat(datetime.datetime.now()) +
                  "Le client {} est connecté sur le serveur via le port {}".format(clients_connected, PORT))
        log.close()


def process_server(client, msg_recv):
    response = str(msg_recv)
    log(response)

    return response


# def bridge_com(client):


def connexion_server(HOST, PORT):
    documentation()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print('{serverver-status}:', '\033[32m', 'Online', '\033[1m')

    server_ready = True
    client_connected = []
    while server_ready:

        wait_connexions, wlist, xlist = select.select([s], [], [], 0.05)

        for connexion in wait_connexions:
            connexion_client, info_connexion = connexion.accept()
            client_connected.append(connexion_client)


########################################################################################################################

            for client in client_connected:
                msg_recv = client.recv(1024)
                print(client_connected)

                msg_recv = msg_recv.decode()

                print('[', '\033[31m', 'SERVER@', '\033[36m', HOST, '\033[33m', '-p', str(PORT),
                      '\033[39m', ']: Client send a message. Go to ./log.txt to see more.')

                if msg_recv == "/disconnexion":
                    server_ready = False

                p_server = process_server(client, msg_recv)

                byte_data = p_server.encode()

                client.sendall(byte_data)



        read_client = []
        try:
            read_client, wlist, xlist = select.select(client_connected, [], [], 0.05)

        except select.error:
            pass
        else:

            for client in read_client:
                print(read_client)

                msg_recv = client.recv(1024)

                msg_recv = msg_recv.decode()

                print('[', '\033[31m', 'SERVER@', '\033[36m', HOST, '\033[33m', '-p', str(PORT),
                      '\033[39m', ']: Client send a message. Go to ./log.txt to see more.')

                if msg_recv == "/disconnexion":
                    server_ready = False

                p_server = process_server(client, msg_recv)

                byte_data = p_server.encode()

                client.sendall(byte_data)

########################################################################################################################

    print(client_connected)

    print("Close all connections")
    for client in client_connected:
        client.close()

    s.close()


def run():
    print('[' + '\033[31m' + 'SERVER@' + '\033[36m' + HOST + ' ' + '\033[33m' + '-p' + str(PORT) + '\033[39m' + ']:\n')

    while True:
        connexion_server(HOST, PORT)


run()
