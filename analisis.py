from json import dumps
from operator import itemgetter

from ojota import Ojota


class Day(Ojota):
    plural_name = "Days"
    default_order = "pk"

    def __repr__(self):
        return "%s > %s" % (self.pk, self.precip)


def get_most_rain():
    days = Day.all(sorted="-precip")[:5]
    return days

def get_rainy_date(month, day):
    ret = None, None
    days = Day.all(month=month, day=day, year__lt="2012")
    if len(days):
        dat = [item for item in days if item.precip != 0.0]
        ret = len(dat), sum([item.precip for item in dat])
    return ret

if __name__ == "__main__":
    print "el dia que mas llovio:", get_most_rain()
    data = []
    for month in range(1, 13):
        for day in range(1, 32):
            rain, precip = get_rainy_date(month, str(day).rjust(2, "0"))
            if rain is not None:
                media = precip / 7
                data.append(("%s/%s" % (month, day), rain, precip, media))
    print "el verdadero Santa Rosa:", sorted(data, key=itemgetter(1), reverse=True)[:5]



