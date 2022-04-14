import random

print("Iniciando teste.\nBoa sorte.")
i = 1
acer = 0
while i <= 5:
    val1 = random.randint(0, 100)
    val2 = random.randint(0, 100)
    while val1 + val2 > 100:
        val1 = random.randint(0, 100)
        val2 = random.randint(0, 100)
    print(f'Qual é a soma de {val1} + {val2}?')
    res = int(input())
    if res == val1 + val2:
        acer = acer + 1
        print(f'Resposta Correta.\n'
              f'{val1} + {val2} = {val1 + val2}')
    else:
        print(f'Resposta Incorreta.\n'
              f'{val1} + {val2} = {val1 + val2}')
    i = i + 1
print(f'Teste finalizado.\n'
      f'Quantidade de acertos {acer}')
