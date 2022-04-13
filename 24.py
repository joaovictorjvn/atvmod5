prec = float(input("Informe o preço original do produto: R$ "))
est = str(input("Informe o estado no qual o produto será vendido(MG/SP/RJ/MS):"))
if est.lower() == "mg":
    print(f'O preço final do produto em MG é R$ {prec + (prec * 0.07)}')
elif est.lower() == "sp":
    print(f'O preço final do produto em SP é R$ {prec + (prec * 0.12)}')
elif est.lower() == "rj":
    print(f'O preço final do produto em RJ é R$ {prec + (prec * 0.15)}')
elif est.lower() == "ms":
    print(f'O preço final do produto em MS é R$ {prec + (prec * 0.08)}')
else:
    print("Estado Inválido.")
