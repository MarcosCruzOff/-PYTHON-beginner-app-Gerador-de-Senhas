import random
import tkinter as tk

# Define a janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Define a variável de controle para a barra de força
strength_var = tk.StringVar()

# Define as opções de força
STRENGTHS = ["Fracas", "Médias", "Fortes"]

# Define a função para gerar senhas
def generate_password():
    # Define as opções de caracteres para a senha
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{};:,.<>/?"
    all_chars = lower + upper + numbers + symbols
    
    # Define o tamanho da senha
    length = 12
    
    # Gera a senha aleatória
    password = "".join(random.sample(all_chars, length))
    
    # Atualiza a barra de força com base na senha gerada
    if any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in symbols for char in password):
        strength_var.set(STRENGTHS[2])
    elif (any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password)) or (any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char in symbols for char in password)) or (any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in symbols for char in password)) or (any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in symbols for char in password)):
        strength_var.set(STRENGTHS[1])
    else:
        strength_var.set(STRENGTHS[0])
    
    # Atualiza o campo de texto com a senha gerada
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Define a barra de força
strength_label = tk.Label(root, textvariable=strength_var)
strength_label.pack()

# Define o campo de texto para a senha gerada
password_entry = tk.Entry(root, width=20)
password_entry.pack()

# Define o botão para gerar senhas
generate_button = tk.Button(root, text="Gerar senha", command=generate_password)
generate_button.pack()

# Define o botão para copiar a senha gerada
copy_button = tk.Button(root, text="Copiar", command=lambda: root.clipboard_append(password_entry.get()))
copy_button.pack()

# Inicia o loop principal da janela
root.mainloop()
