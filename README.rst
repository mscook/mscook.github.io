Single repo Pelican based blog with GitHub Pages
================================================

I wanted to begin using a static site generator to blog. `_Pelican` seemed
nice. I wanted to use GitHub to `_host` the site. Most importantly I wanted a 
single repo with distinction between the pelican config/`_reST` files and the
static generated content. Here are the steps that I devised:
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



.. _Pelican: http://blog.getpelican.com/ 
.. _host: http://pages.github.com/
.. _reST: http://docutils.sourceforge.net/rst.html 
