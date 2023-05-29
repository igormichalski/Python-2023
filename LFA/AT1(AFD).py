def verificar_palavra(alfabeto, estados, estado_inicial, estados_aceitacao, delta, palavra):
    estado_atual = estado_inicial
    caminhos = [estado_atual]

    for letra in palavra:
        if letra not in alfabeto:
            return False, caminhos

        estado_atual = delta[estado_atual][letra]
        caminhos.append(estado_atual)

    return estado_atual in estados_aceitacao, caminhos

n=1;

while(n!=-1):
    alfabeto = input("Digite o alfabeto (separe os símbolos por espaço): ").split()
    estados = input("Digite os estados (separe os estados por espaço): ").split()
    estado_inicial = input("Digite o estado inicial: ")
    estados_aceitacao = input("Digite os estados de aceitação (separe os estados por espaço): ").split()
    x = 1;

    #Recebe Delta
    delta = {}
    for estado in estados:
        delta[estado] = {}
        for simbolo in alfabeto:
            delta[estado][simbolo] = input(f"Delta({estado}, {simbolo}): ")


    while (x!= -1): #LOOP PARA VERIFICAR MAIS DE UMA PALAVRA
        palavra = input("Digite a palavra a ser verificada: ")
        aceita, caminhos = verificar_palavra(alfabeto, estados, estado_inicial, estados_aceitacao, delta, palavra)


        print("\nCAMINHOS:")
        print(" --> ".join(caminhos))

        if aceita:
            print("ACEITA!")
        else:
            print("RECUSADA!")

        x = int(input("\nVerificar outra palavra? (-1 para sair)"))

    n = int(input("\nVerificar outra autonomo? (-1 para sair)"));
