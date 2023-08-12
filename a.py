import json
from dataclasses import dataclass
from typing import Any


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Device):
            return {'_type': 'Device', 'value': o.__dict__}  # (*)
        return json.JSONEncoder.default(self, o)


class Device:

    def __init__(self, deviceId, version):
        self.deviceId = deviceId
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> str(obj.get("deviceId")):
        _deviceId = str(obj.get("deviceId"))
        _version = str(obj.get("version"))
        return A(_deviceId, _version)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)


device1 = Device("a", "b")
device2 = Device("b", "c")

devices = [device1, device2]

deviceByDeviceId = {devices[i].deviceId: devices[i] for i in range(0, len(devices), 2)}

# jsonObject = json.dumps(deviceByDeviceId, indent=2)
print(json.dumps(device1.__dict__, indent=2))


# print(jsonObject)


@dataclass
class A:
    deviceId: str
    version: str

    @staticmethod
    def from_dict(obj: Any) -> 'A':
        _deviceId = str(obj.get("deviceId"))
        _version = str(obj.get("version"))
        return A(_deviceId, _version)


@dataclass
class Root:
    object: Object

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _object = Object.from_dict(obj.get("object"))
        return Root(_object)
