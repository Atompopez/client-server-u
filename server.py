import socket
import threading

# Configuración del servidor
HOST = '192......'  # Dirección IP del servidor
PORT = 3002        # Puerto en el que escuchará el servidor

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Almacena referencias a clientes
clientes = []

# Función para manejar la comunicación con un cliente
def handle_client(client_socket):
    while True:
        try:
            mensaje = client_socket.recv(1024)
            for cliente in clientes:
                cliente.send(mensaje)
        except:
            # Si hay un error, el cliente se desconecta
            clientes.remove(client_socket)
            client_socket.close()

# Aceptar conexiones de clientes
while True:
    client_socket, addr = server_socket.accept()
    clientes.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()