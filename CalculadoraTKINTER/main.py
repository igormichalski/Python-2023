from tkinter import *
from tkinter import ttk

# cores
cor1 = "#242323"
cor2 = "#474545"
cor3 = "#000000"
cor4 = "#bfbfbf"
cor5 = "#fc8200"
cor6 = "#ffffff"

janela = Tk()
# configurações basicas
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)


# Frame 1
frameTela = Frame(janela, width=235, height=50, bg=cor2)
frameTela.grid(row=0, column=0)


# Frame 2
frameTeclado = Frame(janela, width=235, height=268, bg=cor1)
frameTeclado.grid(row=1, column=0)


#variavel todos valores
todos_valores = ""

# Funções
def entrada_dig(evento):
    global todos_valores

    todos_valores = todos_valores + str(evento)
    texto.set(str(todos_valores))

def calcular():
    global todos_valores

    try:
        resultados = eval(todos_valores)
    except SyntaxError:
        texto.set("Sintaxe Inválida")
    pass

    texto.set(str(resultados))
    todos_valores = ""
    todos_valores = str(resultados)

def limpar():
    global todos_valores

    todos_valores = ""
    texto.set(str("0"))


# Display
texto = StringVar()

display = Label(frameTela, textvariable=texto, width=16, height=2, padx=6, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 18", fg=cor6, bg=cor2)
display.place(x=0, y=0)


# botões 1 LINHA
b_1 = Button(frameTeclado,command= limpar, text="C",  width=11, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frameTeclado,command = lambda: entrada_dig("%"), text="%",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frameTeclado,command = lambda: entrada_dig("/"), text="/",  width=5, height=2, bg=cor5, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)


# botões 2 LINHA
b_4 = Button(frameTeclado,command = lambda: entrada_dig("7"), text="7",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frameTeclado,command = lambda: entrada_dig("8"), text="8",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frameTeclado,command = lambda: entrada_dig("9"), text="9",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frameTeclado,command = lambda: entrada_dig("*"), text="*",  width=5, height=2, bg=cor5, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)


# botões 2 LINHA
b_8 = Button(frameTeclado,command = lambda: entrada_dig("4"), text="4",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frameTeclado,command = lambda: entrada_dig("5"), text="5",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frameTeclado,command = lambda: entrada_dig("6"), text="6",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frameTeclado,command = lambda: entrada_dig("-"), text="-",  width=5, height=2, bg=cor5, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)


# botões 3 LINHA
b_12 = Button(frameTeclado,command = lambda: entrada_dig("1"), text="1",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frameTeclado,command = lambda: entrada_dig("2"), text="2",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frameTeclado,command = lambda: entrada_dig("3"), text="3",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frameTeclado,command = lambda: entrada_dig("+"), text="+",  width=5, height=2, bg=cor5, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)


# botões 4 LINHA
b_16 = Button(frameTeclado,command = lambda: entrada_dig("0"), text="0",  width=11, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frameTeclado,command = lambda: entrada_dig("."), text=".",  width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frameTeclado,command = calcular, text="=",  width=5, height=2, bg=cor5, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()
