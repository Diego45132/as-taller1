# Cliente
import socket

HOST = '127.0.0.1'
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hola, servidor!')
    data = s.recv(1024)

print(f"Mensaje del servidor: {data.decode('utf-8')}")