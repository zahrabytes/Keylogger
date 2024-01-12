
import socket
import pynput

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen(5)

while True: 
    clientSocket, address = s.accept()
    print(f"Connection established from address: {address}")
    message = input("Enter your message")
    clientSocket.send(bytes(message, "utf-8"))
    clientSocket.close()
