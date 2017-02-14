'''
Objective
1. Create a simple client app
2. Connect to the server port
3. Infinite loop and accept user input
'''

import socket

#Create a TCP/IP socket. No need to bind it, as it a client side app. Can use any random port
sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect to server
sock.connect(('127.0.0.1',50001))

#Infinite loop to Accept user input and send to server
while(True):
    sock.send(input().encode())

#sock.close() -- very Important

