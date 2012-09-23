#!/usr/bin/env python
# encode: utf-8

import httplib
import urllib
import simplejson as json

conf = {
    'base_url'  : 'api.pushover.net',
    'push_path' : '/1/messages.json',
}

class Coinshot( object ):
    def __init__( self, app_key, user_key = None ):
        self.__dict__ = conf
        self.app_key  = app_key
        if user_key:
            self.user_key = user_key
        return None

    def push( self, msg, title = None, device = None, user_key = None ):

        if user_key == None:
            try:
                user_key = self.user_key
            except AttributeError:
                self.err = 'No user_key provided!'
                return 0

        payload = {
            'token'   : self.app_key,
            'user'    : user_key,
            'message' : msg,
            'title'   : '',
        }

        if title:
            payload['title'] = title

        if device:
            payload['device'] = device

        json_payload = json.dumps( payload )

        connection = httplib.HTTPSConnection(
            self.base_url
        )

        connection.request(
            'POST',
            self.push_path,
            json_payload,
            { "Content-type": "application/json" }
        )

        try:
            response = connection.getresponse()
        except Exception as e:
            self.err = e
            return 0

        json_result = response.read()
        result = json.loads( json_result )

        if response.status != 200:
            self.err = response.reason
            self.err = self.err + '\n%s' % json_result
            if response.status == 400:
                self.err = self.err + '\n%s' % json_payload
            return 0


        if result['status']:
            return 1
        else:
            self.err = result
            return 0

    def fetch_err( self ):
        try:
            msg = self.err
        except AttributeError:
            return 0

        del self.err
        return msg
