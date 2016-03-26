import unittest
from datetime import datetime
import julian


class JulianTests(unittest.TestCase):
    def test_simple_to_mjd(self):
        input_dt = datetime(year=2004, day=1, month=1)

        self.assertAlmostEqual(53005, julian.to_jd(input_dt, 'mjd'))

    def test_simple_from_mjd(self):
        input_mjd = 53005.1

        dt = julian.from_jd(input_mjd, 'mjd')

        self.assertEqual(dt.month, 1)
        self.assertEqual(dt.year, 2004)
        self.assertEqual(dt.day, 1)

    def test_mjd_full(self):
        start_mjd = 54372
        mjd_delta = 0.017
        end_mjd = 55372

        mjd = start_mjd

        while mjd < end_mjd:
            temp_dt = julian.from_jd(mjd, 'mjd')
            new_mjd = julian.to_jd(temp_dt, 'mjd')
            self.assertAlmostEqual(mjd, new_mjd)

            mjd += mjd_delta

    def test_jd_full(self):
        start_jd = 2457471.93681 - 500
        jd_delta = 0.017
        end_jd = 2457471.93681

        jd = start_jd

        while jd < end_jd:
            temp_dt = julian.from_jd(jd)
            new_jd = julian.to_jd(temp_dt)
            self.assertAlmostEqual(jd, new_jd)

            jd += jd_delta

if __name__ == "__main__":
    unittest.main()
