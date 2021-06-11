import base64
import json
import binascii
import logging
import struct


logger = logging.getLogger(__name__)


class BOOLEAN():
    @staticmethod
    def encode(value):
        return '1' if int(value) else '0'

    @staticmethod
    def decode(value):
        return 1 if int(value) else 0


class UINT():
    @staticmethod
    def encode(value):
        return str(int(value))

    @staticmethod
    def decode(value):
        return int(value)


class FLOAT():
    @staticmethod
    def encode(value):
        return str(float(value))

    @staticmethod
    def decode(value):
        return float(value)


class DECIMAL(UINT):
    pass


class TEXT():
    @staticmethod
    def encode(value):
        return value

    @staticmethod
    def decode(value):
        return value


class ARGOSDUTYCYLE():
    @staticmethod
    def encode(value):
        return str(int(value, 16))

    @staticmethod
    def decode(value):
        return '{:06X}'.format(int(value))


class DATESTRING():
    @staticmethod
    def encode(value):
        return value

    @staticmethod
    def decode(value):
        return value


class BASE64():
    @staticmethod
    def encode(value):
        return base64.b64encode(value)

    @staticmethod
    def decode(value):
        return base64.b64decode(value)


class ARGOSFREQ():
    ARGOS_FREQUENCY_OFFSET = 4016200
    ARGOS_FREQUENCY_MULT = 10000

    @staticmethod
    def encode(value):
        return str(int((float(value) * ARGOSFREQ.ARGOS_FREQUENCY_MULT) - ARGOSFREQ.ARGOS_FREQUENCY_OFFSET))

    @staticmethod
    def decode(value):
        return (float(value) + ARGOSFREQ.ARGOS_FREQUENCY_OFFSET) / ARGOSFREQ.ARGOS_FREQUENCY_MULT


class ARGOSPOWER():
    allowed = [-1, 3, 4, 200, 500]

    @staticmethod
    def encode(value):
        return str(ARGOSPOWER.allowed.index(int(value)))

    @staticmethod
    def decode(value):
        return ARGOSPOWER.allowed[int(value)]


class ARGOSMODE():
    allowed = ['OFF', 'PASS_PREDICTION', 'LEGACY', 'DUTY_CYCLE']

    @staticmethod
    def encode(value):
        return str(ARGOSMODE.allowed.index(value))

    @staticmethod
    def decode(value):
        return ARGOSMODE.allowed[int(value)]


class DEPTHPILE():
    allowed = [-1,1,2,3,4,-1,-1,-1,8,12,16,20,24]

    @staticmethod
    def encode(value):
        return str(DEPTHPILE.allowed.index(int(value)))

    @staticmethod
    def decode(value):
        return DEPTHPILE.allowed[int(value)]


class AQPERIOD():
    allowed = [-1,10,15,30,60,120,360,720,1440]

    @staticmethod
    def encode(value):
        return str(AQPERIOD.allowed.index(int(value)))

    @staticmethod
    def decode(value):
        return AQPERIOD.allowed[int(value)]


class GNSSFIXMODE():
    allowed = [-1, '2D', '3D', 'AUTO']

    @staticmethod
    def encode(value):
        return str(GNSSFIXMODE.allowed.index(value))

    @staticmethod
    def decode(value):
        return GNSSFIXMODE.allowed[int(value)]


class GNSSDYNMODEL():
    allowed = ['PORTABLE', -1, 'STATIONARY', 'PEDESTRIAN', 'AUTOMOTIVE', 'SEA', 'AIRBORNE_1G', 'AIRBORNE_2G', 'AIRBORNE_4G',
               'WRIST_WORN_WATCH', 'BIKE']

    @staticmethod
    def encode(value):
        return str(GNSSDYNMODEL.allowed.index(value))

    @staticmethod
    def decode(value):
        return GNSSDYNMODEL.allowed[int(value)]



class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Packer():

    def __init__(self, data):
        self._data = [int(x) for x in data]
        self._pack_pos = 0
        self._unpack_pos = 0

    def result(self):
        return bytearray(self._data)

    def extract_bits(self, total_bits):
        result = 0
        start = self._unpack_pos
        num_bits = total_bits
        in_byte_offset = int(start / 8)
        in_bit_offset = start % 8
        out_bit_offset = 0
        n_bits = min(8 - in_bit_offset, num_bits)

        while (num_bits):
            mask = 0xFF >> (8 - n_bits)
            result |= (((self._data[in_byte_offset] >> (8-in_bit_offset-n_bits)) & mask) << (total_bits - out_bit_offset - n_bits))
            out_bit_offset = out_bit_offset + n_bits
            in_bit_offset = in_bit_offset + n_bits
            if (in_bit_offset >= 8):
                in_byte_offset += 1
                in_bit_offset %= 8
            num_bits -= n_bits
            n_bits = min(8 - in_bit_offset, num_bits)
        self._unpack_pos += total_bits
        return result

    def pack_bits(self, value, total_bits):
        start = self._unpack_pos
        num_bits = total_bits
        out_byte_offset = int(start / 8)
        out_bit_offset = start % 8
        in_bit_offset = 0
        n_bits = min(8 - out_bit_offset, num_bits)

        while (num_bits):
            mask = (0xFFFFFFFF >> (total_bits - in_bit_offset - n_bits)) if ((total_bits - in_bit_offset) == 32) else (((1 << (total_bits - in_bit_offset))-1) >> (total_bits - in_bit_offset - n_bits))
            self._data[out_byte_offset] |= (((value >> (total_bits - in_bit_offset - n_bits)) & mask) << (8-out_bit_offset-n_bits))
            out_bit_offset = out_bit_offset + n_bits
            in_bit_offset = in_bit_offset + n_bits

            if (out_bit_offset >= 8):
                out_byte_offset += 1
                out_bit_offset = out_bit_offset % 8
            num_bits -= n_bits
            n_bits = min(8 - out_bit_offset, num_bits)

        self._unpack_pos += total_bits


class ZONE():

    @staticmethod
    def decode_arg_loc_argos(x):
        options = [-1, 7 * 60, 15 * 60, 30 * 60, 1 * 60 * 60, 2 * 60 * 60, 3 * 60 * 60, \
                    4 * 60 * 60, 6 * 60 * 60, 12 * 60 * 60, 24 * 60 * 60, -1, -1, -1, -1, 0]
        return options[x]

    @staticmethod
    def decode_comms_vector(x):
        options = ['UNCHANGED', 'ARGOS_PREFERRED', 'CELLULAR_PREFERRED']
        return options[x]

    @staticmethod
    def encode_comms_vector(x):
        options = ['UNCHANGED', 'ARGOS_PREFERRED', 'CELLULAR_PREFERRED']
        return options.index(x)

    @staticmethod
    def encode_depth_pile(x):
        return DEPTHPILE.encode(x)

    @staticmethod
    def encode_arg_loc_argos(x):
        options = [-1, 7 * 60, 15 * 60, 30 * 60, 1 * 60 * 60, 2 * 60 * 60, 3 * 60 * 60, \
                    4 * 60 * 60, 6 * 60 * 60, 12 * 60 * 60, 24 * 60 * 60, -1, -1, -1, -1, 0]
        return options.index(int(x))

    @staticmethod
    def encode_zone_type(x):
        options = [-1, 'CIRCLE']
        return options.index(x)

    @staticmethod
    def decode_zone_type(x):
        options = [-1, 'CIRCLE']
        return options[int(x)]

    @staticmethod
    def convert_longitude_to_float(longitude):
        if ((float(longitude) / 20000) > 180):
            return (float(longitude) / 20000) - 360;
        else:
            return float(longitude) / 20000;

    @staticmethod
    def convert_float_to_longitude(longitude):
        if (float(longitude) < 0):
            return int((float(longitude) + 360) * 20000)
        else:
            return int(float(longitude) * 20000);

    @staticmethod
    def convert_latitude_to_float(latitude):
        return (float(latitude) / 20000) - 90;

    @staticmethod
    def convert_float_to_latitude(latitude):
        return int((float(latitude) + 90) * 20000);

    @staticmethod
    def decode(b64_data):

        zone = dotdict({})
        packer = Packer(base64.b64decode(b64_data))

        zone.zone_id = packer.extract_bits(7)
        zone.zone_type = ZONE.decode_zone_type(packer.extract_bits(1))
        zone.enable_monitoring = packer.extract_bits(1)
        zone.enable_entering_leaving_events = packer.extract_bits(1)
        zone.enable_out_of_zone_detection_mode = packer.extract_bits(1)
        zone.enable_activation_date = packer.extract_bits(1)
        zone.year = packer.extract_bits(5)
        zone.year += 2020
        zone.month = packer.extract_bits(4)
        zone.day = packer.extract_bits(5)
        zone.hour = packer.extract_bits(5)
        zone.minute = packer.extract_bits(6)
        comms_vector = packer.extract_bits(2)
        zone.comms_vector = ZONE.decode_comms_vector(comms_vector)
        zone.delta_arg_loc_argos_seconds = packer.extract_bits(4)
        zone.delta_arg_loc_argos_seconds = ZONE.decode_arg_loc_argos(zone.delta_arg_loc_argos_seconds)
        zone.delta_arg_loc_cellular_seconds = packer.extract_bits(7)  # Not used
        zone.argos_extra_flags_enable = packer.extract_bits(1)
        argos_depth_pile = packer.extract_bits(4)
        zone.argos_depth_pile = DEPTHPILE.decode(argos_depth_pile)
        zone.argos_power = ARGOSPOWER.decode(packer.extract_bits(2)+1)
        zone.argos_time_repetition_seconds = packer.extract_bits(7)
        zone.argos_time_repetition_seconds *= 10
        zone.argos_mode = ARGOSMODE.decode(packer.extract_bits(2))
        zone.argos_duty_cycle = '{:06X}'.format(packer.extract_bits(24))
        zone.gnss_extra_flags_enable = packer.extract_bits(1)
        zone.hdop_filter_threshold = packer.extract_bits(4)
        zone.gnss_acquisition_timeout_seconds = packer.extract_bits(8)
        center_longitude_x = packer.extract_bits(23)
        zone.center_longitude_x = ZONE.convert_longitude_to_float(center_longitude_x)
        center_latitude_y = packer.extract_bits(22)
        zone.center_latitude_y = ZONE.convert_latitude_to_float(center_latitude_y)
        zone.radius_m = packer.extract_bits(12) * 50
        return zone

    @staticmethod
    def encode(zone_dict):

        zone = dotdict(zone_dict)

        # Zero out the data buffer to the required number of bytes -- this will round up to
        # the nearest number of bytes and zero all bytes before encoding
        total_bits = 160
        packer = Packer(bytearray([0] * int((total_bits + 4) / 8)))

        packer.pack_bits(int(zone.zone_id), 7)
        packer.pack_bits(ZONE.encode_zone_type(zone.zone_type), 1)
        packer.pack_bits(int(zone.enable_monitoring), 1)
        packer.pack_bits(int(zone.enable_entering_leaving_events), 1)
        packer.pack_bits(int(zone.enable_out_of_zone_detection_mode), 1)
        packer.pack_bits(int(zone.enable_activation_date), 1)
        packer.pack_bits((int(zone.year) - 2020), 5)
        packer.pack_bits(int(zone.month), 4)
        packer.pack_bits(int(zone.day), 5)
        packer.pack_bits(int(zone.hour), 5)
        packer.pack_bits(int(zone.minute), 6)
        packer.pack_bits(ZONE.encode_comms_vector(zone.comms_vector), 2)
        delta_arg_loc_argos_seconds = ZONE.encode_arg_loc_argos(int(zone.delta_arg_loc_argos_seconds))
        packer.pack_bits(delta_arg_loc_argos_seconds, 4)
        packer.pack_bits(zone.delta_arg_loc_cellular_seconds, 7)
        packer.pack_bits(int(zone.argos_extra_flags_enable), 1)
        argos_depth_pile = int(DEPTHPILE.encode(zone.argos_depth_pile))
        packer.pack_bits(argos_depth_pile, 4)
        packer.pack_bits(int(ARGOSPOWER.encode(zone.argos_power))-1, 2)
        packer.pack_bits(int(int(zone.argos_time_repetition_seconds) / 10), 7)
        packer.pack_bits(int(ARGOSMODE.encode(zone.argos_mode)), 2)
        packer.pack_bits(int(zone.argos_duty_cycle, 16), 24)
        packer.pack_bits(int(zone.gnss_extra_flags_enable), 1)
        packer.pack_bits(int(zone.hdop_filter_threshold), 4)
        packer.pack_bits(int(zone.gnss_acquisition_timeout_seconds), 8)
        center_longitude_x = ZONE.convert_float_to_longitude(zone.center_longitude_x)
        packer.pack_bits(center_longitude_x, 23)
        center_latitude_y = ZONE.convert_float_to_latitude(zone.center_latitude_y)
        packer.pack_bits(center_latitude_y, 22)
        packer.pack_bits(int(int(zone.radius_m) / 50), 12)

        return base64.b64encode(packer.result()).decode('ascii')


class PASPW():

    @staticmethod
    def encode(value):
        d = json.loads(value)
        allcast = d['allcastFormats']
        hex_bytes = ''
        for entry in allcast:
            for x in entry['adaptedOrbitParametersBurst']:
                hex_bytes += entry['adaptedOrbitParametersBurst'][x]
            for x in entry['constellationStatusBurst']:
                csb = entry['constellationStatusBurst'][x]
                if len(csb) & 1:
                    logger.warn('Stuffing CSB record %s with 0000 missing bits', x)
                    csb += '0'
                hex_bytes += csb
        logger.debug('Allcast packet: %s', hex_bytes)
        return base64.b64encode(binascii.unhexlify(hex_bytes)).decode('ascii')


class LOGRECORD(dotdict):
    pass


class LOGFILE():
    LOG_TYPES = ['LOG_GPS',
                 'LOG_STARTUP',
                 'LOG_ARTIC',
                 'LOG_UNDERWATER',
                 'LOG_BATTERY',
                 'LOG_STATE',
                 'LOG_ZONE',
                 'LOG_OTA_UPDATE',
                 'LOG_BLE',
                 'LOG_ERROR',
                 'LOG_WARN',
                 'LOG_INFO',
                 'LOG_TRACE']

    @staticmethod
    def decode_log_gps(payload, r):
        r.batt_voltage, r.iTOW, r.fix_year, r.fix_month, r.fix_day, r.fix_hour, r.fix_min, r.fix_sec, r.valid, r.onTime, r.ttff, r.fixType, _, _, _, r.numSV, \
        r.lon, r.lat, r.height, r.hMSL, r.hAcc, r.vAcc, r.velN, r.velE, r.velD, r.gSpeed, r.headMot, \
        r.sAcc, r.headAcc, r.pDOP, r.vDOP, r.hDOP, r.headVeh = \
            struct.unpack('<xHIHBBBBBBIiBBBBBddiiIIiiiifIfffff', payload[:104])
        return r

    @staticmethod
    def decode(data):
        records = []
        while data:
            r = LOGRECORD()
            r.day, r.month, r.year, r.hours, r.mins, r.secs, r.log_t, payload_size = struct.unpack('<BBHBBBBB', data[:9])
            r.log_t = LOGFILE.LOG_TYPES[r.log_t]
            if (r.log_t == 'LOG_GPS'):
                LOGFILE.decode_log_gps(data[9:], r)
            else:
                r.message = data[9:9+payload_size].decode('ascii', errors='ignore')
            records.append(r)
            data = data[9+payload_size:]
        return records
