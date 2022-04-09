not1 = float(input("Informe a primeira nota: "))
not2 = float(input("Informe a segunda nota: "))
if not1 < 0 or not1 > 10:
    print("Nota 1 Inválida.")
elif not2 < 0 or not2 > 10:
    print("Nota 2 Inválida.")
else:
    print(f'A média do aluno é {(not1 + not2) / 2}')
