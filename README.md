# Python-SEM-API-Client
This is a python-library for interfacing with the Smart-Energy-Manager-API.

## Description
This library makes it easy to interface with the [Smart Energy Manager](https://sems.energy). I currently use the "vX" version of the API.

## Requirements
* Python 2.7 (could work on Python 3 too - not tested)
* Requests-module

## Documentation

### Importing the module
```python
import SEMClient

sem = SEMClient.Client("<IP-address of your sem>")
```
