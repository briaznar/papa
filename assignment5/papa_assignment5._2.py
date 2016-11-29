import os
import re
import urllib
import numpy as npy
from collections import deque
import matplotlib.pyplot as plt
from urllib.parse import urljoin
import matplotlib.patches as mpatches

total_num_links = []
num_external_links = []
num_internal_links = []


# def get_links(file_name, qurl):
def get_links(data, qurl):
    links = []
    links_to_return = []
    internal = 0
    external = 0
    domain = 'http://141.26.208.82'

    # regex to check the a tag
    hrefs = re.compile(r'<\s*a [^>]*href="([^"]+)')

    # with open(file_name, encoding="utf8") as file:
    #     for line in file:
    #         reg = hrefs.findall(line)
    #         if reg:
    #             links.extend(reg)

    regex = hrefs.findall(data)
    if regex:
        links.extend(regex)

    for link in links:
        if link.find(domain) > -1 or link.find('http') != 0:
            internal += 1
            #Dont include links that starts with #
            if link.find('#') != 0:
                link = urljoin(qurl, link)
                links_to_return.append(link)
        else:
            external += 1

    num_external_links.append(external)
    num_internal_links.append(internal)
    total_num_links.append(internal + external)

    return links_to_return

def plot():
    plt.scatter(num_internal_links, num_external_links)

    # adds labels to the axis
    plt.xlabel('Internal Links')
    plt.ylabel('External Links')

    # generates legend
    legend = mpatches.Patch(color='blue', label='Number of link in page')
    plt.legend(handles=[legend])
    plt.title("Number of Internal and External links in pages")
    plt.show()
    return plt

def histogram(total_links):
    total_links = npy.transpose(total_links)
    plt.hist(total_links, bins=5, range =(0,150))
    plt.title("Histogram with 'auto' bins")
    return plt

def main():

    path_to_file = os.path.realpath('.') + '\\wikipedia_crawl'
    os.makedirs(path_to_file, exist_ok=True)
    url = 'http://141.26.208.82/articles/g/e/r/Germany.html'
    #url = 'http://localhost/wikipedia-simple-html/simple/articles/g/e/r/Germany.html'
    queue = deque([url])
    visited = set()
    web_page = set()

    while True:
        if queue:
            element = queue.popleft()
            file_name = element.split('/')[-1]
            if file_name.find(".html") == -1:
                visited.add(element)
                continue
            if element not in visited:
                try:
                    response = urllib.request.urlopen(element)
                    data = response.read()
                    response.close()
                    visited.add(element)
                    web_page.add(element)

                    with open(os.path.join(path_to_file, file_name), 'wb') as file_to_write:
                       file_to_write.write(data)
                       file_to_write.close()

                    if len(web_page) % 1000 == 0:
                        print("pages downloaded: ", len(web_page))
                    print(element)
                    queue.extend(get_links(data.decode(), element))
                except Exception:
                    visited.add(element)
                    #print("Couldn't download " + element)
                    pass
        else:
            break

    print("Hurray! you just crawled simple english wikipedia")

    total_web_pages  = len(web_page)
    total_visited   = sum(total_num_links)
    avg = total_visited / total_web_pages
    median = npy.median(total_num_links)

    print("Now some statistics:")
    print("Phase I")
    print("----------------------------------------")
    print("Total number of web pages visited: ", total_web_pages)
    print("Total number of links encountered: ", total_visited)
    print("Average number of links per website: ", avg)
    print("Median of links per website: ", median)
    hist = histogram(total_num_links)
    hist.show()
    scatter = plot()
    scatter.show()

if __name__ == "__main__":
            main()
