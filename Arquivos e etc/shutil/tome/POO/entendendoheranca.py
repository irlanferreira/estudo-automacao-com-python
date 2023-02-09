class Ativo:
    def __init__(self, nome, juros):
        self.nome = nome
        self.juros = juros
    def info(self):
        print(f"Nome do ativo: {self.nome}\nJuros anuais do ativo: {format(self.juros, '.2f')}%")
class Acao(Ativo):
    def __init__(self, nome, juros):
        super().__init__(nome, juros)
a1 = Acao("PETR3", 7)
print(a1.juros)