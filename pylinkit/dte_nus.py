import logging
from threading import Event


logger = logging.getLogger(__name__)


NUS_CHAR_LENGTH = 20
NUS_RX_CHAR_UUID = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
NUS_TX_CHAR_UUID = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'


class DTENUS():
    def __init__(self, device):
        self._device = device
        self._event = Event()
        self._queued_data = ''
        device.subscribe(NUS_TX_CHAR_UUID, self._data_handler)

    def send(self, data, timeout=2.0, multi_response=False):
        self._queued_data = ''
        self._event.clear()
        for x in [ data[0+i:NUS_CHAR_LENGTH+i] for i in range(0, len(data), NUS_CHAR_LENGTH) ]:
            logger.debug('PC -> DTE: %s', x.encode('ascii'))
            self._device.char_write(NUS_RX_CHAR_UUID, x.encode('ascii'))
        while True:
            is_set = self._event.wait(timeout)
            if multi_response is False:
                if is_set:
                    break
                else:
                    raise Exception('Timeout')
            else:
                if not is_set:
                    break
        return self._queued_data

    def _data_handler(self, _, data):
        logger.debug('PC <- DTE: %s', data.decode('ascii'))
        self._queued_data += data.decode('ascii')
        if data and data[-1] == 0xd:
            self._event.set()
            self._event.clear()
