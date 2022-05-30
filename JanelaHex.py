from tkinter import *

#criar a janela
janela = Tk()
janela.geometry('800x800+300+500')
janela.minsize(width=100, height=80)
janela.maxsize(width=600, height=110)
janela.config(background='#E6E6FA')

#criar operação
def soma():
    x = int(entry1.get())
    y = int(entry2.get())
    soma = x + y
    label1['text'] = soma

#criar os widgets
label1 = Label(janela, text='insira um numero', font='Arial 27')
entry1 = Entry(janela)
entry2 = Entry(janela)
btn1 = Button(janela, text='Somar', command=soma)

#organizar os widgets
label1.pack()
entry1.pack()
entry2.pack()
btn1.pack()

#executar a janela
janela.mainloop()