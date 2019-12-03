'''
Created on 3 dic. 2019

@author: root
'''
import socket


def inicia_servidor():
    mi_socket = socket.socket()
    mi_socket.bind(('localhost',9999))
    mi_socket.listen(5)
    
    
    while True:
        conexion,addr = mi_socket.accept()
        print "Nueva Conexión"
        print addr
        
        conexion.send("Hey!!")
        conexion.close()

if __name__ == "main":
    inicia_servidor()