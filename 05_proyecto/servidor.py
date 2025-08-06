# Servidor

import socket
import json
import threading

def diagnosticar_vehiculo(datos):
    """
    Simula un diagnóstico basado en los datos del vehículo.
    """
    if datos["kilometraje"] > 200000:
        return "Revisión urgente: Alto kilometraje detectado."
    elif datos["año"] < 2010:
        return "Revisión recomendada: Vehículo antiguo."
    else:
        return "Vehículo en condiciones aceptables."


def manejar_cliente(conexion, direccion):
    """
    Maneja la conexión con un cliente individual.
    """
    print(f"[SERVIDOR] Conectado con {direccion}")

    try:
        # Recibir datos del cliente
        datos = conexion.recv(4096).decode()
        datos_vehiculo = json.loads(datos)
        print(f"[SERVIDOR] Datos recibidos de {direccion}: {datos_vehiculo}")

        # Diagnóstico
        resultado = diagnosticar_vehiculo(datos_vehiculo)

        # Enviar resultado al cliente
        conexion.send(resultado.encode())

    except json.JSONDecodeError:
        conexion.send("Error: Formato JSON inválido.".encode())
    except Exception as e:
        print(f"[ERROR] Ocurrió un error con el cliente {direccion}: {e}")
    finally:
        # Cerrar la conexión
        conexion.close()
        print(f"[SERVIDOR] Conexión cerrada con {direccion}")


def iniciar_servidor(host='localhost', puerto=12345):
    """
    Inicia el servidor que acepta múltiples clientes usando hilos.
    """
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, puerto))
    servidor.listen(5)

    print(f"[SERVIDOR] Servidor en ejecución en {host}:{puerto}")

    while True:
        conexion, direccion = servidor.accept()
        # Crear un hilo para manejar al nuevo cliente
        hilo_cliente = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
        hilo_cliente.start()
        print(f"[SERVIDOR] Cliente {direccion} atendido en hilo separado.")


if __name__ == "__main__":
    iniciar_servidor()
