class Nodo():
    
    def __init__(self,dado):
        self.__dado = dado
        self.__prox_nodo = None
        
    def get_dado(self):
        return self.__dado
    
    def set_dado(self,novo):
        self.__dado = novo
        
    def get_prox_nodo(self):
        return self.__prox_nodo
    
    def set_prox_nodo(self,novo):
        self.__prox_nodo = novo
        
class Lista():
  
    def __init__(self):
        self.nodo_inicio = None
        self.nodo_fim = None
        self.campo = ""
        
    def vazio(self):
        if self.nodo_inicio == None:
            return True
        else:
            return False
            
    def __iter__(self):
        if self.vazio() == True:
            print("ListaVazia")
        else:
            currentNode = self.nodo_inicio
            while currentNode is not None:
                yield currentNode.get_dado()
                currentNode = currentNode.get_prox_nodo()
                
    def __str__(self):#caso eu precise printar a lista
        if self.vazio() == True:
            return "Tem nada aqui, não!"
        else:
          nodo_atual = self.nodo_inicio
          self.campo = ""
          while nodo_atual is not None:  
              self.campo += str(nodo_atual.get_dado())
              nodo_atual = nodo_atual.get_prox_nodo()
          return self.campo
                    
        
    def add_inicio(self,dado):
        novo_nodo = Nodo(dado)
        if self.vazio() == True:
            self.nodo_inicio = self.nodo_fim = novo_nodo
        else:
            novo_nodo.set_prox_nodo(self.nodo_inicio)
            self.nodo_inicio = novo_nodo
            
    def add_fim(self,dado):
        novo_nodo = Nodo(dado)
        if self.vazio() == True:
            self.nodo_inicio = self.nodo_fim = novo_nodo
        else:
            self.nodo_fim.set_prox_nodo(novo_nodo)
            self.nodo_fim = novo_nodo
            
    def remover_inicio(self):
        if self.vazio() == True:
            print("Não dá pra remover algo que não existe, mizéra")
            return None
        valor = self.nodo_inicio.get_dado()
        if self.nodo_inicio == self.nodo_fim:
            self.nodo_inicio = self.nodo_fim = None
        else:
            self.nodo_inicio = self.nodo_inicio.get_prox_nodo()
        return valor
    
    def remover_fim(self):
        if self.vazio() == True:
            print("Não dá pra remover algo que não existe, mizéra")
            return None
        valor = self.nodo_fim.get_dado()
        if self.nodo_inicio == self.nodo_fim:
            self.nodo_inicio = self.nodo_fim = None
        else:
            nodo_atual = self.nodo_inicio
            while nodo_atual.get_prox_nodo() is not self.nodo_fim:#is not tests object identity, != tests object value
                nodo_atual = nodo_atual.get_prox_nodo()
            nodo_atual.set_prox_nodo(None)
            self.nodo_fim = nodo_atual
        return valor
        
    def tamanho(self):
        if self.vazio() == True:
            return 0
        else:
            cont = 0
            nodo_atual = self.nodo_inicio
            while nodo_atual is not None:
                cont += 1
                nodo_atual = nodo_atual.get_prox_nodo()
            return cont
    def first(self):
      if self.vazio() is not True:
        valor = self.nodo_inicio.get_dado()
        return valor
#pilha = add no inicio, remover do inicio
class Pilha(Lista):
  def push(self,dado):
    self.add_inicio(dado)
  def pop(self):
    return self.remover_inicio()
#lista = add no fim, remover do inicio
class Fila(Lista):
  def remove_comeco(self):
    return self.remover_inicio()
  def add_final(self,dado):
    self.add_fim(dado)


    
a = int(input())
for j in range(a):
    b = int(input())
    normal = Fila()
    pref = Fila()
    casos = ""
    for i in range(b):
        c = input()
        if c != "A" and c != "B" and c != "I":
            d = c.split()
            if d[0] == "f":
                normal.add_final(d[1])
            elif d[0] == "p":
                pref.add_final(d[1])
        else:
            if c == "A" and normal.vazio() is True and pref.vazio() is False:
                pref.remove_comeco()
            elif c == "A" and normal.vazio() is False:
                normal.remove_comeco()
            elif c == "B" and pref.vazio() is True and normal.vazio() is False:
                normal.remove_comeco()
            elif c == "B" and pref.vazio() is False:
                pref.remove_comeco()
            elif c == "I":
                if normal.vazio() is True and pref.vazio() is True:
                    casos += "0 0\n" 
                if normal.vazio() is True and pref.vazio() is False:
                    casos += "{} {}\n".format(0,pref.first())
                if normal.vazio() is False and pref.vazio() is True:
                    casos += "{} {}\n".format(normal.first(),0)
                if normal.vazio() is False and pref.vazio() is False:
                    casos += "{} {}\n".format(normal.first(),pref.first())
    print("Caso {}:\n{}".format(j+1,casos.strip("\n")))






