# inicializa a variável que representa o estado do botão
botao_bloqueado = True

# verifica se algum radio foi selecionado
def radio_selecionado():
    if radio1.get() or radio2.get() or radio3.get():
        return True
    else:
        return False



# código para a interface gráfica
from tkinter import *
from tkinter import messagebox


root = Tk()

# função que será executada quando o botão for pressionado
def botao_pressionado():
    if radio_selecionado():
        # desbloqueia o botão
        botao_bloqueado = False
        # executa a ação do botão
        # ...
    else:
        # exibe uma mensagem de alerta
        messagebox.showwarning("Aviso", "Escolha uma opção antes de pressionar o botão.")

radio1 = IntVar()
radio2 = IntVar()
radio3 = IntVar()

radio_button1 = Radiobutton(root, text="Opção 1", variable=radio1, value=1)
radio_button2 = Radiobutton(root, text="Opção 2", variable=radio1, value=2)
radio_button3 = Radiobutton(root, text="Opção 3", variable=radio1, value=3)

botao = Button(root, text="Executar ação", state="disabled", command=botao_pressionado)

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()
botao.pack()

# atualiza o estado do botão quando algum radio for selecionado
radio1.trace("w", lambda name, index, mode: botao.config(state="normal") if radio_selecionado() else botao.config(state="disabled"))
radio2.trace("w", lambda name, index, mode: botao.config(state="normal") if radio_selecionado() else botao.config(state="disabled"))
radio3.trace("w", lambda name, index, mode: botao.config(state="normal") if radio_selecionado() else botao.config(state="disabled"))

root.mainloop()
