import struct, time
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

    def send_update_file(self, file_id, data):
        action = ACTION_START | file_id << 8
        self._event.clear()
        self._device.char_write(OTA_BASE_ADDR_CHAR_UUID, struct.pack('<I', action))
        print('Waiting for device to ACK our START request')
        is_set = self._event.wait(15.0)
        total_length = len(data)
        count = 0
        if is_set is False:
            raise Exception('Time out waiting for START handshake')
        print('Received ACK, sending data....')
        for x in [ data[0+i:OTA_CHAR_LENGTH+i] for i in range(0, len(data), OTA_CHAR_LENGTH) ]:
            self._device.char_write(OTA_RAW_DATA_UUID, x)
            count += len(x)
            print(count, '/', total_length, end = '\r')
            if self._status:
                print('Aborted remotely')
                self._device.char_write(OTA_BASE_ADDR_CHAR_UUID, struct.pack('<I', ACTION_ABORT))
                return
        self._device.char_write(OTA_BASE_ADDR_CHAR_UUID, struct.pack('<I', ACTION_DONE))
        print('Data has been submitted...')
        print('Waiting for image transfer ACK...this may take some time...CTRL-C to abort')
        is_set = self._event.wait(5*60)
        if is_set is False:
            raise Exception('Time out waiting for STATUS handshake')
        if (self._status == 0):
            print('Image transfer ACK')
            time.sleep(3)  # Allow time for procedure to clean up
        else:
            print('Image transfer NACK')

    def _status_handler(self, _, data):
        self._status = int(data[0])
        self._event.set()
        self._event.clear()
