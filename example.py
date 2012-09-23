#!/usr/bin/env python
# encode: utf-8

import coinshot.coinshot as coinshot
from coinshot.coinshot import CoinshotException

coinshot_object = coinshot.Coinshot( app_key = 'NGVmD0DWi9vE3KftytbHM0RUwKIbQI', user_key = None )

args = {
    'user_key' : None,
    'message'   : 'This is a test push to pushover with coinshot!',
    'title'     : 'Hello world!',
    'device'    : None,
    'url'       : 'http://code.cha.rlesthom.as/coinshot',
    'url_title' : 'This code can be downloaded here.',
    'priority'  : 1,
    'timestamp' : None,
}

try:
    coinshot_object.push( **args )

except CoinshotException as e:
    print e[0]['message']

    if e[0]['details']:
        print "Details:"
        for k, v in e[0]['details'].items():
            print "\t%s => %s" % ( k, v )
