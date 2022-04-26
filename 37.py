import sys
horc = int(input("Informe a hora do horário de chegada: "))
minuc = int(input("Informe os minutos do horário de chegada:  "))
print(f'Horário de chegada definido para: {horc}:{minuc}.')
horf = int(input("Informe a hora do horário de partida: "))
minuf = int(input("Informe os minutos do horário de partida:  "))
print(f'Horário de partida definido para: {horf}:{minuf} na data.')
if horc > 23 or horf > 23 or minuc > 60 or minuf > 60:
    sys.exit("Dados Inválidos.")
elif horf > horc and minuf == 0 and minuc == 0:
    auxh = horf - horc
    auxm = 0
    print(f'Duração da estadia: {auxh} horas e {auxm} minutos.')
    if auxh >= 5:
        cust = 2.00 + 2.80 + (auxh - 4) * 2.00
    elif auxh < 5 >= 3:
        cust = 2.00 + (1.40 * (auxh - 2))
    else:
        cust = 1.00 * auxh
    print(f'O custo da estadia foi de: R$ {cust}')
elif horf == horc and minuf != 0:
    auxh = 0
    auxm = minuf - minuc
    print(f'Duração da estadia: {auxh} horas e {auxm} minutos.')
    cust = 1.00
    print(f'O custo da estadia foi de: R$ {cust}')
elif horc > horf and minuf != 0:
    auxh = horf - horc + 24
    auxm = (minuf - minuc)
    print(f'Duração da estadia: {auxh} horas e {auxm} minutos.')
    cust = 2.00 + 2.80 + (auxh - 3) * 2
    print(f'O custo da estadia foi de: R$ {cust}')
elif horc <= horf and minuc > minuf:
    auxh = horf - horc - 1
    auxm = (minuf - minuc) * -1
    print(f'Duração da estadia: {auxh} horas e {auxm} minutos.')
    if auxh >= 4:
        cust = 2.00 + 2.80 + (auxh - 3) * 2.00
    elif auxh < 3 >= 2:
        cust = 2.00 + (1.40 * (auxh - 1))
    else:
        cust = 1.00 + 1.00 * auxh
    print(f'O custo da estadia foi de: R$ {cust}')
elif horc > horf and minuc >= minuf:
    auxh = horf - horc + 24
    auxm = (minuf - minuc) * -1
    print(f'Duração da estadia: {auxh} horas e {auxm} minutos.')
    cust = 2.00 + 2.80 + (auxh - 4) * 2.00
    print(f'O custo da estadia foi de: R$ {cust}')
