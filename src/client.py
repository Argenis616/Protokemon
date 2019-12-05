import socket 
from struct import pack

TRAINER_CHOOSE = 11
CAPTURE_POKEMON = 10
CHOOSE_POKEMON = 20
CAPTURE_AGAIN_POKEMON = 21
SEND_POKEMON_IMG = 22
NUMBER_ATTEMP =  23
CHOOSE_YES = 30 
CHOOSE_NO = 31
SESSION_FINISH = 32
def bytes_2_int(byte_repr):
    return int.from_bytes(byte_repr, byteorder='little', signed=True)

host = "localhost"
port = 9999
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(5)
try:
    socket1.connect((host,port))
    print ("\n" +"""
                                          ,'\
            _.----.        ____         ,'  _\   ___    ___     ____
        _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
        \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
         \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
           \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
            \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
             \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
              \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
               \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
                \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                        `'                            '-._|
        """)
    print ("Bienvenido!!")
    trainers = socket1.recv(1024)
    print (trainers.decode("utf-8"))
    trainer_elegido = input("Elige tu entrenador").strip()
    if trainer_elegido != "0":
        socket1.send(bytes(trainer_elegido.encode()))
        socket1.send(pack("i",TRAINER_CHOOSE))

        respuesta = socket1.recv(1024)
        print (respuesta.decode("utf-8"))
    else:
        print ("Vuelve pronto!")
        socket1.close()
    
    #socket1.sendall()
    #print (pack('i',CHOOSE_YES))
        
    
        
    
finally:
    socket1.close()