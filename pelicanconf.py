#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'0atman'
AUTHORS = AUTHOR
SITENAME = u'Articles'
__SITEURL = 'http://articles.0atman.com'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

GITHUB_URL = 'http://github.com/0atman/'
DISQUS_SITENAME = "namtao"
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}

THEME = "/home/oatman/pelican-themes/pelican-sober"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
)

PELICAN_SIMPLEGREY_TWITTER_CARD_ACCOUNT = '__fle__'
# Social widget
SOCIAL = (
        ('Twitter', 'http://twitter.com/0atman'),
)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
