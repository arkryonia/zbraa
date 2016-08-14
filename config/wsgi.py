# @Author: drxos
# @Date:   2016-08-14T13:17:56+01:00
# @Email:  drxost@gmail.com
# @Project: zbraaku
# @Last modified by:   drxos
# @Last modified time: 2016-08-14T13:18:01+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)



"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
