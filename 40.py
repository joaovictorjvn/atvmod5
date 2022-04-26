pref = float(input("Informe o preço de fábrica do automóvel: R$ "))
if pref <= 0:
    print("Dados Inválidos.")
elif pref <= 12000 > 0:
    print(f'O automóvel custará R$ {pref + (pref * 0.05)}, sendo R$ {pref * 0.05} a comissão do distribuidor\n, '
          f'equivalente a 5% do preço de fábrica, estando também isento de impostos.')
elif pref <= 25000 > 12000:
    print(f'O automóvel custará R$ {pref + (pref * 0.10) + (pref * 0.15)}, sendo R$ {pref * 0.10} a comissão'
          f' do distribuidor, equivalente a 10% do preço de fábrica e também R$ {pref * 0.15} de impostos,\n'
          f'equivalente a 15% do preço de fábrica.')
elif pref > 25000:
    print(f'O automóvel custará R$ {pref + (pref * 0.20) + (pref * 0.15)}, sendo R$ {pref * 0.15} a comissão'
          f' do distribuidor, equivalente a 15% do preço de fábrica e também R$ {pref * 0.20} de impostos,\n'
          f'equivalente a 20% do preço de fábrica.')
