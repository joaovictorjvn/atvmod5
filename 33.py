preca = float(input("Informe o preço atual do produto: R$ "))
precn = 0
if preca <= 50:
    precn = preca + (preca * 0.05)
elif preca <= 100 > 50:
    precn = preca + (preca * 0.1)
elif preca > 100:
    precn = preca + (preca * 0.15)
else:
    print("Preço inválido.")
if precn <= 80:
    print(f'O novo preço do produto é R$ {precn} e ele pertence a categoria "Barato"')
elif precn <= 120 > 80:
    print(f'O novo preço do produto é R$ {precn} e ele pertence a categoria "Normal"')
elif precn <= 200 > 120:
    print(f'O novo preço do produto é R$ {precn} e ele pertence a categoria "Caro"')
elif precn > 200:
    print(f'O novo preço do produto é R$ {precn} e ele pertence a categoria "Muito Caro"')
