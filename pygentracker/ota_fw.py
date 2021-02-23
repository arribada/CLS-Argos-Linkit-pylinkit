import pygatt   # noqa

class OTAFW():
    def __init__(self, device):
        self._device = device

    def send_update_file(self, file_id, data):
        #self._update_start(file_id)
        #self._send_data(data)
        pass
