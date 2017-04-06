#!/usr/bin/python
# coding: utf8
import requests

__version__ = "0.1"

class Client(object):
    apiVersion = "vX"   # test-version??
    def __init__(self, ip):
        self.ip = ip
        self.apiAddress = "http://" + ip + "/api/" + self.apiVersion
    
    def getDeviceIds(self):
        req = requests.get(self.apiAddress + "/device")
        return (req.json())["deviceIds"]
    

    def getDevice(self, id):
        req = requests.get(self.apiAddress + "/device/" + str(id))
        return req.json()

    def getDevices(self):
        deviceIds = self.getDeviceIds()
        devices = {}
        for id in deviceIds:
            device = self.getDevice(id)
            devices[id] = device
        
        return devices
