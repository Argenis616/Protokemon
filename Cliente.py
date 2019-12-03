'''
Created on 3 dic. 2019

@author: root
'''
import socket


def inicia_cliente(ip):
    mi_socket = socket.socket()
    mi_socket.connect((ip,9999))
    mi_socket.send("Hola desde el cliente")
    respuesta = mi_socket.recv(1024)
    print respuesta
    mi_socket.close()
    
if __name__ == "__main__":
    ip = "127.0.0.0"
    inicia_cliente(ip)