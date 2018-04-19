def h(k,T):
    A = 5**(1/2)
    m = len(T)
    return int(m(k*A) % 1) # Função hash foda

def Teste_Linear(k,j,T):
    m = len(T)
    return (h(k,T)+j)%m

def Teste_Quadr(k,j,T):
    m = len(T)
    return (h(k,T)+j**2)%m
    
def Insert_Aberto(T,k):
    i = 0
    m = len(T)
    while True:
        j = Teste_Linear(k,j,T) #Função de sondagem
        if T[j] == None: #Se não tiver nada na posição
            T[j] = k #Adiciona k na posição
            return j
        else:
            i += 1 #Se tiver, houve colisão, então incremente o i
        if i == m:
            break #acabou a tabela
def Search_Aberto(T,k):
    i = 0
    while True:
        j = Teste_Linear(k,j,T)
        if T[j] == k:
            return j #ou k
        i += 1
        if T[j] == None or i > len(T):
            return None #Não está na tabela
            
print("0i")