Single repo Pelican based blog with GitHub Pages
================================================

I wanted to begin using a static site generator to blog. `Pelican`_ seemed
nice. I wanted to use GitHub to `host`_ the site. Most importantly I wanted a 
single repo with distinction between the pelican config/`reST`_ files and the
static generated content. 

Here are the steps that I devised:
    * Create a new repo on GitHub with the format username.github.io
    * Install pelican (clone the themes, plugins) & grab ghp-import
    * pelican-quickstart (with ~/username.github.io as the location)
    * cd ~/username.github.io
    * git init .
    * echo '\*.pyc' > .gitignore
    * echo 'output/' >> .gitignore
    * git add .gitignore
    * git commit -m 'gitignore'
    * git add (all untracked files)
    * git commit -m 'Initial Pelican blog'
    * git remote add origin git@github.com:username/username.github.io.git
    * git branch pelican-source
    * git checkout pelican-source
    * git push origin pelican-source
    * git branch -d master
    * make html
    * ghp-import output
    * git push git@github.com:username/username.github.io.git gh-pages:master


Visit username.github.io and have a look at your shiny new Pelican based blog.


What is going on under the hood
-------------------------------

Lets look at our local repo::

    user@host:~/username.github.io> git branch
    gh-pages
    * pelican-source


Now if you look at your GitHub repo, you have  a default branch called 
**pelican-source** which only contains the Pelican config and raw reST content 
files (if you have added content) and a master repo to which the local gh-pages 
is pushed to. GitHub serves the content from the master.


Streamlinig publication with Fabric
-----------------------------------

TODO


.. _Pelican: http://blog.getpelican.com/ 
.. _host: http://pages.github.com/
.. _reST: http://docutils.sourceforge.net/rst.html 
