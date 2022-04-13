idd = int(input("Informe a idade do nadador: "))
if idd >= 5 and not idd > 7:
    print("O nadador pertence a categoria 'Infantil A'")
elif idd > 7 and not idd > 10:
    print("O nadador pertence a categoria 'Infantil B'")
elif idd > 10 and not idd > 13:
    print("O nadador pertence a categoria 'Juvenil A'")
elif idd > 13 and not idd > 17:
    print("O nadador pertence a categoria 'Juvenil B'")
elif idd > 17:
    print("O nadador pertence a categoria 'Sênior'")
else:
    print("Não possuimos nadadores com menos de 5 anos")
