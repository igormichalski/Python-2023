tamanho = 4
aux = 0
vetor = []
x = int(input("Digite um valor: "))

#RECEBENDO VETOR
for i in range(tamanho):
    valor = int(input(f"Digite o valor da posição {i}: "))
    vetor.append(valor) #JOGA O VALOR DENTRO DO VETOR

##VALIDANDO SE A SOMA DE 4 PEDAÇOS DO VETOR É IGUAL A X
for i in range(tamanho):
    aux = aux + vetor[i]

if aux==x:
    print("SIM")

#VALIDANDO SE A SOMA DE 3 PEDAÇOS DO VETOR É IGUAL A X

if vetor[0]+vetor[1]+vetor[2]==x:
    print("SIM")

if vetor[1]+vetor[2]+vetor[3]==x:
    print("SIM")

if vetor[2]+vetor[3]+vetor[0]==x:
    print("SIM")

if vetor[3]+vetor[0]+vetor[1]==x:
    print("SIM")

#VALIDANDO SE A SOMA DE DOIS PEDAÇOS DO VETOR É IGUAL A X
encontrado = False
for i in range(tamanho):
    for j in range(i+1, tamanho):
        if vetor[j]+vetor[i]==x:
            encontrado = True

if encontrado:
    print("SIM")

