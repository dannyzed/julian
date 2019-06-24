from datetime import datetime
import math


def __to_format(jd: float, fmt: str) -> float:
    """
    Converts a Julian Day object into a specific format.  For
    example, Modified Julian Day.
    Parameters
    ----------
    jd: float
    fmt: str

    Returns
    -------
    jd: float
    """
    if fmt.lower() == 'jd':
        return jd
    elif fmt.lower() == 'mjd':
        return jd - 2400000.5
    elif fmt.lower() == 'rjd':
        return jd - 2400000
    else:
        raise ValueError('Invalid Format')


def __from_format(jd: float, fmt: str) -> (int, float):
    """
    Converts a Julian Day format into the "standard" Julian
    day format.
    Parameters
    ----------
    jd
    fmt

    Returns
    -------
    (jd, fractional): (int, float)
         A tuple representing a Julian day.  The first number is the
         Julian Day Number, and the second is the fractional component of the
         day.  A fractional component of 0.5 represents noon.  Therefore
         the standard julian day would be (jd + fractional + 0.5)
    """
    if fmt.lower() == 'jd':
        # If jd has a fractional component of 0, then we are 12 hours into
        # the day
        return math.floor(jd + 0.5), jd + 0.5 - math.floor(jd + 0.5)
    elif fmt.lower() == 'mjd':
        return __from_format(jd + 2400000.5, 'jd')
    elif fmt.lower() == 'rjd':
        return __from_format(jd + 2400000, 'jd')
    else:
        raise ValueError('Invalid Format')


def to_jd(dt: datetime, fmt: str = 'jd') -> float:
    """
    Converts a given datetime object to Julian date.
    Algorithm is copied from https://en.wikipedia.org/wiki/Julian_day
    All variable names are consistent with the notation on the wiki page.

    Parameters
    ----------
    fmt
    dt: datetime
        Datetime object to convert to MJD

    Returns
    -------
    jd: float
    """
    a = math.floor((14-dt.month)/12)
    y = dt.year + 4800 - a
    m = dt.month + 12*a - 3

    jdn = dt.day + math.floor((153*m + 2)/5) + 365*y + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) - 32045

    jd = jdn + (dt.hour - 12) / 24 + dt.minute / 1440 + dt.second / 86400 + dt.microsecond / 86400000000

    return __to_format(jd, fmt)


def from_jd(jd: float, fmt: str = 'jd') -> datetime:
    """
    Converts a Julian Date to a datetime object.
    Algorithm is from Fliegel and van Flandern (1968)

    Parameters
    ----------
    jd: float
        Julian Date as type specified in the string fmt

    fmt: str

    Returns
    -------
    dt: datetime

    """
    jd, jdf = __from_format(jd, fmt)

    l = jd+68569
    n = 4*l//146097
    l = l-(146097*n+3)//4
    i = 4000*(l+1)//1461001
    l = l-1461*i//4+31
    j = 80*l//2447
    k = l-2447*j//80
    l = j//11
    j = j+2-12*l
    i = 100*(n-49)+i+l

    year = math.trunc(i)
    month = math.trunc(j)
    day = math.trunc(k)

    # in microseconds
    frac_component = math.trunc(jdf * (1e6*24*3600))

    hours = math.trunc(frac_component // (1e6*3600))
    frac_component -= hours * 1e6*3600

    minutes = math.trunc(frac_component // (1e6*60))
    frac_component -= minutes * 1e6*60

    seconds = math.trunc(frac_component // 1e6)
    frac_component -= seconds*1e6

    frac_component = math.trunc(frac_component)

    dt = datetime(year=year, month=month, day=day,
                  hour=hours, minute=minutes, second=seconds, microsecond=frac_component)
    return dt
