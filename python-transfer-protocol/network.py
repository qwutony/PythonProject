import socket
import select

# Define the superclass Network
class Network():
    # Create Connection class
    class Connection():
        """Encapsulates a connection to a remote host"""

        def __init__(self, host = None, port = None, socket_ = None):
            """Initiatialisation of Connection class, requiring inputs of host, port and socket"""

            # Connect a socket if one exists
            if socket_ is not None:
                self.socket = socket_
                self.connected = True

            # Allocate host and port, and create a new socket
            elif host is not None:
                self.host = host
                self.port = port

                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.setblocking(0)

                self.try_connect()
                self.connected = False

            # Error handler
            else:
                raise TypeError()

        def try_connect(self):
            """Tries to connect to the host and port specified in the constructor
            and sets self.connected to True if successful"""

            try:
                self.socket.connect((self.host, int(self.port)))
                self.connected = True
            except BlockingIOError as e:
                pass

        # Send encrypted information through the socket
        def send(self, plaintext_bytes):
            """Sends some encrypted data (a bytes object) to the other host"""
            encrypted_bytes = []
            key = 77

            for byte in plaintext_bytes:
                encrypted_bytes.append(byte ^ key)

            encrypted_bytes = bytes(encrypted_bytes)
            
            self.socket.send(encrypted_bytes)

        # Receive encrypted data from socket and unencrypts it
        def try_receive(self):
            """Recieves and returns some data (a bytes object) from the other host"""

            (inputs_ready, dontcare, dontcare) = select.select([self.socket], [], [], 0)

            if len(inputs_ready) == 0:
                return None

            decrypted_bytes = []
            encrypted_bytes = self.socket.recv(1024)

            for byte in encrypted_bytes:
                decrypted_bytes.append(byte ^ 77)

            decrypted_bytes = bytes(decrypted_bytes)

            return decrypted_bytes

    class Listener():
        """Encapsulates a listener that awaits for connections"""
        def __init__(self, port):
            """Create a listening socket that is bound to a local port and listen"""

            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(('0.0.0.0', int(port)))
            self.socket.listen()

        # Tries to connect to socket, accept or else None
        def try_get_connection(self):
            """Tries to get an incoming Connection, returning it or None"""

            (inputs_ready, dontcare, dontcare) = select.select([self.socket], [], [], 0)

            if len(inputs_ready) == 0:
                return None

            (client_socket, dontcare) = self.socket.accept()

            return Network.Connection(socket_ = client_socket)