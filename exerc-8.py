class Pessoa:
    def __init__(self, idade=0, altura=0):
        self.idade = idade
        self.altura = altura

    def __repr__(self):
        return f"Idade: {self.idade}\nAltura: {self.altura}"


i = int(input("Quantidade de pessoas: "))
for i in range(i):
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    pessoa = Pessoa(idade, altura)
    print(pessoa)