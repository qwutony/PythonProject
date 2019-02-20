#!/bin/bash

scp bot.py localhost:/tmp/

ssh qwutony@localhost "nohup python3 /tmp/bot.py &>/dev/null 2>&1 &"
