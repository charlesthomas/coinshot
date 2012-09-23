coinshot
========

A simple Python module for Pushover.net

Currently working.

Example:

    import coinshot.coinshot as coinshot

    coinshot_object = coinshot.Coinshot( application_key[, user_key] )

    coinshot_object.push( message[, title, device, user_key] )

Note:

    user_key is required either during object initialization or when calling
    push. If a user_key is provided for both, the one passed to push takes
    precedent.

To Do:

    * Add optional fields
    * Cleanup code (Argument handling)
    * Better error handling
    * Create example code
    * Add documentation

Requirements:

    See pip_requirements.txt
