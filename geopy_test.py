from geopy.geocoders import Nominatim

geolocator = Nominatim (user_agent="geoapiExercises")

la = "25.594095"
lo = "85.137566"

location = geolocator.geocode(la + "," + lo)

print(location)



