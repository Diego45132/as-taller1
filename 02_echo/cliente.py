# Cliente
import socket


HOST = '127.0.0.1'
PORT = 12345

def iniciar_cliente_echo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        
        while True:
            mensaje = input("Introduce un mensaje para enviar (o 'salir' para terminar): ")
            if mensaje.lower() == 'salir':
                break
            
            
            s.sendall(mensaje.encode('utf-8'))
            
            
            data = s.recv(1024)
            print(f"Mensaje enviado: '{mensaje}'")
            print(f"Respuesta del servidor: '{data.decode('utf-8')}'")
            print("-" * 20)

if __name__ == "__main__":
    iniciar_cliente_echo()

