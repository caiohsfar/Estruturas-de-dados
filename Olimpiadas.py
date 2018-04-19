def RevMaxHeapify(a,pai,tam_a):#HeapSort Reverso com o HeapSort normal imbutido
  menor = pai
  left =  pai*2+1
  right = pai*2+2
  if left < tam_a and a[left].pontos < a[pai].pontos: 
    menor = left
  if left < tam_a and a[left].pontos == a[pai].pontos:#maxHeapify dentro do RevMaxheapify
    if a[left].nome > a[pai].nome:
      menor = left
  if right < tam_a and a[right].pontos < a[menor].pontos:
    menor = right
  if right < tam_a and a[right].pontos == a[menor].pontos:
    if a[right].nome > a[menor].nome:
      menor = right
  if menor != pai:#swap de elementos
    chave = a[pai]
    a[pai] = a[menor]
    a[menor] = chave
    RevMaxHeapify(a,menor,tam_a)
def ReverseHeapSort(a):
  tam_a = len(a)
  for k in range(tam_a, -1, -1): #do fim ao começo da árvore transforma-se as folhas em heap
    RevMaxHeapify(a, k, tam_a)
  for l in range(tam_a-1,0,-1):
    a[l], a[0] = a[0], a[l]
    RevMaxHeapify(a,0,l)
###########################################################
class Pais():
  def __init__ (self,nome):
    self.nome = nome
    self.pontos = 0
  def add_pontos(self,pontos):
    self.pontos += pontos
    
x = input().split()
paises = int(x[0])
mod = int(x[1])
matrix = []
for i in range(mod):
    med = input().split()
    temp = []
    for j in range(3):
        temp.append(int(med[j]))
    matrix.append(temp)
ouro = []
prata = []
bronze = []
for i,x in enumerate(matrix):
    for j,y in enumerate(x):
        if j == 0:
            ouro.append(y)
        if j == 1:
            prata.append(y)
        if j == 2:
            bronze.append(y)
lista = []
for i in range(1,paises+1):
    lista.append(Pais(i))
for i in ouro:
    lista[i-1].add_pontos(100)
for i in prata:
    lista[i-1].add_pontos(10)
for i in bronze:
    lista[i-1].add_pontos(1)
ReverseHeapSort(lista)
ordem = []
for i in lista:
  ordem.append(i.nome)
campo = ""
for i in ordem:
  campo += "{}" " ".format(i)
print(campo)

    

      




        





        

