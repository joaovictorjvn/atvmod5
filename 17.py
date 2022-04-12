bsmai = float(input("Informe o valor da base maior do trapézio em metros: "))
bsmen = float(input("Informe o valor da base menor do trapézio em metros: "))
alt = float(input("Informe o valor da altura do trapézio em metros: "))
if bsmai <= 0 or bsmen <= 0:
    print("Informações inválidas foram inseridas, ambas as bases do trapézio devem ser maiores que 0.")
else:
    print(f'A área do trapézio é de {((bsmai + bsmen) * alt) / 2} metros.')
