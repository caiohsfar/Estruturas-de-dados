#Aluno: Caio Henrique de Souza Farias, BSI-UFRPE
def F(n):
  F.counter += 1
  if n == 1:
    return 1
  if n%2 == 0:
    return F(n/2)
  if n%2 == 1:
    return F(3*n+1)
def G(m,n):
  F.counter = 0
  chamadas = []
  for i in range(m,n):
    F(i)
    chamadas.append(F.counter)
    F.counter = 0
  print(chamadas)
  return max(chamadas)
x = int(input())
casos = []
for i in range (x):
  y = input().split()
  num = G(int(y[0]),int(y[1]))
  casos.append(num)
for i,j in enumerate(casos):
  print("Caso {}: {}".format(i+1,j))

