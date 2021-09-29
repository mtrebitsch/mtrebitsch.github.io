#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Maxime Trebitsch'
SITENAME = u'Maxime Trebitsch'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
DISPLAY_TAGS_ON_SIDEBAR = False


# # Pages settings
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Menu
MAIN_MENU=True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', 'index.html'),
    # ('Research', 'research.html'),
    ('CV', 'cv.html'),
    ('Contact', 'contact.html'),
)
# LINKS = (
#     # ('Research', 'research.html'),
#     ('CV', 'cv.html'),
#     ('Contact', 'contact.html'),
# )


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

AVATAR = "img/maximetrebitsch.jpg"
ABOUT_ME = "I am a post-doctoral researcher in astrophysics working on high-redshift galaxy formation and reionization in Groningen."



#THEME = './pelican-themes/pelican-bootstrap3'
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo'

PAGE_EXCLUDES = []


#THEME = './pelican-themes/smoothie'
#HEADER_COVER = 'img/obelisk.png'
USER_LOGO_URL = AVATAR
#LOGO=AVATAR
#SITELOGO=AVATAR
# ROUND_USER_LOGO=True
TAGLINE=ABOUT_ME
PROFILE_IMAGE_URL='img/maximetrebitsch.jpg'
HEADER_COVER= 'img/Obelisk_composite.png'





BANNER_ALL_PAGES=True
#BANNER = 'img/Obelisk_allvert_circle_crop.png'
BANNER = 'img/Obelisk_allvert_small.jpg'
HIDE_SITENAME=True
#BOOTSTRAP_NAVBAR_INVERSE=True

CUSTOM_CSS = 'theme/css/academicons.min.css'

# Theme stuff
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math',
           'i18n_subsites',   ## For Bootstrap
           'pelican_fontawesome',
           'twitter_bootstrap_rst_directives',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', # 'liquid_tags.notebook'
]

MATH_JAX = {'mathjax_font': 'sanserif'}

STATIC_PATHS = ['img', 'pdf', 'video', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
TYPOGRIFY = True
TWITTER_USERNAME = 'maximetrebitsch'
#GITHUB_USER='mtrebitsch'
# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/maximetrebitsch', 'twitter'),
          ('Bitbucket', 'https://bitbucket.org/mtrebitsch', 'bitbucket'),
          ('GitHub', 'https://github.com/mtrebitsch', 'github'),
          ('ORCID', 'https://orcid.org/0000-0002-6849-5375', 'orcid'),
)


