import tkinter as tk
from tkinter import scrolledtext
from chat_client import ChatClient
import datetime


class ChatGUI:

    def __init__(self, root):

        self.root = root

        root.title("Chat Application")

        frame = tk.Frame(root)

        frame.pack()

        tk.Label(frame, text="IP").grid(row=0, column=0)

        self.ip = tk.Entry(frame)

        self.ip.insert(0, "127.0.0.1")

        self.ip.grid(row=0, column=1)

        tk.Label(frame, text="Port").grid(row=0, column=2)

        self.port = tk.Entry(frame)

        self.port.insert(0, "5000")

        self.port.grid(row=0, column=3)

        tk.Label(frame, text="Username").grid(row=0, column=4)

        self.username = tk.Entry(frame)

        self.username.grid(row=0, column=5)

        tk.Button(frame, text="Connect", command=self.connect).grid(row=0, column=6)

        self.chat = scrolledtext.ScrolledText(root)

        self.chat.pack()

        self.chat.config(state="disabled")

        bottom = tk.Frame(root)

        bottom.pack()

        self.msg = tk.Entry(bottom, width=50)

        self.msg.pack(side=tk.LEFT)

        tk.Button(bottom, text="Send", command=self.send).pack(side=tk.LEFT)

    def connect(self):

        self.client = ChatClient(

            self.ip.get(),

            int(self.port.get()),

            self.username.get(),

            self.display

        )

        self.client.connect()

    def send(self):

        message = self.msg.get()

        if message:

            self.client.send(message)

            self.msg.delete(0, tk.END)

    def display(self, message):

        time = datetime.datetime.now().strftime("%H:%M:%S")

        self.chat.config(state="normal")

        self.chat.insert(tk.END, f"[{time}] {message}\n")

        self.chat.config(state="disabled")

        self.chat.yview(tk.END)


root = tk.Tk()

ChatGUI(root)

root.mainloop()