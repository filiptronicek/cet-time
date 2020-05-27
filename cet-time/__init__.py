from pytz import timezone, utc
from datetime import datetime
from time import time

def InCity(city="Prague", timestamp=time()):
    fmt = '%Y-%m-%d %H:%M:%S'

    utc_dt = utc.localize(datetime.utcfromtimestamp(timestamp))
    utc_dt.strftime(fmt)

    cs_tz = timezone('Europe/Prague')
    cs_dt = utc_dt.astimezone(cs_tz)

    return city +": "+ cs_dt.strftime(fmt)
print(InCity("Libeznice"))