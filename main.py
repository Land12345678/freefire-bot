import socket
import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8080))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Bot running on port", PORT)

while True:
    conn, addr = s.accept()
    print("Connected:", addr)
    conn.send(b"Hello from Railway TCP bot\n")
    conn.close()
