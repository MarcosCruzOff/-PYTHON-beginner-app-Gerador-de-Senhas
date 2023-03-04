from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# Criar a app principal
app = Tk()
app.title("Gerador de Senhas")
app.geometry("380x380")
app.resizable(False, False)
app.config(bg="#212121")

# inicializa a variável que representa o estado do botão
botao_bloqueado = True



# Variável para armazenar a opção selecionada
opcao = IntVar()

# Caixa de seleção de força da senha
fraca_radio = Radiobutton(app, text="Fraca", bg="#121212", font=("jetBrainz Mono", 12, "bold"), variable=opcao, value=1, fg="red")
fraca_radio.place(x=50,y=15)

media_radio = Radiobutton(app, text="Média", bg="#121212", font=("jetBrainz Mono", 12, "bold"), variable=opcao, value=2, fg="orange")
media_radio.place(x=150,y=15)

forte_radio = Radiobutton(app, text="Forte", bg="#121212", font=("jetBrainz Mono", 12, "bold"), variable=opcao, value=3, fg="green")
forte_radio.place(x=250,y=15)

# verifica se algum radio foi selecionado
def radio_selecionado():
    if opcao.get():
        return True
    else:
        return False

# Função para gerar a senha
def gerar_senha():
    if radio_selecionado():
        # desbloqueia o botão
        botao_bloqueado = False
        # executa a ação do botão
        # ...
    else:
        # exibe uma mensagem de alerta
        messagebox.showwarning("Aviso", "Escolha uma opção antes de pressionar o botão.")  
        
    # Caracteres possíveis na senha
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()_+-=[]{}|;:,.<>/?"
    
    # Tamanho da senha
    if opcao.get() == 1:
        tamanho = 8
    elif opcao.get() == 2:
        tamanho = 12
    else:
        tamanho = 16
    
    # Gerar a senha
    senha = ""
    for i in range(tamanho):
        senha += random.choice(caracteres)
    
    # Exibir a senha na tela
    senha_var.set(senha)

# Variável para armazenar a senha gerada
senha_var = StringVar()

# Rótulo para exibir a senha gerada
senha_label = Label(app, textvariable=senha_var, font=("Courier", 14), width=30, height=2, relief="solid")
senha_label.place(x=20, y=150)  

        
# Botão para gerar a senha
gerar_botao = Button(app, text="Gerar Senha", bg="#121212", font=("jetBrainz Mono", 12, "bold"), fg="white",command=gerar_senha, width=20)
gerar_botao.place(x=90, y=80)

# Função para copiar a senha para a área de transferência
def copiar_senha():
    pyperclip.copy(senha_var.get())
    
# Botão para copiar a senha
copiar_botao = Button(app, text="Copiar Senha", bg="#121212", font=("jetBrainz Mono", 12, "bold"), fg="white", command=copiar_senha, width=20)
copiar_botao.place(x=90 , y=250)  



mainloop()