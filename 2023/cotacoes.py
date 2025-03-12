import requests
from tkinter import *

def atualizar():
    return requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()
def valorDolar():
    cotacao = atualizar()
    valor_Dolar = cotacao['USDBRL']['bid']
    textTotal["text"] = valor_Dolar


def valorEuro():
    cotacao = atualizar()
    valor_Euro = cotacao["EURBRL"]["bid"]
    textTotal["text"] = valor_Euro

def valorBTC():
    cotacao = atualizar()
    valor_BTC = cotacao["BTCBRL"]["bid"]
    textTotal["text"] = valor_BTC


janela = Tk()
janela.geometry("130x115")
janela.title("Conversor de moeda")

botaoDolar = Button(janela, text="Dolar => Real", command=valorDolar)
botaoEuro = Button(janela, text="Euro => Real", command=valorEuro)
botaoBTC = Button(janela, text="Bitcoin => Real", command=valorBTC)

botaoDolar.grid(column=1,row=2)
botaoEuro.grid(column=1,row=3)
botaoBTC.grid(column=1,row=4)

textTotal = Label(janela, text="")
textTotal.grid(column=1,row=5)

janela.mainloop()
