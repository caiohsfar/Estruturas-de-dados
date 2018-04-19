from Lista import Lista
class Pilha (Lista):
    def push(self,dado):
        return self.add_inicio(dado)

    def pop(self):
        return self.remover_fim()
