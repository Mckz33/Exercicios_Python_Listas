vetor = [1, 2, 3, 4, 5]

soma = 0
mult = 0
for i in range(len(vetor)):
    soma += vetor[i]
    mult = vetor[i] * vetor[i]
    print(f"MULTIPLICAÇÃO: {mult}")

print(f"SOMA: {soma}\n"
      f"NÚMEROS: {vetor}")
