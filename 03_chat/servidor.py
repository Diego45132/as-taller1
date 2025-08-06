# Servidor

import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

clientes = []
nombres = {}

def manejar_cliente(cliente, direccion):
    print(f"[NUEVA CONEXIÓN] {direccion} conectado.")
    cliente.send("Escribe tu nombre: ".encode("utf-8"))
    nombre = cliente.recv(1024).decode("utf-8")
    nombres[cliente] = nombre

    bienvenida = f"{nombre} se ha unido al chat."
    broadcast(bienvenida, cliente)
    cliente.send("Conectado al servidor de chat.\n".encode("utf-8"))

    while True:
        try:
            mensaje = cliente.recv(1024)
            if mensaje:
                broadcast(f"{nombre}: {mensaje.decode('utf-8')}", cliente)
            else:
                eliminar_cliente(cliente)
                break
        except:
            eliminar_cliente(cliente)
            break

def broadcast(mensaje, cliente_actual):
    for cliente in clientes:
        if cliente != cliente_actual:
            try:
                cliente.send(mensaje.encode("utf-8"))
            except:
                eliminar_cliente(cliente)

def eliminar_cliente(cliente):
    if cliente in clientes:
        nombre = nombres.get(cliente, "Alguien")
        clientes.remove(cliente)
        cliente.close()
        broadcast(f"{nombre} ha salido del chat.", cliente)

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[ESCUCHANDO] Servidor en {HOST}:{PORT}")

    while True:
        cliente, direccion = servidor.accept()
        clientes.append(cliente)
        hilo = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
        hilo.start()
        print(f"[CONEXIONES ACTIVAS] {threading.active_count() - 1}")

if __name__ == "__main__":
    iniciar_servidor()

