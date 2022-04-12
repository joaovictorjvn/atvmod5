prov1 = float(input("Informe a primeira nota: "))
prov2 = float(input("Informe a segunda nota: "))
prov3 = float(input("Informe a terceira nota: "))
if (prov1 * 1 + prov2 * 1 + prov3 * 2) / (1 + 1 + 2) > 100 or (prov1 * 1 + prov2 * 1 + prov3 * 2) / (1 + 1 + 2) < 0:
    print("Informações inválidas foram inseridas, as notas não podem ser maiores que 100 ou menores do que 0.")
elif (prov1 * 1 + prov2 * 1 + prov3 * 2) / (1 + 1 + 2) >= 60:
    print(f'A média do aluno foi {(prov1 * 1 + prov2 * 1 + prov3 * 2) / (1 + 1 + 2)}, ele está aprovado.')
else:
    print(f'A média do aluno foi {(prov1 * 1 + prov2 * 1 + prov3 * 2) / (1 + 1 + 2) }, ele está reprovado.')
