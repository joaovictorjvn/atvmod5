not1 = float(input("Informe a nota referente ao trablho de laboratório: "))
not2 = float(input("Informe a nota referente a avaliação semestral: "))
not3 = float(input("Informe a nota referente ao teste final: "))
if (not1 * 2 + not2 * 3 + not3 * 5) / (2 + 3 + 5) > 10 or (not1 * 2 + not2 * 3 + not3 * 5) / (2 + 3 + 5) < 0:
    print("Informações inválidas foram inseridas, as notas não podem ser maiores que 10 ou menores do que 0.")
elif (not1 * 2 + not2 * 3 + not3 * 5) / (2 + 3 + 5) > 4.9:
    print(f'A média do aluno foi {(not1 * 2 + not2 * 3 + not3 * 5) / (2 + 3 + 5)}, ele está aprovado.')
elif (not1 * 2 + not2 * 3 + not3 * 5) / (2 + 3 + 5) >= 3 <= 4.9:
    print(f'A média do aluno foi {(not1 * 2 + not2 * 3 + not3 * 5) / (2 + 3 + 5)}, ele está em recuperação.')
else:
    print(f'A média do aluno foi {(not1 * 2 + not2 * 3 + not3 * 5) / (2 + 3 + 5)}, ele está reprovado.')
