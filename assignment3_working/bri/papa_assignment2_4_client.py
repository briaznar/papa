import socket
import json 
def Main():
    host = 'localhost'
    port = 8080

    print('Sending http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#InTheDocument to the server')

    clientSocket = socket.socket()
    clientSocket.connect((host, port))

    url = "http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#InTheDocument\\r\\n"
    clientSocket.send(url.encode('utf-8'))

    clientSocket.close()


if __name__ == '__main__':
    Main()