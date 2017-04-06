import SEMClient

sem = SEMClient.Client("192.168.168.33")

print sem.getDeviceIds()
print sem.getDevices()