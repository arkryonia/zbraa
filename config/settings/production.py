# @Author: Hodonou SOUNTON <drxos>
# @Date:   2016-08-14T01:52:31+01:00
# @Email:  sounton@gmail.com
# @Project: djangoku
# @Last modified by:   drxos
# @Last modified time: 2016-08-14T08:32:58+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)



from .common import *

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Simplified static file serving.
# -----------------------------------------------------------------------------
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
