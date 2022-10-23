vet = [0] * 20
par = [0] * 10
imp = [0] * 10
contPar = 0
contImp = 0
for i in range(0, len(vet)):
    num = int(input("Numero: "))
    vet[i] = num

for i in range(0, len(vet)):
    if vet[i] % 2 == 0:
        par[contPar] = vet[i]
        contPar += 1
    else:
        imp[contImp] = vet[i]
        contImp += 1

print(f"TOTAL: {vet}")
print(f"Pares: {par}")
print(f"Impares: {imp}")