import tkinter as tk

janela = tk.Tk()

#por default, o padrao da variavel vai ser tudo marcado, para não aparecer nada marcado
#tem que inicializar o valor com algum texto no valor
var_aviao = tk.StringVar(value='nada')

#tb é possivel adicionar o command nos parametros abaixo, para não precisar de botão enviar.
#para isso, a def enviar deve estar antes dos botoes

botao_classeexecutiva = tk.Radiobutton(text='classe executiva', variable=var_aviao, value='Classe Executiva')
botao_classeeconomica = tk.Radiobutton(text='classe economica', variable=var_aviao, value='Classe Economica')
botao_primeiraclasse = tk.Radiobutton(text='primeira classe', variable=var_aviao, value='Primeira Classe')
botao_primeiraclasse.grid(row=0, column=0)
botao_classeexecutiva.grid(row=0, column=1)
botao_classeeconomica.grid(row=0, column=2)

def enviar():
    print(var_aviao.get())

botao_enviar = tk.Button(text='enviar', command=enviar)
botao_enviar.grid(row=1,column=1)


janela.mainloop()