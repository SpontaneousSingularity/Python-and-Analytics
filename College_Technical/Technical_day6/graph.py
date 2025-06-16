class Graph:
    def __init__(self):
        self.adjacencey = {}
    
    # def add_edge(self, vertex):
    #     if vertex not in self.adjacencey.keys():
    #         self.adjacencey[vertex] = []
    #         return True
    #     return False
    
    def add_vertex(self,vertex):
        if vertex not in self.adjacencey.keys():
            self.adjacencey[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacencey.keys() and vertex2 in self.adjacencey.keys():
            self.adjacencey[vertex1].append(vertex2)
            self.adjacencey[vertex2].append(vertex1)
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacencey.keys():
            print(f'{vertex} : {self.adjacencey[vertex]}')

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.add_vertex('E')
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'E')
my_graph.add_edge('C', 'D')
my_graph.add_edge('D', 'E')
my_graph.print_graph()