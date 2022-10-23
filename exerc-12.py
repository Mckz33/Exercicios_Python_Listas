class Alunos:
    def __init__(self, idade=0, altura=0):
        self.idade = idade
        self.altura = altura

    def __repr__(self):
        return f"Idade: {self.idade} Altura: {self.altura}"


i = int(input("Quantidade de Alunos: "))
mediaAltura = 0
listaAlunos = []
altura = 0
menorMedia = []
for i in range(i):
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    aluno = Alunos(idade, altura)
    listaAlunos.append(aluno)
    mediaAltura += altura

mediaAltura / len(listaAlunos)
print(mediaAltura)
print(listaAlunos)
'''INCOMPLETO'''