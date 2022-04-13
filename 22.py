idd = int(input("Informe a idade do trabalhador: "))
ant = int(input("Informe a quantidade de anos trabalhados: "))
if idd >= 65 or ant >= 30 or idd >= 60 and ant >= 25:
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador não pode se aposentar ainda.")
