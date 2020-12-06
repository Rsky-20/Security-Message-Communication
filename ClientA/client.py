#!/bin/python3 -*- coding: utf-8 -*-
"""
@Author : Jessy JOSE -- Pierre VAUDRY
IPSA Aero1 - Prim2
Release date: 09/12/2020


[other information]
Licence: MIT


[Description]

    SMC is a security message communication.
    This program is the part of client program.
    The client uses the socket module to work.
    The datetime is used to make the client fully functional.


[Functions]:
    documentation() --
    info() --
    str2dict() --
    pgcd() -- calculate the greatest common divisor of a and b
    chiffrementAffine() -- algorithm which enables the message to be encrypted using an affine calculation method
    inverse() -- calculation by a inversion of a number
    dechiffrementAffine() -- inverse algorithm which enables the message to be encrypted using an affine calculation method
    crypt() -- crypt process
    decrypt() -- decrypt process
    process_response() -- interprets the data received and exploits it
    connection_client() -- main process of the client
    run() -- run and launch client


[Global variable]:
    {int variable}
        HOST

    {str variable}
        PORT

    {dict variable}
        client_data


[Other variable]:

    Many other constants and variable may be defined; these may be used in calls to
    the info(), str2dict(), pgcd(), chiffrementAffine(), inverse(), dechiffrementAffine(), crypt(), decrypt(),
    process_response(), connection_client() functions

"""

# ----------------------------------------------Import module section------------------------------------------------- #

import socket
import datetime

# -------------------------------------------------Global variable---------------------------------------------------- #
# Definition of local server variable

# Host is local adress for binding the server
HOST = "127.0.0.1"

# Port is the gate than the client take to discuss with the client
PORT = 50100

# client_data is a dict. It's use to make a information of client
client_data = {
    "client": {
        "id": "#8hdjajcur5d9l2",
        "user_name": "",
        "message_send": 0,
        "message_receive": 0,
        "password": "test"
    }
}


# --------------------------------------------------Functions & process----------------------------------------------- #


def documentation():
    """
    [Description]
    This process return a native and basic documentation to the administrator of the serverS with a great ascii art
    screen

    :return: none
    """

    TEXT = '\033[36m' + """
 __       __            __                                                    __                   ______   __       __   ______  
|  \  _  |  \          |  \                                                  |  \                 /      \ |  \     /  \ /      \ 
| $$ / \ | $$  ______  | $$  _______   ______   ______ ____    ______         \$$ _______        |  $$$$$$\| $$\   /  $$|  $$$$$$\ 
| $$/  $\| $$ /      \ | $$ /       \ /      \ |      \    \  /      \       |  \|       \       | $$___\$$| $$$\ /  $$$| $$   \$$
| $$  $$$\ $$|  $$$$$$\| $$|  $$$$$$$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\      | $$| $$$$$$$\       \$$    \ | $$$$\  $$$$| $$      
| $$ $$\$$\$$| $$    $$| $$| $$      | $$  | $$| $$ | $$ | $$| $$    $$      | $$| $$  | $$       _\$$$$$$\| $$\$$ $$ $$| $$   __ 
| $$$$  \$$$$| $$$$$$$$| $$| $$_____ | $$__/ $$| $$ | $$ | $$| $$$$$$$$      | $$| $$  | $$      |  \__| $$| $$ \$$$| $$| $$__/  \ 
| $$$    \$$$ \$$     \| $$ \$$     \ \$$    $$| $$ | $$ | $$ \$$     \      | $$| $$  | $$       \$$    $$| $$  \$ | $$ \$$    $$
 \$$      \$$  \$$$$$$$ \$$  \$$$$$$$  \$$$$$$  \$$  \$$  \$$  \$$$$$$$       \$$ \$$   \$$        \$$$$$$  \$$      \$$  \$$$$$$
                                                                                                                                                                                                                                                  
                                                              /%&@@@@@&%/                           
                                                       @@@@@@@@&&(((((&&@@@@@@@@.                   
                                                   @@@@@,,,,,,,,,,,,,,,,,,,,,,,@@@@@                
                                                @@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@             
                                              &@@@,,,,,,,,,,,,,,%@*,,%/%@%***@,,,,,,,&@@&           
                                             @@@(@@@@@@@@@@@*,,,,*,,,,,,,,,,,,,,,,,,,,,@@@          
                                         &@@@@@@@&,,,.....%@@@@@@@@*,,,,,,,,,,,,,,,,,,,,@@@         
                                     (@@@@&(#((***,,,,....,.......@@@@@,,,,,,,,,,,,,,,,,@@@         
                                   @@@@*,#*((/(/(/,,,,,,,,...,....   ,@@@&,,,,,,,,,,,,,,@@@         
                                 @@@,,/,,(*,/%/(((*,,,,.,....,.,..  ,..,@@@%,,,,,,,,,,,&@@          
                                @@@./.  ..*(((/#//***,*,,,,*,,*.. ..,, .  @@@,,,,,,,,,@@@           
                               @@@#,/**..*@@@#(//***#@@&,*,.,,.&@@#. ,,.. .@@%,,,,,,@@@#            
                               @@(*%(,,/@@@(@@@%/*#@@@/@@@**.@@@/&@@(.. .  @@@,,/@@@@               
                               @@@#.,(/,@@@@@@@(..*@@@@@@@(..@@@@@@@       @@@@@@@                  
                               ,@@(/((*#**#/(/,  .*, ..&*////(,,          @@@                       
                                 @@@  */*(/*/. ..... . ...  /*(.,.,,    .@@@                        
                                  %@@@. . . ..,  .,   . .     *,**.*, #@@@                          
                                     @@@@(.   ..,  ,.          ,.   .@@@                            
                                        %@@@@@@(,.. ,. .. . .&@@@ ,  &@@                            
                                              %@@@@@@@@@@@@@@@* @@@. (@@                            
                                                                  @@@.@@.                           
                                                                    @@@@.                           
                                                                      @@.                           
            """ + '\033[39m'
    print(TEXT)


def info(client_data):
    """
    [description]
    Info process make a screen of client information

    :param client_data: dict
    :return: none
    """

    # New variable with importante information about client
    UserTag = client_data['client']['user_name']
    UserID = client_data['client']['id']
    MessageReceive = client_data['client']['message_receive']
    MessageSend = client_data['client']['message_send']
    text = """
    Information : {}{} 
    Message send : {}
    Message receive : {}
    
    """.format(UserTag, UserID, MessageSend, MessageReceive)

    print(text)


def str2dict(data):
    """
    [description]
    Convert a str to dict

    :param data: str
    :return:
    """

    str_msg = data.split(',')
    return str_msg


def pgcd(a, b):
    """
    [description]
    calculate the greatest common divisor of a and b

    :param a: it is an Int
    :param b: it is an Int

    :return: a -> it is an Int
    """

    while b != 0:
        a, b = b, a % b
    return a


def chiffrementAffine(a, b, L):
    """
    [description]
    create a list with all the characters that can be used,
    modulo 97 because in all, there are 97 characters.


    :param a: it is an Int
    :param b: it is an Int
    :param L: it is a character (97 possibilities)
    :return: data[y] -> it is one of the 97 defined characters
    """

    data = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w',
            'x', 'c', 'v', 'b', 'n', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H',
            'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-',
            '_', " ", '?', '.', '/', '§', ':', '!', '%', '$', '£', '€', '*', '=', '"', "'", '|', '`', '\ ', "^", "@",
            '&', '~', '#', '(', '{', '[', '<', '>', "]", "}", ')', 'ù', 'é', 'è', 'ç', 'à', ',']
    x = data.index(L)
    y = (a * x + b) % 97
    return data[y]


def inverse(a):
    """
    [description]
    calculating the inverse of the number of characters,
    we do this to be able to find our departure when we arrive.
    this part will be used to decrypt the message received.

    :param a: it is an Int
    :return: x -> it is an Int
    """

    x = 0
    while a * x % 97 != 1:
        x = x + 1
    return x


def dechiffrementAffine(a, b, L):
    """
    [description]
    create a list with all the characters that can be used,
    modulo 97 because in all, there are 97 characters.
    to decipher we use the inverse calculate just before.

    :param a: it is an Int
    :param b: it is an Int
    :param L: it is a character (97 possibilities)
    :return: data[y] -> it is one of the 97 defined characters
    """

    data = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w',
            'x', 'c', 'v', 'b', 'n', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Q', 'S', 'D', 'F', 'G', 'H',
            'J', 'K', 'L', 'M', 'W', 'X', 'C', 'V', 'B', 'N', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-',
            '_', " ", '?', '.', '/', '§', ':', '!', '%', '$', '£', '€', '*', '=', '"', "'", '|', '`', '\ ', "^", "@",
            '&', '~', '#', '(', '{', '[', '<', '>', "]", "}", ')', 'ù', 'é', 'è', 'ç', 'à', ',']
    x = data.index(L)
    y = (inverse(a) * (x - b)) % 97
    return data[y]


def crypt(M, a, b):
    """
    [description]
    we finally use our functions, we enter the word (M), we enter our values
    of the couple a and b, which corresponds to our encryption key.
    each character entered will match another character, making it impossible to read.
    A character will therefore have two matches, the first is its true value, and the second is false.
    here, it is a question of transforming the true into false.


    :param M: it is a string
    :param a: it is an Int
    :param b: it is an Int
    :return: it is a string, is a succession of characters
    """

    if pgcd(a, 97) == 1:
        mot = []
        for i in range(0, len(M)):
            mot.append(chiffrementAffine(a, b, M[i]))
        return "".join(mot)
    else:
        return "Chiffrement impossible. Veuillez choisir un nombre ( a ) premier avec 97."


def decrypt(M, a, b):
    """
    [description]
    we finally use our functions, we enter the word (M), we enter our values
    of the couple a and b, which corresponds to our encryption key.
    each character entered will match another character, making it impossible to read.
    A character will therefore have two matches, the first is its true value, and the second is false.
    here, it is a question of transforming the false into true.

    :param M: it is a string
    :param a: it is an Int
    :param b: it is an Int
    :return: it is a string, is a succession of characters
    """

    if pgcd(a, 97) == 1:
        mot = []
        for i in range(0, len(M)):
            mot.append(dechiffrementAffine(a, b, M[i]))
        return "".join(mot)
    else:
        return "Déchiffrement impossible. Le nombre a n'est pas premier avec 97"


def process_response(data, data2, messager):
    """
    [description]
    process_response is a function that processes data given by client.
    It's a part of server to use client data.
    He use a str value given by client and use it in process.

    :param data: str -> message give by user
    :param data2: str element of a dict -> used for client information
    :param messager: int -> used for count the number of message send
    :return: messager -> counter of message send
    """

    str_l = data
    client_ = str_l.split('|')
    # print(client_) # line that allows you to see what is happening

    del client_[0]

    msg = str2dict(str(client_[0]))

    if msg[0] != data2:
        print('Response: ' + decrypt(msg[1], 35, 19))
        messager = messager + 1
    else:
        print('')
    return messager


def connection_client(HOST, PORT):
    """
    [description]
    connection_client is a main process in the client program.
    He use socket module to create a client.
    It's the main part of client.
    He take global value of the program like HOST and PORT, to bind and communicate with the server.
    Make a connection with server, wait to send data, process it with the
    process_responce function.

    AF_INET represents the IPv4 address family.
    SOCK_STREAM represents the TCP protocol.

    :param HOST: str
    :param PORT: int
    :return: none
    """

    client_data['client']['user_name'] = input("Donnez votre nom d'utilisateur : ")

    # Creating a socket, by creating a socket object named s.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # s.connect((address,port)) binds an address and a port to socket s.
    # The address parameter is a tuple consisting of the IP address of the
    # server and a port number.
    # s.bind((data_server['HOST'], data_server['PORT']))
    s.connect((HOST, PORT))

    print("connection établie avec le serveur sur le port {}".format(PORT))
    # Make a variable client_info. This variable contains all the important information of client.
    client_info = '[' + 'CLIENT ' + s.getsockname()[0] + ':' + '' + str(s.getsockname()[1]) + "]"
    print('\033[31m' + 'CLIENT ' + client_data['client']['user_name'] + ' \033[36m' + s.getsockname()[0] + ':'
          + '\033[33m' + str(s.getsockname()[1]))
    print('\033[31m' + 'SERVER  ' + '\033[36m' + HOST + ':' + '\033[33m' + str(PORT))

    # Initialization of message Send and message Receive during the process
    messageS = 0
    messageR = 0
    # Initialization of the message send by user.
    # Bytes literals are always prefixed with 'b' or 'B';
    # they produce an instance of the bytes type instead of the str type.
    # They may only contain ASCII characters;
    # bytes with a numeric value of 128 or greater must be expressed with escapes.
    send_msg = b""
    while send_msg != b"/stop":
        # msg contains message given by user
        msg = input("> ")
        # Condition to count messages, stop the process or continue sending
        if msg:
            messageS = messageS + 1
            client_data['client']['message_send'] = messageS

        # Variable that contains the encrypted message
        send_msg = crypt(msg, 35, 19)

        if msg == '/stop':
            send_msg = b"/stop"
        else:
            # Contains information about send_time, relative id of client, client_info and encrypted user message
            send_msg = datetime.datetime.isoformat(datetime.datetime.now()) + '|' + client_data['client']['id'] \
                       + client_info + "@" + send_msg

            # Encode the final client message in byte array
            sending_msg = send_msg.encode()
            # Send encoding message to client
            s.sendall(sending_msg)

            # And wait to receive response. 1024 is max information able to receive
            msg_recv = s.recv(1024)

            # Decipher
            response = msg_recv.decode()
            # print(response)

            #######################################################################

            # use returned value of counter to update global value in client_data dict
            messageR = process_response(response, client_data['client']['id'] + client_info, messageR)

            # Update of information contained in client_data
            client_data['client']['message_receive'] = messageR
            client_data['client']['message_send'] = messageS

            #######################################################################

    # Return stop command to server and close the client when the process is finished
    print("Close all connection")
    send_stop = '/stop'
    sending_stop = send_stop.encode()
    s.sendall(sending_stop)
    info(client_data)
    s.close()


def run():
    """
    [description]
    Run process

    :return: none
    """

    connection_client(HOST, PORT)


# -----------------------------------------------Run & Start server program------------------------------------------- #


if __name__ == '__main__':

    # Give basic and native documentation in console
    documentation()

    # Run the program
    run()
