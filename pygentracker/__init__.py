import pygatt    # noqa
from .dte import DTE
from .ota_fw import OTAFW


class GenTracker():
    def __init__(self, address):
        self._backend = pygatt.GATTToolBackend()
        self._backend.start()
        self._backend.reset()
        self._device = self._backend.connect(address, address_type=pygatt.BLEAddressType.random)
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

    def dumpd(self, log_type):
        return self._dte.dumpd(log_type)

    def factw(self):
        self._dte.factw()

    def rstvw(self):
        self._dte.rstvw()

    def rstbw(self):
        self._dte.rstbw()
