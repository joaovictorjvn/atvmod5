dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))
if dia < 0 or dia > 31 or mes < 0 or mes > 12 or ano < 0:
    print("Data Inválida")
if mes == 2:
    if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
        if dia <= 29 > 0:
            print("Data Válida.")
        else:
            print("Data Inválida")
    else:
        if dia <= 28 > 0:
            print("Data Válida.")
        else:
            print("Data Inválida")
else:
    print("Data Válida.")
