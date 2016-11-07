import socketserver

class EchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        self.request.send(data)
        return

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 8080)
    server = socketserver.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address # find out what port we were given

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # don't hang on exit
    t.start()

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    #ask for the data
    userinfo = input("Please provide your name, age, and matriklenumer separated by colons (,)")
    #encode input 
    userinfo = userinfo.encode('utf-8')
    # Send the data
    print('Sending : "%s"' % userinfo)
    len_sent = s.send(userinfo)

    # Receive/decode the response
    response = s.recv(len_sent).decode('utf-8')
    #Formatting the response
    response = response.split(',')
    print("Name: ",response[0])
    print("Age: ",response[1])
    print("Matriklenummer: ",response[2])


    # Clean up
    s.close()
    server.socket.close()