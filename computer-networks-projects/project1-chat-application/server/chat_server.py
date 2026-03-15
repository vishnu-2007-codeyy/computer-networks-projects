import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = {}
lock = threading.Lock()


def broadcast(message, sender=None):
    with lock:
        for client in clients:
            if client != sender:
                try:
                    client.send(message.encode())
                except:
                    remove_client(client)


def remove_client(client):
    with lock:
        username = clients.get(client)

        if username:
            print(username, "disconnected")
            del clients[client]

            broadcast(f"SERVER: {username} left chat")


def handle_client(client):

    try:
        username = client.recv(1024).decode()

        with lock:
            clients[client] = username

        broadcast(f"SERVER: {username} joined chat")

        while True:

            msg = client.recv(1024).decode()

            if not msg:
                break

            message = f"{username}: {msg}"

            print(message)

            broadcast(message, client)

    except:
        pass

    finally:
        remove_client(client)
        client.close()


def start():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))

    server.listen()

    print("Server running on port", PORT)

    while True:

        client, addr = server.accept()

        print("Connected:", addr)

        thread = threading.Thread(target=handle_client, args=(client,))

        thread.start()


start()