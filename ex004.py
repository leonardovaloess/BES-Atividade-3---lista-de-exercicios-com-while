n = int(input('informe n: '))
numerosQtd = 0
soma = 0

while numerosQtd < n:
    x = int(input(f"insira o valor de x{numerosQtd}): "))
    if x < 10:
        print("informe novamente")
    else:
        soma += x
        numerosQtd+=1
    
print(f"o somatório para n = {n} fica: {soma}")

