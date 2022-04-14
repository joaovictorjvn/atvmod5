print("Iniciando o cálculo do valor do pedido... ")
ped = 0
nvi = int(input("Pressione 1 para continuar ou 0 para encerrar: "))
while nvi == 1:
    cod = int(input("Informe o código do produto: "))
    quant = int(input("Informe a quantidade adquirida do produto: "))
    if cod == 100:
        ped = ped + 1.20 * quant
    elif cod == 101:
        ped = ped + 1.30 * quant
    elif cod == 102:
        ped = ped + 1.50 * quant
    elif cod == 103:
        ped = ped + 1.20 * quant
    elif cod == 104:
        ped = ped + 1.70 * quant
    elif cod == 105:
        ped = ped + 2.20 * quant
    elif cod == 106:
        ped = ped + 1.00 * quant
    else:
        print("Código de produto inválido.")
    nvi = int(input("Deseja continuar?\n"
                    "Pressione 1 para continuar ou 0 para finalizar: "))
if ped == 0:
    print("Pedido Cancelado.")
else:
    print(f'O valor do pedido é R$ {ped}')
