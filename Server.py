import socket
import threading

def handle_client(client_socket):
    name = client_socket.recv(1024).decode('utf-8')
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{name}: {message}")
            
            # Broadcast the message to all clients
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(f"{name}: {message}".encode('utf-8'))
                    except:
                        clients.remove(client)
        except:
            break

    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)

clients = []

print("Server listening on port 12345")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    print(f"Connection from {addr[0]}:{addr[1]}")
    
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
