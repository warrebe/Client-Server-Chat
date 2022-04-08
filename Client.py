# Author: Benjamin Warren
# Date: 02/26/2022
# Description: Portfolio Project: Client-Server Chat (Client)

    # Citation for the following program:
      # Date: 02/26/2022
      # Based on: Real Python examples
      # Source URL: https://realpython.com/python-sockets/

import socket # for socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect(("127.0.0.1", 2000)) # Connect to server at 127.0.0.1:2000
    print("Connected to: localhost on port: 2000")
    print("Type /q to quit")
    print("Enter message to send...")
    while True:
        receive = None
        send = input(">") # Wait for input
        send = send.encode() # Format
        soc.sendall(send) # Send data to server
        while receive is None: # Wait for response
            receive = soc.recv(1024)
        print(receive.decode()) # Decode Byte message
        if send.decode() == "/q": # If sent /q end loop
            break
