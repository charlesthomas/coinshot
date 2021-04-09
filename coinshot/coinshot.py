#!/usr/bin/env python
from __future__ import print_function
try:
    import httplib
except ModuleNotFoundError:
    import http.client as httplib

from simplejson import loads
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

conf = {
    'base_url' : 'api.pushover.net',
    'push_url' : '/1/messages.json',
}

class CoinshotException(Exception):
    def __init__(self, message, details=None):
        Exception.__init__(self, message)
        self.details = details

class Coinshot(object):
    VALID_SOUNDS = ['pushover',
                    'bike',
                    'bugle',
                    'cashregister',
                    'classical',
                    'cosmic',
                    'falling',
                    'gamelan',
                    'incoming',
                    'intermission',
                    'magic',
                    'mechanical',
                    'pianobar',
                    'siren',
                    'spacealarm',
                    'tugboat',
                    'alien',
                    'climb',
                    'persistent',
                    'echo',
                    'updown',
                    'none']

    def __init__(self, app_key, user_key=None):
        self.__dict__ = conf
        self.app_key  = app_key
        if user_key:
            self.user_key = user_key

    def push(self, message, title=None, user_key=None, device=None, sound=None,
             url=None, url_title=None, priority=None, timestamp=None):
        if user_key is None:
            try:
                user_key = self.user_key
            except AttributeError:
                raise CoinshotException({'message': 'No user_key provided!'})
        payload = {
            'token'  : self.app_key,
            'user'   : user_key,
            'message': message,
        }
        if title:
            payload['title'] = title

        if device:
            payload['device'] = device

        if sound:
            assert sound in self.VALID_SOUNDS
            payload['sound'] = sound

        if url:
            payload['url'] = url
            if url_title:
                payload['url_title'] = url_title

        if priority:
            if priority not in range(-2, 3):
                raise CoinshotException("Priority must be between -2 and 2")
            payload['priority'] = priority

        if timestamp:
            payload['timestamp'] = timestamp

        connection = httplib.HTTPSConnection(self.base_url)
        connection.request('POST', self.push_url, urlencode(payload),
                           {"Content-type": "application/x-www-form-urlencoded"})
        response = connection.getresponse()
        json_result = response.read()
        result = loads(json_result)

        if response.status != 200:
            result['http status'] = response.status
            result['http reason'] = response.reason
            raise CoinshotException({'message': 'Bad Request',
                                     'details': result})

        if result['status'] != 1:
            raise CoinshotException({'message': 'Bad Status',
                                     'details': result})
