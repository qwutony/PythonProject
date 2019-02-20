#!/usr/bin/env python3

from rpyc_classic import *
from switch_device import *

class GarageDoor(SwitchDevice):
    def get_name(self):
        return 'Garage Door'

    def get_label(self):
        return 'Current state:'

    def get_on_label(self):
        return 'Open'

    def get_off_label(self):
        return 'Closed'

    def turn_on(self):
        print('opening door')
        self.value = True

    def turn_off(self):
        print('closing door')
        self.value = False

my_device = GarageDoor()
my_device.value = False

ClassicServer.host = '127.0.0.2'
ClassicServer.run()

