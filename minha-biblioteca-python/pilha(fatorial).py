def Fatorial(n):
    pilha = []
    for i in range(1,n+1):
        pilha.insert(0,i) #push
    fatorial = 1
    while pilha != []:
        retirado = pilha.pop(0)
        fatorial *= retirado
    return fatorial
print(Fatorial(5))