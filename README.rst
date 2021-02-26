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
<Zone data>

A configuration file can have multiple configuration sections.
