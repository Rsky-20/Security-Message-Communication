"""

Description

"""

# -------------------------------------------------Import module section---------------------------------------------- #

import datetime
import select
import socket

# -------------------------------------------------------------------------------------------------------------------- #

# Definition of local server variable
# Host is local adress for binding the server
HOST = '127.0.0.1'

# Port is the gate than the client take to discuss with the client
PORT = 50100

# Initialisation of list to make a stockage of connected client on the server
client_connected = []

# data_server is a dict. It's use to make a count of client
data_server = {
    'HOST': '127.0.0.1',
    'PORT': 50100
}
"""
client envoie une requette start, ensuite le server récup la requet, il regarde puis il lu donne un nombbre
Le serveur renvoie le num 1
Quand le deuxieme client envoie start => le serveur renvoie le num 2
==> position / identifiant

variable turn

count = 0
"""


def documentation():
    """
    This process return a native and basic documentation to the administrator of the serverS

    """

    print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
    print('#                   Welcome in SMC server                      #')
    print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
    print('Reste de la doc à venir °°°')


def log(data):
    """
    log is a process to make a history file of all conversation between client in the server.
    He use a str value given by client and save it in a texte file.

    Arguments
        arg1: data => str value given by client to the server

    Return:
        resturn none because it's a process

    """
    # Open file text as lmsg and write data with return line, after close the file in use
    with open("log.txt", "a") as lmsg:
        lmsg.write(data + "\n")
        lmsg.close()


def log_connection(client_connected):
    """
    log_connection is a process to make a history file of all connection client in the server.
    He use a type value given by module socket and save it in a texte file..

        Arguments
            arg1: client_connected => type value given by socket module

        Retourne:
            resturn none because it's a process

    """

    # Open file text as lc and write in file the date time of server, the client information in str
    # After close the file
    with open("log_connection.txt", "a") as lc:
        lc.write(datetime.datetime.isoformat(datetime.datetime.now()) +
                 "> {} connected on server \n".format(client_connected))
        lc.close()


def process_server(data):
    """
    process_server is a function that processes data given by client.
    It's a part of server to use client data.
    He use a str value given by client and use it in process.

        Arguments
            arg1: data => str value given by client in main bool of server in the part where data are receive

        Return:
            resturn response a str but this variable is not use in the rest of program (because we have not make yet a
            functionnaly than use this var)

    """

    # Rename data as response and use it in log process
    response = data
    log(response)
    return response


def dict_log():
    """
    dict_log is a function to change text file to list.
    He open and take all data in log.txt.
    He take all ligne and append in output list named dlog

        Arguments
            arg1: none

        Return:
            resturn dlog list created to use data in file txt

    """

    # Open file text as lg and create a list named dlog.
    # for line in lg, in variable named lastL, make a str variable named s and split the line with separator '@'
    # After append variable l in list dlog and close
    with open('log.txt', 'r') as lg:
        dlog = []
        for line in lg:
            s = line.strip("\n")
            lastL = s.split("@")
            dlog.append(lastL)
        lg.close()

    return dlog


def str_log(data):
    """
    str_log is a function to change a list to str data.
    He split element of list and join all element to make a str data.
    But only the last line is returned and use

        Arguments
            arg1: data => list of all data exchange between client2server and server2client

        Return:
            resturn str_l contain str data of the last element of the list given in argument

    """

    # Create a empty local variable named str_l
    # for i in the range of len data, for j in range of len of all data element, join the last element in variable str_l
    str_l = ''
    for i in range(len(data)):
        for j in range(len(data[i])):
            str_l = ','.join(data[i - 1])

    return str_l

def consoleCommand(event):
    if event == '/log.txt':
        log = open("./log.txt", "r")
        contenu = log.read()
        print(contenu)
    else:
        exit()


def connection_server():
    """
    connection_server is a main process in the server program.
    He use socket module to create a server.
    It's the main part of server.
    He take global value of the program like HOST and PORT, to bind and launch the server and listen all connection in
    socket
    Create a connection, wait to receive data, process it with the
    process_request function.

    AF_INET represents the IPv4 address family.
    SOCK_STREAM represents the TCP protocol.

        Arguments
            arg1: none

        Return:
            resturn self

    """

    # Creating a socket, by creating a socket object named s.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allows to reuse the same address
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # s.bind (address,port) binds an address and a port to socket s.
    # The address parameter is a tuple consisting of the IP address of the
    # server and a port number.
    # s.bind((data_server['HOST'], data_server['PORT']))
    s.bind((HOST, PORT))


    # s.listen () makes the server ready to accept connections.
    s.listen(5)
    print('{serverver-status}:', '\033[32m', 'Online', '\033[1m')
    print(s)

    # Variable that starts the while loop
    server_ready = True

    while server_ready:

        # wait_connections is variable with client waiting for connection and dialogue with server
        # Select allows the first client in wait client to connect with the server every 0,05 second
        wait_connections, wlist, xlist = select.select([s], [], [], 0.05)
        select.select([s], [], [], 0.05)

        # for connection in wait connections, accept the first client who wants to connect with server
        # and append this client in list of connected_client, print connection_client in the console and log this
        # connection with the process log_connection
        for connection in wait_connections:
            connection_client, info_connection = connection.accept()
            client_connected.append(connection_client)
            print(connection_client)
            log_connection(connection_client)

    ####################################################################################################################

        # Create a empty list read_client
        read_client = []

        # Part of the program that passes the possible errors in order to run the rest program
        try:
            read_client, wlist, xlist = select.select(client_connected, [], [], 0.05)

        except select.error:
            pass
        else:

            # for client in read_client, receive message of this client, and use process_server to record the message
            for client in read_client:
                msg_recv = client.recv(1024)

                msg_recv = msg_recv.decode()

                process_server(msg_recv)

                print('[', '\033[31m', 'SERVER@', '\033[36m', HOST, '\033[33m', '-p ', str(PORT),
                      '\033[39m', ']: Client send a message. Go to ./log.txt to see more.')

                if msg_recv == "Qj-oK":
                    server_ready = False
                    break

                ###############################################
                # Function or process to open last message and convert him
                d_l = dict_log()

                c2c = str_log(d_l)

                p_server = c2c

                ###############################################

                # encode the message give by server
                byte_data = p_server.encode()

                # send message to the client
                client.sendall(byte_data)

    ####################################################################################################################
    console = input("[" + datetime.datetime.isoformat(datetime.datetime.now()) + "]>")
    consoleCommand(console)
    print("Close all connections")
    # For client in client_connected, disconnect all client
    for client in client_connected:
        client.close()

    # close the server after executing while bool
    s.close()


def run():
    """
    Run process

        Arguments
            arg1: none

        Return:
            resturn self

    """

    print('[' + '\033[31m' + 'SERVER@' + '\033[36m' + HOST + ' ' + '\033[33m' + '-p ' + str(PORT) + '\033[39m' + ']:\n')

    while True:
        connection_server()


# Give basic and native documentation in console
documentation()

# Run the program
run()
