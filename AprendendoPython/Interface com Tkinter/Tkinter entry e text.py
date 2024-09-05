from tkinter import *  # Importa todas as funcionalidades do módulo Tkinter para criar interfaces gráficas.

# Cria a janela principal do aplicativo
app = Tk()

# Define o título da janela
app.title("CFB Cursos")

# Define as dimensões da janela (largura x altura)
app.geometry("500x300")

# Configura a cor de fundo da janela usando um código hexadecimal (neste caso, uma cor cinza claro)
app.configure(bg="#dde")

# Anchor => Direcionamento do texto dentro do widget (N = Norte, S = Sul, E = Leste, W = Oeste)
# NE = Nordeste, SE = Sudeste, SO = Sudoeste, NO = Noroeste

# Cria um rótulo (Label) para o campo "Nome" e o posiciona na janela.
# A cor de fundo é igual à da janela, o texto tem a cor azul (#009) e é ancorado à esquerda (W).
Label(app, text="Nome", bg="#dde", fg="#009", anchor=W).place(x=10, y=10, width=100, height=20)

# Cria uma caixa de entrada de texto (Entry) para o usuário inserir o nome e a posiciona na janela
vnome = Entry(app)
vnome.place(x=10, y=30, width=200, height=20)

# Cria um rótulo para o campo "Telefone" e o posiciona na janela
Label(app, text="Telefone", bg="#dde", fg="#009", anchor=W).place(x=10, y=60, width=100, height=20)

# Cria uma caixa de entrada de texto para o usuário inserir o telefone
vphone = Entry(app)
vphone.place(x=10, y=80, width=110, height=20)

# Cria um rótulo para o campo "Email" e o posiciona na janela
Label(app, text="Email", bg="#dde", fg="#009", anchor=W).place(x=10, y=110, width=100, height=20)

# Cria uma caixa de entrada de texto para o usuário inserir o email
vemail = Entry(app)
vemail.place(x=10, y=130, width=300, height=20)

# Cria um rótulo para o campo "OBS" (observações) e o posiciona na janela
Label(app, text="OBS", bg="#dde", fg="#009", anchor=W).place(x=10, y=150, width=100, height=20)

# Cria uma caixa de texto maior (Text) para o usuário inserir observações
vobs = Text(app)
vobs.place(x=10, y=170, width=300, height=80)

# Inicia o loop principal do aplicativo, que mantém a janela aberta e responde a eventos
app.mainloop()
