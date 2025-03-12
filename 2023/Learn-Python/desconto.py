#DESCONTO EM PRODUTO
valor_compra = float(input("Qual o valor da compra?"))
forma_pagamento = input("Qual a forma de pagamento")
if (forma_pagamento=="A vista"):
    desconto = valor_compra * 0.10
elif(forma_pagamento=="Cartão"):
    desconto = valor_compra * 0.05
else:
    desconto = 0

print(f"O valor final é de: R${valor_compra - desconto}")
