import network
import time

apif =  network.WLAN(network.AP_IF) 
staif = network.WLAN(network.STA_IF)


apif.active(False)
staif.active(False)
time.sleep(1)
apif.active(True)
staif.active(True)

apif.config(essid="ESPAX")
apif.config(password="12345678") 
#apif.ifconfig( ( self.config["webserver"], self.config["netmask"], self.config["gateway"], self.config["dns"] ) )