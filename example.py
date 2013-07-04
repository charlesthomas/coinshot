#!/usr/bin/env python
from sys import argv
from coinshot import Coinshot, CoinshotException

coinshot_object = Coinshot(app_key='NGVmD0DWi9vE3KftytbHM0RUwKIbQI',
                           user_key=None)
args = {
    'user_key'  : argv[1],
    'message'   : 'This is a test push to pushover with coinshot!',
    'title'     : 'Hello world!',
    'device'    : None,
    'url'       : 'http://code.cha.rlesthom.as/coinshot',
    'url_title' : 'Coinshot project page',
    'priority'  : 1,
    'timestamp' : None,
}

try:
    coinshot_object.push(**args)

except CoinshotException as e:
    print e[0]['message']

    if e[0].get('details'):
        print "Details:"
        for k, v in e[0]['details'].items():
            print "\t%s => %s" % (k, v)
