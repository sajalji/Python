import socket

#this is server which handles one client more efficiently

def recieveData(s,conn):# function to receive data
    data=conn.recv(1024)
    print(conn,data,"\n")
    return data;

def broadcastData(s,conn,data):
    conn.sendall(data)
    print("Data sent to all clients\n")
    



def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('',8888))
    s.listen(5)#no of connection listening for
    print("Server is running")
    conn,addr=s.accept()
    print (addr,"is now connected")
    while True:
        data=recieveData(s,conn)
        broadcastData(s,conn,data)

main()
    
