#!/usr/bin/env python

import socket

#HOST, PORT = '', 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server=''
print(server)
port=8888
s.bind((server,port))
s.listen(1)
conn, addr =s.accept()
print ("connected by",addr)
while True:
    data=conn.recv(1024)
    print ("Received", repr(data))
    if not data: break
    reply= input("Reply : ")
    conn.sendall(reply.encode())
conn.close()
server_ip=socket.gethostbyname(server)

	   
