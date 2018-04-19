a = input().split()
linha = int(a[0])
coluna = int(a[1])
base1 =[] 
m = [base1]
for i in range(coluna+2):
    base1.append(".")
for i in range(linha):
    k = list("."+input()+".")
    m.append(k)
base2 = []
for i in range(coluna+2):
    base2.append(".")
m.append(base2)

def Explorar(m,i,j):
    global contador 
    if m[i][j] == "." or m[i][j] == contador:
        return
    elif m[i][j] == "#":
        m[i][j] = contador 
        global tamanho 
        tamanho += 1
        Explorar(m,i-1,j)
        Explorar(m,i,j+1)
        Explorar(m,i+1,j)
        Explorar(m,i,j-1)

navios = []
contador = 1
for i in range(linha+2):
    for j in range(coluna+2):
        tamanho = 0
        Explorar(m,i,j)
        if tamanho > 0:
            navios.append(tamanho)
            contador += 1

n_tiros = int(input())
for i in range(n_tiros):
    jogada = input().split()
    l = int(jogada[0])
    c = int(jogada[1])
    if type(m[l][c]) is int:
        navios[m[l][c]-1] -= 1
print(navios.count(0))



