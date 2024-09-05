from tkinter import *  # Importa todas as funcionalidades do módulo Tkinter, que permite criar interfaces gráficas.

# Cria uma instância da janela principal do aplicativo
app = Tk()

# Define o título da janela
app.title("Curso de Python")

# Define o tamanho da janela (largura x altura)
app.geometry("500x300")

# Configura a cor de fundo da janela usando um código hexadecimal (neste caso, azul)
app.configure(background="#008")

# Cria um rótulo (Label) com o texto "Curso de Python" e define suas cores de fundo e texto
txt1 = Label(app, text="Curso de Python", bg="#ff0", fg="#000")

# Posiciona o rótulo em coordenadas absolutas (x=10, y=10) e define suas dimensões
txt1.place(x=10, y=10, width=150, height=30)

# Define variáveis para o segundo rótulo (texto, cor de fundo e cor do texto)
vtxt = "Modulo Tkinter"
vbg = "#ff0"  # Cor de fundo amarelo
vfg = "#000"  # Cor do texto preto

# Cria um segundo rótulo com o texto e as cores definidos nas variáveis acima
txt2 = Label(app, text=vtxt, bg=vbg, fg=vfg)

# Posiciona o rótulo usando o método 'pack', que organiza widgets de forma sequencial.
# O preenchimento interno (ipadx, ipady) e externo (padx, pady) é definido,
# e o widget preenche o eixo Y, expandindo se a janela aumentar de tamanho.
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=Y, expand=True)

# Inicia o loop principal do aplicativo, que mantém a janela aberta e responde a eventos
app.mainloop()
