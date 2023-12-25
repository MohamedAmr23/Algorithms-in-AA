
from collections import defaultdict



class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  
        self.V = vertices  


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def topological_sort_util(self, v, visited, stack):


        visited[v] = True
        print(v," is visited")
        

        for i in self.graph[v]:
            if not visited[i]:
                print("send ",i," (which is connected to ",v," ) to topological sort until")
                self.topological_sort_util(i, visited, stack)


        print("add ",v," to front of topological order")
        stack.insert(0, v)


    def topological_sort(self):

        visited = [False] * self.V
        stack = []


        for i in range(self.V):
            if not visited[i]:
                print("send ",i," to topological sort until")
                self.topological_sort_util(i, visited, stack)

        print(stack)


ge = Graph(6)
ge.add_edge(0, 1)
ge.add_edge(0, 2)
ge.add_edge(2, 1)
ge.add_edge(2, 3)
ge.add_edge(2, 4)
ge.add_edge(4, 3)
ge.add_edge(5, 0)
ge.add_edge(5, 3)

print("Following is a Topological Sort of the given ge graph")
ge.topological_sort()