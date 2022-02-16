import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all') #adicionando o API da lista de moedas
dicionario_moedas = requisicao.json()
moedas = list(dicionario_moedas.keys())

janela = tk.Tk()

#editando a janela automaticamente
janela.rowconfigure(0,weight=1)
janela.columnconfigure([0,1], weight=1)

janela.title('Cotação de Moedas')

#para pegar a cotação, usar o link do json para datas especificas
def pegar_cotacao():
    moeda_escolhida = combobox_moeda.get()
    data_cotacao = calendario_cotacao.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/{moeda_escolhida}-BRL/10?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json() #editando o json para lista
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f"A cotação da {moeda_escolhida} no dia {data_cotacao} foi de: R$ {valor_moeda}"

# -----cotacao unica-----
label_moeda = tk.Label(text='Edite sua cotação', foreground='white', background='black', borderwidth=2, relief='solid')
label_moeda.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky='NSEW')

#escolher lista suspensa moedas
label_escolhamoeda = tk.Label(text='Selecionar Moeda', anchor='e')
label_escolhamoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nwse', columnspan=2)

combobox_moeda = ttk.Combobox(values=moedas)
combobox_moeda.grid(row=1, column=2, padx=10, pady=10)

#Label Calendario
label_diacotacao = tk.Label(text='Selecionar o dia que quer pegar a cotação', anchor='e')
label_diacotacao.grid(row=2, column=0, padx=10, pady=10, sticky='nwse', columnspan=2)

calendario_cotacao = DateEntry(year=2021, locale='pt_br')
calendario_cotacao.grid(row=2, column=2, padx=10, pady=10, sticky='nwse')

#botão enviar cotação
label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nwse', columnspan=2)

botao_cotacao = tk.Button(text='Cotar', command=pegar_cotacao)
botao_cotacao.grid(row=3, column=2, padx=10, pady=10, columnspan=2, sticky='nwse')

# -----varias moedas-----

def selecionar_arquivo():
    pass

def atualizar_cotacoes():
    pass

label_variasmoedas = tk.Label(text='Varias Cotações', foreground='white', background='black', borderwidth=2, relief='solid')
label_variasmoedas.grid(row=4, column=0, padx=10, pady=10, columnspan=3, sticky='NSEW')

label_cotarvariasmoedas = tk.Label(text='Selecione o arquivo em excel com as moedas na coluna A')
label_cotarvariasmoedas.grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky='NSEW')

botao_selecionararquivo = tk.Button(text='Enviar Arquivo', command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='NWSE')

label_arquivoselecionado = tk.Label(text='Nenhum arquivo selecionado', anchor='e') #anchor faz o alinhamento do texto
label_arquivoselecionado.grid(row=6,column=0, columnspan=3,padx=10,pady=10, sticky='NWSE')

label_datainicial = tk.Label(text='Data Inicial')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nwse')

calendario_cotacaoinicial = DateEntry(year=2021, locale='pt_br')
calendario_cotacaoinicial.grid(row=7, column=1, padx=10, pady=10)

label_datafinal = tk.Label(text='Data Inicial')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='nwse')

calendario_cotacaoinicial = DateEntry(year=2021, locale='pt_br')
calendario_cotacaoinicial.grid(row=8, column=1, padx=10, pady=10)

botao_atualizarcotacoes = tk.Button(text='Atualizar cotações', command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nwse')

label_atualizarcotacoes = tk.Label(text='')
label_atualizarcotacoes.grid(row=9, column=1, padx=10, pady=10, sticky='nwse')

botao_fechar = tk.Button(text='Fechar Janela', command=janela.quit) #para fechar a janela não precisa criar def, só usar o janela.quit
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nwse')

janela.mainloop()
