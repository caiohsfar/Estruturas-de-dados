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
            print("Lista Vazia")
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
              self.campo += str(nodo_atual.get_dado()) + " "
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
        if self.vazio() is False:
            valor = self.nodo_inicio.get_dado()
            return valor
        else:
            return None
      
    
      
#pilha = add no inicio, remover do inicio
class Pilha(Lista):
  def push(self,dado):
    self.add_inicio(dado)
  def pop(self):
    return self.remover_inicio()


#lista = add no fim, remover do inicio
class Fila(Lista):
  def remover_noinicio(self):
    return self.remover_inicio()
  def add_nofim(self,dado):
    self.add_fim(dado)


festas = int(input())
for i in range(festas):
    k = input().split()
    deck = Fila()
    for i in k:
        deck.add_nofim(i) 
    jogadores = []
    while True:
        a = input()
        if a != "-1":
            a = a.split()
            b = Fila()
            for i in a:
                b.add_nofim(i)     
            jogadores.append(b)
        else:
            break
    i = 0
    ganhou = False
    while i <= 1000:
        for b in (jogadores):
            if b.vazio() == False:
                if deck.first() == b.first():
                    b.remover_noinicio() 
                    i +=1
                else:
                    z = b.remover_noinicio()
                    b.add_nofim(z)   
                    i += 1  
            else:
                print(jogadores.index(b)+1)
                ganhou = True
                break
        if ganhou is True:
            break
        if i == 1000:
            print(0)
            break
        else:
            x = deck.remover_noinicio()
            deck.add_nofim(x)

    
        
        
    
