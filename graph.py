from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


#Optimized BFS function Author : Sreyo Biswas
def BFS2(G, node1, node2):
    #initialize all nodes as unmarked and track the predecessors
    marked = {node: False for node in G.adj}
    marked[node1] = True
    prev = {node1: None}
    Q= deque([node1])

    #start BFS traversal
    while len(Q) !=0:
        current_node = Q.popleft()
        if current_node == node2:
            #reconstruct path using predecessors 
            result = []
            node = current_node
            while node is not None:
                result.append(node)
                node = prev[node]
            return result[::-1]
        #visit neighbours and mark them accordingly
        for node in G.adj[current_node]:
            if not marked[node]:
                marked[node] = True
                prev[node] = current_node
                Q.append(node)
    #if no path exists, we return an empty list
    return []

#Optimized DFS function Author : Sreyo Biswas
def DFS2(G, node1, node2):
    #initialize all nodes as unmarked and track the predecessors
    marked = {node: False for node in G.adj}
    marked[node1] = True
    predecessor= {node1: None}
    S = [node1]

    #start DFS traversal
    while len(S) != 0:
        current_node = S.pop()
        if current_node == node2:
            #reconstruct path using predecessors
            result = []
            node = current_node
            while node is not None:
                result.append(node)
                node = predecessor[node]
            return result[::-1]
        #visit neighbours and mark them accordingly
        for node in G.adj[current_node]:
            if not marked[node]:
                marked[node] = True
                predecessor[node] = current_node
                S.append(node)
    #if no path exists, we return an empty list
    return []

#BFS3 function Author : Sreyo Biswas
def BFS3(G, node):
    #initialize all nodes as unmarked
    marked = {n : False for n in G.adj}
    marked[node] = True
    predecessor = {}
    Q = deque([node])

    #start BFS traversal
    while len(Q) != 0:
        current_node = Q.popleft()
        #visit neighbours and mark them accordingly
        for neighbor in G.adj[current_node]:
            if not marked[neighbor]:
                marked[neighbor] = True
                predecessor[neighbor] = current_node
                Q.append(neighbor)
    #return the dictionary of predecessors 
    return predecessor

#DFS3 function Author : Sreyo Biswas
def DFS3(G, node):
    #initialize all nodes as unmarked
    marked = {n: False for n in G.adj}
    marked[node] = True
    predecessor = {}
    S = [node]

    #start DFS traversal
    while len(S) != 0:
        current_node = S.pop()
        #visit neighbours and mark them accordingly
        for neighbor in G.adj[current_node]:
            if not marked[neighbor]:
                marked[neighbor] = True
                predecessor[neighbor] = current_node
                S.append(neighbor)
    #return the dictionary of predecessors
    return predecessor
