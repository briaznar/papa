import pandas as pd
import networkx as nx
#Functional way, but it takes ages stopped after 6h
def bfs(graph, start, end, visited = []):
    print("{} --- {}".format(start, end))
    # maintain a queue of paths
    queue = []
    if end in visited:
        visited = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            if adjacent not in visited:
                visited.append(adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
    return new_path
def diameter(G, df):
    length = 0
    sub_graph = None
    for subgraph in nx.strongly_connected_components(G):
        if len(subgraph) > length:
            sub_graph = subgraph
            length = len(subgraph)

    graph2 = df.ix[list(sub_graph)]['out_links']
    graph2dict = graph2.to_dict()
    G = nx.DiGraph(graph2dict)
    pG = G.subgraph(sub_graph)
    return nx.diameter(pG)
def createDictionary(df):
    graph = {}
    names = []
    for item in df.itertuples():
        graph[item.name] = item.out_links
    return graph
def readStore():
    store = pd.HDFStore('store.h5')
    return store['df2']
def main():
    df = readStore()
    df = df.set_index("name")
    graph = df.to_dict()['out_links']
    G = nx.DiGraph(graph)
    longest_shortest = diameter(G, df)

    #for i in range(0, len(names)):
     #for j in range(0, len(names)):
        #shortest.append(bfs(graph, names[i], names[j]))

    #print(shortest)
    #longest_shortest = max(shortest)
    print("The longest shortest path aka diameter is {}".format(longest_shortest))
if __name__ == "__main__":
        main()