#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Mitchell Stanton-Cook'
SITENAME = u'Bio.Dev.Op'
SITESUBTITLE = 'Biology, Code & Computers'
SITEDESCRIPTION = "Bio.Dev.Op - Biology, Code & Computers"
SITEURL = 'http://mscook.github.io/'

TIMEZONE = 'Australia/Brisbane'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

THEME = os.path.expanduser("~/3rd-repos/spoonbill")
FOOTER_TEXT = '(c) 2013 Mitchell Stanton-Cook'
SINGLE_AUTHOR = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

#### External services ###
GOOGLE_WEBMASTER = "tYDBAsj8peJGDx84OVpLivF0Q8n0Q94PaL38KKLPLdg"
GOOGLE_ANALYTICS = 'UA-43147617-1'
TWITTER_URL      = "https://twitter.com/mscook"
TWITTER_USERNAME = 'mscook'
# Note - real is Bio.Dev.Op but giving this seems to override shortname...
DISQUS_SITENAME  = 'biodevop'
DISQUS_SHORTNAME = 'biodevop'
GITHUB_URL       = 'https://github.com/mscook'


#FILES_TO_COPY = (
#    ('CNAME/CNAME', 'CNAME'),)
