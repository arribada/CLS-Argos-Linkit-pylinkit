from .dte_types import *     # noqa

class DTEParamMap():
    param_map = [
    [ "DEVICE_MODEL", "IDT02", TEXT ],
    [ "FW_APP_VERSION", "IDT03", TEXT ],
    [ "HW_VERSION", "IDT04", TEXT ],
    [ "LAST_TX", "ART01", DATESTRING ],
    [ "TX_COUNTER", "ART02", UINT ],
    [ "BATT_SOC", "POT03", UINT ],
    [ "LAST_FULL_CHARGE_DATE", "POT05", DATESTRING ],
    [ "BATT_VOLTAGE", "POT06", FLOAT ],
    [ "PROFILE_NAME", "IDP11", TEXT ],
    [ "ARGOS_DECID", "IDP12", UINT ],
    [ "ARGOS_HEXID", "IDT06", TEXT ],
    [ "ARGOS_AOP_DATE", "ART03", DATESTRING ],
    [ "ARGOS_FREQ", "ARP03", ARGOSFREQ ],
    [ "ARGOS_POWER", "ARP04", ARGOSPOWER ],
    [ "ARGOS_TX_REPETITION", "ARP05", UINT ],
    [ "ARGOS_MODE", "ARP01", ARGOSMODE ],
    [ "ARGOS_NTRY_PER_MESSAGE", "ARP19", UINT ],
    [ "ARGOS_DUTY_CYCLE", "ARP18", ARGOSDUTYCYLE ],
    [ "GLONASS_CONST_SELECT", "GNP08", DECIMAL ],
    [ "GNSS_ENABLE", "GNP01", BOOLEAN ],
    [ "GNSS_DELTATIME_ACQ", "ARP11", AQPERIOD ],
    [ "GNSS_NBLASTFIX_TOSEND", "ARP16", DEPTHPILE ],
    [ "GNSS_HDOPFILT_ENABLE", "GNP02", BOOLEAN ],
    [ "GNSS_HDOPFILT_THR", "GNP03", UINT ],
    [ "GNSS_ACQ_TIMEOUT", "GNP05", UINT ],
    [ "GNSS_NTRY", "GNP04", UINT ],
    [ "GNSS_COLD_ACQ_TIMEOUT", "GNP09", UINT ],
    [ "GNSS_FIX_MODE", "GNP10", GNSSFIXMODE ],
    [ "GNSS_DYN_MODEL", "GNP11", GNSSDYNMODEL ],
    [ "UW_ENABLE", "UNP01", BOOLEAN ],
    [ "UW_DRY_TIME_BEFORE_TX", "UNP02", UINT ],
    [ "UW_WET_SAMPLING", "UNP03", UINT ],
    [ "UW_DRY_SAMPLING", "UNP04", UINT ],
    [ "LB_EN", "LBP01", BOOLEAN ],
    [ "LB_TRESHOLD", "LBP02", UINT ],
    [ "LB_ARGOS_POWER", "LBP03", ARGOSPOWER ],
    [ "LB_ARGOS_TX_REPETITION", "ARP06", UINT  ],
    [ "LB_ARGOS_MODE", "LBP04", ARGOSMODE ],
    [ "LB_ARGOS_DUTY_CYCLE", "LBP05", ARGOSDUTYCYLE ],
    [ "LB_GNSS_EN", "LBP06", BOOLEAN ],
    [ "LB_GNSS_DELTATIME_ACQ", "ARP12", AQPERIOD ],
    [ "LB_GNSS_HDOPFILT_THR", "LBP07", UINT ],
    [ "LB_GNSS_NBLASTFIX_TOSEND", "LBP08", DEPTHPILE ],
    [ "LB_GNSS_ACQ_TIMEOUT", "LBP09", UINT ],
    [ "PP_MIN_ELEVATION", "PPP01", FLOAT ],
    [ "PP_MAX_ELEVATION", "PPP02", FLOAT ],
    [ "PP_MIN_DURATION", "PPP03", UINT ],
    [ "PP_MAX_PASSES", "PPP04", UINT ],
    [ "PP_LINEAR_MARGIN", "PPP05", UINT ],
    [ "PP_COMP_STEP", "PPP06", UINT ],
    [ "GNSS_HACCFILT_ENABLE", "GNP20", BOOLEAN ],
    [ "GNSS_HACCFILT_THR", "GNP21", UINT ],
    [ "GNSS_MIN_NUM_FIXES", "GNP22", UINT ],
    [ "GNSS_COLD_START_RETRY_PERIOD", "GNP23", UINT ],
    [ "ARGOS_TIME_SYNC_BURST_EN", "ARP30", BOOLEAN ],
    [ "LED_MODE", "LDP01", LEDMODE ],
    [ "ARGOS_TX_JITTER_EN", "ARP31", BOOLEAN ],
    [ "ARGOS_RX_EN", "ARP32", BOOLEAN ],
    [ "ARGOS_RX_MAX_WINDOW", "ARP33", UINT ],
    [ "ARGOS_RX_AOP_UPDATE_PERIOD", "ARP34", UINT ],
    [ "ARGOS_TCXO_WARMUP_TIME", "ARP35", UINT ],
    [ "RX_COUNTER", "ART10", UINT ],
    [ "RX_TIME", "ART11", UINT ],
    [ "GNSS_ASSISTNOW_EN", "GNP24", BOOLEAN ],
    [ "LB_GNSS_HACCFILT_THR", "LBP10", UINT ],
    [ "LB_NTRY_PER_MESSAGE", "LBP11", BOOLEAN ],
    [ "ZONE_TYPE", "ZOP01", ZONETYPE ],
    [ "ZONE_ENABLE_OUT_OF_ZONE_DETECTION_MODE", "ZOP04", BOOLEAN ],
    [ "ZONE_ENABLE_ACTIVATION_DATE", "ZOP05", BOOLEAN ],
    [ "ZONE_ACTIVATION_DATE", "ZOP06", DATESTRING ],
    [ "ZONE_ARGOS_DEPTH_PILE", "ZOP08", DEPTHPILE ],
    [ "ZONE_ARGOS_POWER", "ZOP09", ARGOSPOWER ],
    [ "ZONE_ARGOS_REPETITION_SECONDS", "ZOP10", UINT ],
    [ "ZONE_ARGOS_MODE", "ZOP11", ARGOSMODE ],
    [ "ZONE_ARGOS_DUTY_CYCLE", "ZOP12", ARGOSDUTYCYLE ],
    [ "ZONE_ARGOS_NTRY_PER_MESSAGE", "ZOP13", UINT ],
    [ "ZONE_GNSS_DELTATIME_ACQ", "ZOP14", UINT ],
    [ "ZONE_GNSS_HDOPFILT_THR", "ZOP15", UINT ],
    [ "ZONE_GNSS_HACCFILT_THR", "ZOP16", UINT ],
    [ "ZONE_GNSS_ACQ_TIMEOUT", "ZOP17", UINT ],
    [ "ZONE_CENTER_LONGITUDE", "ZOP18", FLOAT ],
    [ "ZONE_CENTER_LATITUDE", "ZOP19", FLOAT ],
    [ "ZONE_RADIUS", "ZOP20", UINT ],
    [ "CERT_TX_ENABLE", "CTP01", BOOLEAN ],
    [ "CERT_TX_PAYLOAD", "CTP02", UPPERCASETEXT ],
    [ "CERT_TX_MODULATION", "CTP03", ARGOSMODULATION ],
    [ "CERT_TX_REPETITION", "CTP04", UINT ],
    [ "DEBUG_OUTPUT_MODE", "DBP01", DEBUGMODE ],
    ]

    @staticmethod
    def param_to_key(p):
        for (param, key, cls) in DTEParamMap.param_map:
            if p == param:
                return key
        raise Exception('Param {} not found'.format(p))

    @staticmethod
    def key_to_param(k):
        for (param, key, cls) in DTEParamMap.param_map:
            if k == key:
                return param
        raise Exception('Key {} not found'.format(k))

    @staticmethod
    def decode(k, v):
        for (_, key, cls) in DTEParamMap.param_map:
            if k == key:
                return cls.decode(v)
        raise Exception('Key {} not found'.format(k))

    @staticmethod
    def encode(p, v):
        for (param, _, cls) in DTEParamMap.param_map:
            if p == param:
                return cls.encode(v)
        raise Exception('Param {} not found'.format(p))
