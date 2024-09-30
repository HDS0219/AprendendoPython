from tkinter import *
from tkinter import messagebox

# Função para mostrar diferentes tipos de mensagens
def mostrarMsg(tipomsg, msg):
    if tipomsg == "1":
        messagebox.showinfo(title="CFB Cursos", message=msg)
    elif tipomsg == "2":
        messagebox.showwarning(title="CFB Cursos", message=msg)
    elif tipomsg == "3":
        messagebox.showerror(title="CFB Cursos", message=msg)

# Função para resetar o textbox
def resetarTB():
    res = messagebox.askyesno("Resetar", "Confirma Reset do textbox?")
    #asyesno / askquestion - sim e não(True e False)
    #askokcancel - Ok e Cancelar(True e False)
    #askretrycancel - Repetir e Cancelar (True e False)
    #askyesnocancel - Sim, não e cancelar (True, False e NONE)
    if res == True:
        tb_num.delete(0, END)  # Apaga o conteúdo da caixa de texto
        tb_num.insert(0, "1")  # Insere o valor padrão "1"

# Variável que contém a mensagem
vmsg = "Curso de Python/Tkinter"

# Configuração da janela principal
app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

# Variável que armazenará o tipo de caixa de mensagem
vnum_cxtexto = StringVar()

# Label para indicar a entrada
Label(app, text="Tipo de caixa (1, 2, 3)").pack()

# Caixa de texto para o usuário escolher o tipo de mensagem
tb_num = Entry(app, textvariable=vnum_cxtexto)
vnum_cxtexto.set("1")  # Valor inicial
tb_num.pack()

# Botão para mostrar a mensagem com base na seleção do usuário
btn_msg = Button(app, text="Mostrar mensagem", command=lambda: mostrarMsg(vnum_cxtexto.get(), vmsg))
btn_msg.pack()  # Exibe o botão na janela

# Botão para resetar o conteúdo da caixa de texto
btn_reset = Button(app, text="Resetar textbox", command=resetarTB)
btn_reset.pack()  # Exibe o botão na janela

# Loop principal da interface gráfica
app.mainloop()
