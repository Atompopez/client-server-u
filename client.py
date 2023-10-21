import socket
import threading

# Configuración del cliente
HOST = '192......'  # Dirección IP del servidor
PORT = 3002        # Puerto en el que está escuchando el servidor

# Crear un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Función para enviar mensajes al servidor
def send_message():
    while True:
        mensaje = input()
        client_socket.send(mensaje.encode())

# Función para recibir mensajes del servidor
def receive_messages():
    while True:
        mensaje = client_socket.recv(1024).decode()
        print(mensaje)

# Iniciar subprocesos para enviar y recibir mensajes
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_messages)
send_thread.start()
receive_thread.start()