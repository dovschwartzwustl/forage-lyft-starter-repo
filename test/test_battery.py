import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = datetime(2022, 2, 27)
        current_date = datetime(2028, 2, 27)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service)

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = datetime(2022, 2, 27)
        current_date = datetime(2028, 2, 27)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service)






if __name__ == '__main__':
    unittest.main()  