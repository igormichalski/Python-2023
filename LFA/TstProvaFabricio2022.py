sequencia = input("Infome uma sequencia: ")
tamanho_sequencia = len(sequencia)
aceita = 0
i=0

while(i<tamanho_sequencia):
    if sequencia[i] == "1" or sequencia[i] == "0":
        continue
    else:
        exit(-1)
    i += 1
    
i=0

while(i<tamanho_sequencia):
    if sequencia[i] == "1":
        aceita = 1
    else:
        aceita = 0
    i += 1

if aceita == 1:
    print("Aceito")
else:
    print("Recusado")
