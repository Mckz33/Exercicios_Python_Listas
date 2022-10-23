acimaTemp = []
media = []
um = float(input("Temperatura: "))
media.append(um)
dois = float(input("Temperatura: "))
media.append(dois)
tres = float(input("Temperatura: "))
media.append(tres)
quatro = float(input("Temperatura: "))
media.append(quatro)
cinco = float(input("Temperatura: "))
media.append(cinco)
seis = float(input("Temperatura: "))
media.append(seis)
sete = float(input("Temperatura: "))
media.append(sete)
oito = float(input("Temperatura: "))
media.append(oito)
nove = float(input("Temperatura: "))
media.append(nove)
dez = float(input("Temperatura: "))
media.append(dez)
onze = float(input("Temperatura: "))
media.append(onze)
doze = float(input("Temperatura: "))
media = um + dois + tres + quatro + cinco + seis + sete + oito + nove + dez + onze + doze / 12
if um > media:
    acimaTemp.append(um)
if dois > media:
    acimaTemp.append(um)
if tres > media:
    acimaTemp.append(um)
if quatro > media:
    acimaTemp.append(um)
if cinco > media:
    acimaTemp.append(um)
if seis > media:
    acimaTemp.append(um)
if sete > media:
    acimaTemp.append(um)
if oito > media:
    acimaTemp.append(um)
if nove > media:
    acimaTemp.append(um)
if dez > media:
    acimaTemp.append(um)
if onze > media:
    acimaTemp.append(um)
if doze > media:
    acimaTemp.append(um)

print(acimaTemp)
print(f"Janeiro: {um}, Fevereiro: {dois}, Março: {tres}, Abril: {quatro}, Maio: {cinco}, Junho: {seis}, Julho: {sete}, Agosto: {oito}, Setembro: {nove}, Outubro: {dez}, Novembro: {onze}, Dezembro: {doze}.")