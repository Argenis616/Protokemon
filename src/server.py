import SocketServer
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

class MiTopHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        '''
        self.trainers = get_trainers()
        self.request.send(str(self.trainers))
        self.inicio = self.request.recv(1)
        print self.inicio
        '''
        i = self.request.recv(1)
        print (i) 
        
    
def main():
    host = "localhost"
    port = 9999

    server1 = SocketServer.TCPServer((host,port), MiTopHandler)
    server1.serve_forever()


main()





            




