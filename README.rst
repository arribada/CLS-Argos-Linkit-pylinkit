Installation
============

python setup.py install

Usage
=====

To scan for beacons:

pygentracker --scan

To read configuration parameters into a file:

pygentracker --device xx:xx:xx:xx:xx:xx --read params.txt

To write configuration parameters from a file:

pygentracker --device xx:xx:xx:xx:xx:xx --write params.txt

Configuration file format
=========================

Configuration files are organised in sections according to the bluetooth
device ID e.g.,

[CE:BD:65:D5:4F:D2]
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

A configuration file can have multiple configuration sections for different
devices as required.  The tool will only pull out the configuration matching
the device ID of the device it connects with when performing updates.
