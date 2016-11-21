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

def make_new_dir(path):
        #Creates relative path to the pictures
        path = path.split('/')
        img_path = ''
        path_len = len(path) - 1
        i = 1
        while i < path_len:
            img_path += '\\' + path[i]
            i += 1

        dir = img_path
        os.makedirs(dir, exist_ok=True)
        return dir


def download_files(url, path = None):
    url = (urlparse(url))
    HOST = url.netloc
    PORT = 80
    #end of line string
    CRLF = "\r\n\r\n"

    if not url.path:
        url_path = "/index.html"
    else:
        url_path = url.path

    print(url_path)
    file_name = get_file(url_path)

    if not path:
        dir = os.path.realpath('.')
    else:
        dir = make_new_dir(path)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    #get request to the server
    request = "GET " + url_path + " HTTP/1.0" + CRLF
    sock.send(request.encode())

    byte_data = b''
    #while the sockets return some data:
    while True:
        data = sock.recv(1024)
        byte_data = byte_data + data
        if not data:
            #write the dowloaded file
            with open(os.path.join(dir, file_name), 'wb') as file_to_write:
                header, sep, body = byte_data.partition(b'\r\n\r\n')
                file_to_write.write(body)
                file_to_write.close()
            break
    #write the header of the file
    with open(os.path.join(dir, file_name + ".header"), 'wb') as file_to_write:
        print(header.decode())
        file_to_write.write(header)
        file_to_write.close()
    sock.close()
def main():

    url = input("Type in the URL: ")
    url = url.strip()
    download_files(url)

if __name__ == "__main__":
    main()