vetor = [0] * 10

for i in range(0, len(vetor), 1):
    vetor[i] = i
    print(vetor[i], end=" ")

vetor.reverse()
print()

for i in range(0, len(vetor)):
    print(vetor[i], end=" ")
