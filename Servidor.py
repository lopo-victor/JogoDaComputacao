import socket
import threading

perguntas_respostas = {
    "Qual é a linguagem de programação mais popular atualmente?": "Python",
    "Qual empresa desenvolveu o sistema operacional Android?": "Google",
    "Quem é considerado o pai da computação?": "Alan Turing"
}

def Tcliente(cliente, score_clientes):
    pontos = 0
    cliente.send("--Bem Vindo ao JDC--".encode())
    cliente.send("Digite seu nome de jogador: ".encode())
    nome = cliente.recv(1024).decode()

    for pergunta, resposta in perguntas_respostas.items():
        cliente.send(("PERGUNTA:\n"+pergunta).encode())
        resposta_cliente = cliente.recv(1024).decode()

        if resposta_cliente.lower() == resposta.lower():
            pontos += 1

    score_clientes[nome] = pontos

    string_user_scores = "\n".join([f"{key}: {value}" for key, value in score_clientes.items()])
    cliente.send(("--PLACAR--\n" + string_user_scores).encode())
    cliente.close()

def main():
    host = '127.0.0.1'
    port = 5555
    score_clientes = {}

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(5)
    print(f"Servidor iniciado em {host}:{port}")

    while True:
        cliente, endereco = servidor.accept()
        print(f"Conexão estabelecida com {endereco}")

        thread = threading.Thread(target=Tcliente, args=(cliente, score_clientes))
        thread.start()

if __name__ == "__main__":
    main()
