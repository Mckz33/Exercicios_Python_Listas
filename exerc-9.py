vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0
for i in range(len(vetor)):
    soma = vetor[i] ** vetor[i]
    print(f"N{i+1}: {soma}")