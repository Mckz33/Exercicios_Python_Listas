import random

numeros = []

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

for i in range(100):
    dado = random.randrange(1, 7)
    if dado == 1:
        num1 += 1
    elif dado == 2:
        num2 += 1
    elif dado == 3:
        num3 += 1
    elif dado == 4:
        num4 += 1
    elif dado == 5:
        num5 += 1
    elif dado == 6:
        num6 += 1
    numeros.append(dado)

print("Números das 100 rodadas:\n"
      f"Número 1: {num1}\n"
      f"Número 2: {num2}\n"
      f"Número 3: {num3}\n"
      f"Número 4: {num4}\n"
      f"Número 5: {num5}\n"
      f"Número 6: {num6}\n")