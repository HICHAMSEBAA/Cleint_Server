#! /usr/bin/python3

import socket
import sys

HOST = "127.0.0.7"
PORT = 8080
CODE = "Utf8"

# Create a connection socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the precise address
try:
    server.bind((HOST, PORT))
except socket.error:
    print("The Binding socket to the address failed !")
    sys.exit(11)

while 1:
    # waiting for a client connection
    print("Server is listening ...")
    server.listen()

    # Connection is established
    client, address = server.accept()
    print(f"Client on {address[0]}  and Port {address[1]}")

    # 5. The Dialog with the client
    msgSrv = "You are connected to Hicham Server."
    client.send(msgSrv.encode(CODE))

    while 1:
        msgClient = client.recv(1024).decode(CODE)
        print(f"Client sent: {msgClient}")

        if msgClient.upper() == "END":
            break

        msgSrv = "I received your message, OK Continue"
        client.send(msgSrv.encode(CODE))
    # Close the connection
    client.send("The Connection is Finishes".encode(CODE))
    client.close()
    print(f"Connection Finishes With {address}")

    taste = input("Give R to redo, or E to End : ")
    if taste.upper() == "E":
        break
