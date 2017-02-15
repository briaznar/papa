import os
import re
import wget
import sys
import urllib
from urllib.parse import urlparse

#increments the number of times a function can call itself
sys.setrecursionlimit(1000)
url = 'http://141.26.208.82/articles/g/e/r/Germany.html'
path_to_file = os.path.realpath('.') + '\\wikipedia_crawl'
domain = 'http://141.26.208.82'
absolute_link = []

def get_links(file_name):
    links = []
    # lin = []
    # regex to check the a tag
    regex = re.compile(r'<\s*a [^>]*href="([^"]+)')

    with open(file_name, encoding="utf8") as file:
        for line in file:
            if regex.findall(line):
                if line.find(domain) > -1 or line.find('http://') == -1:
                        links.extend(regex.findall(line))
        file.close()

    #print("Number of links in " + file_name + ": " + len(links))
    for l in links:
        #if the first charater is # ignore
        if l.find('#') != 0:
            get_absolute_link(l)

def get_absolute_link(link):
    url_path = urlparse(url)
    protocol = url_path.scheme
    host = url_path.netloc
    path = url_path.path
    parts = path.split('/')
    #removes first element ''
    parts.pop(0)
    #removes file name
    parts.pop()
    parts_length = len(parts)
    i = 0
    index = 0

    while True:
        index = link.find('..', index)
        if index == -1:
            #dir = os.listdir(path=path_to_file)
            #print(dir)
            if link not in absolute_link:
                absolute_link.append(link)
                abs_link = protocol + '://' + host + '/' + link
                go_crawl(abs_link)
            break
        if i < parts_length:
            link = link.replace('../', '', 1)
            i += 1
        else:
            link = link.strip('../')
            if link not in absolute_link:
                absolute_link.append(link)
                abs_link = protocol + '://' + host + '/' + link
                go_crawl(abs_link)
                break

def go_crawl(url):
    os.makedirs(path_to_file, exist_ok=True)
    file_name = url.split('/')[-1]
    try:
        # file_name = url.split('/')[-1]
        # response = urllib.request.urlopen(url)  # 1469 files
        # data = response.read()  # a `bytes` object
        # response.close()
        # with open(os.path.join(path, file_name), 'wb') as file_to_write:
        #    file_to_write.write(data)
        #   file_to_write.close()
        # print(path + '\\' + file_name)
        # get_links(path + '\\' + file_name)

        file = wget.download(url, out=path_to_file) #1380 files
        print(file)
        #print(len(absolute_link))
        #print(sys.getsizeof(absolute_link) )
        #links_in_page = len(links)
        get_links(file)
    except Exception:
        print("¯\_(ツ)_/¯ Couldn't download " + url)

def main():
    go_crawl(url)
    print("\(•◡•)/ Hurray! you just crawled simple english wikipedia")

if __name__ == "__main__":
            main()
