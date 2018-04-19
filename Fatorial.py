#-*- coding: utf-8 -*-
#Aluno: Caio Henrique de Souza Farias - BSI - UFRPE - Laboratório de Programação
def fat(n):
    if n == 1:
        return 1
    else:
        return n*fat(n-1)
lista = []
x = int(input())
cont = 0
i = 1
while cont < x:
    fator = fat(i)
    if fator + cont < x:
        i += 1
    if fator + cont > x:
        i -= 1
        fator = fat(i)
        if fator + cont <= x:
            cont += fator
            lista.append(i)
    if fator + cont == x:
        cont += fator
        lista.append(i)
        

print(len(lista))       




    
        
    
