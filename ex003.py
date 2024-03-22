contPar = 0
contImpar = 0
somaImpar = 0
while contPar < 5 and somaImpar <= 30:
    numero = int(input('informe um numero inteiro qualquer: '))
    
    if numero < 0:
        print("o numero tem que ser maior que 0 (não pode ser negativo)")
    else:
        if numero % 2 == 0:
            contPar += 1
        else:
            somaImpar += numero
            contImpar += 1
        
if contPar == 5:
    print("5 numeros pares")
    print(f"a quantidade de numeros ímpares foi de: {contImpar}")
elif somaImpar >= 30:
    print(f"a quantidade de numeros pares foi de: {contPar}")
    print(f"a quantidade de numeros ímpares foi de: {contImpar}")
    print(f"a soma dos impares passou de 30 ({somaImpar})")
    