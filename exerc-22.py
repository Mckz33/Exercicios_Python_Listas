esfera = []
limpeza = []
caboConector = []
condenado = []
cont = 0

media1 = 0
media2 = 0
media3 = 0
media4 = 0

while True:
    num = int(input("1- necessita da esfera\n"
                    "2- necessita de limpeza\n"
                    "3- necessita troca do cabo ou conector\n"
                    "4- quebrado ou inutilizado\n"
                    "0- Sair\n"
                    "Digite um número: "))

    if num == 1:
        esfera.append(num)
        cont += 1
    elif num == 2:
        limpeza.append(num)
        cont += 1
    elif num == 3:
        caboConector.append(num)
        cont += 1
    elif num == 4:
        condenado.append(num)
        cont += 1
    elif num == 0:
        media1 = len(esfera) + len(esfera) * cont / cont
        media2 = len(limpeza) + len(limpeza) * cont / cont
        media3 = len(caboConector) + len(caboConector) * cont / cont
        media4 = len(condenado) + len(condenado) * cont / cont
        break
    else:
        print("Número invalido!")
        continue

print(f"Situação                        Quantidade              Percentual\n"
        f"1- necessita da esfera                  {len(esfera)}                     {media1}%\n"
        f"2- necessita de limpeza                 {len(limpeza)}                     {media2}%\n"
        f"3- necessita troca do cabo ou conector  {len(caboConector)}                     {media3}%\n"
        f"4- quebrado ou inutilizado              {len(condenado)}                     {media4}%\n")