from math import radians, cos, sin, asin, sqrt


class Haversine:
    def __init__(self, coordinates):
        self.lon1 = coordinates[0]
        self.lat1 = coordinates[1]
        self.lon2 = coordinates[2]
        self.lat2 = coordinates[3]

    def haversine(self):
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [self.lon1, self.lat1, self.lon2, self.lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of earth in kilometers.
        return str(round(c * r, 2))

    def get(self):
        return self.haversine()
