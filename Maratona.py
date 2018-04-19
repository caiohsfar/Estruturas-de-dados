# -*- coding: utf-8 -*-
#UFRPE - Laboratório de Programação - 2017.2
#Aluno: Caio Henrique de Souza Farias
linha1 = input().split()
linha2 = input().split()
entrada1 = []
entrada2 = []

for i in linha1:
    i = int(i)
    entrada1.append(i)
for j in linha2:
    j = int(j)
    entrada2.append(j)
    
i = entrada1[0] -1
while i >= 0:
    if entrada2[i] - entrada2[i-1] <= entrada1[1]:
        i -= 1
    if entrada2[i] - entrada2[i-1] > entrada1[1]:
        print("N")
        break
    if i == 0:
        print("S")
        
    
    
    

  
