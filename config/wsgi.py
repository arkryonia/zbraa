# @Author: Hodonou SOUNTON <drxos>
# @Date:   2016-08-14T01:48:08+01:00
# @Email:  sounton@gmail.com
# @Project: djangoku
# @Last modified by:   drxos
# @Last modified time: 2016-08-14T02:21:36+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)



"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
