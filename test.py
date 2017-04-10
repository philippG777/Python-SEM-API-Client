import SEMClient

sem = SEMClient.Client("192.168.168.33")

print "device IDs"
print sem.getDeviceIds()

print "\ndevices"
print sem.getDevices()

print "\nbyName"
print sem.getDeviceByName("Smart Plug")

print "\nstatusFields"
print sem.getStatusFields()

print "\nstatusField:consumption"
print sem.getStatus("consumption")

print "\nConsumption"
print sem.getConsumption()

print "\ndevice with id = 1"
print sem.getDevice(1)