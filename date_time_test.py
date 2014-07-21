import dateutil.parser
import pytz

d1="2014-05-20 18:34:59 +0800"
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