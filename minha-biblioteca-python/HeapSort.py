"""
raiz = 0
pai(i) = (i-1)/2
filho_esq(i) = i*2 +1
filho_dir(i) = i*2+2
"""

def MaxHeapify(a,pai,tam_a):#Tornar as subárvores em um Heap
  maior = pai
  left =  pai*2+1
  right = pai*2+2
  if left < tam_a and a[left] > a[pai]:#swap de índices ao verificar qual índice está o maior elemento
    maior = left
  if right < tam_a and a[right] > a[maior]:
    maior = right
  if maior != pai:#swap de elementos
    chave = a[pai]
    a[pai] = a[maior]
    a[maior] = chave
    MaxHeapify(a,maior,tam_a)
    
def HeapSort(a):
  tam_a = len(a)
  for k in range(int(tam_a/2), -1, -1): #do fim ao começo da árvore transforma-se as folhas em heap
    MaxHeapify(a, k, tam_a)
  for l in range(tam_a-1,0,-1):
    a[l], a[0] = a[0], a[l]
    MaxHeapify(a,0,l)

def RevMaxHeapify(a,pai,tam_a):#Tornar as subárvores em um Heap
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
    RevMaxHeapify(a,menor,tam_a)
    
def ReverseHeapSort(a):
  tam_a = len(a)
  for k in range(int(tam_a/2), -1, -1): #do fim ao começo da árvore transforma-se as folhas em heap
    RevMaxHeapify(a, k, tam_a)
  for l in range(tam_a-1,0,-1):
    a[l], a[0] = a[0], a[l]
    RevMaxHeapify(a,0,l)
a = [0,2,4,1,4,5,7,34,345,2,2]
HeapSort(a)
print(a)


