import json
import urllib
import urllib.request

def get_location(ip_address):

    url = 'http://ip-api.com/json/{}'
    url = url.format(ip_address)
    json_obj = urllib.request.urlopen((url))
    js = json.load(json_obj)

    return js["city"], js["country"]
