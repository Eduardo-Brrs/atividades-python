turno = str(input("Informe em qual turno você estuda (M - matutino; V - vespertino; N - noturno.): ")).upper()

match turno:
    case 'M':
        print("Bom dia!")
    case 'V':
        print("Boa tarde!")
    case 'N':
        print("Boa noite!")
    case _:
        print("Valor inválido")