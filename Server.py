# Author: Benjamin Warren
# Date: 02/26/2022
# Description: Portfolio Project: Client-Server Chat (Server)

    # Citation for the following program:
      # Date: 02/26/2022
      # Based on: Real Python examples
      # Source URL: https://realpython.com/python-sockets/

import socket  # for socket

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

soc.bind(("127.0.0.1", 2000)) #Specifies network and port number
soc.listen(1)#Lets the server accept 1 connection
connect, address = soc.accept() #.accept returns tuple of host and port of connection
with connect:
    print("Server listening on: localhost on port: 2000")
    print('Connected by', address)
    print("Waiting for message...")
    while True:
        receive = None # Wait for message from client
        while receive is None:
            receive = connect.recv(1024)
        if receive.decode() == "/q": # If /q quit
            break
        print(receive.decode()) # Print receiving message
        send = input(">") # Wait for input
        send = send.encode() # Format
        connect.sendall(send) # Send data to client


