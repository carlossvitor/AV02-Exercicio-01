try:
    numero1 = int(input("Digite um numero inteiro: "))
    numero2 = int(input("Digite outro numero inteiro: "))
    print(numero1/numero2)
except ValueError:
    print("Entrada invalida! Digite apenas números.")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")