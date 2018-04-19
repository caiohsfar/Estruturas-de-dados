class Graph():
    def __init__(self):
        self.edges = {}
        self.adj = {}
    def add_e(self,v1,v2,w):
        if v1 not in self.adj:
             self.adj[v1] = []
        if v2 not in self.adj:
            self.adj[v2] = []
        if (v1,v2) not in self.edges and (v2,v1) not in self.edges:
            self.edges[(v1,v2)] = w
            self.edges[(v2,v1)] = w
            self.adj[v1].append(v2)
            self.adj[v2].append(v1)
        else:
            if self.edges[(v1,v2)] > w:
                self.edges[(v1,v2)] = w
                self.edges[(v2,v1)] = w
    def get_w(self,v1,v2):
        return self.edges[(v1,v2)] 
    def __str__(self):
        return str(self.edges)
        
class Vertice():
    def __init__(self,name,pi = None,distance = float("inf")):
        self.__name = name
        self.__pi = pi
        self.__distance = distance
    def get_name(self):
        return self.__name
    def get_pi(self):
        return self.__pi
    def set_pi(self,new):
        self.__pi = new
    def get_distance(self):
        return self.__distance
    def set_distance(self,new):
        self.__distance = new          
    def __repr__ (self): 
        return str(self.get_name()) 

def Rlx(graph,u,v):
    if v.get_distance() > (u.get_distance() + graph.edges[u,v]):
        v.set_distance(u.get_distance() + graph.edges[u,v])
        v.set_pi(u)

def Start(graph,s):
    for v in graph.adj.keys():
        v.set_distance(float("inf"))
        v.set_pi(None)
    s.set_distance(0)

def Extract_Min(Q):
    menor = float("inf")
    vertice = ""
    for v in Q:
        if v.get_distance() < menor: ########### O(n)
            menor = v.get_distance()
            vertice = v
    Q.remove(vertice)
    return vertice

def Dijkstra(graph,menor_dist):
    lista_vertices = list(grafo.adj.keys())
    Start(graph,menor_dist)
    S_list = []
    Q = lista_vertices
    while Q != []:
        minimo = Extract_Min(Q) #Vértice de menor distancia
        S_list.append(minimo)
        for vert_adj in graph.adj[minimo]:
            Rlx(graph,minimo,vert_adj)           
    S_list = [x.get_distance() for x in S_list]
    return S_list