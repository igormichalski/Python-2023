import requests
from tkinter import *

def atualizar():
    return requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
def valorDolar():
    cotacao = atualizar()
    valor = entrada.get()
    valor = int(valor)
    valor_Dolar = cotacao['USDBRL']['bid']
    textTotal["text"] = valor_Dolar


def valorEuro():
    cotacao = atualizar()
    valor_Euro = cotacao["EURBRL"]["bid"]
    textTotal["text"] = valor_Euro*entrada

def valorBTC():
    cotacao = atualizar()
    valor_BTC = cotacao["BTCBRL"]["bid"]
    textTotal["text"] = valor_BTC*entrada


janela = Tk()
janela.title("Conversor de moeda")
janela.geometry("400x300")

botaoDolar = Button(janela, text="Dolar => Real", command=valorDolar)
botaoEuro = Button(janela, text="Euro => Real", command=valorEuro)
botaoBTC = Button(janela, text="Bitcoin => Real", command=valorBTC)

botaoDolar.grid(column=1,row=2, padx=150, pady=2)
botaoEuro.grid(column=1,row=3, padx=150, pady=2)
botaoBTC.grid(column=1,row=4, padx=150, pady=2)

textTotal = Label(janela, text="")
textTotal.grid(column=1,row=5)

entrada = Entry(janela)
entrada.place(x=150, y=110,width=100, height=20)


janela.mainloop()



