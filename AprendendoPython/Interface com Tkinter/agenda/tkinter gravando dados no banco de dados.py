from tkinter import *  # Importa todas as funcionalidades do Tkinter
import os  # Importa o módulo 'os' para manipulação de arquivos e diretórios
import Banco  # Importa o módulo 'Banco'

# Obtém o diretório onde o arquivo Python está localizado e define o caminho para um arquivo de texto chamado "nomes.txt"
c = os.path.dirname(__file__)
nomeArquivo = os.path.join(c, "\\nomes.txt")


# Função que coleta os dados do formulário e insere no banco de dados
def gravarDados():
    # Coleta os valores inseridos nos campos de texto e remove espaços em branco nas extremidades com 'strip()'
    vnome = tb_nome.get().strip()
    vphone = tb_phone.get().strip()
    vemail = tb_email.get().strip()
    vobs = tb_obs.get("1.0", END).strip()  # Coleta o texto completo da caixa de observações (OBS)

    # Verifica se os campos obrigatórios (nome, telefone, email) estão preenchidos
    if vnome and vphone and vemail:
        # Define a query SQL para inserir os dados na tabela 'tb_contatos'
        vquery = """
        INSERT INTO tb_contatos 
        (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS) 
        VALUES (?, ?, ?, ?)
        """
        try:
            # Executa a operação de inserção no banco de dados com os dados coletados
            Banco.dml(vquery, (vnome, vphone, vemail, vobs))

            # Limpa os campos do formulário após gravar os dados com sucesso
            tb_nome.delete(0, END)
            tb_phone.delete(0, END)
            tb_email.delete(0, END)
            tb_obs.delete("1.0", END)

            print("Dados gravados com sucesso!")  # Exibe uma mensagem de sucesso no console
        except Exception as e:
            print(f"Erro ao gravar os dados: {e}")  # Exibe uma mensagem de erro no console se ocorrer uma exceção
    else:
        print(
            "Erro: Todos os campos obrigatórios devem ser preenchidos.")  # Mensagem de erro se os campos obrigatórios estiverem vazios


# Cria a janela principal do aplicativo
app = Tk()

# Define o título da janela
app.title("CFB Cursos")

# Define o tamanho da janela
app.geometry("500x300")

# Configura a cor de fundo da janela
app.configure(bg="#dde")

# Cria e posiciona um rótulo para o campo "Nome"
Label(app, text="Nome", bg="#dde", fg="#009", anchor=W).place(x=10, y=10, width=100, height=20)

# Cria uma caixa de entrada de texto para o campo "Nome"
tb_nome = Entry(app)
tb_nome.place(x=10, y=30, width=200, height=20)

# Cria e posiciona um rótulo para o campo "Telefone"
Label(app, text="Telefone", bg="#dde", fg="#009", anchor=W).place(x=10, y=60, width=100, height=20)

# Cria uma caixa de entrada de texto para o campo "Telefone"
tb_phone = Entry(app)
tb_phone.place(x=10, y=80, width=110, height=20)

# Cria e posiciona um rótulo para o campo "Email"
Label(app, text="Email", bg="#dde", fg="#009", anchor=W).place(x=10, y=110, width=100, height=20)

# Cria uma caixa de entrada de texto para o campo "Email"
tb_email = Entry(app)
tb_email.place(x=10, y=130, width=300, height=20)

# Cria e posiciona um rótulo para o campo "OBS" (observações)
Label(app, text="OBS", bg="#dde", fg="#009", anchor=W).place(x=10, y=150, width=100, height=20)

# Cria uma caixa de texto maior para o campo "OBS"
tb_obs = Text(app)
tb_obs.place(x=10, y=170, width=300, height=80)

# Cria um botão que, ao ser clicado, chama a função 'gravarDados' para salvar as informações no banco de dados
Button(app, text="Gravar Dados", command=gravarDados).place(x=10, y=270, width=100, height=20)

# Inicia o loop principal do aplicativo, que mantém a janela aberta e processa eventos
app.mainloop()
