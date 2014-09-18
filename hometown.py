import facebook as fb
from geopy import geocoders
import simplekml

token = 'CAACEdEose0cBAP0JvJZBqneBbdljE1AFHrCBb6ShaYhAFygl33SgyDXxs3z5QW4i60mZBbtXIiCZA1o9LkxNly0IAEDAouGAjFFZAIywONKlGdS34nJLGlnMg3b3ZAFpx2ctmGZB9rZCYQBthAfrnRzOoLZAZAehFC84r3vhWtvoQE0Mv17CDAZCsZBiENYrBokKI5X8wMZAmmCOi7BZCNA2CopnP'

graph = fb.GraphAPI(token)
maps = geocoders.GoogleV3()
kml = simplekml.Kml()

friends = graph.get_connections("me", "friends")

for friend in friends['data']:
    p = graph.get_object(friend['id'])
    if 'hometown' in p:
        place, (lat, lng) = maps.geocode(p['hometown']['name'].encode('utf-8'))
        kml.newpoint(coords=[(lng, lat)])

kml.save("friends_hometown.kml")
