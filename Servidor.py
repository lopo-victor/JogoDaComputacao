import random
import socket
import threading

perguntas_respostas = {
    "Qual é a linguagem de programação mais popular atualmente?": "Python",
    "Qual empresa desenvolveu o sistema operacional Android?": "Google",
    "Quem é considerado o pai da computação?": "Alan Turing",
    "Qual foi o primeiro computador eletrônico de uso geral?" : "ENIAC",
    "Quem é o criador do sistema operacional Linux?": "Linus Torvalds",
    "O que é WWW?": "World Wide Web",
    "Qual componente é responsável pelo processamento gráfico?": "GPU",
    "Qual tipo de memória é usada para armazenamento temporário?": "RAM",
    "Qual memória só pode ser lida, não alterada?": "ROM"
}

lock = threading.Lock()

def aleatorizador(perguntas_respostas):
    perguntas_aleatorias = random.sample(list(perguntas_respostas.items()), 5)
    perguntas_aleatorias_dict = dict(perguntas_aleatorias)
    return perguntas_aleatorias_dict

def Tcliente(cliente, score_clientes):
    pontos = 0

    cliente.send("--Bem Vindo ao JDC--".encode())
    cliente.send("Digite seu nome de jogador: ".encode())
    nome = cliente.recv(1024).decode()

    perguntas_aleatorias = aleatorizador(perguntas_respostas)

    for pergunta, resposta in perguntas_aleatorias.items():
        cliente.send(("PERGUNTA:\n"+pergunta).encode())
        resposta_cliente = cliente.recv(1024).decode()

        if resposta_cliente.lower() == resposta.lower():
            pontos += 1

    with lock:
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
