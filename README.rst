Single repo Pelican based blog with GitHub Pages
================================================

Steps:
    * Create a new repo on github with the format username.github.io
    * Install pelican (clone the themes, plugins) & grab ghp-import
    * pelican-quickstart (with ~/username.github.io as the location)
    * cd ~/username.github.io
    * git init .
    * echo '\*.pyc > .gitignore
    * echo output/ >> .gitignore
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
