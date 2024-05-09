import socket

def main():
    host = '127.0.0.1'
    port = 5555

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))

    while True:
        pergunta = cliente.recv(1024).decode()
        if not pergunta:
            break

        if pergunta.startswith("PERGUNTA:") or pergunta.startswith("Digite") :
            print(pergunta)
            resposta = input("Sua resposta: ")
            print(f"\n")
            cliente.send(resposta.encode())
        else:
            print(pergunta)


    cliente.close()

if __name__ == "__main__":
    main()
