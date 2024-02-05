#!/usr/bin/env python3
#encode = utf-8

import urllib.request
import urllib.parse
import simplejson

url = 'http://google.com'
print(url)
search = urllib.request.urlopen(url)
json = simplejson.loads(search.read())
print(json['responseData']['results'])