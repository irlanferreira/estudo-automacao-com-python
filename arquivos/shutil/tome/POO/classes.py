class Carro:
    velMax=0
    ligado=False
    cor=""

c1=Carro()

c1.velMax=200

print(f"Velocidade Máxima: {c1.velMax}")
print(f"Ligado?: {'Sim' if c1.ligado else 'Não'}")

#Classe com método Construct (Init)

class Pessoa:
    def __init__(self, n, i, s, c):
        self.nome = n
        self.idade = i
        self.sexo = s
        self.cpf = c
    def mostrardados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nSexo: {self.sexo}\nCPF: {self.cpf}")
p1 = Pessoa("Irlan", 17, "M", 123456789)
p1.mostrardados()