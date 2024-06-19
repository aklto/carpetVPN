import socket

# Конфигурация клиента
SERVER_ADDRESS = ('35.202.57.44', 8080)
try:
    # Создание сокета
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"Attempting to connect to {SERVER_ADDRESS}...")
    sock.settimeout(10)  # Установите таймаут
    sock.connect(SERVER_ADDRESS)
    print("Connection established.")
    sock.send(b"Hello, Server!")
    data = sock.recv(1024)
    print(f"Received: {data.decode('utf-8')}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    sock.close()