import unittest

from pygentracker import dte_types


class TestZoneCodec(unittest.TestCase):

    def test_reference_vector_from_cpp(self):
        vector = 'A/cIQAKAYgbqqqqkeNu6Abd0AAA='
        print(dte_types.ZONE.decode(vector))

    def test_self_coding_decoding(self):
        zone = dte_types.dotdict({})
        zone.zone_id = 1
        zone.zone_type = 'CIRCLE'
        zone.enable_monitoring = 1
        zone.enable_entering_leaving_events = 1
        zone.enable_out_of_zone_detection_mode = 1
        zone.enable_activation_date = 1
        zone.year = 2020
        zone.month = 1
        zone.day = 1
        zone.hour = 0
        zone.minute = 0
        zone.comms_vector = 'ARGOS_PREFERRED'
        zone.delta_arg_loc_argos_seconds = 7*60
        zone.delta_arg_loc_cellular_seconds = 0
        zone.argos_extra_flags_enable = 1
        zone.argos_depth_pile = 1
        zone.argos_power = 500
        zone.argos_time_repetition_seconds = 60
        zone.argos_mode = 'DUTY_CYCLE'
        zone.argos_duty_cycle = 'AAAAAA'
        zone.gnss_extra_flags_enable = 1
        zone.hdop_filter_threshold = 2
        zone.gnss_acquisition_timeout_seconds = 60
        zone.center_latitude_y = 0
        zone.center_longitude_x = 0
        zone.radius_m = 0

        encoded = dte_types.ZONE.encode(zone)
        decoded = dte_types.ZONE.decode(encoded)

        for x in zone.keys():
            self.assertEqual(zone[x], decoded[x])

if __name__ == '__main__':
    unittest.main()
