sim = []
nao = []

a = str(input("Telefonou para a vítima? sim/nao "))
if a == sim:
    sim.append(sim)
else:
    nao.append(nao)
b = str(input("Esteve no local do crime? sim/nao "))
if a == sim:
    sim.append(sim)
else:
    nao.append(nao)

c = str(input("Mora perto da vítima? sim/nao "))
if a == sim:
    sim.append(sim)
else:
    nao.append(nao)

d = str(input("Devia para a vítima? sim/nao "))
if a == sim:
    sim.append(sim)
else:
    nao.append(nao)

e = str(input("Já trabalhou com a vítima? sim/nao "))
if a == sim:
    sim.append(sim)
else:
    nao.append(nao)


if len(sim) == 2:
    print("Suspeito")
elif len(sim) == 3 or 4:
    print("Cúmplice")
elif len(sim) == 5:
    print("Assassino")
else:
    print("Inocente")