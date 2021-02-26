import logging
import argparse
import configparser
import sys
import pygentracker
import pygatt   # noqa


parser = argparse.ArgumentParser()
parser.add_argument('--fw', type=argparse.FileType('rb'), required=False, help='Firmware filename for FW OTA update')
parser.add_argument('--device', type=str, required=False, help='xx:xx:xx:xx:xx:xx BLE device address')
parser.add_argument('--parmr', type=argparse.FileType('w'), required=False, help='Filename to write [PARAM] configuration to')
parser.add_argument('--rstvw', action='store_true', required=False, help='Reset variables (TX_COUNTER)')
parser.add_argument('--rstbw', action='store_true', required=False, help='Reset beacon')
parser.add_argument('--factw', action='store_true', required=False, help='Factory reset (WARNING: erases all stored logs and configuration!)')
parser.add_argument('--parmw', type=argparse.FileType('r'), required=False, help='Filename to read [PARAM] configuration from')
parser.add_argument('--zonew', type=argparse.FileType('r'), required=False, help='Filename to read [ZONE] configuration from')
parser.add_argument('--zoner', type=argparse.FileType('w'), required=False, help='Filename to write [ZONE] configuration to')
parser.add_argument('--paspw', type=argparse.FileType('r'), required=False, help='Filename (JSON) to read pass predict configuration from')
parser.add_argument('--scan', action='store_true', required=False, help='Scan for beacons')
parser.add_argument('--dump_sensor', type=argparse.FileType('wb'), required=False, help='Dump sensor log file')
parser.add_argument('--dump_system', type=argparse.FileType('wb'), required=False, help='Dump system log file')
args = parser.parse_args()


def setup_logging(enabled, level):
    if enabled:
        logging.basicConfig(format='%(asctime)s\t%(module)s\t%(levelname)s\t%(message)s', level=logging.ERROR)
        if level == 'error':
            logging.getLogger().setLevel(logging.ERROR)
        elif level == 'warn':
            logging.getLogger().setLevel(logging.WARN)
        elif level == 'info':
            logging.getLogger().setLevel(logging.INFO)
        elif level == 'debug':
            logging.getLogger().setLevel(logging.DEBUG)


def main():
    setup_logging(True, 'debug')
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(2)

    dev = None
    if args.device:
        dev = pygentracker.GenTracker(args.device)

    if args.parmr:
        dev.sync()
        d = {}
        d['PARAM'] = dev.get()
        cfg = configparser.ConfigParser()
        cfg.optionxform = lambda option: option
        cfg.read_dict(dictionary=d)
        cfg.write(args.parmr)
        args.parmr.close()

    if args.parmw:
        cfg = configparser.ConfigParser()
        cfg.optionxform = lambda option: option
        cfg.read_string(args.parmw.read())
        dev.set(cfg['PARAM'])

    if args.zoner:
        d = {}
        d['ZONE'] = dev.zoner()
        cfg = configparser.ConfigParser()
        cfg.optionxform = lambda option: option
        cfg.read_dict(dictionary=d)
        cfg.write(args.zoner)
        args.zoner.close()

    if args.zonew:
        cfg = configparser.ConfigParser()
        cfg.optionxform = lambda option: option
        cfg.read_string(args.zonew.read())
        dev.zonew(cfg['ZONE'])

    if args.paspw:
        dev.paspw(args.paspw.read())

    if args.dump_sensor:
        args.dump_sensor.write(dev.dumpd('sensor'))
        args.dump_sensor.close()

    if args.dump_system:
        args.dump_system.write(dev.dumpd('system'))
        args.dump_system.close()

    if args.fw:
        dev.firmware_update(args.fw.read(), 0)

    if args.factw:
        dev.factw()
    
    if args.rstvw:
        dev.rstvw()
    
    if args.rstbw:
        dev.rstbw()

    if args.scan:
        result = pygatt.GATTToolBackend().scan(1)
        for x in result:
            if (x['name'] == 'GenTracker'):
                print(x['address'])


if __name__ == "__main__":
    main()
