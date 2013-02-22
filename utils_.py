import calendar
import iso8601

def conv(x,mm=0):
    dt = iso8601.parse_date(x)
    return str(calendar.timegm(dt.timetuple())-mm*60)

