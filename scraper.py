import re

from calendar import monthrange
from datetime import date
from json import dumps
from pyquery import PyQuery as pq

from analisis import Day


keys = ("pk", "year", "month", "day", "precip", "dow")
regexp = re.compile("\d+\.\d+\(24h\)")

def get_month(year, month):
    ndays = monthrange(year, month)[1]
    str_month = str(month).rjust(2, "0")
    days = []
    url = 'http://www.mundomanz.com/meteo_p/byind?countr=ARGENTINA&ind=87593&year=%s&month=%s&day=%s&n_days=%s&trans=PA&time=12Z&action=display' % (year, str_month, ndays, ndays)
    print url
    d = pq(url=url)
    data = d(".dat").map(lambda i, e: pq(e).text())
    for text in data:
        matched = regexp.search(text)
        if matched is not None:
            precip = float(matched.group().strip("(24h)"))
        else:
            precip = 0.0
        day = text.split(" ")[0]
        dow = date(year, month, int(day)).weekday()
        pk = "%s-%s-%s" % (year, str_month, day)
        data = dict(zip(keys, (pk, year, month, day, precip, dow)))
        days.append(data)
    return days

def get_year(year):
    days = []
    for month in range(1, 13):
        for_month = get_month(year, month)
        days.extend(for_month)

    return days

def get_years():
    days = []
    for year in range(2005, 2014):
        days.extend(get_year(year))
    return days

if __name__ == "__main__":
     data = get_years()
     for day in data:
         Day(**day).save()
     #output = file("data/Days.json", "w")
     #output.write(dumps(data))
     #output.close()

