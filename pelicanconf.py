#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

###############################################################################
### GENERAL
##############################################################################
AUTHOR          = u'Mitchell Stanton-Cook'
SINGLE_AUTHOR   = True
SITENAME        = u'Bio.Dev.Op'
SITESUBTITLE    = u'Biology, Code & Computers'
SITEDESCRIPTION = u'Personal blog on Biology, Code & Computers'
SITEURL         = 'http://mscook.github.io'
FOOTER_TEXT     = '(c) 2013 Mitchell Stanton-Cook'
TIMEZONE        = 'Australia/Brisbane'
DEFAULT_LANG    = u'en'
MARKUP          = (("rst"),)
THEME           = os.path.expanduser("~/3rd-repos/spoonbill")


###############################################################################
### READING SETTINGS
###############################################################################
DEFAULT_PAGINATION    = 3
DISPLAY_PAGES_ON_MENU = True


###############################################################################
### RSS Feed
###############################################################################
MAIN                  = SITEURL
FEED_ATOM             = None
FEED_RSS              = None
FEED_ALL_ATOM         = None
FEED_ALL_RSS          = "feeds/rss.xml"
CATEGORY_FEED_ATOM    = None
CATEGORY_FEED_RSS     = None
TAG_FEED_ATOM         = None
TAG_FEED_RSS          = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS  = None


###############################################################################
### Folders/Output
###############################################################################
PATH         = "content"
ARTICLE_DIR  = "posts"
PAGE_DIR     = "pages"
STATIC_PATHS = (("images"), ("files"),)


###############################################################################
### URLs
###############################################################################
ARTICLE_URL     = "posts/{slug}.html" 
ARTICLE_SAVE_AS = "posts/{slug}.html"


###############################################################################
### Blogroll
###############################################################################
LINKS =  ()


###############################################################################
### Social widget
###############################################################################
SOCIAL = (
    ("Twitter", "https://twitter.com/mscook"),
    ("LinkedIn","http://au.linkedin.com/in/mjstantoncook"),
    ("GitHub","https://github.com/mscook"),
    ("Disqus","http://disqus.com/mstantoncook/"),
    ("Scholar","scholar.google.com/citations?user=MGafrX4AAAAJ&hl=en"),
)

###############################################################################
### External services
###############################################################################
GOOGLE_WEBMASTER = "tYDBAsj8peJGDx84OVpLivF0Q8n0Q94PaL38KKLPLdg"
GOOGLE_ANALYTICS = 'UA-43147617-1'
TWITTER_URL      = "https://twitter.com/mscook"
TWITTER_USERNAME = 'mscook'
DISQUS_SITENAME  = 'biodevop'
DISQUS_SHORTNAME = 'biodevop'
GITHUB_URL       = 'https://github.com/mscook'


#FILES_TO_COPY = (
#    ('CNAME/CNAME', 'CNAME'),)
