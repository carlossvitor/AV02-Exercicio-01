def notasAprovadas(notas):
    aprovadas = []
    for nota in notas:
        if nota >= 7:
            aprovadas.append(nota)
    return aprovadas

def regraNotas(notas):
    try:
        notas = float(notas)
    except ValueError:
        raise ValueError("Digite apenas números")
    if notas < 0 or notas > 10:
        raise ValueError("Os números precisam estar entre 0 e 10")
    return notas

def regrasNotas(qtdNotas):
    try:
        qtdNotas = int(qtdNotas)
    except ValueError:
        raise ValueError("Digite apenas números")
    if qtdNotas < 1:
        raise ValueError("A quantidade de notas não pode ser negativa ou zero.")
    return qtdNotas

try:
    counter = 1
    notas = []
    qtdNotas = regrasNotas(input("Digite a quantidade de notas: "))
    while counter <= qtdNotas:
        notas.append(regraNotas(input(f"Digite a nota número {counter}: ")))
        counter += 1
    print(notasAprovadas(notas))
except ValueError as e:
    print(e)