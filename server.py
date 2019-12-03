import SocketServer

class MiTopHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.oracion = self.request.recv(1024).strip()
        self.num = len(self.oracion)
        print "La oracion recv es ", self.oracion, "el num de char ", self.num
        self.request.send(str(self.num))



def main():
    print "Servidores"
    host = "localhost"
    port = 9999

    server1 = SocketServer.TCPServer((host,port), MiTopHandler)
    print "Server corriendo"
    server1.serve_forever()


main()





            




