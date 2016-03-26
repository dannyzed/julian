julian
======

julian is a simple Python library for converting between Julian dates and Python datetime objects.

Examples
--------
```python
import julian
import datetime

mjd = 54372.78
dt = julian.from_jd(mjd, fmt='mjd')
print(dt)

2007-09-29 18:43:11.999982

jd = julian.to_jd(dt + datetime.timedelta(hours=12), fmt='jd')
print(jd)

2454373.78
```

Installation
------------