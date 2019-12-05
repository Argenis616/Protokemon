import socketserver
from model.poke_base import get_trainers

CAPTURE_POKEMON = 10
CHOOSE_POKEMON = 20
CAPTURE_AGAIN_POKEMON = 21
SEND_POKEMON_IMG = 22
NUMBER_ATTEMP =  23
CHOOSE_YES = 30 
CHOOSE_NO = 31
SESSION_FINISH = 32
TRAINER_CHOOSE = 11
def bytes_2_int(byte_repr):
    return int.from_bytes(byte_repr, byteorder='little', signed=True)

def select_pokemon(self):
    self.request.sendall(bytes("Hola si hago lo que quieres","utf-8"))
class MiTopHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.trainers = get_trainers()
        self.request.sendall(bytes(self.trainers,"utf-8"))
        self.trainer = self.request.recv(1)
        self.inicio = self.request.recv(1)
        print (self.trainer.decode())
        print (bytes_2_int(self.inicio))
        if bytes_2_int(self.inicio) == TRAINER_CHOOSE:
            select_pokemon(self)
        
def main():
    host = "localhost"
    port = 9999

    server1 = socketserver.TCPServer((host,port), MiTopHandler)
    server1.serve_forever()


main()





            




