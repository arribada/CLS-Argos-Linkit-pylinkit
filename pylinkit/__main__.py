import logging
import argparse
import configparser
import sys
import pylinkit
from .ble import BLEDevice

erase_options = ['sensor', 'system', 'all']
resetv_options = {'tx_counter': 1, 'rx_counter': 3, 'rx_time': 4}

parser = argparse.ArgumentParser()
parser.add_argument('--fw', type=argparse.FileType('rb'), required=False, help='Firmware filename for FW OTA update')
parser.add_argument('--timeout', type=float, required=False, default=None, help='BLE communications timeout')
parser.add_argument('--erase', type=str, choices=erase_options, required=False, help='Erase log file')
parser.add_argument('--device', type=str, required=False, help='xx:xx:xx:xx:xx:xx BLE device address')
parser.add_argument('--parmr', type=argparse.FileType('w'), required=False, help='Filename to write [PARAM] configuration to')
parser.add_argument('--rstvw', type=str, choices=resetv_options.keys(), required=False, help='Reset variable: tx_counter or rx_counter')
parser.add_argument('--rstbw', action='store_true', required=False, help='Reset beacon')
parser.add_argument('--factw', action='store_true', required=False, help='Factory reset (WARNING: erases all stored logs and configuration!)')
parser.add_argument('--parmw', type=argparse.FileType('r'), required=False, help='Filename to read [PARAM] configuration from')
parser.add_argument('--paspw', type=argparse.FileType('r'), required=False, help='Filename (JSON) to read pass predict configuration from')
parser.add_argument('--scan', action='store_true', required=False, help='Scan for beacons')
parser.add_argument('--debug', action='store_true', required=False, help='Turn on debug trace')
parser.add_argument('--dump_sensor', type=argparse.FileType('wb'), required=False, help='Dump sensor log file')
parser.add_argument('--dump_system', type=argparse.FileType('wb'), required=False, help='Dump system log file')
args = parser.parse_args()


class OrderedRawConfigParser(configparser.RawConfigParser):
    def write(self, fp):
        for section in self._sections:
            fp.write("[%s]\n" % section)
            for key in sorted( self._sections[section] ): 
                if key != "__name__":
                    fp.write("%s = %s\n" %
                             (key, str( self._sections[section][ key ] ).replace('\n', '\n\t')))    
            fp.write("\n")    


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
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(2)

    if args.debug:
        setup_logging(True, 'debug')
    else:
        setup_logging(True, 'info')

    dev = None
    if args.device:
        dev = pylinkit.GenTracker(args.device)

    if args.parmr:
        dev.sync()
        d = {}
        d['PARAM'] = dev.get()
        cfg = OrderedRawConfigParser()
        cfg.optionxform = lambda option: option
        cfg.read_dict(dictionary=d)
        cfg.write(args.parmr)
        args.parmr.close()

    if args.parmw:
        cfg = OrderedRawConfigParser()
        cfg.optionxform = lambda option: option
        cfg.read_string(args.parmw.read())
        dev.set(cfg['PARAM'])

    if args.paspw:
        dev.paspw(args.paspw.read())

    if args.dump_sensor:
        args.dump_sensor.write(dev.dumpd('sensor'))
        args.dump_sensor.close()

    if args.dump_system:
        args.dump_system.write(dev.dumpd('system'))
        args.dump_system.close()

    if args.erase:
        dev.erase(erase_options.index(args.erase) + 1)

    if args.fw:
        dev.firmware_update(args.fw.read(), 0, args.timeout)

    if args.factw:
        dev.factw()

    if args.rstvw:
        dev.rstvw(resetv_options[args.rstvw])

    if args.rstbw:
        dev.rstbw()

    if args.scan:
        scan_dev = BLEDevice()
        result = scan_dev.scan()
        for x in result:
            if ('Linkit' in x.name):
                print(x.address, x.name)


if __name__ == "__main__":
    main()
