class NPC:
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    def info(self):
        print(f"Nome: {self.nome}\nTime: {self.time}\nForca: {self.forca}\nMunição: {self.municao}\nVivo: {'Sim' if self.vivo else 'Não'}\nEnergia: {self.energia}")

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)
class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)
class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 300
        self.municao = 300
        super().__init__(nome, time, self.forca, self.municao)
    def inf(self):
        super().info()
s1=Guarda()