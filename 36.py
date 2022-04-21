vendm = float(input("Informe o valor da venda mensal do vendedor: R$ "))
if vendm >= 100_000:
    print(f'O valor da comissão do vendedor é R$ {700 + (vendm * 0.16)}')
elif vendm < 100_000 >= 80_000:
    print(f'O valor da comissão do vendedor é R$ {650 + (vendm * 0.14)}')
elif vendm < 80_000 >= 60_000:
    print(f'O valor da comissão do vendedor é R$ {600 + (vendm * 0.14)}')
elif vendm < 60_000 >= 40_000:
    print(f'O valor da comissão do vendedor é R$ {550 + (vendm * 0.14)}')
elif vendm < 40_000 >= 20_000:
    print(f'O valor da comissão do vendedor é R$ {500 + (vendm * 0.14)}')
elif vendm < 20_000:
    print(f'O valor da comissão do vendedor é R$ {400 + (vendm * 0.14)}')
else:
    print("Informação inválida.")
