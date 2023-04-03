"""By the name of the city, we determine its geographical coordinates,
 and if we specify the name of the second city,
 then we determine the distance between cities"""

from geopy.geocoders import Nominatim
from geopy.distance import geodesic as gd

loc = Nominatim(user_agent="Vlad")


class GeoPoint:
    def __init__(self, town, other):
        self.town = town
        self.other = other

    def coordinates(self):
        getLog = loc.geocode(self.town)
        return (f"Широта города {self.town.title()} =  {getLog.latitude}\
                \nДолгота города {self.town.title()} =  {getLog.longitude}")

    def distance_between_towns(self):
        A = (loc.geocode(self.town).latitude, loc.geocode(self.town).longitude)
        B = (loc.geocode(self.other).latitude, loc.geocode(self.other).longitude)
        return gd(A, B)


x, y = input("Пожалуйста, введите название первого города, en :  "), \
    input("Пожалуйста, введите название второго города, en :  ")
# Пожалуйста, введите название первого города, en : minsk
# Пожалуйста введите название второго города, en : moscow

print(GeoPoint(x, y).coordinates(), GeoPoint(y, x).coordinates(), sep='\n')
# Широта города Minsk =  53.9024716
# Долгота города Minsk =  27.5618225
# Широта города Moscow =  55.7504461
# Долгота города Moscow =  37.6174943

print(f"Расстояние между городами : {GeoPoint(x, y).distance_between_towns()}")
# Расстояние между городами: 677.5128065372605 km
