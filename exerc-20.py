modelos = []
consumos = []

for i in range(1, 6):
    print(f"Veículo {i}")
    modelos.append(input("Nome: "))
    consumos.append(float(input("Km por litro: ")))

print("Relatório Final")
cont, custo = 0, 0
gasto = 0
menorModelo = ""
menor = 0
for m in modelos:
    custo = 1000 / consumos[cont]
    gasto = custo * 2.25
    print(f"{m} - {consumos[cont]}  - {consumos} litros  - {gasto}")
    if cont == 0:
        menor = custo
        menorModelo = m
    if menor < custo:
        menor = custo
        menorModelo = m
    cont += 1
print(f"O menor consumo é do {menorModelo}.")