# Degrees Minutes Seconds to Decimal Degrees using python

Convert degrees, minutes, seconds for both latitude and longitude to decimal degrees
- lat 2° 41' 44.598" N
- long 72° 57' 48.541" E

``` python
import dms_dd.py as dd

lat = """2° 41' 44.598" N"""
long = """72° 57' 48.541" E"""
print(dms_dd(lat))
# result 2.69572167
print(dms_dd(long))
# result 72.96348361
```

