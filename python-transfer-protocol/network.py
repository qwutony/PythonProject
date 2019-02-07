# The network file that establishes a connection between client-server in peer to peer relationship

# Imports for this module
import select
import socket

class Listener():
    # Boilerplate code for creating a listening socket
    def __init__(self, port):
        # Created a socket that accepts IPv4 with a port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Socket options
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind and listen on localhost and designated port
        self.socket.bind(('0.0.0.0', port))
        self.socket.listen()

    