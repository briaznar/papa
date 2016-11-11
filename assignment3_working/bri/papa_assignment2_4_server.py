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

    url        = data.split(".")
    colon      = url[0].split(":")
    protocol   = colon[0]
    domain     = url[2]
    domain     = domain.split(":")
    domain     = domain[0]
    subdomain  = url[1]

    port       = url[2].split(":")
    path       = port[1]
    port       = port[1].split("/")
    port       = port[0]
    path       = path.split("80")
    path       = path[1]
    tail       = url[3].split("?")
    tail       = tail[1].split("#")
    params     = tail[0]
    fragment   = tail[1]
    fragment   = fragment.split("\\")
    fragment   = fragment[0]

    print('Protocol: ', protocol)
    print('Subdomain: ', subdomain)
    print('Domain: ', domain)
    print('Port: ', port)
    print('Patha: ', path)
    print('Params: ', params)
    print('Fragments: ', fragment)
    conn.close()


if __name__ == '__main__':
    Main()