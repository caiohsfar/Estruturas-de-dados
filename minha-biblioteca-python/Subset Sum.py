def LCS(X,Y):
    n = len(X)
    m = len(Y)
    c = [[0 for j in range(m+1)] for i in range(n+1)]
    for i,x in enumerate(X):
      for j,y in enumerate(Y):
            if x == y:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i+1][j+1] = max(c[i+1][j],c[i][j+1])
    return (c[-1][-1])

