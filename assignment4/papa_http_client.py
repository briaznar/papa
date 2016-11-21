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


def download_files(url):
    url = (urlparse(url))
    HOST = url.netloc
    PORT = 80
    CRLF = "\r\n\r\n"
    file_name = get_file(url.path)
    dir = os.path.realpath('.')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    request = "GET " + url.path + " HTTP/1.0" + CRLF
    sock.send(request.encode())

    if file_name.find(".html") > 0:
        file_type = 'text'
        sep_string = b'\r\n\r\n904f\r\n'
    else:
        file_type = 'image'
        sep_string = b'\r\n\r\n'

    byte_data = b''
    while True:
        data = sock.recv(1024)
        byte_data = byte_data + data
        if not data:
            with open(os.path.join(dir, file_name), 'wb') as file_to_write:
                header, sep, body = byte_data.partition(sep_string)
                file_to_write.write(body)
                file_to_write.close()
            break

    with open(os.path.join(dir, file_name + ".header"), 'wb') as file_to_write:
        print(header.decode())
        file_to_write.write(header)
        file_to_write.close()
    sock.close()
def main():

    url = input("Type in the URL")
    url = url.strip()
    download_files(url)

if __name__ == "__main__":
    main()