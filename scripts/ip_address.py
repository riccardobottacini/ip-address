#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
import urllib.request
""" Takes the ip and return city and country datas through the API """

def get_location(ip_address):

    url = 'http://ip-api.com/json/{}'
    url = url.format(ip_address)
    json_obj = urllib.request.urlopen(url)
    js = json.load(json_obj)

    return (js['city'], js['country'])
