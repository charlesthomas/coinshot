coinshot
========

A simple Python module for Pushover.net

Example:

    import coinshot.coinshot as coinshot

    coinshot_object = coinshot.Coinshot( application_key[, user_key] )

    coinshot_object.push( message[, title, user_key, device, url, url_title, priority, timestamp ] )

Notes:

    * user_key is required either during object initialization or when calling
    push. If a user_key is provided for both, the one passed to push takes
    precedent.

    * url_title can be passed without url, but will be ignored

To Do:

    * Add documentation

Requirements:

    See pip_requirements.txt

What's the deal with the name?

    The name coinshot is derived from a class of characters from Brandon
    Sanderson's Mistborn book series. Coinshot Allomancers "burn" steel to Push
    nearby metals.

    (http://en.wikipedia.org/wiki/Allomancer#Steel_.28external.29)
