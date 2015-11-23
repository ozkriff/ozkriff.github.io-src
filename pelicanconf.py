#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ozkriff'
SITENAME = u'Зона Контроля'
SITEURL = 'http://ozkriff.github.io'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

SECTIONS = [
    (u'Архив', 'archives.html'),
    (u'Тэги', 'tags.html'),
    (u'О блоге', 'pages/about.html')
]

DEFAULT_PAGINATION = 10

THEME = "flasky-theme"

# document-relative URLs when developing
RELATIVE_URLS = True
