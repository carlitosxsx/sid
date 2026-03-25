import socket

HOST = '127.0.0.1'
PORT = 5000

def calcular_area(base, altura):
    return (base * altura) / 2

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT))
        servidor.listen()

        print(f"Servidor rodando em {HOST}:{PORT}...")

        while True:
            conn, addr = servidor.accept()
            with conn:
                print(f"Conectado por {addr}")

                dados = conn.recv(1024).decode()

                try:
                    base_str, altura_str = dados.split(",")
                    base = float(base_str)
                    altura = float(altura_str)

                    if base <= 0 or altura <= 0:
                        raise ValueError

                    area = calcular_area(base, altura)
                    resposta = f"Área: {area:.2f}"

                except:
                    resposta = "ERRO: entrada inválida"

                conn.sendall((resposta + "\n").encode())

if __name__ == "__main__":
    iniciar_servidor()