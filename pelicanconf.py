#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jonathan DEKHTIAR'
SITENAME = u'Born2Data'
SITESUBTITLE = u'Tales of a Data Junkie' 
DATE_FORMATS = {
    'en': ('usa','%A, %Y %B %d')
}

PATH = 'content'
STATIC_PATHS = ['mail', 'images', 'files']
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = "theme_born2data" 
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
	'better_codeblock_line_numbering',
    'feed_summary',
    ]
	
MD_EXTENSIONS = [
    'codehilite(css_class=highlight,linenums=False)',
    'extra'
    ]
	
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

# Feed generation is usually not desired when developing
SITEURL = 'https://www.born2data.com'
FEED_DOMAIN = "https://www.born2data.com"
FEED_ALL_ATOM = 'feed_atom.xml'
FEED_ALL_RSS = 'feed_rss.xml'
CATEGORY_FEED_ATOM = None 
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None 

FEED_USE_SUMMARY = True

#Output settings
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", "LICENSE", "README.md", ".htaccess", ".gitignore"]
OUTPUT_PATH = 'docs/'

# Customization

COLOR_SCHEME_CSS = 'github.css'
TWITTER_HANDLE = "@born2data"
FAVICON = "images/favicon.png"

ADDTHIS_PUBID = "ra-56e6dd573663678e"

# Menu
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('HOME', '/'),
    ('FeedCrunch.io', 'https://www.feedcrunch.io/@dataradar'),
    ('RESUME', 'https://www.jonathandekhtiar.eu'),
    ('RESEARCH', 'http://www.utc.fr/~jdekhtia/dev/'),
    ('CONTACT', '/pages/contact.html'),
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/born2data'),
          ('github', 'https://github.com/DEKHTIARJonathan'),
		  ('linkedin', 'https://fr.linkedin.com/in/jonathandekhtiar'),
		  ('rss', 'https://www.feedcrunch.io/@dataradar/rss/'),
          ('envelope','mailto:contact@born2data.com'))

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
