import analisis
from havaiana import Site
from havaiana.charts import LineChart


class RainChartView(LineChart):
    def __init__(self):
       LineChart.__init__(self, "Tormentas de santa rosa",
                          "milimetros", 800, 400)

    def get_data(self, data):
        keys = []
        points = []
        for element in data:
            keys.append(element.pk)
            points.append({"value": element.precip,
                           "xlink": "/Days/%s" % element.pk})
        return keys, points


if __name__ == "__main__":
    renderers = [("Day", "__index_chart", RainChartView)]
    site = Site(analisis, renderers=renderers)
    site.serve()
