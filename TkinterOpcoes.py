import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
#variable adiciona a variavel ao checkbox
checkbox_promocoes = tk.Checkbutton(text='deseja receber email?', variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text='Aceitar termos de privacidade', variable=var_politicas)
checkbox_politicas.grid(row=1, column=0)

def enviar():
    if var_promocoes.get():
        print('quer receber promocoes')
    else:
        print('não quer receber promocoes')
    if var_politicas.get():
        print('aceitou politicas')
    else:
        print('não aceitou politicas')

botao_enviar = tk.Button(text='enviar', command=enviar)
botao_enviar.grid(row=0, column=1)

janela.mainloop()