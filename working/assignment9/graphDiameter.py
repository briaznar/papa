from collections import deque
import pandas as pd

def createDictionary(df):
    graph = {}
    for item in df.itertuples():
        graph[item.name] = item.out_links
    return graph

def breadthFirstSearch(outLinkSets, root):
    paths = dict()
    visited = set()

    queue = deque()
    queue.append(root)
    paths[root] = 0

    while queue:
        current = queue.pop()
        try:
            for link in outLinkSets[current]:
                if link not in visited:
                    visited.add(link)
                    paths[link] = int(int(paths[current]) + 1)
                    queue.append(link)
        except:
            pass

    return paths


store = pd.HDFStore('store2.h5')
df1 = store['df1']
df2 = store['df2']

# df1=df1[df1.text!=""]
# df1=df1[df1.text.str.len()>20]

#store.close()

#outLinkSets = dict()

#numOfDocuments = len(df1['text'])

#for i in range(numOfDocuments):
    #link = df2.get_value(i, 'out_links')
    #outLinkSets[df1['name'][i]] = set(link)
outLinkSets = createDictionary(df2)
minList = list()

for name in outLinkSets.keys():
    paths = breadthFirstSearch(outLinkSets, name)
    minList.append(max(paths.values()))
   # print(max(paths.values()))


print(max(minList))
print("OVER")