#!/usr/bin/env python3

from rpyc_classic import *
from writeable_device import *

class AirConditioner(WriteableDevice):
    def get_name(self):
        return 'Air Conditioner'

    def get_label(self):
        return 'The current temperature settings:'

my_device = AirConditioner()
my_device.write('20')

ClassicServer.host = '127.0.0.3'
ClassicServer.run()

