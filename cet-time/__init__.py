from pytz import timezone, utc
from datetime import datetime
from time import time

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

utc_dt = utc.localize(datetime.utcfromtimestamp(time()))
utc_dt.strftime(fmt)

cs_tz = timezone('Europe/Prague')
cs_dt = utc_dt.astimezone(cs_tz)

print(utc_dt.strftime(fmt))
print(cs_dt.strftime(fmt))