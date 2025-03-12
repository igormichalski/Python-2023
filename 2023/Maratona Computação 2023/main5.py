
def maior():
    tamanho = 4
    vetor = []
    vetoraux = [0, 0, 0, 0]

    # RECEBENDO VETOR
    for i in range(tamanho):
        valor = int(input(f"Digite o valor da posição {i}: "))
        vetor.append(valor)  # JOGA O VALOR DENTRO DO VETOR

        #SOMANDO OS DIGITOS DO NUMERO
        soma = 0
        numero = vetor[i]
        while numero > 0:
            soma += numero % 10
            numero = int(numero / 10)
        vetoraux[i] = soma

    #ESTAMOS DANDO PRINT NO VETOR NA POSIÇÃO [X]
    #PARA DETERMINAR O VALOR DE X USAMOS UMA FUNÇÃO PARA SABER O INDEX(POSIÇÃO)
    #DO NOSSO VETORAUX QUE RECEBEU AS SOMAS DOS DIGITOS, MAS ANTES TEMOS A FUNÇÃO MAX
    #QUE NOS FALA QUAL O MAIOR NUMERO DO VETOR FAZENDO O INDEX ACHAR A POSIÇÃO DESSE NUMERO
    #{{OS DIGITOS SOMANDOS SÃO ARMAZENADOS NA MESMA POSIÇAO QUE ELES FORAM LIDOS}}
    print(vetor[ vetoraux.index (max(vetoraux)) ])

maior()