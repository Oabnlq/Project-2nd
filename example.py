# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:34:26 2018

@author: baonlq.97
"""

from pulsesensor import Pulsesensor
import time

p = Pulsesensor()
p.startAsyncBPM()

try:
    while True:
        bpm = p.BPM
        if bpm > 0:
            print("BPM: %d" % bpm)
        else:
            print("No Heartbeat found")
        time.sleep(1)
except:
    p.stopAsyncBPM()