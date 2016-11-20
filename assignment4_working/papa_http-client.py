import socket
import os
from urllib.parse import urlparse


def format_file_name(file):
    if file.find(".") == -1:
        return file + ".html"
    else:
        #there is already an extension to the file
        return file

def get_file(path):
    file = path.split("/")
    index = len(file) - 1
    file = format_file_name(file[index])
    return file


#url = input("Type in the URL")
url = "http://west.uni-koblenz.de/en/studying/courses/ws1617/introduction-to-web-science"
#url = "http://west.uni-koblenz.de/sites/default/files/styles/personen_bild/public/_IMG0076-Bearbeitet_03.jpg"
url = url.strip()
url = (urlparse(url))
HOST = url.netloc
PORT = 80
CRLF = "\r\n\r\n"
line_end = "\\r\\n\\r\\n"
file_name = get_file(url.path)
dir = os.path.realpath('.')

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

request = [
    "GET {} HTTP/1.1".format(url.path),
    "Host: {}".format(url.netloc),
    "Connection: Close",
    "User-Agent: Banic_Awesome_User_Agent",
    "",
    "",
]
print(request)
socket.send(CRLF.join(request).encode())

with open(os.path.join(dir, file_name), 'wb') as file_to_write:
    while True:
        data = socket.recv(1024)
        if not data:
            break
        data = data.decode()
        if data.find(CRLF) > 0:
            data = data.replace(CRLF, line_end)
            header = data.split(line_end)[0]
            data = data.replace(header + line_end, '')
        data = data.encode()
        file_to_write.write(data)
    file_to_write.close()


with open(os.path.join(dir, file_name + ".header"), 'wb') as file_to_write:
    print(header)
    header = header.encode()
    file_to_write.write(header)
    file_to_write.close()
socket.close()
