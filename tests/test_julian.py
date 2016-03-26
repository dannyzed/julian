import unittest
from datetime import datetime
import julian


class JulianTests(unittest.TestCase):
    def test_simple_to_mjd(self):
        input_dt = datetime(year=2004, day=1, month=1)

        self.assertAlmostEqual(53005, julian.to_mjd(input_dt))

    def test_simple_from_mjd(self):
        input_mjd = 53005.1

        dt = julian.from_mjd(input_mjd)

        self.assertEqual(dt.month, 1)
        self.assertEqual(dt.year, 2004)
        self.assertEqual(dt.day, 1)

    def full_test(self):
        start_mjd = 54372
        mjd_delta = 0.017
        end_mjd = 55372

        mjd = start_mjd

        while mjd < end_mjd:
            temp_dt = julian.from_mjd(mjd)
            new_mjd = julian.to_mjd(temp_dt)
            self.assertAlmostEqual(mjd, new_mjd)

            mjd += mjd_delta

if __name__ == "__main__":
    unittest.main()