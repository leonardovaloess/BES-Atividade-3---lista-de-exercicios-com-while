soma= 0
contador = 0

while contador < 10:
    contador += 1
    nota = float(input(f"insira a nota {contador}): "))
    soma += nota

media = soma/contador

print(f"A media final foi de: {media:.2f}")


