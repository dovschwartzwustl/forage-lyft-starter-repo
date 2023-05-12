import unittest

from tires.carrigan import Carrigan

class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensory_array = [0, 0, 0, 0.9]

        tires = Carrigan(sensory_array)
        self.assertTrue(tires.needs_service)

    def test_tires_should_not_be_serviced(self):
        sensory_array = [0, 0, 0, 0.89]

        tires = Carrigan(sensory_array)
        self.assertFalse(tires.needs_service)