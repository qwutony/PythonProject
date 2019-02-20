# Concept

`main.py` executed to create a interactive GUI panel that can either 
connect or listen for connections. 

# Files

`network.py` is responsible for the connection and listening of sockets
on the machine and `application.py` is used for creating the interface.

`main.py` is a script intended to be run on the client and server machine.

# Further Instructions

Connect to IP Address:
Connect to an existing listener
Requires input of target IP address and port
If connected, a new panel will open

Listen for connection:
Await for another application to connect
Requires input of listening port

If connected, a new panel will open
Application Interface (after connected):
Left Panel: Local /root/sptp files/folder
Right Panel: Remote /root/sptp files/folder
