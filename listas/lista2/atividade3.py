print("Operação - Adição!")

while True:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    soma = num1 + num2
    print(f"{num1} + {num2} = {soma}")
    resposta = str(input("Deseja realizar outra soma?(S para sim e N para não): ")).upper()
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
    else:
        print("Resposta Inválida. Encerrando...")
        break