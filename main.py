from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#Cores
mainbg = "#212121"
secondbg = "#121212"
green = "#4d943e"
yellow = "#f8be54"
red = "#fb1909"

#Fonts
txt = "jetBrains Mono"


# verifica se algum radio foi selecionado
def radio_selecionado():
    if opcao.get():
        return True
    else:
        return False

# Função para gerar a senha
def gerar_senha():
    if radio_selecionado():
        # Caracteres possíveis na senha
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()_+-=[]{}|;:,.<>/?"
    
        # Tamanho da senha
        if opcao.get() == 1:
            tamanho = 4
        elif opcao.get() == 2:
            tamanho = 12
        else:
            tamanho = 20
    
        # Gerar a senha
        senha = ""
        for i in range(tamanho):
            senha += random.choice(caracteres)
        
        # Exibir a senha na tela
        senha_var.set(senha)
        
    else:
        # exibe uma mensagem de alerta
        messagebox.showwarning("Aviso", "É preciso primeiro escolher uma das opções de SENHA acima.")  
 
# Função para copiar a senha para a área de transferência
def copiar_senha():
    pyperclip.copy(senha_var.get())
    
    if senha_var.get():
        label["text"] = f"senha copiada: {senha_var.get()} com sucesso"

# Criar a app principal
app = Tk()
app.title("Gerador de Senhas")
app.geometry("380x380")
app.resizable(False, False)
app.config(bg=mainbg)

icon = PhotoImage(file="imagens/icon.png")
app.iconphoto(True, icon)

# Variável para armazenar a opção selecionada
opcao = IntVar()

# Caixa de seleção de força da senha
fraca_radio = Radiobutton(app, text="Fraca", bg=secondbg, font=(txt, 12, "bold"), variable=opcao, value=1, fg=red)
fraca_radio.place(x=50,y=15)

media_radio = Radiobutton(app, text="Média", bg=secondbg, font=(txt, 12, "bold"), variable=opcao, value=2, fg=yellow)
media_radio.place(x=150,y=15)

forte_radio = Radiobutton(app, text="Forte", bg=secondbg, font=(txt, 12, "bold"), variable=opcao, value=3, fg=green)
forte_radio.place(x=250,y=15)
    
# Variável para armazenar a senha gerada
senha_var = StringVar()

# Rótulo para exibir a senha gerada
senha_label = Label(app, textvariable=senha_var, font=("Courier", 14), width=30, height=2, relief="solid")
senha_label.place(x=20, y=150)
        
# Botão para gerar a senha
gerar_botao = Button(app, text="Gerar Senha", bg=secondbg, font=(txt, 12, "bold"), fg="white",command=gerar_senha, width=20)
gerar_botao.place(x=90, y=80)


    
# Botão para copiar a senha
copiar_botao = Button(app, text="Copiar Senha", bg=secondbg, font=(txt, 12, "bold"), fg="white", command=copiar_senha, width=20)
copiar_botao.place(x=90 , y=250)

label = Label(width=50, height=4, text='', bg=mainbg, fg="white", font=(txt, 8), justify="center")
label.place(x=10 , y=300)

mainloop()