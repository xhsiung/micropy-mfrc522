import uos
import network
from flashbdev import bdev

def wifi():
    import ubinascii
    ap_if = network.WLAN(network.AP_IF)
    essid = b"MicroPython-%s" % ubinascii.hexlify(ap_if.config("mac")[-3:])
    ap_if.config(essid=essid, authmode=network.AUTH_WPA_WPA2_PSK, password=b"micropythoN")

def check_bootsec():
    buf = bytearray(bdev.SEC_SIZE)
    bdev.readblocks(0, buf)
    empty = True
    for b in buf:
        if b != 0xff:
            empty = False
            break
    if empty:
        return True
    fs_corrupted()

def fs_corrupted():
    import time
    while 1:
        print("""\
The FAT filesystem starting at sector %d with size %d sectors appears to
be corrupted. If you had important data there, you may want to make a flash
snapshot to try to recover it. Otherwise, perform factory reprogramming
of MicroPython firmware (completely erase flash, followed by firmware
programming).
""" % (bdev.START_SEC, bdev.blocks))
        time.sleep(3)

def setup():
    check_bootsec()
    print("Performing initial setup")
    wifi()
    uos.VfsFat.mkfs(bdev)
    vfs = uos.VfsFat(bdev)
    uos.mount(vfs, '/')
    with open("boot.py", "w") as f:
        f.write("""\
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
import network
apif =  network.WLAN(network.AP_IF) 
staif = network.WLAN(network.STA_IF)
apif.active(False)
staif.active(False)
gc.collect()
""")

    with open("main.py", "w") as f:
        f.write("""\
import os
import machine
import axapp
import axreadmfrc522

class Main(object):
    config = None
    server = None
    webroot = "/www"
    confbox = None 
    app = None
    gpio = None
    mqcli = None

    def __init__(self):
        super(Main, self).__init__()
        self.initApp()

    def initApp(self):
        self.app = axapp.App()
        self.config = self.app.getConf()
        self.app.apifConncet()
        self.app.staifConnect()

    def run(self):
        axreadmfrc522.do_read( self.config)

def main():
    m = Main() 
    m.run()
main()
""")
    return vfs
