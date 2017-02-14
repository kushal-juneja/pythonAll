'''
Objective:
Create a simple chat server application
1. Create a socket object for IP and TCP and bind to port
2. Accept one connection
3. Set in receive mode
'''

import socket

#Create a socket object
#socket.AF_INET is for IPV4 socket
#SOCK_STREAM is for TCP
#SOCK_RAW is for RAW socket
sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#Host has double qoutes= To bind the socket to all the interfaces/Ip addresses of the machine
#It can be IP address/Interface too
HOST=''
PORT=50001


#Bind takes a tuple
sock.bind((HOST,PORT ))


#Listen to socket. Waiting for a client to attempt a connection
#1 connection
sock.listen(1)


#Accept the connection and create a new socket for tat. Store tat in conn object. Address of client in addr
conn,addr=sock.accept()


#Data receive loop
while(True):
    conn.recv(1024)

#sock.close() -- very Important