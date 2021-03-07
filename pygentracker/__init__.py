from .ble import BLEDevice
from .dte import DTE
from .ota_fw import OTAFW

class GenTracker():
    def __init__(self, address):
        self._device = BLEDevice()
        self._device.connect(address, 5)
        self._dte = DTE(self._device)
        self._otafw = OTAFW(self._device)
        self._map = {}

    def sync(self):
        a = self._dte.parmr()
        b = self._dte.statr()
        self._map = { **a, **b }

    def set(self, param_values):
        self._dte.parmw(param_values=param_values)

    def get(self, attr=None):
        return self._map[attr] if attr else self._map

    def get_attrs(self):
        return self._map.keys()

    def firmware_update(self, data, file_id=0):
        self._otafw.send_update_file(file_id, data)

    def paspw(self, json_file_data):
        self._dte.paspw(json_file_data)

    def zonew(self, zone_dict):
        self._dte.zonew(zone_dict)

    def zoner(self, zone_id=1):
        return self._dte.zoner(zone_id)

    def dumpd(self, log_type):
        return self._dte.dumpd(log_type)

    def factw(self):
        self._dte.factw()

    def rstvw(self):
        self._dte.rstvw()

    def rstbw(self):
        self._dte.rstbw()
