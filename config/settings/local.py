# @Author: drxos
# @Date:   2016-08-14T09:05:02+01:00
# @Email:  drxost@gmail.com
# @Project: zbraaku
# @Last modified by:   drxos
# @Last modified time: 2016-08-14T13:28:48+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)



from .common import *


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Allow all host headers
# -----------------------------------------------------------------------------
ALLOWED_HOSTS = ['*']

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
