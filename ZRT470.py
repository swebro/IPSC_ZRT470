#
# IPSC_ZRT470
# Copyright (C) 2018 Kristoffer Forss
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import serial
import threading

class ZRT470: 
    """Class for communication with ZRT470 transceiver"""
    def __init__(self, conf, mode):
        self.mode = mode
        if mode == "s":
            self.ser = serial.Serial(conf.simplexCOM, conf.simplexBAUD)
        elif mode == "rx":
            self.ser = serial.Serial(conf.rxCOM, conf.rxBAUD)
        elif mode == "tx":
            self.ser = serial.Serial(conf.txCOM, conf.txBAUD)
        else:
            self.ser = serial.Serial()
            
    def __del__(self)
        self.ser.close()
        
    def init():
        # TODO: Set frequency, baudrate etc. for the ZRT470
        
    def recieve_v():
        self.data = ser.read(33)
        self.busy = false
        
    def recieve():
        self.busy = true
        threading.Thread(target=recieve_v).start()
        
    def selfTest(ZRT470 )
