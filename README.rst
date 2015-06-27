========
coinshot
========

A simple Python module for `Pushover.net`_

Example
=======
See `example.py`_ for full example::

    from coinshot import Coinshot, CoinshotException

    coinshot_object = Coinshot(application_key[, user_key])

    coinshot_object.push(message[, title, user_key, device, url, url_title, priority, timestamp])

shoot
=====
If all you're looking for is an app to send pushover notifications through (not
a library for doing it programmatically, look at `bin/shoot`_.

Usage
-----
::

    Usage: shoot [options] message

    Options:
      -h, --help            show this help message and exit
      -a APP_KEY, --application-key=APP_KEY
                            Application key provided by pushover.net
      -u USER_KEY, --user-key=USER_KEY
                            User key provided by pushover.net
      -t TITLE, --title=TITLE
                            Notification Title

Notes
=====
* ``user_key`` is required either during object initialization or when calling
  push. If a ``user_key`` is provided for both, the one passed to push takes
  precedent.
* ``url_title`` can be passed without ``url``, but will be ignored

To Do
=====
See `todo.md`_

What's the deal with the name?
==============================
The name coinshot is derived from a class of characters from Brandon
Sanderson's Mistborn book series. Coinshot Allomancers "burn" steel to Push
nearby metals.

`Here's the Wikipedia page <http://en.wikipedia.org/wiki/Allomancer#Steel_.28external.29>`_

.. _`Pushover.net`: http://pushover.net
.. _`example.py`: https://github.com/charlesthomas/coinshot/blob/master/example.py
.. _`bin/shoot`: https://github.com/charlesthomas/coinshot/blob/master/bin/shoot
.. _`todo.md`: https://github.com/charlesthomas/coinshot/blob/master/todo.md
