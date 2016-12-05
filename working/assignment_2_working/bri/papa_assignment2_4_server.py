import socket
import json

def Main():

    socket_server = socket.socket()
    socket_server.bind(('localhost', 8080))

    socket_server.listen(1)
    conn, addr = socket_server.accept()
    print("Connection from: " + str(addr))
    data = conn.recv(1024)
    data = data.decode('utf-8')
    if not data:
        print('no data received')
        return

    data = json.loads(data)
    print('Name:  {}'.format(data['name'] ))
    print('Age: {}'.format(data['age'] ))
    print('Matrikelnummer: {}'.format(data['matrikel'] ))

    conn.close()


if __name__ == '__main__':
    Main()