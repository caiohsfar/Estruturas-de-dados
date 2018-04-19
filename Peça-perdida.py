#Aluno: Caio Henrique de Souza Farias - UFRPE - B.S.I.
x = int(input())
y = input().split()
y2 = []
for i in y:
    y2.append(int(i))
soma = 0
for i in range(1,x+1):
    soma += i
resultado = soma - sum(y2)
print(resultado)
