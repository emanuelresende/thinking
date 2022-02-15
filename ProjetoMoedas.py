import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

janela = tk.Tk()

#editando a janela automaticamente
janela.rowconfigure(0,weight=1)
janela.columnconfigure([0,1], weight=1)

janela.title('Cotação de Moedas')

dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 8.00,
    'Bit': 20000,
}

moedas = list(dicionario_cotacoes.keys())

def pegar_cotacao():
    pass

titulo_moeda = tk.Label(text='Edite sua cotação', foreground='white', background='black', borderwidth=2, relief='solid')
titulo_moeda.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky='NSEW')

escolha_moeda = tk.Label(text='Cotação de Moedas')
escolha_moeda.grid(row=1, column=0, padx=10, pady=10)

box_moeda = ttk.Combobox(values=moedas)
box_moeda.grid(row=1, column=2, padx=10, pady=10)

dia_cotacao = tk.Label(text='Dia da Cotação')
dia_cotacao.grid(row=2, column=0, padx=10, pady=10, sticky='nwse', columnspan=2)

calendario_cotacao = DateEntry(year=2021, locale='pt_br')
calendario_cotacao.grid(row=2, column=2, padx=10, pady=10, sticky='nwse')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nwse', columnspan=2)

botao_cotacao = tk.Button(text='Cotar',command=pegar_cotacao)
botao_cotacao.grid(row=3, column=2, padx=10, pady=10)


# varias moedas

titulo_moedas = tk.Label(text='Varias Cotações', foreground='white', background='black', borderwidth=2, relief='solid')
titulo_moedas.grid(row=4, column=0, padx=10, pady=10, columnspan=3, sticky='NSEW')

janela.mainloop()
