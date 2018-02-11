from django.conf import settings as django_settings
from web.default_settings import DEFAULT_ENABLED_COLLECTIONS, DEFAULT_ENABLED_PAGES
from ailedore import models, forms

SITE_NAME = 'Ailedore Academy'
SITE_URL = 'http://ailedore.com/'
SITE_IMAGE = 'ailedore.png'
DISQUS_SHORTNAME = 'ailedore'
SITE_STATIC_URL = '//localhost:{}/'.format(django_settings.DEBUG_PORT) if django_settings.DEBUG else '//i.ailedore.com/'
GAME_NAME = 'I-CHU'
ACCOUNT_MODEL = models.Account
COLOR = '#4a86e8'