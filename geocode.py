import httplib2, json

def fetchGeocodeLocation(input):
    # Unsafe to use API key in vulnerable code, but for this file it's fine.
    # It is just to demonstrate using python's server side to fetch locations.
    google_api_key = "AIzaSyA-pnTIuJqwtfsInE9n1slQictD0FdJjNI"
    string = input.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (string, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)
