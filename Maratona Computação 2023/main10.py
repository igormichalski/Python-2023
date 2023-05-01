tamanho = int(input("Digite o tamanho da palavra (letras): "))
string = input("Digite uma palavra: ")[::-1]
string = string[0] + string[1].upper() + string[2:]
string = string[0:tamanho-2] + string[tamanho-2].upper() + string[tamanho-1]
print(string)