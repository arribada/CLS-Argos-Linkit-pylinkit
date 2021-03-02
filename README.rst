Installation
============

python setup.py install


Usage
=====

To scan for beacons:

pygentracker --scan

To read configuration parameters into a file:

pygentracker --device xx:xx:xx:xx:xx:xx --parmr params.txt

To write configuration parameters from a file:

pygentracker --device xx:xx:xx:xx:xx:xx --parmw params.txt

To send pass prediction from a JSON file:

pygentracker --device xx:xx:xx:xx:xx:xx --paspw paspw.json

To download sensor log data:

pygentracker --device xx:xx:xx:xx:xx:xx --dump_sensor gpslog.json

To download system log data:

pygentracker --device xx:xx:xx:xx:xx:xx --dump_system syslog.json

To perform a factory reset (will erase stored configuration, paspw, zone and log files):

pygentracker --device xx:xx:xx:xx:xx:xx --factw

To perform a software reset:

pygentracker --device xx:xx:xx:xx:xx:xx --rstbw

To reset the TX_COUNTER to zero:

pygentracker --device xx:xx:xx:xx:xx:xx --rstvw

To perform a firmware update:

pygentracker --device xx:xx:xx:xx:xx:xx --fw firmware.img

WARNING: the operation is very slow and make take 1.5 hours.  It is advised not to
run this command if the battery is low and to ensure the device is not reset during
operation.  Also note that the firmware update does not take effect until the
next reboot of the device upon successful completion of the above command.


Debug trace may also optionally be enabled with the --debug flag in conjunction with any of
the above options.


Logging file format
===================

Log files are downloaded as binary and transcoded to JSON format as follows:

GPS
---

[
    {
        "batt_voltage": 4200,
        "day": 1,
        "fixType": 2,
        "fix_day": 1,
        "fix_hour": 13,
        "fix_min": 26,
        "fix_month": 3,
        "fix_sec": 31,
        "fix_year": 2021,
        "gSpeed": 4,
        "hAcc": 18700,
        "hDOP": 1.3799999952316284,
        "hMSL": 240,
        "headAcc": 180.0,
        "headMot": 0.0,
        "headVeh": 0.0,
        "height": 48232,
        "hours": 13,
        "iTOW": 134807995,
        "lat": 51.3767097,
        "log_t": "LOG_GPS",
        "lon": -2.1183726,
        "mins": 26,
        "month": 3,
        "nano": -4712236,
        "numSV": 6,
        "pDOP": 1.6799999475479126,
        "sAcc": 263,
        "secs": 31,
        "tAcc": 4294967295,
        "vAcc": 4116,
        "vDOP": 0.9599999785423279,
        "valid": 1,
        "velD": 0,
        "velE": -3,
        "velN": 1,
        "year": 2021
    },
	...
]

System
------

[
	...
    {
        "day": 1,
        "hours": 13,
        "log_t": "LOG_INFO",
        "message": "GPSScheduler::task_process_gnss_data: lon=-2.118220 lat=51.376792 height=47992",
        "mins": 42,
        "month": 3,
        "secs": 10,
        "year": 2021
    },
    {
        "day": 1,
        "hours": 13,
        "log_t": "LOG_INFO",
        "message": "GPSScheduler::schedule_aquisition in 470 seconds",
        "mins": 42,
        "month": 3,
        "secs": 10,
        "year": 2021
    },
    {
        "day": 1,
        "hours": 13,
        "log_t": "LOG_INFO",
        "message": "ArgosScheduler::next_duty_cycle: found schedule: 1614606165",
        "mins": 42,
        "month": 3,
        "secs": 10,
        "year": 2021
    },
    {
        "day": 1,
        "hours": 13,
        "log_t": "LOG_INFO",
        "message": "ArticTransceiver::send_packet: sending message total_bits=176 tail_bits=7 burst_size=24",
        "mins": 42,
        "month": 3,
        "secs": 52,
        "year": 2021
    },
    {
        "day": 1,
        "hours": 13,
        "log_t": "LOG_INFO",
        "message": "ArgosScheduler::next_duty_cycle: found schedule: 1614606210",
        "mins": 42,
        "month": 3,
        "secs": 56,
        "year": 2021
    },
    {
        "day": 1,
        "hours": 13,
        "log_t": "LOG_INFO",
        "message": "ArticTransceiver::send_packet: sending message total_bits=176 tail_bits=7 burst_size=24",
        "mins": 43,
        "month": 3,
        "secs": 38,
        "year": 2021
    },
	...
]



Configuration file format
=========================

Configuration files are organised in sections accordingly:

[PARAM]  # Optional params for --parmw command
PROFILE_NAME = LIAM
ARGOS_FREQ = 401.6599
ARGOS_POWER = 500
TR_NOM = 120
ARGOS_MODE = DUTY_CYCLE
NTRY_PER_MESSAGE = 1000
DUTY_CYCLE = 16777215
GNSS_EN = 1
DLOC_ARG_NOM = 10
ARGOS_DEPTH_PILE = 1
GNSS_ACQ_TIMEOUT = 60
ARGOS_HEXID = 4E7B54C

[ZONE]   # Optional zone info for --zonew command
zone_id = 1    # Must always be 1
zone_type = CIRCLE
enable_monitoring = 0
enable_entering_leaving_events = 0
enable_out_of_zone_detection_mode = 0
enable_activation_date = 0
year = 2020
month = 1
day = 1
hour = 0
minute = 0
comms_vector = UNCHANGED
delta_arg_loc_argos_seconds = 0
delta_arg_loc_cellular_seconds = 0
argos_extra_flags_enable = 0
argos_depth_pile = 1
argos_power = 500
argos_time_repetition_seconds = 10
argos_mode = OFF
argos_duty_cycle = 000000
gnss_extra_flags_enable = 0
hdop_filter_threshold = 2
gnss_acquisition_timeout_seconds = 45
center_longitude_x = -0.0
center_latitude_y = 0.0
radius_m = 0

A configuration should have either a [PARAM], [ZONE] or both sections.
