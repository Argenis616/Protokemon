import socket 

print "Tutorial 53: Cliente"

host = "10.42.0.185"
port = 9999
socket1 = socket.socket()
socket1.connect((host,port))
oracion = raw_input("Ingrese una oracion: ")
socket1.send(oracion)
num = socket1.recv(1024)
print "la oracion", oracion, "tienen caracteres:", num
tiempo = raw_input("Presione enter para terminar...")

socket1.close()