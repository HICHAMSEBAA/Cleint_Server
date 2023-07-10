#! /usr/bin/python3

import socket
import sys


HOST = "127.0.0.7"
PORT = 8080
CODE = "Utf8"

# Create a connection socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Trying a request to a server, if no error
try:
    client.connect((HOST, PORT))
except socket.error:
    print("The Connection failed !")
    sys.exit(11)


msgServer = client.recv(1024).decode(CODE)
print(msgServer)

# Dialog with server
while 1:

    msgClient = str(input("Enter your Massage : "))
    if msgClient == "" or msgClient.upper() == "END":
        client.send("end".encode(CODE))
        msgServer = client.recv(1024).decode(CODE)
        print(f"From Server : {msgServer}")
        break
    else:
        client.send(msgClient.encode(CODE))

    msgServer = client.recv(1024).decode(CODE)
    print(f"From Server : {msgServer}")

# Communication ends
client.close()