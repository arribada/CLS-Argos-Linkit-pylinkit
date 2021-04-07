from .dte_types import *     # noqa

class DTEParamMap():
    param_map = [
    [ "ARGOS_DECID", "IDT06", UINT, 0, 0xFFFFFF, [], True ],
    [ "ARGOS_HEXID", "IDT07", TEXT, 0, 0xFFFFFF, [], True ],
    [ "DEVICE_MODEL", "IDT02", TEXT, "", "", [], True ],
    [ "FW_APP_VERSION", "IDT03", TEXT, "", "", [], True ],
    [ "LAST_TX", "ART01", DATESTRING, 0, 0, [], True ],
    [ "TX_COUNTER", "ART02", UINT, 0, 0, [], True ],
    [ "BATT_SOC", "POT03", UINT, 0, 100, [], True ],
    [ "LAST_FULL_CHARGE_DATE", "POT05", DATESTRING, 0, 0, [], True ],
    [ "PROFILE_NAME", "IDP11", TEXT, "", "", [], True ],
    [ "AOP_STATUS", "XXXXX", BASE64, 0, 0, [], False ],  # FIXME: missing parameter key
    [ "ARGOS_AOP_DATE", "ART03", DATESTRING, 0, 0, [], True ],
    [ "ARGOS_FREQ", "ARP03", ARGOSFREQ, 401.6200, 401.6800, [], True ],
    [ "ARGOS_POWER", "ARP04", ARGOSPOWER, 0, 0, [ 0, 1, 2, 3 ], True ],
    [ "ARGOS_TX_REPETITION", "ARP05", UINT, 45, 1200, [], True ],
    [ "ARGOS_MODE", "ARP01", ARGOSMODE, 0, 0, [ 0, 1, 2, 3 ], True ],
    [ "ARGOS_NTRY_PER_MESSAGE", "ARP19", UINT, 0, 86400, [], True ],
    [ "ARGOS_DUTY_CYCLE", "ARP18", ARGOSDUTYCYLE, 0, 0xFFFFFF, [], True ],
    [ "GNSS_ENABLE", "GNP01", BOOLEAN, 0, 0, [], True ],
    [ "GNSS_DELTATIME_ACQ", "ARP11", AQPERIOD, 0, 0, [ 1, 2, 3, 4, 5, 6, 7, 8 ], True ],
    [ "GNSS_NBLASTFIX_TOSEND", "ARP16", DEPTHPILE, 0, 0, [1, 2, 3, 4, 8, 9, 10, 11, 12], True ],
    [ "GPS_CONST_SELECT", "", DECIMAL, 0, 0, [], False ],  # FIXME: missing parameter key
    [ "GLONASS_CONST_SELECT", "GNP08", DECIMAL, 0, 0, [], False ],
    [ "GNSS_HDOPFILT_ENABLE", "GNP02", BOOLEAN, 0, 0, [], True ],
    [ "GNSS_HDOPFILT_THR", "GNP03", UINT, 2, 15, [], True ],
    [ "GNSS_ACQ_TIMEOUT", "GNP05", UINT, 10, 600, [], True ],
    [ "GNSS_NTRY", "GNP04", UINT, 0, 0, [], False ],
    [ "UW_ENABLE", "UNP01", BOOLEAN, 0, 0, [], True ],
    [ "UW_DRY_TIME_BEFORE_TX", "UNP02", UINT, 1, 1440, [], True ],
    [ "UW_WET_SAMPLING", "UNP03", UINT, 1, 1440, [], True ],
    [ "LB_EN", "LBP01", BOOLEAN, 0, 0, [], True ],
    [ "LB_TRESHOLD", "LBP02", UINT, 0, 100, [], True ],
    [ "LB_ARGOS_POWER", "LBP03", ARGOSPOWER, 0, 0, [ 0, 1, 2, 3 ], True ],
    [ "LB_ARGOS_TX_REPETITION", "ARP06", UINT, 45, 1200, [], True ],
    [ "LB_ARGOS_MODE", "LBP04", ARGOSMODE, 0, 0, [ 0, 1, 2, 3 ], True ],
    [ "LB_ARGOS_DUTY_CYCLE", "LBP05", ARGOSDUTYCYLE, 0, 0xFFFFFF, [], True ],
    [ "LB_GNSS_EN", "LBP06", BOOLEAN, 0, 0, [], True ],
    [ "LB_GNSS_DELTATIME_ACQ", "ARP12", AQPERIOD, 0, 0, [ 1, 2, 3, 4, 5, 6, 7, 8 ], True ],
    [ "LB_GNSS_HDOPFILT_THR", "LBP07", UINT, 2, 15, [], True ],
    [ "LB_GNSS_NBLASTFIX_TOSEND", "LBP08", DEPTHPILE, 0, 0, [1, 2, 3, 4, 8, 9, 10, 11, 12], True ],
    [ "LB_GNSS_ACQ_TIMEOUT", "LBP09", UINT, 10, 600, [], True ],
    [ "UW_DRY_SAMPLING", "UNP04", UINT, 1, 1440, [], True ],
    [ "PP_MIN_ELEVATION", "PPP01", FLOAT, 0.0, 90.0, [], True ],
    [ "PP_MAX_ELEVATION", "PPP02", FLOAT, 0.0, 90.0, [], True ],
    [ "PP_MIN_DURATION", "PPP03", UINT, 20, 3600, [], True ],
    [ "PP_MAX_PASSES", "PPP04", UINT, 1, 10000, [], True ],
    [ "PP_LINEAR_MARGIN", "PPP05", UINT, 1, 3600, [], True ],
    [ "PP_COMP_STEP", "PPP06", UINT, 1, 1000, [], True ],
    [ "GNSS_COLD_ACQ_TIMEOUT", "GNP09", UINT, 10, 600, [], True ],
    [ "GNSS_FIX_MODE", "GNP10", GNSSFIXMODE, 0, 0, [], True ],
    [ "GNSS_DYN_MODEL", "GNP11", GNSSDYNMODEL, 0, 0, [], True ],
    ]

    @staticmethod
    def param_to_key(p):
        for (param, key, cls, minimum, maximum, allowed, is_implemented) in DTEParamMap.param_map:
            if p == param:
                return key
        raise Exception('Param {} not found'.format(param))

    @staticmethod
    def key_to_param(k):
        for (param, key, cls, minimum, maximum, allowed, is_implemented) in DTEParamMap.param_map:
            if k == key:
                return param
        raise Exception('Key {} not found'.format(key))

    @staticmethod
    def decode(k, v):
        for (param, key, cls, minimum, maximum, allowed, is_implemented) in DTEParamMap.param_map:
            if k == key:
                return cls.decode(v)
        raise Exception('Key {} not found'.format(key))

    @staticmethod
    def encode(p, v):
        for (param, key, cls, minimum, maximum, allowed, is_implemented) in DTEParamMap.param_map:
            if p == param:
                return cls.encode(v)
        raise Exception('Param {} not found'.format(param))
