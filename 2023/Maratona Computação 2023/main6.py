tamanho = int(input("Digite o tamanho do seu vetor: "))
A = []
B = []
R = [0]*tamanho

# RECEBENDO VETOR
for i in range(tamanho):
    valor = int(input(f"Digite o valor da posição {i} no A: "))
    A.append(valor)  # JOGA O VALOR DENTRO DO VETOR
    valor = int(input(f"Digite o valor da posição {i} no B: "))
    B.append(valor)  # JOGA O VALOR DENTRO DO VETOR
    R[i] = A[i]+B[i]

print(R)
