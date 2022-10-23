vetor = [0] * 4

for i in range(0, len(vetor)):
    num = int(input(f"Nota {i}: "))
    vetor[i] = num

media = 0
for i in range(0, len(vetor)):
    media += vetor[i]

total = media / len(vetor)

print(total)