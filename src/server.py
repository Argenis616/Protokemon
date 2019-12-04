import SocketServer

class MiTopHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.inicio = self.request.recv(1024)
        print("{} wrote:".format(self.client_address[0]))
        if self.inicio == "1":
            s = "Bienvenido"
            self.request.send(s)


def main():
    host = "localhost"
    port = 9999

    server1 = SocketServer.TCPServer((host,port), MiTopHandler)
    server1.serve_forever()


main()





            




