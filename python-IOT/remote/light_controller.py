#!/usr/bin/env python3

from rpyc_classic import *
from switch_device import *

class LightController(SwitchDevice):
    def get_name(self):
        return 'Light Controller (Lounge Room)'

    def get_label(self):
        return 'Turn on/off the light:'

my_device = LightController()
my_device.value = False

ClassicServer.host = '127.0.0.4'
ClassicServer.run()

