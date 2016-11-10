import unittest
from datetime import datetime, timedelta
import julian


class JulianTests(unittest.TestCase):
    def test_simple_to_mjd(self):
        """
        Tests a simple conversion from datetime to MJD
        """
        input_dt = datetime(year=2004, day=1, month=1)

        self.assertAlmostEqual(53005, julian.to_jd(input_dt, 'mjd'))

    def test_simple_from_mjd(self):
        """
        Tests a simple conversion from mjd to datetime

        """
        input_mjd = 53005.1

        dt = julian.from_jd(input_mjd, 'mjd')

        self.assertEqual(dt.month, 1)
        self.assertEqual(dt.year, 2004)
        self.assertEqual(dt.day, 1)

    def test_mjd_full(self):
        """
        Ensures that to_jd and from_jd are inverses for a large number of mjds.
        """
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
        """
        Ensures that to_jd and from_jd are inverses for a large number of jd's
        """
        start_jd = 2457471.93681 - 500
        jd_delta = 0.017
        end_jd = 2457471.93681

        jd = start_jd

        while jd < end_jd:
            temp_dt = julian.from_jd(jd)
            new_jd = julian.to_jd(temp_dt)
            self.assertAlmostEqual(jd, new_jd)

            jd += jd_delta

    def test_to_jd_with_numpy(self):
        """
        Tests functionality with numpy arrays
        """
        import numpy as np

        mjds = np.linspace(54372, 54380, 100)

        dts = julian.from_jd(mjds, fmt='mjd')

        for mjd, dt in zip(mjds, dts):
            self.assertAlmostEqual(dt, julian.from_jd(mjd, fmt='mjd'))

    def test_from_jd_with_numpy(self):
        """
        Tests functionality of converting to jd with numpy arrays
        """
        start_dt = datetime(year=2015, day=1, month=1, second=40)

        dts = [start_dt + timedelta(hours=idx) for idx in range(0, 100)]
        mjds = julian.to_jd(dts, fmt='mjd')

        for mjd, dt in zip(mjds, dts):
            self.assertAlmostEqual(mjd, julian.to_jd(dt, fmt='mjd'))

if __name__ == "__main__":
    unittest.main()
