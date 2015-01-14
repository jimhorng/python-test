import dateutil.parser
import pytz
import time
import datetime

d1 = '2013-11-25T23:59:59.0012+08:00'
# d1="2014-05-20 18:34:59 +0800"
print(dateutil.parser.parse(d1).astimezone(dateutil.tz.tzutc()))
print(dateutil.parser.parse(d1).astimezone(dateutil.tz.tzutc()).isoformat())
print(dateutil.parser.parse(d1).astimezone(dateutil.tz.tzutc()).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
print("d3: " + str((dateutil.parser.parse(d1)
                    .astimezone(dateutil.tz.tzutc())
                    .strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z")))
print(dateutil.parser.parse(d1))
print(dateutil.parser.parse(d1).isoformat())
print(dateutil.parser.parse(d1).astimezone(pytz.utc))
print(dateutil.parser.parse(d1).astimezone(pytz.utc).isoformat())

# print datetime.datetime.utcnow().astimezone(dateutil.tz.tzutc())
# print datetime.datetime(datetime.datetime.utcnow(), tzinfo=pytz.utc)

print pytz.utc.localize(datetime.datetime.utcfromtimestamp(time.time())).isoformat()
print type(pytz.utc.localize(datetime.datetime.utcfromtimestamp(time.time())))