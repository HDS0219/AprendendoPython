from tkinter import *
import os

pastaApp = os.path.dirname(__file__)

def semComando():
    print("TESTE")

def novoContato():
    #Péssima solução. por favor, substitua o nome do arquivo e se possivel, não utilize de jeito algum meus exemplos.
    #
    with open(os.path.join(pastaApp, 'tkinter gravando dados no banco de dados.py'), 'r') as file:
        code = file.read()
        exec(code)


app = Tk()
app.title("Curso de Python")
app.geometry("500x300")
app.configure(bg="#dde")

barraDeMenus = Menu(app)

menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Novo", command=novoContato)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de dados", command=semComando)
menuManutencao.add_command(label="Manutenção", command=semComando)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Curso de python", command=semComando)
menuSobre.add_command(label="sobre", command=semComando)

barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraDeMenus)
app.mainloop()
