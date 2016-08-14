# @Author: Hodonou SOUNTON <drxos>
# @Date:   2016-08-14T08:33:13+01:00
# @Email:  sounton@gmail.com
# @Project: djangoku
# @Last modified by:   drxos
# @Last modified time: 2016-08-14T08:33:47+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)



from .common import *


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Allow all host headers
# -----------------------------------------------------------------------------
ALLOWED_HOSTS = ['*']
