import re

#Degrees Minutes Seconds to Decimal Degrees
def dms_dd(dd):
    dd = f"""{dd}"""
    dd = re.sub('[^a-zA-Z0-9. ]', '', dd)
    dd = dd.split(" ")
    return round(float(dd[0])+(float(dd[1])/60)+(float(dd[2])/3600), 8)
