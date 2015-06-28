3.0.2
=====

Bug Fixes
---------
* derp, *actually* adding the rest of the Coishot options to ``shoot``

3.0.1
=====
* Added the rest of the Coinshot options to ``shoot``

3.0.0
=====

Bug Fixes
---------

* home dir was only working on linux, should now work cross-platform (not tested on windows)

Other Changes
-------------

* ``shoot.py`` has been renamed shoot
* ``shoot -t`` option for title is gone
    * previously the message contents were from the args, **now that is the title**
* ``shoot`` **requires** stdin
    * **the message contents now come from stdin**, rather than unflagged args
    * ``cat some_big_file.txt | shoot this is the contents of some_big_file`` now works
