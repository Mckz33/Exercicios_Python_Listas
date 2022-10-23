jogadores = []
votos = []
i = 0
while i < 23:
    jogadores.append(i+1)
    i += 1

print(f"Total de jogadores: {jogadores}")

while True:
    num = int(input("Número do jogador (0=fim): "))
    if num <= 0:
        break
    else:
        votos.append(num)
    votos.sort()

rep = 0
for i in range(0, len(votos)-1):
    if votos[i] == votos[i+1]:
        rep += 1
        if i == len(votos)-2:
            print(f"Jogador {votos[i]},Votos: {rep + 1}")
    else:
        print(f"Jogador {votos[i]},Votos: {rep + 1}")
        rep = 0

print(votos)
print(rep)


