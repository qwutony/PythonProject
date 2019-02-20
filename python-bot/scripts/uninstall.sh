#!/bin/bash

kill $(pgrep -f 'python3 bot.py')
# else: pkill -f bot.py

rm -- $0