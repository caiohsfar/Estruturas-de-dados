#Caio Henrique de Souza Farias - UFRPE - 2017.2
def edition(a,b):
    c = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]#Faz a matriz zerada contando com o caso base
    for col in range(len(b)+1):#Preenche as colunas do caso base
        c[0][col] = col
    for lin in range(len(a)+1):#Preenche as linhas do caso base
        c[lin][0] = lin
    for i,x in enumerate(a):#i = indice, x = letra a ser comparada
        for j,y in enumerate(b):
            if x == y:
                c[i+1][j+1] = c[i][j]#É i+1 e j+1 pois temos que partir depois do caso base que é i,j = 0,0
            else:
                c[i+1][j+1] = min(c[i][j+1],c[i][j],c[i+1][j]) + 1
    return c[-1][-1]

entr = input().split()
x = int(entr[0])
y = int(entr[1])
dic = []
err = []
for i in range(x):
    dic.append(input())
for i in range(y):
    err.append(input())
for j in (err):
    temp = []
    for i in (dic):
        if len(i) - len(j) <= 2 and len(j) - len(i) <= 2:
            min_edit = edition(i,j)
            if min_edit < 3:
                temp.append(i)
    campo = " "
    print(campo.join(temp))    


        

            
    





















                
            
    
            
    
