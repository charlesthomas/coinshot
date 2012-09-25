#!/usr/bin/env python
# encode: utf-8

import httplib
import simplejson as json

conf = {
    'base_url' : 'api.pushover.net',
    'push_url' : '/1/messages.json',
}

class CoinshotException( Exception ):
    def __init__( self, message, details = None ):
        Exception.__init__( self, message )

        self.details = details

class Coinshot( object ):
    def __init__( self, app_key, user_key = None ):
        self.__dict__ = conf
        self.app_key  = app_key
        if user_key:
            self.user_key = user_key
        return None

    def push(
        self, message, title = None, user_key = None, device = None,
        url = None, url_title = None, priority = None, timestamp = None
    ):

        if user_key == None:
            try:
                user_key = self.user_key
            except AttributeError:
                raise CoinshotException( 'No user_key provided!' )

        payload = {
            'token'   : self.app_key,
            'user'    : user_key,
            'message' : message,
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
            payload['priority'] = priority

        if timestamp:
            payload['timestamp'] = timestamp

        json_payload = json.dumps( payload )

        connection = httplib.HTTPSConnection(
            self.base_url
        )

        connection.request(
            'POST',
            self.push_url,
            json_payload,
            { "Content-type": "application/json" }
        )

        try:
            response = connection.getresponse()
        except Exception as e:
            raise CoinshotException( e )

        json_result = response.read()
        result = json.loads( json_result )

        if response.status != 200:
            result['http status'] = response.status
            result['http reason'] = response.reason
            raise CoinshotException( {
                'message' : 'Bad Request',
                'details' : result,
            } )

        if result['status'] == 1:
            return
        else:
            raise CoinshotException( {
                'message' : 'Bad Status',
                'details'  : result,
            } )

if __name__ == '__main__':
    from optparse import OptionParser

    usage = "usage: %prog [options] user_key message"

    parser = OptionParser( usage = usage )
    parser.add_option(
        '--app-key',
        help = "To use a custom app key, pass it here. Defaults to coinshot's app key.",
        default = 'NGVmD0DWi9vE3KftytbHM0RUwKIbQI',
    )
    parser.add_option( '--title', help = 'Pushover Notification Title' )
    parser.add_option( '--device', )
    parser.add_option( '--timestamp', )
    parser.add_option( '--priority', action = 'store_true', )
    parser.add_option( '--url', )
    parser.add_option(
        '--url-title', dest = 'url_title', help = 'Link text. Ignored without URL',
    )

    ( opts, args ) = parser.parse_args()

    if len( args ) != 2:
        raise CoinshotException(
            'user_key and message arguments are both required!'
        )

    coinshot_object = Coinshot( app_key = opts.app_key, user_key = args[0] )

    payload = { 'message' : args[1] }

    if opts.title:     payload['title'    ] = opts.title
    if opts.device:    payload['device'   ] = opts.device
    if opts.url:       payload['url'      ] = opts.url
    if opts.url_title: payload['url_title'] = opts.url_title
    if opts.priority:  payload['priority' ] = 1
    if opts.timestamp: payload['timestamp'] = opts.timestamp

    try:
        coinshot_object.push( **payload )
    except CoinshotException as e:
        print e[0]['message']

        if e[0]['details']:
            print 'Details:'
            for k, v in e[0]['details'].items():
                print "\t%s => %s" % ( k, v )
