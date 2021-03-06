import json
import pprint

from app.clients import yelpClient, yelp3Client
from app.representation import venueRecord

# categories="beaches"

# def getLocality(lat, lon, **kwargs):
#     return yelpClient.search_by_coordinates(lat, lon, **kwargs)

# locality = getLocality(19.915403, -155.887403, 
#   radius_filter=25000, 
#   sort=1, 
#   limit=20, 
#   offset=0, 
#   category_filter=categories
# )

# businesses = locality.businesses
# print(json.dumps([venueRecord(b) for b in businesses], indent=2))

#yelpID = "north-india-restaurant-san-francisco"
yelpID = "holoholokai-beach-park-waimea"
yelp3Biz = yelp3Client.request("/businesses/%s" % yelpID)
print(json.dumps(yelp3Biz, indent=2))