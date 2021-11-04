import unittest
import temperature_utils_v2


class TemperatureUtilsTest(unittest.TestCase):

    def test_convert_to_celsius(self):
        test_cases = [
            (32, 0),
            (68, 20),
            (100, 37.78),
            (104, 40)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_celsius(temp_in))

    def test_convert_to_fahrenheit(self):
        test_cases = [
            (-17.7778, 0),
            (0, 32),
            (100, 212)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_fahrenheit(temp_in))

    def test_covert_from_kelvin(self):
        test_cases = [
            (278.15, (5, 41)),
            (315.82, (43, 109)),
            (284.65, (12, 53))
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.covert_from_kelvin(temp_in))



    def test3_temperature_tuple(self):
        temps_input = (278.15, 315.82, 284.65)
        expected = ((278.15, (5,41)), (315.82, (43, 109)), (284.65, (12, 53)))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "k")
        self.assertEqual(expected, actual)