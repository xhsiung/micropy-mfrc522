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
