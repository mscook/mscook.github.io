What not to do in Python when working with Big Data
###################################################

:date: 2013-06-16 01:50
:category: programming
:slug: bad-with-big-data
:author: Mitchell Stanton-Cook
:summary: Don't do this with a big data file


Please do not do this If you're developing software that is working with big 
data files:

.. code:: python

    f = open("really_big_fucking_file.dat")
    lines = f.readlines()
    for line in lines:
        do_something(line)
    f.close()

Please do this:

.. code:: python

    with open("really_big_fucking_file.dat") as f:
        for line in f:
            do_something(line)
            
