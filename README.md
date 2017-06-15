# Python-SEM-API-Client
This is a python-library for interfacing with the Smart-Energy-Manager-API.

## Description
This library makes it easy to interface with the [Smart Energy Manager](https://sems.energy). I currently use the "vX" version of the API.

## Requirements
* Python 2.7 (could work on Python 3 too - not tested)
* Requests-module

## Documentation

### Client-class
#### Importing the module
> ```python
> import SEMClient
>
> sem = SEMClient.Client("<IP-address of your sem>")  # new SEM-object
> ```
> This makes a new Client-object.

#### Get all Device-IDs
> ```python
> ids = sem.getDeviceIds()
> ```
> This function returns the IDs of all Devices in the SEMS-network as an array.
##### Example
> ```python
> ids = sem.getDeviceIds()
> print ids
> ```
> Output:
> ```
> [1, 2, 3, 4, 5, 6]
> ```

#### Get Device by ID
> ```python
> device = sem.getDevice(1)
> ```
> obj.getDevice(id) is a function that returns you the device with the ID given to it.
> It returns a ```Device```-object.

#### Get Device by name
> ```python
> device = sem.getDeviceByName("Smart Plug")
> ```

#### Get all Devices
> ```python
> devices = sem.getDevices()
> ```

#### Get a Value from a specific Device
> ```python
> device = sem.getDevice(1)
> deviceName = device.get("name")       # this prints the name of the Device with ID = 1
> ```

#### Get the Consumption
> ```python
> cons = sem.getConumption()
> ```

#### Get the Production
> ```python
> prod = sem.getProduction()
> ```

#### Get Meter-data
> ```python
> meterData = sem.getMeter()
> ```

### Device-class

#### Get specific Data-value
> ```python
> deviceName = device.get("name")
> ```
> This function returns the value of the given Field
