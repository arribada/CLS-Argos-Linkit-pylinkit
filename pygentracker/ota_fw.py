import struct
from threading import Event

OTA_CHAR_LENGTH = 20
OTA_BASE_ADDR_CHAR_UUID = '0000FE22-CC7A-482A-984A-7F2ED5B3E58F'
OTA_STATUS_CHAR_UUID = '0000FE23-CC7A-482A-984A-7F2ED5B3E58F'
OTA_RAW_DATA_UUID = '0000FE24-CC7A-482A-984A-7F2ED5B3E58F'

ACTION_START = 1
ACTION_DONE = 7
ACTION_ABORT = 8


class OTAFW():
    def __init__(self, device):
        self._device = device
        self._event = Event()
        self._status = 0
        device.subscribe(OTA_STATUS_CHAR_UUID, self._status_handler)

    def send_update_file(self, file_id, data, timeout=5.0):
        action = ACTION_START | file_id << 8
        self._event.clear()
        self._device.char_write(OTA_BASE_ADDR_CHAR_UUID, struct.pack('<I', action))
        is_set = self._event.wait(timeout)
        total_length = len(data)
        count = 0
        if is_set is False:
            raise Exception('Time out waiting for START handshake')
        for x in [ data[0+i:OTA_CHAR_LENGTH+i] for i in range(0, len(data), OTA_CHAR_LENGTH) ]:
            print(count, '/', total_length, end = '\r')
            self._device.char_write(OTA_RAW_DATA_UUID, x)
            count += len(x)
            if self._status:
                print('Aborted remotely')
                self._device.char_write(OTA_BASE_ADDR_CHAR_UUID, struct.pack('<I', ACTION_ABORT))
                return
        self._device.char_write(OTA_BASE_ADDR_CHAR_UUID, struct.pack('<I', ACTION_DONE))
        is_set = self._event.wait(timeout)
        if is_set is False:
            raise Exception('Time out waiting for STATUS handshake')
        if (self._status == 0):
            print('Image transfer ACK')
        else:
            print('Image transfer NACK')

    def _status_handler(self, _, data):
        self._status = int(data[0])
        self._event.set()
