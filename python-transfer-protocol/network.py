# The network file that establishes a connection between client-server
# In peer to peer relationship

# Imports
import select
import socket

class Network():
    class Connection():
    def __init__(self, socket)
        self.socket = socket

     def connect(self):
            pass

    def send(self, bytes):
        self.socket.send(bytes)

    def try_receive(self):
        (inputs_ready, dontcare, dontcare) = select.select([self.socket], [], [], 0)
            if len(inputs_ready) == 0:
                return None
            return self.socket.recv(1024)

    class Listener():
        def __init__(self, host="0.0.0.0", port):
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((host, port))
            self.socket.listen()

        def try_connect(socket):
            (input_ready, output_ready, except_ready) = select.select(self.socket, [], [])

            if len(inputs_ready) == 0:
                    return None

            (client_sock, client_addr) = self.socket.accept()

            return Network.Connection(client_sock)