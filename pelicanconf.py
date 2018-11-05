#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'0atman'
AUTHORS = AUTHOR
SITENAME = u'0atman'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

DEFAULT_DATE = 'fs'

GITHUB_URL = 'http://github.com/0atman/'

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/custom.css'
]

EXTRA_PATH_METADATA = {
    'extra/CNAME':      {'path': 'CNAME'},
    'extra/custom.css': {'path': 'static/custom.css'}
}
CUSTOM_CSS = 'static/custom.css'

THEME = "themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "yeti"

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
    ('Jinja2', 'http://jinja.pocoo.org/')
)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/0atman'),
    ('Github', 'http://github.com/0atman'),
    ('Tumblr', 'http://blog.0atman.com'),
    ('Stackoverflow', 'http://careers.stackoverflow.com/oatman'),
    ('Last.fm', 'http://www.last.fm/user/namtao'),
    ('Soundcloud', 'http://soundcloud.com/namtao')
)
# PAGE_URL = '{slug}'
# PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# pelican-bootstrap3 settings
SHOW_ARTICLE_AUTHOR = True

# SITELOGO="images/hex-moon.png"
# DISPLAY_BREADCRUMBS=True
# DISPLAY_CATEGORY_IN_BREADCRUMBS=True
# DISPLAY_ARTICLE_INFO_ON_INDEX=True

ABOUT_ME = "Professional amateur developer. Amateur professional composer."
AVATAR = "/images/hex-moon-black.png"
BANNER = "/images/composer.png"
BANNER_SUBTITLE = 'Professional amateur developer.\nAmateur professional composer.'
BANNER_ALL_PAGES = False

DISPLAY_TAGS_INLINE = True
CC_LICENSE = "CC-BY-SA"
GITHUB_USER = "0atman"

TWITTER_CARDS = True
TWITTER_USERNAME = "0atman"

FAVICON = 'images/favicon.png'
