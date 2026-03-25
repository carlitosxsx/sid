import socket
import tkinter as tk
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 5000

def calcular():
    base = entry_base.get()
    altura = entry_altura.get()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((HOST, PORT))

            mensagem = f"{base},{altura}"
            cliente.sendall(mensagem.encode())

            resposta = cliente.recv(1024).decode()

            label_resultado.config(text=resposta)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro na comunicação:\n{e}")

# Janela
janela = tk.Tk()
janela.title("Calculadora de Área do Triângulo")
janela.geometry("300x200")

# Campo Base
label_base = tk.Label(janela, text="Base:")
label_base.pack()

entry_base = tk.Entry(janela)
entry_base.pack()

# Campo Altura
label_altura = tk.Label(janela, text="Altura:")
label_altura.pack()

entry_altura = tk.Entry(janela)
entry_altura.pack()

# Botão Resultado
botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack(pady=10)

# Exibir Resultado
label_resultado = tk.Label(janela, text="Resultado aparecerá aqui")
label_resultado.pack()

# Loop da interface
janela.mainloop()