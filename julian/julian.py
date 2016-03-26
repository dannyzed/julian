from datetime import datetime
import math


def to_mjd(dt: datetime) -> float:
    """
    Converts a given datetime object to modified Julian date.
    Algorithm is copied from https://en.wikipedia.org/wiki/Julian_day
    All variable names are consistent with the notation on the wiki page.

    Parameters
    ----------
    dt: datetime
        Datetime object to convert to MJD

    Returns
    -------
    mjd: int
    """
    a = math.floor((14-dt.month)/12)
    y = dt.year + 4800 - a
    m = dt.month + 12*a - 3

    jdn = dt.day + math.floor((153*m + 2)/5) + 365*y + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) - 32045

    jd = jdn + (dt.hour - 12) / 24 + dt.minute / 1440 + dt.second / 86400 + dt.microsecond / 86400000000

    return jd - 2400000.5


def from_mjd(mjd: float) -> datetime:
    """
    Converts a Modified Julian Date to a datetime object.
    Algorithm is copied from https://en.wikipedia.org/wiki/Julian_day
    All variable names are consistent with the notation on the wiki page.

    Parameters
    ----------
    mjd: int
        Modified Julian Date

    Returns
    -------
    dt: datetime

    """
    # Constants that are defined
    y = 4716
    j = 1401
    m = 2
    n = 12
    r = 4
    p = 1461
    v = 3
    u = 5
    s = 153
    w = 2
    B = 274277
    C = -38

    # Calculate the month, day, and year from the integer component
    # of the mjd
    jd = math.floor(mjd) + 2400000.5 + 1

    f = jd + j + ((4*jd + B) // 146097 * 3) // 4 + C
    e = r*f + v
    g = (e % p) // r
    h = u*g + w
    day = int((h % s) // u + 1)
    month = int((h // s + m) % n + 1)
    year = int(e // p - y + (n + m - month) // n)

    # in microseconds
    frac_component = int((mjd - math.floor(mjd)) * (1e6*24*3600))

    hours = int(frac_component // (1e6*3600))
    frac_component -= hours * 1e6*3600

    minutes = int(frac_component // (1e6*60))
    frac_component -= minutes * 1e6*60

    seconds = int(frac_component // 1e6)
    frac_component -= seconds*1e6

    frac_component = int(frac_component)

    dt = datetime(year=year, month=month, day=day,
                  hour=hours, minute=minutes, second=seconds, microsecond=frac_component)
    return dt
