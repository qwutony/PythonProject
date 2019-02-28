# Test Procedures for Internet of Things Python Application

***Test One: Successful Control of the IOT Application***

The IOT device can be successfully controlled through the console panel. This application is started using the command `python3 main.py` in the local directory of the python-IOT application. Once the application is opened, there should be a GUI connection panel with a default localhost IP address. When the hypothetical IOT is connected, the python script in the remote directory will execute, such as for the kitchen light there will be `python3 kitchen_light.py` executed. The test procedure will thus be as follows:

1. Navigate to the local directory and type `python3 main.py`.
2. In another console, navigate to the remote directory and type `python3 [script_name]`, where script name is the appliance that you want to connect.
3. The appliance script should have an output of something like this: "INFO:SLAVE/18812:server started on [127.0.0.X]:188", where X is any number. This indicates the script is listening.
4. In the main console GUI, type the IP address of the appliance and press "Link new device".
5. Once connected, the appliance GUI will show directly beneath the console.
6. The appliance (kitchen light for example) can be turned off and on. If the radio button "on" is selected, a message in the appliance console will say that the appliance is turning on.
7. Similarly, this works when the appliance is being turned off, or if another input is required.

The expected outcome is that the device can be controlled remotely via the control panel. If the button is pressed, the light in the kitchen of the household will be turned on. This coincides with our actual result, where pressing the button will allow the appliance panel to turn on. If we actually connect the execution of the script to a household appliance, it is likely that this application will work.

***Test Two: Use of the Drag and Drop functionality of the IOT Application***

Another behaviour of the IOT application is that having multiple panels can allow for drag and drop functionality to shift different appliance panels to suit the needs of the user.

1. Navigate to the local directory and type `python3 main.py`.
2. In another console, navigate to the remote directory and type `python3 [script_name]`, where script name is the appliance that you want to connect.
3. The appliance script should have an output of something like this: "INFO:SLAVE/18812:server started on [127.0.0.X]:188", where X is any number. This indicates the script is listening.
4. In the main console GUI, type the IP address of the appliance and press "Link new device".
5. Once connected, the appliance GUI will show directly beneath the console.
6. Repeat the steps until there are several appliances.
7. Place the cursor onto a appliance console, it should display that the console can be moved.
8. Move it to a chosen location and drop the console. The layout of the console should be changed in response to this movement.

The expected outcome is that any device console can be moved and shifted through the drag and drop technique. This is also reflective of the actual result, where it is possible to do so.