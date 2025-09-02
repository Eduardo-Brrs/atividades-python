contador = 0
pergunta1 = str(input("Telefonou para a vítima?(Responda S para sim e N para não): ")).upper()
if pergunta1 == 'S':
    contador += 1
pergunta2 = str(input("Esteve no local do crime?(Responda S para sim e N para não): ")).upper()
if pergunta2 == 'S':
    contador += 1
pergunta3 = str(input("Mora perto da vítima?(Responda S para sim e N para não): ")).upper()
if pergunta3 == 'S':
    contador += 1
pergunta4 = str(input("Devia para a vítima?(Responda S para sim e N para não): ")).upper()
if pergunta4 == 'S':
    contador += 1
pergunta5 = str(input("Já trabalhou com a vítima?(Responda S para sim e N para não): ")).upper()
if pergunta5 == 'S':
    contador += 1

if contador == 2:
    print("Suspeita")
elif contador == 3 or contador == 4:
    print("Cúmplice")
elif contador == 5:
    print("Assassino")
else:
    print("Inocente")