import socket
import pynput

from pynput.keyboard import Key, Listener

def on_press(key):
    print(f"{key} pressed")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 6060))

message = s.recv(2048)

print(f"Message received: {message}")