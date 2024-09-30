from tkinter import *  # Importa todas as funcionalidades da biblioteca tkinter

# Função que imprime o esporte selecionado
def imprimirEsporte():
    ve = vesporte.get()  # Obtém o valor selecionado no Radiobutton de esportes
    # Condicionais para verificar qual esporte foi escolhido e imprimir a mensagem correspondente
    if ve == "futebol":
        print("Esporte Futebol")
    elif ve == "volei":
        print("Esporte Vôlei")
    elif ve == "basquete":
        print("Esporte Basquete")

# Criação da janela principal da aplicação
app = Tk()  # Inicializa o objeto principal da interface gráfica
app.title("Curso de Python")  # Define o título da janela
app.geometry("500x300")  # Define o tamanho da janela (largura x altura)

# Variáveis associadas aos Radiobuttons para armazenar a seleção do usuário
vesporte = StringVar()  # Variável para armazenar o esporte selecionado
vcor = StringVar()  # Variável para armazenar a cor selecionada

# Label (rótulo) para identificar a seção de esportes
bl_esportes = Label(app, text="Esportes")
bl_esportes.pack()  # Exibe o rótulo na janela

# Radiobuttons para seleção dos esportes
rb_futebol = Radiobutton(app, text="Futebol", value="futebol", variable=vesporte)
rb_futebol.pack()  # Exibe o Radiobutton para Futebol

rb_volei = Radiobutton(app, text="Vôlei", value="volei", variable=vesporte)
rb_volei.pack()  # Exibe o Radiobutton para Vôlei

rb_basquete = Radiobutton(app, text="Basquete", value="basquete", variable=vesporte)
rb_basquete.pack()  # Exibe o Radiobutton para Basquete

# Label (rótulo) para identificar a seção de cores
bl_cores = Label(app, text="Cores")
bl_cores.pack()  # Exibe o rótulo na janela

# Radiobuttons para seleção de cores
rb_verde = Radiobutton(app, text="Verde", value="#0f0", variable=vcor)
rb_verde.pack()  # Exibe o Radiobutton para a cor Verde

rb_vermelho = Radiobutton(app, text="Vermelho", value="#f00", variable=vcor)
rb_vermelho.pack()  # Exibe o Radiobutton para a cor Vermelha

rb_azul = Radiobutton(app, text="Azul", value="#00f", variable=vcor)
rb_azul.pack()  # Exibe o Radiobutton para a cor Azul

# Botão que, ao ser clicado, chama a função imprimirEsporte()
btn_esporte = Button(app, text="Esporte selecionado", command=imprimirEsporte)
btn_esporte.pack()  # Exibe o botão na janela

# Loop principal da aplicação para manter a janela aberta
app.mainloop()  # Mantém a interface gráfica em execução até o usuário fechá-la
