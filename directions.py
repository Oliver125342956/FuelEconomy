import urllib.request
import json
class Directions():
    
    def __init__(self):
        pass

    def places():
        endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&fields=geometry/location&'
        API_KEY = 'AIzaSyAs1daagnDlS-hVSVlZtFxzSlX3iqPnr9E'
        origin = input('Where are you?: ').replace(' ','+')
        destination = input('Where do you want to go?: ').replace(' ','+')
        nav_request = 'input={}&key={}'.format(input,API_KEY)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        place = json.loads(response)
        print(place)
        
    def getTimeAndDist():
        endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
        API_KEY = 'AIzaSyAs1daagnDlS-hVSVlZtFxzSlX3iqPnr9E'
        origin = input('Where are you?: ').replace(' ','+')
        destination = input('Where do you want to go?: ').replace(' ','+')
        nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,API_KEY)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        directions = json.loads(response)


        routes = directions['routes']

        legs = routes[0]['legs']
        routeTime = legs[0]['duration']['value']
        routeDist = legs[0]['distance']['value']


        routeDistMiles = round(float(routeDist/1609.34), 3)
        routeDistKm = round(float(routeDist/1000), 3)
        routeTimeHours = round(float(routeTime/60/60), 3)
        return routeDistKm
        return routeTimeHours
        return routeDistMiles
        
    places()