#Python program to print topological sorting of a DAG 
from collections import defaultdict 
import json


#Class to represent a graph 
class Graph:
    def __init__(self,vertices,graph): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices
        for node,vertex in graph.items():
            for v in vertex:
                self.addEdge(node,v)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self, u, color):
        # GRAY : This vertex is being processed (DFS
        #		 for this vertex has started, but not
        #		 ended (or this vertex is in function        
        #		 call stack)
        color[u] = "GRAY"
        for v in self.graph[u]:
            if color[v] == "GRAY":
                return True	
            if color[v] == "WHITE" and self.DFSUtil(v, color) == True: 
                return True

        color[u] = "BLACK"
        return False

    def isCyclic(self): 
        color = ["WHITE"] * self.V 

        for i in range(self.V): 
            if color[i] == "WHITE": 
                if self.DFSUtil(i, color) == True: 
                    return True
        return False

    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 

        # Mark the current node as visited. 
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 

        # Push current vertex to stack which stores result 
        stack.insert(0,v)

    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[]

        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        if self.isCyclic():
            print("You have cycle in graph")
            return None

        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack)

        # Print contents of the stack 
        print(type(stack))
        print("Following is a Topological Sort of the given graph")
        print(stack)
        return stack

dict1 = {0: [1,2,4], 1: [3], 2: [4], 3: [], 4: []}
JSONgraph = json.dumps(dict1)
graph =json.loads(JSONgraph)        
g= Graph(5,graph)
g.topologicalSort() 