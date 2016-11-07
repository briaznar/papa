import socket
import json 
def Main():
    host = 'localhost'
    port = 8080

    name     = input('Enter your name: ')
    age      = input('Enter your age: ')
    m_nummer = input('Enter your matrikelnummer: ')

    clientSocket = socket.socket()
    clientSocket.connect((host, port))

    data = {}
    data['name'] = name
    data['age'] = age
    data['matrikel'] = m_nummer
    json_data = json.dumps(data)
    clientSocket.send(json_data.encode('utf-8'))

    clientSocket.close()


if __name__ == '__main__':
    Main()