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

def main():
    grafo = Graph()
    lista = []
    entrada = input().split()
    cidades = int(entrada[0]) 
    for i in range(cidades):
        lista.append(Vertice(i))
    voos = int(entrada[1])
    for i in range(voos):
        edge = input().split()
        v1 = lista[int(edge[0])]
        v2 = lista[int(edge[1])]
        w = int(edge[2])
        grafo.add_e(v1,v2,w)
    lista = list(grafo.adj.keys())
    maiores = []
    for v in grafo.adj.keys():
        menores = Dijkstra(grafo,v)
        maiores.append(max(menores))
    print(min(maiores))
    
def getKeyPeso(a):
    return a[1],a[0][0] #ordena pelo peso principalmente, depois pelo primeiro valor da tupla
def Ordena_Peso(dic):
    tuplas = [(v,k) for v,k in dic.items()] #transforma dicionario em tuplas
    tuplas.sort(key=getKeyPeso) #ordena a tupla pelas keys dadas
    ordenado = {}
    for i,j in tuplas:  #transforma novamente as tuplas em dic
        ordenado[i] = j
    return ordenado
'''
1 2 15
1 3 12
2 4 13
2 5 5
3 2 6
3 4 6
'''
def Kruskal(grafo,n_vertices):
    conjuntos = {}
    for i in range(1,n_vertices+1):
        conjuntos[i] = set({i})
    A =  []
    E = Ordena_Peso(grafo.edges)
    for u,v in E.keys():
        if u not in conjuntos[v]:
            conjuntos[u] = conjuntos[u].union(conjuntos[v])
            conjuntos[v] = conjuntos[v].union(conjuntos[u])
            for i in conjuntos[u]:
                conjuntos[i] = conjuntos[u]
            A.append((u,v))
    def getKeySaida(A):
        return A[0],A[1] #prioridades
    A.sort(key=getKeySaida)
    return A
while True:
    grafo = Graph
    entrada = input().split()
    n_vertices = int(entrada[0])
    if n_vertives == 0:
        break
    for i in range(int(entrada[1])):
        


    
        
        
           




    


