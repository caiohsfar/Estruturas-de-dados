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
    
def getKeyPeso(a):
    return a[1],a[0][0] #ordena pelo peso principalmente, depois pelo primeiro valor da tupla

def getKeySaida(A):
        return A[0],A[1] #prioridades

def Ordena_Peso(dic):
    tuplas = [(v,k) for v,k in dic.items()] #transforma dicionario em tuplas
    tuplas.sort(key=getKeyPeso) #ordena a tupla pelas keys dadas
    ordenado = {}
    for i,j in tuplas:  #transforma novamente as tuplas em dic
        ordenado[i] = j
    return ordenado

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
    A.sort(key=getKeySaida)
    return A

def Cacique():
    cont = 1
    while True:
        grafo = Graph()
        entrada = input().split()
        n_vertices = int(entrada[0])
        if n_vertices != 0:
            if cont > 1:
                print("")
            print("Teste {}".format(cont))
            cont +=1
            for i in range(int(entrada[1])):
                arestas = input().split()
                v1 = int(arestas[0])
                v2 = int(arestas[1])
                peso = int(arestas[2])
                grafo.add_e(v1,v2,peso)
                arvore = Kruskal(grafo,n_vertices)
            for i,j in arvore:
                print("{} {}".format(i,j))     
        else:
            break

Cacique()


    
        
        
           




    


