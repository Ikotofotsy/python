#!/usr/bin/env python3

import httplib2

class HTTPConnection :
    

    def get(self, URL) :
        h = httplib2.Http('.cache')
        response, contenu = h.request(URL, 'GET')
        print(response)
        
HTTPConnection().get('http://fr.wikipedia.org/wiki/Kruder')