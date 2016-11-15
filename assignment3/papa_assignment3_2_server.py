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

    def protocol(url):
        protocol = url.split("://")
        return protocol

    def domain(url):
        domain = url.split(":")
        domain_string = domain[0].strip("www.")
        if domain_string.count(".") == 1:
            parts  = domain_string.split('.')
            domain = parts[0] + "." +parts[1] 
        elif domain_string.count(".") > 1:
            parts = domain_string.split('.')
            total = len(parts)
            domain = parts[total - 2] + "." + parts[total - 1]
        return domain

    def subdomain(url, domain):
        subdomain = url.split(domain)
        subdomain = subdomain[0].strip("www.")
        return subdomain

    def port(url):
        port = url.split(":")
        port = port[1]
        port = port.split("/")
        port = port[0]
        return port

    def path(url, port):
        path = url.split(port)
        path = path[1].split("?")
        path = path[0]
        return path 

    def params(url, path):
        params = url.split(path)
        params = params[1]
        params = params.split("#")
        params = params[0]
        return params

    def fragment(url):
        fragment = url.split("#")
        fragment = fragment[1]
        fragment = fragment.strip("\\r\\n")
        return fragment

    protocol  = protocol(data)
    url       = protocol[1]
    protocol  = protocol[0]
    domain    = domain(url)
    subdomain = subdomain(url, domain)
    port      = port(url)
    path      = path(url, port)
    params    = params(url,path)
    fragment  = fragment(url)

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