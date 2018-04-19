while True:
    try:
        x = input().split()
        operandos = []
        for i in range(len(x)-1,-1,-1):
            if x[i] == "+":
                a = (operandos.pop(0))
                b = (operandos.pop(0))
                result = (a+b)
                operandos.insert(0,result)
            elif x[i] == "-":
                a = operandos.pop(0)
                b = operandos.pop(0)
                result = (a-b)
                operandos.insert(0,result)
            elif x[i] == "*":
                a = operandos.pop(0)
                b = operandos.pop(0)
                result = (a*b)
                operandos.insert(0,result)
            elif x[i] == "/":
                a = operandos.pop(0)
                b = operandos.pop(0)
                result = int(a//b)
                if result < 0:
                    result += 1
                operandos.insert(0,result)
            else:
                operandos.insert(0,int(x[i]))
        for i in operandos:
            print(i)
    except Exception as err:
        break
