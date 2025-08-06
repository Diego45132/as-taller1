# Servidor
import socket

HOST = '127.0.0.1'  
PORT = 8080         

def manejar_peticion_http(peticion):
    """Procesa la petición HTTP y devuelve una respuesta simple."""
    lineas = peticion.split('\r\n')
    if not lineas:
        return respuesta_http_400()

    metodo, ruta, _ = lineas[0].split()

    if metodo != 'GET':
        return respuesta_http_405()

    
    if ruta == '/':
        return respuesta_http_200()
    else:
        return respuesta_http_404()

def respuesta_http_200():
    cuerpo = """
    <html>
        <head><title>Servidor HTTP</title></head>
        <body>
            <h1>¡Hola desde tu servidor HTTP en Python!</h1>
        </body>
    </html>
    """
    respuesta = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(cuerpo.encode('utf-8'))}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{cuerpo}"
    )
    return respuesta

def respuesta_http_404():
    cuerpo = "<h1>Error 404: Recurso no encontrado</h1>"
    return (
        "HTTP/1.1 404 Not Found\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(cuerpo)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{cuerpo}"
    )

def respuesta_http_400():
    cuerpo = "<h1>Error 400: Petición mal formada</h1>"
    return (
        "HTTP/1.1 400 Bad Request\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(cuerpo)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{cuerpo}"
    )

def respuesta_http_405():
    cuerpo = "<h1>Error 405: Método no permitido</h1>"
    return (
        "HTTP/1.1 405 Method Not Allowed\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(cuerpo)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{cuerpo}"
    )

def iniciar_servidor_http():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen(5)
        print(f"Servidor HTTP escuchando en http://{HOST}:{PORT}/")

        while True:
            cliente, direccion = servidor.accept()
            with cliente:
                peticion = cliente.recv(1024).decode('utf-8')
                print(f"Petición de {direccion}:\n{peticion}\n{'-'*40}")
                respuesta = manejar_peticion_http(peticion)
                cliente.sendall(respuesta.encode('utf-8'))

if __name__ == "__main__":
    iniciar_servidor_http()

