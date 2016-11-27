import os
import re
import wget
import numpy as npy
import traceback
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from collections import deque
from urllib.parse import urljoin

total_num_links = []
num_external_links = []
num_internal_links = []


def get_links(file_name, qurl):
    links = []
    links_to_return = []
    internal = 0
    external = 0
    domain = 'http://141.26.208.82'
    # regex to check the a tag
    regex = re.compile(r'<\s*a [^>]*href="([^"]+)')

    with open(file_name, encoding="utf8") as file:
        for line in file:
            reg = regex.findall(line)
            if reg:
                links.extend(reg)
                #total_links.append(len(links) + len(external_link))

    for link in links:
        if link.find(domain) > -1 or link.find('http://') == -1:
            internal += 1
            #Dont include links that starts with #
            if link.find('#') != 0:
                link = urljoin(qurl, link)
                links_to_return.append(link)
        else:
            external += 1

    num_external_links.append(external)
    num_internal_links.append(internal)
    total_num_links.append(internal+external)
    return links_to_return

def plot():
    plt.scatter(num_internal_links, num_external_links)
    #plt.plot(total_links, num_internal_links, 'r')
    #point = internal_external


    #plt.plot(point, 'o')
    # adds labels to the axis
    plt.xlabel('Internal Links')
    plt.ylabel('External Links')
    # generates legend
    legend = mpatches.Patch(color='blue', label='External vs Internal')
    plt.legend(handles=[legend], loc=5)
    plt.title("Internal vs External links")
    return plt

def histogram(total_links):
    total_links = npy.transpose(total_links)
    plt.hist(total_links, bins=5, range =(0,150))  # plt.hist passes it's arguments to np.histogram
    plt.title("Histogram with 'auto' bins")
    return plt

def main():
    path_to_file = os.path.realpath('.') + '\\wikipedia_crawl'
    os.makedirs(path_to_file, exist_ok=True)
    url = 'http://141.26.208.82/articles/g/e/r/Germany.html'

    queue = deque([url])
    visited = []
    i = 0
    while True:
        if queue:
            element = queue.popleft()
            if element not in visited:
                try:
                    file = wget.download(element, out=path_to_file)
                    visited.append(element)
                    #print(file)
                    queue.extend(get_links(file, element))
                except Exception:
                    visited.append(element)
                    #print("Couldn't download " + element)
                    pass
            i += 1
            if i == 100:
                break

        else:
            print("queue problem")
            break

    print("Hurray! you just crawled simple english wikipedia")

    total_web_pages = len(visited)
    total_visited   = sum(total_num_links)
    avg = total_visited / total_web_pages
    median = npy.median(total_num_links)
    print("Now some statistics:")
    print("Phase I")
    print("----------------------------------------")
    print("Total number of web pages: ", total_web_pages)
    print("Total number of links encountered: ", total_visited)
    print("Average number of links per website: ", avg)
    print("Median of links per website: " , median)
    hist = histogram(total_num_links)
    hist.show()
    print("----------------------------------------")
    print("Phase II")
    print("----------------------------------------")
    plt = plot()
    plt.show()
    print("----------------------------------------")
if __name__ == "__main__":
            main()
