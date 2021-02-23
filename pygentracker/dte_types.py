import base64


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


class DECIMAL(UINT):
    pass


class TEXT():
    @staticmethod
    def encode(value):
        return value

    @staticmethod
    def decode(value):
        return value


class HEXADECIMAL(TEXT):
    pass


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
    allowed = [-1, 3, 4, 20, 500]

    @staticmethod
    def encode(value):
        return str(ARGOSPOWER.allowed.index(int(value)))

    @staticmethod
    def decode(value):
        return ARGOSPOWER.allowed[int(value)]


class ARGOSMODE():
    allowed = ['OFF', 'LEGACY', 'PASS_PREDICTION', 'DUTY_CYCLE']

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
