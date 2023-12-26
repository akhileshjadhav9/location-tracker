import phonenumbers
from phonenumbers import geocoder
#from test import number
import folium
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


key= "86567aab760b4380bc74c41520b3f627"

number=input("number with country code")

check_number = phonenumbers.parse(number)
nummber_location = geocoder.description_for_number(check_number,"en")
print(nummber_location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

geocoder = OpenCageGeocode(key)

query = str(nummber_location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=nummber_location).add_to(map_location)
map_location.save("mylocation.html")



