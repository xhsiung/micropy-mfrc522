# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import network
import gc
#import webrepl
#webrepl.start()
apif =  network.WLAN(network.AP_IF) 
staif = network.WLAN(network.STA_IF)
apif.active(False)
staif.active(False)
gc.collect()
