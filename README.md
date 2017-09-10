# MicroPython mrf522 Project

push mrf522 data to server

## Show
![image](https://)

## Installation
```install
$sudo pip install esptool
$sudo pip install adafruit-ampy
$wget https://github.com/xhsiung/microweb/blob/master/esp8266-custom-0.0.1.bin
$esptool.py --port /dev/ttyUSB0 erase_flash
$esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-mrf522-0.0.1.bin

```

CONFIG
```config
{
    "webserver":"192.168.4.2",
    "webport": 88,
    "netmask": "255.255.255.0",
    "gateway":"",
    "dns":"",

    "broker":"",
    "brkport": 0,
    "brkuser":"",
    "brkpasswd":"",
    "noapport": 1880,
    "topic":"",
    "device":"",
    "durationpub": 600,

    "apssid":"ESPAX",
    "appasswd":"",
    "stassid":"",
    "stapasswd":"",
    "ticktime": 500
}
```

## Usage

## Current status

Done  work:
* scan mrf522
* request server

## History

* **v1.0.0** : 2017-09-10
