salarios = [200, 299, 300, 399, 400, 499, 500, 599, 600, 699, 700, 799, 800, 899, 900, 999, 1000]
total = [] * 9

i = 0
for salario in salarios:
    indice = salario // 100 - 2
    maximo = len(total) - 1
    indice = min(indice, maximo)
    total[indice] += 1

print(total)



