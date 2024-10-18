class IllegalArgumentError(Exception):
    pass

class Graph:
    def __init__(self, v):
        if v < 0:
            raise IllegalArgumentError("Number of vertices cannot be negative")
        
        self.V = v
        self.E = 0
        self.adj = [[] for i in range(0,v)]

    def add_edge(self, v, w):
        
        if v < 0 or v >= self.V or w < 0 or w >= self.V:
            raise IllegalArgumentError("Invalid vertex index")

        self.E += 1
        self.adj[v].append(w)
        self.adj[w].append(v)
        