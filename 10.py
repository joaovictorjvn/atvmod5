alt = float(input("Informe a sua altura:"))
sex = str(input("Informe o seu sexo (M/F): "))
if sex.lower() == "m":
    print(f'O seu peso ideal é {(72.7 * alt) - 58} Kg')
elif sex.lower() == "f":
    print(f'O seu peso ideal é {(62.1 * alt) - 44.7} Kg')
else:
    print("Sexo inválido, reinicie o programa e use apenas 'M/m' ou 'F/f'")
