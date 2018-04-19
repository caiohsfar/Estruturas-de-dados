def Constroi_Heap(a):
  tam_a = len(a)
  #É /2 pois todas as folhas de uma árvore já são obrigatóriamente um heap
  for k in range(int(tam_a/2), -1, -1): 
      MinHeapify(a, k,tam_a)

def MinHeapify(a,pai,tam_a):#Tornar as subárvores em um Heap
  menor = pai
  left =  pai*2+1
  right = pai*2+2
  if left < tam_a and a[left] < a[pai]:#swap de índices ao verificar qual índice está o menor elemento
    menor = left
  if right < tam_a and a[right] < a[menor]:
    menor = right
  if menor != pai:#swap de elementos
    chave = a[pai]
    a[pai] = a[menor]
    a[menor] = chave
    MinHeapify(a,menor,tam_a)
def Constroi_Heap_Max(a):
  tam_a = len(a)
  #É /2 pois todas as folhas de uma árvore já são obrigatóriamente um heap
  for k in range(int(tam_a/2), -1, -1): 
      MaxHeapify(a, k,tam_a)

def MaxHeapify(a,pai,tam_a):#Tornar as subárvores em um Heap
  menor = pai
  left =  pai*2+1
  right = pai*2+2
  if left < tam_a and a[left] > a[pai]:#swap de índices ao verificar qual índice está o menor elemento
    menor = left
  if right < tam_a and a[right] > a[menor]:
    menor = right
  if menor != pai:#swap de elementos
    chave = a[pai]
    a[pai] = a[menor]
    a[menor] = chave
    MaxHeapify(a,menor,tam_a)
def Extract_Max(A):
  tam = len(A)
  if len(A) < 1:
    return
  minimo = A[0]
  A[0] = A[-1]
  del A[-1]
  tam -= 1
  MaxHeapify(A,0,tam)
  return minimo

def Extract_Min(A):
  tam = len(A)
  if len(A) < 1:
    return
  minimo = A[0]
  A[0] = A[-1]
  del A[-1]
  tam -= 1
  MinHeapify(A,0,tam)
  return minimo

def teste():
  Q = [4,2,8,2,6,10,1,0,50]
  Constroi_Heap(Q)
  for i in range(len(Q)):
    print(Extract_Min(Q))
    print(Q)
teste()







