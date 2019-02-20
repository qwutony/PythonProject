# Deploy Applications

**Create a software installation plan for the bot. It must:**

*1. outline THREE installation approaches for installation of the bot (approximately 100 words each)*

One: If there is already access to the remote machine, it is possible to create an apache or simple python server and allow the remote machine to download the malicious bot to the /tmp directory, which will most likely have RWT privileges. Then it is possible to install and execute the script there. There will be no necessity to create an installation script, as the process has already been accomplished through remote code access. This can be done either through a bind/reverse shell from an exploit that is already capitalised on the server, or by actual valid credential access from a pre-existing venture.

Two: It is also possible to use social engineering through a malicious email with a link that redirects the user to download the bot to their computer. A download server such as apache or python server will be initially established, that will allow any connection to automatically download the bot onto their server. An installation script can then be executed from their computer, which will install and execute the bot on the remote system. Alternatively, the malicious link can be used as a phishing method to retrive actual credentials, which can then be used to login and install the bot manually.

Three: The final option will be to take advantage of a pre-existing vulnerability on the system that allows for LFI/RFI/RCE, which will allow the servers to accept uploading of files onto the system, and then using a local file execution vulnerability to execute the file. This isn't the only method, as each different vulnerability has it's own strengths and weaknesses. For example, it is possible to upload a jpg file containing php shell code as a payload, it may also be possible to upload a file somewhere that can also be executed.

*2. determine ONE installation method to be used and create an ordered list of installation steps that a person with no technical expertise could follow (200 - 400 words)*

The objective is to create an installation method that can allow for the remote execution of the bot application. One installation method is the SSH installation method, where an attacker with a ssh credential of a server can execute an installation script to execute the bot, and then terminate the connection:

    1. Obtain the python-bot application folder. It is assumed that this step is already accomplished. Enter the folder.

    2. The folder should contain a "install.sh" file and a bot.py file, as well as other files which are irrelevant for now

    3. In the linux command line, type "./test_server.py". This will open a listener, which means your computer will be ready and waiting for a new connection.

    4. Open another terminal window.

    5. In the new terminal window, type ./install.sh. The script should prompt you to enter the ssh credentials of the remote server twice.

    6. After typing in the credentials twice, the script will automatically exit.

    7. Open the other window and see the bot script being executed. The installation script has been successfully implemented.

    8. If you wish to stop the test_server.py script from continuously running, simply press Ctrl+C to terminate the script.

    Note: It is possible to calibrate the script to allow it to be more efficient, such as giving it an uninstall command afterwards, which will automatically terminate the bot script as well.

*3. list the requirements for the client and server machines to run the bot (100 - 200 words)*

To run the bot, both client and server machines need to have a functional Linux operating system. They must also have ssh installed and the port open for connection. The attacker should also have the ssh credentials of the other machine, so that they can ssh into it. The ssh should also have the basic functionalities, such as the ability to copy and transfer files, and be able to allow ssh authentication and establish connection to execute the python script.

*4. outline of how at least TWO security features in a network can affect the installation of the bot (150 words each)*

Since the application is used to install a software, the antivirus may discover that the program is attempting to execute code and thus prevent it from being installed. Antivirus software is used to detect and remove computer viruses and other sorts of malware. This to a certain extent includes worms and bots that attempt to install or execute malicious software. Many antivirus softwares still use the signature based methods, which match a well known virus signature with the potential suspect file. Since the bot was self-programmed, no signature is available, and thus may easily bypass the security of the antivirus. However, there are new methods of antivirus detection, especially the non-signature based methods which can detect virus applications in the wild.

As the bot.py program attempts to communicate with my own server through the establishment of a connection, the firewall of the server may decide that it is risky and block the connection, thus making the bot unable to communicate back to the malicious server. A firewall is designed to either allow or disallow traffic to enter/leave the system.  The most prominent task for a firewall is to restrict the internet accessibility of some applications, thereby preventing unauthorised applications and malicious applications the ability to connect back to the malicious server, rendering it powerless. The bot that we created needs to establish a connection with our server before malicious code can be executed, and the install file must also connect back to download the bot. If the firewall succeeds, it will prevent the file from executing.

**Review the security requirements for the software installation plan you created in Instruction Step 1 for the bot host machine & control server, and determine if the client and server meet the requirements for installation by explaining how features of the client system may impact the operation of the bot (400 words).**

3. Create an installation script for the bot.

4. Create an uninstall script for the bot.

5. Arrange for your trainer to observe you:

 - testing your installation script in a test and production environment
 - testing your uninstall script in a test environment
 - configuring and testing a server to be aligned with an incident response plan process in terms of allocation of user accounts and privileges
 - deploying a database from a test environment to a production environment
 - specifying an appropriate configuration string for the database

6. Write a log which documents a security incident which you resolved by implementing your incident response plan. In the log you must (200 - 300 words):

 - describe the nature of the security incident
 - outline the measures taken to deal with the security incident
 - outline any future steps required to handle the security incident and sign off on these future steps