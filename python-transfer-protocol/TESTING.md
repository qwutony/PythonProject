***Test Procedure 1: Basic Behaviour of Application***
1. In the python-transfer-protocol folder, open/type "python3 main.py"
2. In another window, type the same command to open another instance.
3. In the first instance, select "Listen for Connection" and choose a port to listen to
4. Press listen. It should bring up a loading screen.
5. In the second instance, select "Connect to IP address" and choose an IP and Port.
6. Press connect, it should automatically connect if there is a listener.
7. For testing, please select localhost and the same port address.
8. If connection is complete, both windows should have a new interface.
9. Your folders in the /root/sptp directory should be showing.

Upon execution of this test, the application successfully connected to another instance of itself. 
There are not issues with the application when run following the instructions outlined above.

***Test Procedure 2: Unusual Input in Application***
1. Open the application.
2. Select the "Listen to connection" option
3. In the port address, type a non-numerical input
4. It is likely that the application will crash and an error message be shown:

The result:
"Traceback (most recent call last):
File "/home/qwutony/Python/python-transfer-protocol/application.py", line 211, in create_main_panel_listen
self.listener = Network.Listener(self.l_input.text())
File "/home/qwutony/Python/python-transfer-protocol/network.py", line 85, in __init__
self.socket.bind(('0.0.0.0', int(port)))
ValueError: invalid literal for int() with base 10: 'dfngjkd'
Aborted"

The test resulted in the application breaking. This is because it did not expect a literal character inserted into the port parameter.
To improve the product it is necessary to sanitise the input to prevent non-numerical input.

***Test Procedure 3: Unusual Input in Application***
1. Open the application.
2. Select the "Connect to IP Address"
3. Instead of a numerical input, type non-numerical characters in the IP and Port.
4. Alternatively, type nothing and press connect.
5. Alternatively, connect without a listener.
6. Click connect.
7. It is likely that there will be problems with the application:

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

These tests all resulted in the application breaking. The literal characters once again broke the application because it expected an integer.
Furthermore, the application broke when connecting to an address that does not have a listener. This terminated the application as expected.
To make the product more viable, it should result in an error, rather than breaking.
