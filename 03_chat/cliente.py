# Cliente

import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def recibir_mensajes(sock):
    while True:
        try:
            mensaje = sock.recv(1024).decode("utf-8")
            if mensaje:
                print(mensaje)
            else:
                break
        except:
            print("¡Error al recibir mensaje del servidor!")
            break

def enviar_mensajes(sock):
    while True:
        mensaje = input()
        try:
            sock.send(mensaje.encode("utf-8"))
        except:
            print("¡Error al enviar mensaje al servidor!")
            break

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_recibir.start()

    hilo_enviar = threading.Thread(target=enviar_mensajes, args=(cliente,))
    hilo_enviar.start()

if __name__ == "__main__":
    iniciar_cliente()

def enviar_mensajes(sock):
    while True:
        mensaje = input()
        if mensaje.lower() == "salir":
            print("Saliendo del chat...")
            sock.close()
            break
        try:
            sock.send(mensaje.encode("utf-8"))
        except:
            print("¡Error al enviar mensaje al servidor!")
            break
