Test Procedure 1: Basic Behaviour of Application
	1. In the python-transfer-protocol folder, open/type "python3 main.py"
	2. In another window, type the same command to open another instance.
	3. In the first instance, select "Listen for Connection" and choose a port to listen to
	3a. Press listen. It should bring up a loading screen.
	4. In the second instance, select "Connect to IP address" and choose an IP and Port.
	4a. Press connect, it should automatically connect if there is a listener.
	4b. For testing, please select localhost and the same port address.
	5. If connection is complete, both windows should have a new interface.
	6. Your folders in the /root/sptp directory should be showing.

Test Procedure 2: Unusual Input in Application
	1. Open the application.
	2. Select the "Listen to connection" option
	3. In the port address, type a non-numerical input
	4. It is likely that the application will crash and an error message be shown:

"Traceback (most recent call last):
File "/home/qwutony/Python/python-transfer-protocol/application.py", line 211, in create_main_panel_listen
self.listener = Network.Listener(self.l_input.text())
File "/home/qwutony/Python/python-transfer-protocol/network.py", line 85, in __init__
self.socket.bind(('0.0.0.0', int(port)))
ValueError: invalid literal for int() with base 10: 'dfngjkd'
Aborted"

Test Procedure 3: Unusual Input in Application
	1. Open the application.
	2. Select the "Connect to IP Address"
	3. Instead of a numerical input, type non-numerical characters in the IP and Port.
	3a. Alternatively, type nothing and press connect.
	3b. Alternatively, connect without a listener.
	4. Click connect.
	5. It is likely that there will be problems with the application:

For connection without listener:
Traceback (most recent call last):
  File "/home/qwutony/Python/python-transfer-protocol/application.py", line 296, in tick
    self.connection.try_connect()
  File "/home/qwutony/Python/python-transfer-protocol/network.py", line 41, in try_connect
    self.socket.connect((self.host, int(self.port)))
ConnectionRefusedError: [Errno 111] Connection refused
Aborted

For connection with non-numerical characters:
Traceback (most recent call last):
  File "/home/qwutony/Python/python-transfer-protocol/application.py", line 167, in create_main_panel_connect
    self.connection = Network.Connection(self.c_input_host.text(), self.c_input_port.text())
  File "/home/qwutony/Python/python-transfer-protocol/network.py", line 29, in __init__
    self.try_connect()
  File "/home/qwutony/Python/python-transfer-protocol/network.py", line 41, in try_connect
    self.socket.connect((self.host, int(self.port)))
ValueError: invalid literal for int() with base 10: 'sdjkfnsdkjg'
Aborted

