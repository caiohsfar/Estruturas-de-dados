class Graph():
    def __init__(self):
        self.edges = {}
        self.adj = {}
    def add_e(self,v1,v2,w):
        if v1 not in self.adj:
            self.adj[v1] = []
            
        if v2 not in self.adj:
            self.adj[v2] = []
            
        if (v1,v2) not in self.edges:
            self.edges[(v1,v2)] = w
            self.adj[v1].append(v2)
            
    def Sequencial(self,vert):
        for i in range(len(vert)-1):
            self.add_e(vert[i],vert[i+1],1)
            self.add_e(vert[i+1],vert[i],1)
               
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


def Dijkstra(graph,menor_dist,fim):
    lista_vertices = list(grafo.adj.keys())
    Start(graph,menor_dist)
    S_list = []
    Q = lista_vertices
    while Q != []:
        minimo = Extract_Min(Q) #Vértice de menor distancia
        S_list.append(minimo)
        for vert_adj in graph.adj[minimo]:
            Rlx(graph,minimo,vert_adj)           
    S_list = [x.get_distance() for x in S_list if x.get_name() == fim]
    return S_list

def getKey(item):
    return item.get_name()

def Existe(v1,lista):
    novo_v = None
    for v in lista:
        if v.get_name() == v1:
            novo_v = v
    return novo_v

tamanho = int(input())
lista = []
grafo = Graph()
for i in range(tamanho):
    entrada = input().split(" ")
    v1_nome = entrada[0]
    vertice = Existe(v1_nome,lista)
    if vertice == None:
        v1 = Vertice(v1_nome,float("inf"))
        lista.append(v1)
    else:
        v1 = vertice
    v2_nome = entrada[1]
    vertice2 = Existe(v2_nome,lista)
    if vertice2 == None:
        v2 = Vertice(v2_nome,float("inf"))
        lista.append(v2)
    else:
        v2 = vertice2
    grafo.add_e((v1),(v2),1)

lista = list(grafo.adj.keys())    
vert = sorted(lista,key=getKey)
grafo.Sequencial(vert)
for i in range(2):
    viagem = input()
viagem = viagem.split()
inicio = [x for x in grafo.adj.keys() if x.get_name() == viagem[0]]
fim = viagem[1]
print(Dijkstra(grafo,inicio[0],fim)[0])

