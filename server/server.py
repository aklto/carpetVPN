import socket
import ssl

# Конфигурация сервера
SERVER_ADDRESS = ('0.0.0.0', 8080)
CERT_FILE = 'server.crt'
KEY_FILE = 'server.key'

# Создание сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(SERVER_ADDRESS)
sock.listen(5)

# Настройка SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

print("Server is listening...")

while True:
    client_socket, addr = sock.accept()
    print(f"Connection from {addr}")

    with context.wrap_socket(client_socket, server_side=True) as ssl_socket:
        data = ssl_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
        ssl_socket.send(b"Hello, Secure World!")

    client_socket.close()
