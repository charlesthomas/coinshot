#!/usr/bin/env python
import httplib
from simplejson import loads
from urllib import urlencode

conf = {
    'base_url' : 'api.pushover.net',
    'push_url' : '/1/messages.json',
}

class CoinshotException(Exception):
    def __init__(self, message, details=None):
        Exception.__init__(self, message)
        self.details = details

class Coinshot(object):
    def __init__(self, app_key, user_key=None):
        self.__dict__ = conf
        self.app_key  = app_key
        if user_key:
            self.user_key = user_key

    def push(self, message, title=None, user_key=None, device=None,
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

        if url:
            payload['url'] = url
            if url_title:
                payload['url_title'] = url_title

        if priority:
            if priority not in rage(-2, 3):
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
