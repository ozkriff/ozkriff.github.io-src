#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

STATIC_PATHS = ['images', 'pdfs']

AUTHOR = u'ozkriff'
SITENAME = u'ozkriff\'s devlog'
SITEURL = 'http://ozkriff.github.io'

TIMEZONE = 'Europe/Moscow'

LOCALE = 'en_US.UTF-8'
DEFAULT_LANG = u'en'

FILENAME_METADATA = '(?P<slug>(?P<date>\d{4}-\d{2}-\d{2})--.*)'

EXTRA_PATH_METADATA = {
    'images/favicon.png': {'path': 'favicon.png'},
}

# TODO: change to "2017.03.28"
# DEFAULT_DATE_FORMAT = '%a. %d %B %Y'
DEFAULT_DATE_FORMAT = '%Y.%m.%d'

SECTIONS = [
    (u'archives', 'archives.html'),
    (u'tags', 'tags.html'),
    (u'about', 'about.html')
]

# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DISQUS_SITENAME = "ozkriffgithubio"
TWITTER_USERNAME = 'ozkriff'
LINKEDIN_URL = 'https://www.linkedin.com/profile/view?id=AAMAABfeM3EBZh_SzJlI-iSEgVAs12f9d0S6ues'
GITHUB_URL = 'https://github.com/ozkriff'

DEFAULT_PAGINATION = 20

THEME = "theme"
PDF_GENERATOR = False


# dev settings

RELATIVE_URLS = True

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
