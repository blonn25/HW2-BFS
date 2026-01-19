import networkx as nx
from collections import deque


class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None
        """

        # check if the start node exists. If not, throw a ValueError
        if start not in self.graph:
            raise ValueError("Provided start node does not exist in the current graph.")

        # if the end node is not None, check if the end node exists. If not, throw a ValueError
        if end is not None and end not in self.graph:
            raise ValueError("Provided end node does not exist in the current graph.")

        # initialize queue, Q, and a list of visited nodes, visited
        Q = deque([start])      # init queue
        visited = [start]       # init visited nodes list
        
        # if an end node input is provided, initialize the parent dictionary tracking the parent
        # node (value) for each node (key) during BFS traversal
        if end is not None:
            parent_dict = {start: None}

        # while nodes are still in Q, continue to traverse the graph
        while len(Q) > 0:

            # pop off node v at the front of the queue (popleft)
            v = Q.popleft()

            # get the neighbors of v
            N = list(self.graph.neighbors(v))

            # loop through each neighbor, w
            for w in N:
                
                # if w has not been visited, add it to the visited set and enqueue it
                if w not in visited:
                    visited.append(w)
                    Q.append(w)

                    # if an end node input is provided, set node v as the parent of node w in
                    # the parent dictionary
                    if end is not None:
                        parent_dict[w] = v

                        # check if w matches the end node input; if so, construct the shortest
                        # path using the parent dictionary, and return the path
                        if w == end:
                            path = [w]
                            current = w
                            while parent_dict[current] is not None:
                                current = parent_dict[current]
                                path.insert(0, current)
                            return path
        
        # if there is an end node input and a path was not found, return None
        if end is not None:
            return None

        # if an end node input was not provided, return the order of BFS traversal
        return visited