import socket
import threading


class ChatClient:

    def __init__(self, host, port, username, callback):

        self.host = host
        self.port = port
        self.username = username
        self.callback = callback

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):

        self.sock.connect((self.host, self.port))

        self.sock.send(self.username.encode())

        thread = threading.Thread(target=self.receive)

        thread.daemon = True

        thread.start()

    def receive(self):

        while True:

            try:

                message = self.sock.recv(1024).decode()

                if message:
                    self.callback(message)

            except:
                break

    def send(self, message):

        try:
            self.sock.send(message.encode())

        except:
            pass