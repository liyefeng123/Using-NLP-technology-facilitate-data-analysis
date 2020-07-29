from geopy.geocoders import GoogleV3

geolocator = GoogleV3(api_key='AIzaSyDjafRf1OLCAy3FzWjxfUse0VjMJSjy6ao')
location = geolocator.geocode("Stretford uk")
print(location)
print((location.latitude, location.longitude))

