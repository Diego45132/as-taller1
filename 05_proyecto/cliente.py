# Cliente

import socket
import json
import threading


def enviar_datos_vehiculo(host='localhost', puerto=12345):
    """
    Solicita datos del vehículo al usuario y los envía al servidor.
    """
    
    datos_vehiculo = {
        "placa": input("📝 Placa del vehículo: "),
        "tipo": input("🚗 Tipo de vehículo (Carro/Moto/Camión): "),
        "año": int(input("📆 Año de fabricación: ")),
        "kilometraje": int(input("🛣️ Kilometraje (en km): "))
    }

    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    cliente.connect((host, puerto))

    
    cliente.send(json.dumps(datos_vehiculo).encode())

   
    respuesta = cliente.recv(4096).decode()
    
    print(f"\n✅ Diagnóstico recibido: {respuesta}")

    cliente.close()

if __name__ == "__main__":
    enviar_datos_vehiculo()
