x = 0
soma = 0
expoente = 0

numero = int(input("Digite um valor: "))
numero_aux = numero

#DESCOBRINDO EXPORENTE
while numero_aux > 0:
    soma += numero_aux % 10
    numero_aux = int(numero_aux / 10)
    expoente += 1

numero_aux = numero

#REALIZANDO OS NUMEROS ELEVADO
while numero_aux > 0:
    x += (numero_aux % 10) ** expoente
    numero_aux = int(numero_aux / 10)

if x == numero:
    print("É um numero de Armstrong")
else:
    print("Não é um numero de Armstrong")