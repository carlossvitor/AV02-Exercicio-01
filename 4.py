def regrasSaldo(saldo):
    try:
        saldo = float(saldo)
    except ValueError:
        raise ValueError("Digite apenas números")
    return saldo

def regrasDeposito(valueDeposito):
    try:
        valueDeposito = float(valueDeposito)
    except ValueError:
        raise ValueError("Digite apenas números")
    if valueDeposito <= 0:
        raise TypeError("Só é possível depositar valores maiores do que Zero")

    return (valueDeposito)

def regrasSaque(valueSaque, saldo):
    try:
        valueSaque = float(valueSaque)
    except ValueError:
        raise ValueError("Digite apenas números")
    if valueSaque <= 0:
        raise TypeError("Só é possível sacar valores maiores do que Zero")
    if saldo < valueSaque:
        raise TypeError("Saldo insuficiente para saque")
    return (valueSaque)



while True:
    try:
        saldo = regrasSaldo(input("Digite o valor do seu saldo atual: "))
        break
    except ValueError as e:
        print(f"Erro: {e}")

while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print(f"Seu Saldo é de {saldo}")
    decisao = int(input("Digite a opção desejada: "))

    try:
        if decisao == 1:
            valueDeposito = regrasDeposito(input("Digite o valor que você deseja depositar: "))
            saldo += valueDeposito
            print(f"O seu saldo atual é de {saldo}")
        elif decisao == 2:
            valueSaque = regrasSaque(input("Digite o valor que você deseja sacar: "), saldo)
            saldo -= valueSaque
            print(f"O seu saldo atual é de {saldo}")
        else:
            print("Opção invalida")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(f"{e}")