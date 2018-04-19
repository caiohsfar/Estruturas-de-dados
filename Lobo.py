o = (input()).split()
a = int(o[0])
b = int(o[1])
base1 =[]
for i in range(b+2):
    base1.append("X")
m = [base1]
for i in range(a):
    p = (" ".join(input()).split())
    p.append("X")
    p.insert(0,"X")
    m.append(p)
base2 = []
for i in range(b+2):
    base2.append("X")
m.append(base2)

def Pasto(i,j,m):
    if m[i][j] is "X":
        return
    if m[i][j] is "#":
        return
    if m[i][j] is "k":
        global ovelha_pasto
        ovelha_pasto += 1
    if m[i][j] is "v":
        global lobo_pasto
        lobo_pasto += 1
    m[i][j] = "X"
    Pasto(i-1,j,m)
    Pasto(i+1,j,m)
    Pasto(i,j-1,m) 
    Pasto(i,j+1,m)
    
lobo_total= 0
ovelha_total = 0
for i in range(1,a+1):
    for j in range(1,b+1):
        if m[i][j] is not "#" and m[i][j] is not "X":
            ovelha_pasto = 0
            lobo_pasto = 0
            Pasto(i,j,m)
            if ovelha_pasto > lobo_pasto:
                ovelha_total += ovelha_pasto
                lobo_pasto = 0
            elif ovelha_pasto <= lobo_pasto:
                lobo_total += lobo_pasto
                ovelha_pasto = 0
print(ovelha_total,lobo_total)
        

            

    
