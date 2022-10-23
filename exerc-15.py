vetor = []
acimaMedia = []
abaixoSete = []
cont = 0
contSete = 0
valor = len(vetor)
while True:
    numero = int(input("Notas: "))
    vetor.append(numero)
    if numero < 0:
        break

print(f"Total de Valores: {len(vetor)}")
print(f"Vetor: {vetor}")
media = sum(vetor)
media / len(vetor)
print(f"Media: {media}")

i = 0
while valor:
    if vetor[i] < 7:
        abaixoSete.append(vetor[i])
        contSete += 1
        i += 1
print(f"Valores abaixo de 7: {contSete}")
i = 0
while valor:
    if vetor[i] > media:
        acimaMedia.append(vetor[i])
        cont += 1
        i += 1
print(f"Acima da Media: {cont}")
sum(vetor)
print(f"Soma: {vetor}")
vetor.reverse()
print(f"Reverso: {vetor}")

print("ISSO É TUDO PESSOAL!")