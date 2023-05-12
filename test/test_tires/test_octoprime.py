import unittest

from tires.octoprime import Octoprime

class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensory_array = [1, 1, 1, 0]

        tires = Octoprime(sensory_array)
        self.assertTrue(tires.needs_service)

    def test_tires_should_not_be_serviced(self):
        sensory_array = [1, 1, 0, 0.99]

        tires = Octoprime(sensory_array)
        self.assertFalse(tires.needs_service)