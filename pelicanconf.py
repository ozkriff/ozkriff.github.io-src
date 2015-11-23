#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

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

DISQUS_SITENAME = "ozkriffgithubio"
LINKEDIN_URL = 'https://www.linkedin.com/profile/view?id=AAMAABfeM3EBZh_SzJlI-iSEgVAs12f9d0S6ues'
GITHUB_URL = 'http://github.com/ozkriff'

DEFAULT_PAGINATION = 10

THEME = "flasky-theme"
PDF_GENERATOR = False

# document-relative URLs when developing
RELATIVE_URLS = True
