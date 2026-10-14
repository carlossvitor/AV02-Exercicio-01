def minHoras(horas):
    try:
        horas = float(horas)
    except ValueError:
        raise ValueError("Digite apenas números.")
    if horas < 0:
        raise ValueError("as horas não podem ser negativas")
    if horas >= 40:
        return "Carga completa"
    return "Carga incompleta"

try:
    resultado = minHoras(input("Digite a quantidade de horas: "))
    print(resultado)
except ValueError as e:
    print(f"Erro: {e}")