import tkinter as tk 

#---------- FUNÇÕES DE FUNCIONALIDADE DA CALCULADORA ----------
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

#---------- CONFIGURAÇÃO DA JANELA PRINCIPAL DA CALCULADORA ----------
janela = tk.Tk()
janela.title("Calculadora personalizada")
janela.configure(bg="#000000")

#---------- CAMPO DE ENTRADA DA CALCULADORA ----------
entrada = tk.Entry(
    janela,
    width=16,
    font=('Arial', 24),
    borderwidth=2,
    relief='solid',
    justify='right',
    bg="#393B3B",
    fg='#ffffff',
    insertbackground='#ffffff'
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

#---------- BOTÕES DA CALCULADORA ----------
botoes = [
    '7', '8', '9', '÷',
    '4', '5', '6', '×',
    '1', '2', '3', '−',
    '0', '.', 'C', '+'
]

def cor_botao(texto):
    if texto in ['÷', '×', '−', '+']:
        return "#ff7b00"
    elif texto == 'C':
        return "#f7180d"
    else:
        return "#454849"
    
row = 1 
col = 0 
for botao in botoes:
    tk.Button(
        janela,
        text=botao,
        width=5,
        height=2,
        font=('Arial', 18),
        fg='white',
        bg=cor_botao(botao),
        activebackground='#a6a6a6',
        activeforeground='black',
        borderwidth=0,
        command=lambda x=botao: limpar() if x == 'C' else adicionar_numero(x)
    ).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    janela, 
    text='=',
    width=22,
    height=2,
    font=('Arial', 18),
    fg='white',
    bg='#34c759',
    activebackground='#28a745',
    activeforeground='black',
    borderwidth=0,
    command=calcular
).grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

#---------- Tornar as Linhas e Colunas da Calculadora Responsivas ----------
total_linhas = row
for i in range(total_linhas + 1):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

#---------- Iniciar Loop da Interface da Calculadora ----------
janela.mainloop()