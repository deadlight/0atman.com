#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'0atman'
AUTHORS = AUTHOR
SITENAME = u'0atman'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

GITHUB_URL = 'http://github.com/0atman/'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}

THEME = "themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "darkly"

TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/0atman'),
    ('Github', 'http://github.com/0atman'),
    ('tumblr', 'http://blog.0atman.com'),
    ('stack careers', 'http://careers.stackoverflow.com/oatman'),
    ('last.fm', 'http://www.last.fm/user/namtao'),
    ('bandcamp', 'http://music.namtao.com/')
)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# pelican-bootstrap3 settings
SHOW_ARTICLE_AUTHOR = True

# SITELOGO="https://avatars1.githubusercontent.com/u/354231?v=3&s=200"
# DISPLAY_BREADCRUMBS=True
# DISPLAY_CATEGORY_IN_BREADCRUMBS=True
# DISPLAY_ARTICLE_INFO_ON_INDEX=True

# ABOUT_ME="I'm Tris"
# AVATAR="https://avatars1.githubusercontent.com/u/354231?v=3&s=200"
BANNER = "images/composer.png"
BANNER_SUBTITLE = 'My bow is all strings'
BANNER_ALL_PAGES = True

DISPLAY_TAGS_INLINE = True
CC_LICENSE = "CC-BY-SA"
GITHUB_USER = "0atman"

TWITTER_CARDS = True
TWITTER_USERNAME = "0atman"

FAVICON = 'images/favicon.png'

