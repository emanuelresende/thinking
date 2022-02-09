import tkinter as tk

janela = tk.Tk()

janela.title('Cotação de Moedas')

#para  adicionar algo na janela, primeiro cria o objeto depois utiliza o .pack()
#para adicionar cores, foreground ou só fg muda a cor da letra, e backround ou bg muda o fundo
#para width e heigt, a proporção não é a mesma, sendo a altura maior que a largura. por isso, tem que ajustar
mensagem = tk.Label(text='sistema cotação moeda', foreground='pink', background='black', width=50, height=10)
mensagem.pack()

janela.mainloop()
