#!/usr/bin/env python
from getpass import getuser
from optparse import OptionParser
from os import path

from coinshot import Coinshot, CoinshotException

parser = OptionParser(usage="%prog [options] message")
parser.add_option('--application-key', '-a', dest='app_key',
                  help="Application key provided by pushover.net")
parser.add_option('--user-key', '-u', dest='user_key',
                  help="User key provided by pushover.net")
parser.add_option('--title', '-t', dest='title', help="Notification Title")

# TODO add the rest of the push options as command options

(opts, args) = parser.parse_args()
# turn all non-option args into the message
# allows: shoot.py this is the message
# in addition to: shoot.py "this is the message"
message = ' '.join(args)
if message == '':
    raise CoinshotException("message cannot be blank")

if opts.app_key is None:
    opts.app_key = 'NGVmD0DWi9vE3KftytbHM0RUwKIbQI'

if opts.user_key is None:
    user_key_path = path.join('/home', getuser(), '.pushover_user_key')
    try:
        opts.user_key = open(user_key_path).read().strip()
    except Exception as e:
        raise Exception("exception type (%s)\n%s" % (type(e), e))

coinshot = Coinshot(opts.app_key, opts.user_key)
coinshot.push(message, title=opts.title)
