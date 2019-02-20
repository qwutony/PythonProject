# Concept

`bot.py` is installed on the victim machine. Every so often, it wakes up
and does a standard HTTP request to a server machine. The server replies
with a file containing one instruction and an optional payload. If the
client has anything to reply with, it sends a POST request otherwise
goes back to sleep.

Note: for Window OS, use `bot.exe` instead.

# Files

`test_server.py` and `command.txt` are files running on the server
(attacker) machine.

`bot.py` is a script intended to be run on the client (victim) machine.

# Command codes

See bot.py for command codes and their meaning. For example,

    write
    test.txt
    These are the contents

can be put into `command.txt`.

# Installation script

`setup.sh` and `install.sh` are both scripts that can be executed on
a victim's machine to get them to download the `bot.py` file and execute it

# TODO

* An uninstall script added to the bot
