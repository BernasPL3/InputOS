import socket

def connect_3ds(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((ip, 8000))
        print("Conectado ao 3DS")
    except:
        print("Erro ao conectar")
