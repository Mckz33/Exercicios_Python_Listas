class Atleta:
    def __init__(self, nome, salto1, salto2, salto3, salto4, salto5):
        self.nome = nome
        self.salto1 = salto1
        self.salto2 = salto2
        self.salto3 = salto3
        self.salto4 = salto4
        self.salto5 = salto5

    def mediaSalto(self):
        return (self.salto1 + self.salto2 + self.salto3 + self.salto4 + self.salto5) / 5

    def __repr__(self):
        return f"Nome: {self.nome}\nPrimeiro Salto: {self.salto1} m\nSegundo Salto: {self.salto2} m\nTerceiro Salto: {self.salto3} m\nQuarto Salto: {self.salto4} m\nQuinto Salto: {self.salto5} m"


atleta = []
while True:
    nome = str(input("Atleta: "))
    if len(nome) == 0:
        break
    primeiroSalto = float(input("Primeiro Salto: "))
    segundoSalto = float(input("Segundo Salto: "))
    terceiroSalto = float(input("Terceiro Salto: "))
    quartoSalto = float(input("Quarto Salto: "))
    quintoSalto = float(input("Quinto Salto: "))
    atleta.append({"Nome": nome, "Segundo Salto": segundoSalto, "Terceiro Salto": terceiroSalto, "Quarto Salto": quartoSalto, "Quinto Salto": quintoSalto})
    atle = Atleta(nome, primeiroSalto, segundoSalto, terceiroSalto, quartoSalto, quintoSalto)
    media = atle.mediaSalto()
    print(atle)
    print(f"Média dos saltos: {media}")

print("Programa finalizado")