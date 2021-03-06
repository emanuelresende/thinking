import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.title('Cotação de Moedas')

#configurando a linha e coluna para ajustar automaticamente
janela.rowconfigure(0,weight=1)
janela.columnconfigure([0,1], weight=1)

#para  adicionar algo na janela, primeiro cria o objeto depois utiliza o .pack()
#para adicionar cores, foreground ou só fg muda a cor da letra, e backround ou bg muda o fundo
#para width e heigt, a proporção não é a mesma, sendo a altura maior que a largura. por isso, tem que ajustar
mensagem = tk.Label(text='sistema cotação moeda', foreground='white', background='black', width=35, height=5)

#mensagem.pack() pode ser usuado se for uma unica coluna
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW') #NSEW sigfica norte sul leste oeste, para estender a linha

mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.grid(row=1,column=0)

#campo para entrada de informações do usuario, o pack adiciona na caixa
#moeda = tk.Entry()
#moeda.grid(row=1,column=1)

dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 8.00,
    'Bit': 20000,
}

#criando lista suspensa
moedas = list(dicionario_cotacoes.keys())

moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

#para interagir com o botao, o get() devolve o dado do usuario
def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text="cotacao não existe")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'cotação do {moeda_preenchida} é {cotacao_moeda} reais'

botao = tk.Button(text='Buscar cotação', command=buscar_cotacao)
botao.grid(row=2, column=1)

mensagem3 = tk.Label(text='Digite mais de uma moeda')
mensagem3.grid(row=4, column=0, columnspan=2)

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0)

def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split('\n') #separando as paavras da caixa de texto
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}: {cotacao}')
    mensagem4 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=1)

botao_multiplascotacoes = tk.Button(text="buscar cotações", command=buscar_cotacoes)
botao_multiplascotacoes.grid(row=5, column=1)




janela.mainloop()
