class Nodo():
    
    def __init__(self,dado):
        self.__dado = dado
        self.__prox_nodo = None
        
    def __iter__(self):
        return self.get_dado.itervalues()
    def __str__(self):
        return (str(self.get_dado()))
    
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

    def __str__(self):
        if self.vazio() == True:
            return "Tem nada aqui, não!"
        nodo_atual = self.nodo_inicio
        campo = ""
        while nodo_atual is not None:  
            campo += str(nodo_atual.get_dado()) + " "
            nodo_atual = nodo_atual.get_prox_nodo()
        return campo
                    
    def vazio(self):
        if self.nodo_inicio == None:
            return True
        
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
            print("Não dá pra remover algo que não existe")
        valor = self.nodo_inicio.get_dado()
        if self.nodo_inicio == self.nodo_fim:
            self.nodo_inicio = self.nodo_fim = None
        else:
            self.nodo_inicio = self.nodo_inicio.get_prox_nodo()
        return valor
    
    def remover_fim(self):
        if self.vazio() == True:
            print("Não dá pra remover algo que não existe")
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
    def __iter__(self):
        if self.vazio() == True:
            print("Lista vazia!")
        else:
            correntNode = self.nodo_inicio
            while correntNode is not None:
                yield correntNode.get_dado()
                correntNode = correntNode.get_prox_nodo()

def Interseção(l1,l2):
    lista = Lista()
    aux1 = l1.nodo_inicio
    aux2 = l2.nodo_inicio
    while aux1 != None:
        while aux2 != None:
            if aux1.get_dado() == aux2.get_dado():
                lista.add_fim(aux1)
                aux2 = aux2.get_prox_nodo()
            else:
                aux2 = aux2.get_prox_nodo()
        aux1 = aux1.get_prox_nodo()
        aux2 = l2.nodo_inicio
    return lista

    
l1 = Lista()
l2 = Lista()


l1.add_fim(20)
l1.add_fim(30)
l1.add_fim(35)

l2.add_fim(10)
l2.add_fim(20)
l2.add_fim(40)
l2.add_fim(50)

lista = Interseção(l1,l2)
print(lista)



 



       
        
        
            
        
            
        
    
