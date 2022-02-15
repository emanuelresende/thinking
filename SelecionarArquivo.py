from tkinter.filedialog import askopenfilename
import pandas as pd

caminho_arquivo = askopenfilename(title='selecione um arquivo excel')

df = pd.read_excel(caminho_arquivo)

print(caminho_arquivo)