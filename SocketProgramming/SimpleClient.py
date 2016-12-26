import socket

HOST ='localhost'
print(HOST)
port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,port))
while True:
    message=input("Your message")
    s.send(message.encode())
    print("Ammiting Message")
    reply=s.recv(1024)#maximum data that can be received
    print("Received: ", repr(reply))
s.close()
    
    
