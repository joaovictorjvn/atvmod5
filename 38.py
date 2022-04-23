dia = int(input("Informe o dia do nascimento do usuário: "))
mes = int(input("Informe o mês do nascimento do usuário: "))
ano = int(input("Informe o ano do nascimento do usuário: "))
if dia < 0 or dia > 31 or mes < 0 or mes > 12 or ano < 0 or ano > 2022:
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
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30 > 0:
        print("Data Válida.")
    else:
        print("Data Inválida")
else:
    print("Data Válida.")
