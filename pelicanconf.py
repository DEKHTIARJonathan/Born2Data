#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os

AUTHOR       = 'Jonathan DEKHTIAR'
SITENAME     = 'Born2Data'
SITESUBTITLE = 'Tales of a Data Junkie'


TIMEZONE     = 'Europe/Paris'
LOCALE       = (
    'usa',    # On Windows
    'en_US'   # On Unix/Linux
)
DEFAULT_LANG = u'en_US.utf8'
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'

PATH            = 'content'
STATIC_PATHS    = ['images', 'files']
ARTICLE_PATHS   = ['articles']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL     = '{date:%Y}/{slug}.html'

DRAFT_BASE_URL = 'ah3d3eIjwUqNd7Mx'  # a random URI

DRAFT_URL = "%s/articles/{slug}.html" % DRAFT_BASE_URL
DRAFT_SAVE_AS = '%s/articles/{slug}.html' % DRAFT_BASE_URL
DRAFT_LANG_URL = '%s/articles/{slug}-{lang}.html' % DRAFT_BASE_URL
DRAFT_LANG_SAVE_AS = '%s/articles/{slug}-{lang}.html'

DRAFTS_URL = "{}/".format(DRAFT_BASE_URL)
DRAFTS_SAVE_AS = '{}/index.html'.format(DRAFT_BASE_URL)
SHOW_DRAFTS = True

THEME = "theme_born2data"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'better_codeblock_line_numbering',
    "drafts",
    'feed_summary',
    'render_math',  # https://github.com/barrysteyn/pelican_plugin-render_math
    'readtime',    # https://github.com/deepakrb/Pelican-Read-Time
    'share_post',
]

# deactivate image optimization for the server
if not os.environ.get("DEV_SERVER", 0):
    PLUGINS += ['optimize_images']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        # 'markdown.extensions.headerid': {},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

# Feed generation is usually not desired when developing
SITEURL     = 'http://www.born2data.com'
FEED_DOMAIN = "http://www.born2data.com"

FEED_RSS              = None
FEED_ATOM             = None

FEED_ALL_ATOM         = 'feed_atom.xml'
FEED_ALL_RSS          = 'feed_rss.xml'

TAG_FEED_RSS          = None
TAG_FEED_ATOM         = None

CATEGORY_FEED_ATOM    = None
CATEGORY_FEED_RSS     = None

TRANSLATION_FEED_RSS  = None
TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

FEED_USE_SUMMARY      = True

#Output settings
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ["CNAME"]
OUTPUT_PATH = '../Born2Data_HTML/'

# Customization

COLOR_SCHEME_CSS = 'github.css'
TWITTER_HANDLE = "@born2data"
FAVICON = "images/favicon.png"

# Menu
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('HOME', '/'),
    ('FeedCrunch.io', 'https://www.feedcrunch.io/@dataradar'),
    ('RESUME', 'http://www.jonathandekhtiar.eu'),
    ('RESEARCH', 'https://www.utc.fr/~jdekhtia/dev/'),
    ('CONTACT', '/pages/contact.html'),
)

if os.environ.get("DEV_SERVER", 0):
    MENUITEMS = list(MENUITEMS)
    MENUITEMS.insert(1, ("DRAFTS", "/{}/".format(DRAFT_BASE_URL)))
    MENUITEMS = tuple(MENUITEMS)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/born2data'),
    ('github', 'https://github.com/DEKHTIARJonathan'),
    ('linkedin', 'https://fr.linkedin.com/in/jonathandekhtiar'),
    ('rss', 'https://www.feedcrunch.io/@dataradar/rss/'),
    ('envelope', 'mailto:contact@jonathandekhtiar.eu')
)

DISQUS_SITENAME = "born2data"
DISQUS_SHOW_COMMENTS_COUNT = False

DEFAULT_PAGINATION = 5

# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Settings for Read Time plugin
READTIME_CONTENT_SUPPORT  = ["Article"]
READTIME_WPM = {
    'default': {
        'wpm': 120,
        'min_singular': 'minute',
        'min_plural': 'minutes'
    },
    'fr': {
        'wpm': 140,
        'min_singular': 'minute',
        'min_plural': 'minutes'
    }
}
