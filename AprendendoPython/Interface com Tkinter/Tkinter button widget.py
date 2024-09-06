from tkinter import *  # Importa todas as funcionalidades do módulo Tkinter
import os  # Importa o módulo 'os' para manipulação de arquivos e diretórios

# Obtém o diretório onde o arquivo Python está localizado
c = os.path.dirname(__file__)

# Define o nome do arquivo onde os dados serão salvos, usando o diretório do script
nomeArquivo = c + "\\nomes.txt"


# Função que grava os dados inseridos no formulário em um arquivo de texto
def gravarDados():
    # Abre o arquivo no modo "a" (append), que adiciona dados ao final do arquivo
    arquivo = open(nomeArquivo, "a")

    # Grava os dados do campo 'Nome' no arquivo
    arquivo.write("Nome: %s" % vnome.get())

    # Grava os dados do campo 'Telefone' no arquivo
    arquivo.write("\nTelefone: %s" % vphone.get())

    # Grava os dados do campo 'Email' no arquivo
    arquivo.write("\nEmail: %s" % vemail.get())

    # Grava os dados do campo 'OBS' (observações). '1.0' é a posição inicial do texto, e 'END' é o fim
    arquivo.write("\nOBS: %s" % vobs.get("1.0", END))

    # Adiciona uma quebra de linha no final de cada conjunto de dados
    arquivo.write("\n")

    # Fecha o arquivo após a gravação
    arquivo.close()


# Cria a janela principal do aplicativo
app = Tk()

# Define o título da janela
app.title("CFB Cursos")

# Define o tamanho da janela
app.geometry("500x300")

# Define a cor de fundo da janela
app.configure(bg="#dde")

# Cria e posiciona um rótulo para o campo "Nome"
Label(app, text="Nome", bg="#dde", fg="#009", anchor=W).place(x=10, y=10, width=100, height=20)

# Cria uma caixa de entrada de texto para o campo "Nome"
vnome = Entry(app)
vnome.place(x=10, y=30, width=200, height=20)

# Cria e posiciona um rótulo para o campo "Telefone"
Label(app, text="Telefone", bg="#dde", fg="#009", anchor=W).place(x=10, y=60, width=100, height=20)

# Cria uma caixa de entrada de texto para o campo "Telefone"
vphone = Entry(app)
vphone.place(x=10, y=80, width=110, height=20)

# Cria e posiciona um rótulo para o campo "Email"
Label(app, text="Email", bg="#dde", fg="#009", anchor=W).place(x=10, y=110, width=100, height=20)

# Cria uma caixa de entrada de texto para o campo "Email"
vemail = Entry(app)
vemail.place(x=10, y=130, width=300, height=20)

# Cria e posiciona um rótulo para o campo "OBS" (observações)
Label(app, text="OBS", bg="#dde", fg="#009", anchor=W).place(x=10, y=150, width=100, height=20)

# Cria uma caixa de texto maior para o campo "OBS"
vobs = Text(app)
vobs.place(x=10, y=170, width=300, height=80)

# Cria um botão que, ao ser clicado, chama a função 'gravarDados' para salvar as informações
Button(app, text="Gravar Dados", command=gravarDados).place(x=10, y=270, width=100, height=20)

# Inicia o loop principal do aplicativo, que mantém a janela aberta e processa eventos
app.mainloop()
