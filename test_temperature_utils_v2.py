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
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.covert_from_kelvin(temp_in))



    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        expected = ((1, 274.15), (2, 275.15), (3, 276.15))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "a")
        self.assertEqual(expected, actual)



def covert_from_kelvin(temperature):
    kelvin_to_celsius = (temperature - 273.15)
    ktc_float = round(kelvin_to_celsius, 2)
    kelvin_to_fahrenheit = (((kelvin_to_celsius - 32)/1.8))
    ktf_float = int(kelvin_to_fahrenheit)
    return ktc_float, ktf_float