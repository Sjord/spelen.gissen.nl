#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sjoerd Langkemper'
SITENAME = u'Spelen'
SITESUBTITLE = u'Buiten spelletjes doen met een groep kinderen'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'nl'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
TAG_URL = '{slug}/'
TAG_SAVE_AS = '{slug}/index.html'

CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

THEME = 'themes/spelen'

SLUG_SUBSTITUTIONS = [
    ("Spelen", "spelen", False),
    ("Avond en nacht", "avond", False),
    ("Balspelen", "bal", False),
    ("Behendigheid", "behendigheid", False),
    ("Bosspelen", "bos", False),
    ("Creativiteit", "creativiteit", False),
    ("Denken", "denk", False),
    ("Estafette", "estafette", False),
    ("Improvisatie", "improvisatie", False),
    ("Kringspelen", "kring", False),
    ("Team en samenwerken", "team", False),
    ("Reactie", "reactie", False),
    ("Rennen en sporten", "ren", False),
    ("Tikken", "tik", False),
    ("Zoeken", "zoek", False),
    ("Geheugen", "geheugen", False),
    ("Stelen", "stelen", False),
]

STATIC_PATHS = ['images', 'static']
EXTRA_PATH_METADATA = {'static/htaccess.txt': {'path': '.htaccess'}}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
