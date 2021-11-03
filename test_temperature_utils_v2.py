import unittest
import temperature_utils_v2


class TemperatureUtilsTest(unittest.TestCase):

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        expected = ((1, 274.15), (2, 275.15), (3, 276.15))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "a")
        self.assertEqual(expected, actual)