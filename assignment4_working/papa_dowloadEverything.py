from urllib.parse import urlparse
#call to the http client program
from  papa_http_client import download_files
import re

def get_images_path(file_name,url):
    images = []
    image_path = []
    #regex to check the image tag
    regex = re.compile(r'<\s*img [^>]*src="([^"]+)')
    url = (urlparse(url))
    #gets prefix to absolute path
    host = url.scheme + "://" + url.netloc

    with open(file_name) as file:
        for line in file:
            if regex.findall(line):
                images.append(regex.findall(line))
    for img in images:
        for i in img:
            # homogenizes relative paths to absolute
            if i.find("http://") == -1:
                i = host + i
            image_path.append(i)
    return image_path

def main():
    file_name = "introduction-to-web-science.html"
    url = "http://west.uni-koblenz.de/en/studying/courses/ws1617/introduction-to-web-science"

    images = get_images_path(file_name, url)
    for img in images:
        print(img)
        download_files(img)


if __name__ == "__main__":
            main()
