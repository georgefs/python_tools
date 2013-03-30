#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george 
#
# Distributed under terms of the MIT license.

__all__ = ['memoized', 'image_check', 'google_search_image', 'google_search_address']

import inspect
import Image
from cStringIO import StringIO
import urllib2, urllib
import json
import collections


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        self.cache[args] = self.cache[args] if self.cache.get(args, False) else self.func(*args)
 
        return self.cache[args]
 
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)



def image_check(img_url):
    try:
        img = StringIO(urllib2.urlopen(img_url).read())
        Image(img)
        return True

    except Exception, e:
        return False

@memoized
def google_search_image(keyword):
    api = "https://ajax.googleapis.com/ajax/services/search/images?"
    data = dict()
    data['v'] = '1.0'
    data['q'] = keyword
    data['imgsz'] = 'large'
    data['rsz'] = 8
    data['start'] = 0

    while True:
        url = api + urllib.urlencode(data)
        result = json.loads(urllib2.urlopen(url).read())
        
        if result.get('responseStatus') != 200:
            break
        
        img_infos = result.get('responseData', {}).get('results', [])
        for img_info in img_infos:
            yield img_info
        
        data['start'] += data['rsz']

@memoized
def google_search_address(address):
    api = "http://maps.googleapis.com/maps/api/geocode/json?"
    data = dict()
    data['sensor'] = "true"
    data['address'] = address
    
    url = api + urllib.urlencode(data)
    tmp = json.loads(urllib2.urlopen(url).read())

    if tmp.get('status') != "OK":
        return 
    else:
        return tmp.get('results')
    




imgs = google_search_image('台北')   
print imgs.next()
print google_search_address('台北')
