class Node():
  def __init__(self,key):
    self._p = None
    self._right = None
    self._key = key
    self._left = None
    
  def get_key(self):
    return self._key
    
  def set_key(self,value):
    self._key = value
    
  def get_right(self):
    return self._right
    
  def set_right(self,value):
    self._right = value
    
  def get_left(self):
    return self._left
    
  def set_left(self,value):
    self._left = value
    
  def get_p(self):
    return self._p
    
  def set_p(self,value):
    self._p = value
 
class BST():
  def __init__(self):
    self.__root = None
    
  def get_root(self):
    return self.__root
    
  def set_root(self,valor):
    self.__root = valor
    
  def Inorder(self,x,lista):##################
    if x != None:
      self.Inorder(x.get_left(),lista)
      lista.append(str(x.get_key()))
      self.Inorder(x.get_right(),lista)
      
  def Preorder(self,x,lista):##################
    if x != None:
      lista.append(str(x.get_key()))
      self.Preorder(x.get_left(),lista)
      self.Preorder(x.get_right(),lista)
      
  def Postorder(self,x,lista):##################
    if x != None:
      self.Postorder(x.get_left(),lista)
      self.Postorder(x.get_right(),lista)
      lista.append(str(x.get_key()))
      
  def Search(self,k):
    j = self.get_root()
    while j != None and k != j.get_key():
      if k < j.get_key():
        j = j.get_left()
      else:
        j = j.get_right()
    return j
    
  def Minimo(self,x):
    while x.get_left() != None:
      x = x.get_left()
    return x

  def Print_Min(self,x):
    return print(self.Minimo(x).get_key())
    
  
  def Maximo(self,x):
    while x.get_right() != None:
      x = x.get_right()
    return x

  def Print_Max(self,x):
      return print(self.Maximo(x).get_key())
    
  def Sucessor(self,data):
    x = self.Search(data)
    if x.get_right() != None:
      return self.Minimo(x.get_right())
    else:
      y = x.get_p()
      while y != None and x == y.get_right():
        x = y
        y = y.get_p()
      return y
    
  def Print_Sucessor(self,x):
      return print(self.Sucessor(x).get_key())
      
  def Predecessor(self,x):
    x = self.Search(x)
    if x.get_left() != None:
      return self.Maximo(x.get_left())
    else:
      y = x.get_p()
      while y != None and x == y.get_left():
        x = y
        y = y.get_p()
      return y
    
  def Print_Predecessor(self,x):
      return print(self.Predecessor(x).get_key())
      
  def Insert(self,dado):
    novo = Node(dado)
    y = None
    x = self.get_root()
    while x != None:
      y = x
      if novo.get_key() < x.get_key():
        x = x.get_left()
      else:
        x = x.get_right()
    novo.set_p(y)
    if y == None:
      self.set_root(novo)
    elif novo.get_key() < y.get_key():
      y.set_left(novo)
    else:
      y.set_right(novo)
      

  def Delete(self,data):
    z = self.Search(data)
    if z is None:
      return False
    if self.get_root() == None:
      return False
    else:
      if z.get_left() == None or z.get_right() == None:
        y = z
      else:
        y = self.Sucessor(z.get_key())
      if y.get_left() != None:
        x = y.get_left()
      else:
        x = y.get_right()
      if x != None:
        z.set_p(y.get_p())
      if y.get_p() == None:
        self.set_root(x)
      else:
        if y == y.get_p().get_left():
          y.get_p().set_left(x)
        else:
          y.get_p().set_right(x)
      if y != z:
        z.set_key(y.get_key())
    return y
  
j = 1
while True:
    try:
        qnt_entr = int(input())
        arvore = BST()
        print("Caso {}:".format(j))
        j += 1
        for i in range(qnt_entr):
            caso = input().split()
            op = caso[0]
            if op == "A" or op == "B" or op == "C": 
                num = int(caso[1])
                if op == "A":
                    arvore.Insert(num)
                if op == "B":
                    arvore.Delete(num)
                if op == "C":
                    if arvore.Search(num) is not None:
                        if arvore.Predecessor(num) is None:
                            print(0)
                        else:
                            arvore.Print_Predecessor(num)
                    else:
                        print(0)
            else:
                if op == "PRE":
                    campo = " "
                    lista = []                    
                    arvore.Preorder(arvore.get_root(),lista)
                    if lista == []:
                        print(0)
                    else:
                        print(campo.join(lista))
                if op == "IN":
                    campo = " "
                    lista = []
                    arvore.Inorder(arvore.get_root(),lista)
                    if lista == []:
                        print(0)
                    else:
                        print(campo.join(lista))
                if op == "POST":
                    campo = " "
                    lista = []      
                    arvore.Postorder(arvore.get_root(),lista)
                    if lista == []:
                        print(0)
                    else:
                        print(campo.join(lista))
    except EOFError:
      break
