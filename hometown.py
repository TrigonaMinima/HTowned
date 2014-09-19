from facepy import GraphAPI
from geopy.geocoders import Nominatim
import simplekml

token = 'access token'

graph = GraphAPI(token)
geolocator = Nominatim()

friendsAndMe = [graph.get("me")]
pages = graph.get("me/friends", page=True)
for page in pages:
    for friend in page['data']:
        friendsAndMe.append(friend)

hometown = {}
location = {}

for friend in friendsAndMe:
    p = graph.get(friend['id'])
    if 'hometown' in p:
        ht = p['hometown']['name']
        if ht not in hometown:
            place = geolocator.geocode(ht, timeout=5)
            hometown[ht] = place.raw
    if 'location' in p:
        lc = p['location']['name']
        if lc not in location:
            place = geolocator.geocode(lc, timeout=5)
            location[lc] = place.raw

kml = simplekml.Kml()
for i in hometown:
    kml.newpoint(name=i, coords=[(hometown[i]['lon'], hometown[i]['lat'])])
kml.save("friends_hometown.kml")

kml = simplekml.Kml()
for i in location:
    kml.newpoint(name=i, coords=[(location[i]['lon'], location[i]['lat'])])
kml.save("friends_location.kml")
