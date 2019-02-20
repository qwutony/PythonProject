#!/usr/bin/env python3

from rpyc_classic import *
from switch_device import *

class KitchenLight(SwitchDevice):
    def get_name(self):
        return 'Light Controller (Kitchen)'

    def get_label(self):
        return 'Toggle light on/off:'

my_device = KitchenLight()
my_device.value = False

ClassicServer.host = '127.0.0.5'
ClassicServer.run()
