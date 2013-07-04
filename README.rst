========
coinshot
========

A simple Python module for Pushover.net

Example
=======
See example.py for full example::

    from coinshot import Coinshot, CoinshotException

    coinshot_object = Coinshot(application_key[, user_key])

    coinshot_object.push(message[, title, user_key, device, url, url_title, priority, timestamp])

Notes
=====
* ``user_key`` is required either during object initialization or when calling push. If a ``user_key`` is provided for both, the one passed to push takes precedent.
* ``url_title`` can be passed without ``url``, but will be ignored

What's the deal with the name?
==============================
The name coinshot is derived from a class of characters from Brandon
Sanderson's Mistborn book series. Coinshot Allomancers "burn" steel to Push
nearby metals.

`Here's the Wikipedia page <http://en.wikipedia.org/wiki/Allomancer#Steel_.28external.29>`_
