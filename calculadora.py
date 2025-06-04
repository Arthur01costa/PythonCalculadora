import tkinter as tk 

def adicionar_numero(numero):
    entrada.insert(tk.END, str(numero))
def limpar():
    entrada.delete(0, tk.END)
def calcular(): 
    expressao = entrada.get()    
    expressao = expressao.replace('÷', '/').replace('×', '*').replace('−', '-')
    try:
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

janela = tk.Tk()
janela.title("Calculadora personalizada")

entrada = tk.Entry(janela, justify='right')
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    '7', '8', '9', '÷',
    '4', '5', '6', '×',
    '1', '2', '3', '−',
    '0', '.', 'C', '+'
]
def acao_botao(x):
    if x == 'C':
        limpar()
    else:
        adicionar_numero(x)
    
row = 1 
col = 0 
for botao in botoes:
    tk.Button(
        janela,
        text=botao,
        command=lambda x=botao: acao_botao(x)
    ).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1
tk.Button(janela, text='=', command=calcular).grid(row=row, column=col)
janela.mainloop()