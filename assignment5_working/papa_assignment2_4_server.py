import socket
import json

def Main():

    socket_server = socket.socket()
    socket_server.bind(('localhost', 8080))

    socket_server.listen(1)
    conn, addr = socket_server.accept()
    print("Connection from: " + str(addr))
    print("Got connection from:", addr)

    inpt = input("Say something nice to the user: ")
    print('Sending ', inpt)
    conn.send(inpt.encode())
    #conn.close()


if __name__ == '__main__':
    Main()