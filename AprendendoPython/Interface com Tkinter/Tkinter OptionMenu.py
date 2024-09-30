from tkinter import *

def imprimirEsporte():
    ve = vesporte.get()
    if ve == "Futebol":
        print("Esporte Futebol")
    elif ve == "Vôlei":
        print("Esporte Vôlei")
    elif ve == "Basquete":
        print("Esporte Basquete")

# Criação da janela principal
app = Tk()
app.title("Curso de Python")
app.geometry("500x300")

# Lista de esportes para o OptionMenu
listaEsportes = ["Futebol", "Vôlei", "Basquete"]

# Variável que armazenará o esporte selecionado
vesporte = StringVar()
vesporte.set(listaEsportes[0])  # Valor padrão da lista

# Label para identificar os esportes
bl_esportes = Label(app, text="Esportes")
bl_esportes.pack()  # Exibe o rótulo

# OptionMenu para selecionar esportes
op_esportes = OptionMenu(app, vesporte, *listaEsportes)
op_esportes.pack()  # Exibe o OptionMenu

# Botão para exibir o esporte selecionado
btn_esporte = Button(app, text="Esporte selecionado", command=imprimirEsporte)
btn_esporte.pack()  # Exibe o botão

# Loop principal da interface gráfica
app.mainloop()
