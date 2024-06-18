import socket
import ssl

# Конфигурация клиента
SERVER_ADDRESS = ('104.154.245.161', 8080)
CERT_FILE = '../server.crt'

# Создание сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(CERT_FILE)

with context.wrap_socket(sock, server_hostname=SERVER_ADDRESS[0])   as ssl_socket:
    ssl_socket.connect(SERVER_ADDRESS)
    ssl_socket.send(b"Hello, Server!")
    data = ssl_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")
